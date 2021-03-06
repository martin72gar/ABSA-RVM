# grid search hypers

params = [
    ('epochs', [50, 75]),
    ('batch_size', [64]),
    ('validation_split', [0.]),
    ('filters', [320]),
    ('kernel_size', [5]),
    ('conv_activation', ['relu']),
    ('conv_l2_regularizer', [0.1, 0.01, 0.001, 0.]),
    ('dropout_rate', [0., 0.2, 0.6]),
    ('dense_activation', ['tanh']),
    ('dense_l2_regularizer', [0.1, 0.01, 0.001, 0.]),
    ('activation', ['sigmoid']),
    ('optimizer', ['nadam']),
    ('loss_function', ['binary_crossentropy']),
    ('units', [128]),
    ('trainable', [False]),
    ('dense_layers', [1, 2]),
]

param_grid = dict(params)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import sys
try:
    sys.path.insert(0, '.')
    from constants import Const
    sys.path.insert(0, Const.ROOT)
except:
    sys.path.insert(0, '..')
    from constants import Const

import utils

from MyClassifier import MyClassifier, Model
from sklearn.base import BaseEstimator, ClassifierMixin

from keras import backend as K
from keras.models import Sequential, Input, load_model
from keras.layers import Dense, LSTM, Flatten, Dropout, Lambda, BatchNormalization
from keras.layers.convolutional import Conv1D
from keras.layers.pooling import AveragePooling1D, MaxPooling1D, GlobalMaxPooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence, text
from keras import regularizers, optimizers
from keras.callbacks import ModelCheckpoint

import dill
import numpy as np

import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

class CNNSentimentPolarityClassifier (MyClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.WEIGHTS_PATH = 'model/cnn/weights/best_{}.hdf5'
        self.MODEL_PATH = 'model/cnn/best_{}.model'
        self.WE_PATH = '../we/embedding_matrix.pkl'
        self.THRESHOLD = 0.5
        self.target_names = ['polarity']
       
        self.cnn_model = None
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def fit(self, X, y,

        filters = 320,
        kernel_size = 5,
        conv_activation = 'tanh',
        conv_l2_regularizer = 0.01,
        dropout_rate = 0.6,
        dense_activation = 'relu',
        dense_l2_regularizer = 0.01,
        activation = 'sigmoid',
        optimizer = "nadam",
        loss_function = 'binary_crossentropy',
        units = 256,
        trainable = False,
        dense_layers = 1,
        class_weight = None,

        is_save = False,
        category = 'NOTSPECIFIED',

        **kwargs):
        self.cnn_model = self._create_model(
        	filters,
            kernel_size,
            conv_activation,
            conv_l2_regularizer,
            dropout_rate,
            dense_activation,
            dense_l2_regularizer,
            activation,
            optimizer,
            loss_function,
            units,
            trainable,
            dense_layers,
        )
        mode = kwargs.get('mode', 'train_validate_split')
        if mode == "train_validate_split":
            # self.cnn_model.summary()
            self.cnn_model.fit(
                X, y,
                class_weight=class_weight,
                **kwargs
            )
        if is_save:
            self.cnn_model.save(self.MODEL_PATH.format(category))
    
    def predict(self, X, **kwargs):
        y_pred = self.cnn_model.predict(X)
        if y_pred.shape[1] > 1:
            return y_pred.argmax(axis=-1)
        else:
            THRESHOLD = self.THRESHOLD
            y_pred[y_pred > THRESHOLD] = 1.
            y_pred[y_pred <= THRESHOLD] = 0.
            return y_pred

    def _fit_train_validate_split(self, X, y):
        pass

    def _fit_gridsearch_cv(self, X, y, param_grid, category="NOTSPECIFIED", **kwargs):
        from sklearn.model_selection import GridSearchCV
        from keras.wrappers.scikit_learn import KerasClassifier

        np.random.seed(7)

        # Wrap in sklearn wrapper
        model = KerasClassifier(build_fn = self._create_model, verbose=0)

        # train
        IS_REFIT = kwargs.get('is_refit','f1_macro')
        grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, refit=IS_REFIT, scoring=['f1_macro', 'precision_macro', 'recall_macro'], verbose=1)
        grid_result = grid.fit(X, y)
        # print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
        print(grid_result.cv_results_.keys())
        means = [grid_result.cv_results_['mean_test_f1_macro'], grid_result.cv_results_['mean_test_precision_macro'], grid_result.cv_results_['mean_test_recall_macro']]
        stds = [grid_result.cv_results_['std_test_f1_macro'], grid_result.cv_results_['std_test_precision_macro'], grid_result.cv_results_['std_test_recall_macro']]
        for mean, stdev in zip(means, stds):
            print("\n{} ({})".format(mean, stdev))
        params = grid_result.best_params_
        print("with:", params)
        with open('output/gridsearch_cnn_{}.pkl'.format(category), 'wb') as fo:
            dill.dump(grid_result.cv_results_, fo)
        if IS_REFIT:
            grid.best_estimator_.model.save('model/cnn/best_{}.model'.format(category))

    def _create_model(
        self,

        filters = 320,
        kernel_size = 5,
        conv_activation = 'tanh',
        conv_l2_regularizer = 0.01,
        dropout_rate = 0.6,
        dense_activation = 'relu',
        dense_l2_regularizer = 0.01,
        activation = 'sigmoid',
        optimizer = "nadam",
        loss_function = 'binary_crossentropy',
        units = 256,
        trainable = False,
        dense_layers = 1,

        **kwargs
    ):
        K.clear_session()
        MAX_SEQUENCE_LENGTH = kwargs.get("max_sequence_length", 150)

        # Define Architecture
        layer_input = Input(shape=(MAX_SEQUENCE_LENGTH,))
        layer_embedding = self._load_embedding(self.WE_PATH, trainable=trainable, vocabulary_size=15000, embedding_vector_length=500)(layer_input)
        layer_conv = Conv1D(filters=filters, kernel_size=kernel_size, padding='same', activation=conv_activation,
        kernel_regularizer=regularizers.l2(conv_l2_regularizer))(layer_embedding)
        layer_pooling = GlobalMaxPooling1D()(layer_conv)
        layer_dropout = Dropout(dropout_rate, seed=7)(layer_pooling)
        for i in range(dense_layers):
            layer_dense = Dense(units, activation=dense_activation, kernel_regularizer=regularizers.l2(dense_l2_regularizer))(layer_dropout)
            layer_dropout = Dropout(dropout_rate, seed=7)(layer_dense)
        layer_softmax = Dense(1, activation=activation)(layer_dropout)
        
        # Create Model
        cnn_model = Model(inputs=layer_input, outputs=layer_softmax)
        
        # Create Optimizer
        # optimizer = optimizers.Nadam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)
        # optimizer = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
        cnn_model.compile(loss=loss_function, optimizer=optimizer, metrics=['accuracy'])
        return cnn_model

    def load_weights(self, path):
        self._create_model()
        self.cnn_model.load_weights(path)
    
    def get_threshold(self):
        return self.THRESHOLD
    
    def load_best_model(self, category):
        best_model = load_model(Const.SPC_ROOT + 'model/cnn/best_{}.model'.format(category))
        del self.cnn_model
        self.cnn_model = best_model

def get_best_params():
    best_params = {
        'food':
        {
            'epochs': 75,
            'batch_size': 64,
            'filters': 320,
            'kernel_size': 5,
            'conv_activation': 'relu',
            'conv_l2_regularizer': 0.01,
            'dropout_rate': 0.2,
            'dense_activation': 'tanh',
            'dense_l2_regularizer': 0.001,
            'activation': 'sigmoid',
            'loss_function': 'binary_crossentropy',
            'units': 128,
            'trainable': False,
            'dense_layers': 1,
        },

        'service':
        {
            'epochs': 75,
            'batch_size': 64,
            'filters': 320,
            'kernel_size': 5,
            'conv_activation': 'relu',
            'conv_l2_regularizer': 0.001,
            'dropout_rate': 0.6,
            'dense_activation': 'tanh',
            'dense_l2_regularizer': 0.001,
            'activation': 'sigmoid',
            'loss_function': 'binary_crossentropy',
            'units': 128,
            'trainable': False,
            'dense_layers': 1,
        },

        'price':
        {
            'epochs': 50,
            'batch_size': 64,
            'filters': 320,
            'kernel_size': 5,
            'conv_activation': 'relu',
            'conv_l2_regularizer': 0.01,
            'dropout_rate': 0.,
            'dense_activation': 'tanh',
            'dense_l2_regularizer': 0.,
            'activation': 'sigmoid',
            'loss_function': 'binary_crossentropy',
            'units': 128,
            'trainable': False,
            'dense_layers': 1,
        },

        'place':
        {
            'epochs': 50,
            'batch_size': 64,
            'filters': 320,
            'kernel_size': 5,
            'conv_activation': 'relu',
            'conv_l2_regularizer': 0.01,
            'dropout_rate': 0.2,
            'dense_activation': 'tanh',
            'dense_l2_regularizer': 0.,
            'activation': 'sigmoid',
            'loss_function': 'binary_crossentropy',
            'units': 128,
            'trainable': False,
            'dense_layers': 1,
        },
    }

    return best_params

def main():
    categories = ['food', 'service', 'price', 'place']
    f1_scores = []
    p_scores = []
    r_scores = []
    for category in categories:
        print("\n\n========= CHECKING CATEGORY:", category, "==========")
        """
            Initialize data
        """
        X, y, X_test, y_test = utils.get_spc_dataset(category)
        # X_train, X_validate, y_train, y_validate = train_test_split(X, y, test_size=0.20, random_state=7)

        """
            Make the model
        """
        # np.random.seed(7)

        # checkpointer = ModelCheckpoint(filepath='model/cnn/weights/CNN.hdf5', verbose=0, save_best_only=True)
        spc = CNNSentimentPolarityClassifier()

        """
            Fit the model
        """
        
        from keras.utils import to_categorical
        # y = to_categorical(y)
        # spc._fit_new_gridsearch_cv(X, y, params, result_path="output/gridsearch_cv_result_{}.csv".format(category), score_verbose=True)
        best_params = get_best_params()

        is_save = {
            'food': False,
            'service': False,
            'price': False,
            'place': False,
        }
        if is_save[category]:
            spc.fit(X, y,
                **best_params[category],
                verbose=1,
                category=category,
                is_save = is_save[category],
                validation_split=0.,
                optimizer='nadam',
            )
        
        """
            Load best estimator and score it
        """

        spc.load_best_model(category)

        # preds = spc.predict(X_test)
        # for pred in preds:
        #     if pred[0] == pred[1]:
        #         print("SAMA", pred[0])

        score = spc.score(X_test, y_test, verbose=1)
        f1_scores.append(score['f1_score_macro'])
        p_scores.append(score['precision_score_macro'])
        r_scores.append(score['recall_score_macro'])
    print("F1-MEAN-MACRO:", np.array(f1_scores).mean())
    print("P -MEAN-MACRO:", np.array(p_scores).mean())
    print("R -MEAN-MACRO:", np.array(r_scores).mean())

def get_wrong_preds(data='train'):
    categories = ['food', 'service', 'price', 'place']
    
    for category in categories:
        print()
        print()
        print("\t######################################################")
        print("\t############## CHECKING CATEGORY: {} ##############".format(category.upper()))
        print("\t######################################################")
        print()
        spc = CNNSentimentPolarityClassifier()
        spc.load_best_model(category=category)
        X, y, X_test, y_test, df, df_test = utils.get_spc_dataset(category, return_df = True)
        
        data = 'train'
        if data == 'test':
            df = df_test
            X = X_test
            y = y_test

        print(len(df))
        y_pred = spc.predict(X)
        
        spc.score(X, y)

        cnt = 0
        for i, (review, y_pred_single, y_single) in enumerate(list(zip(df['review'], y_pred, y.values.tolist()))):
            y_pred_single = int(y_pred_single[0])
            if y_pred_single != y_single:
                cnt += 1
                print("================= {} =================".format(i))
                print(review)
                print('PRED:', y_pred_single)
                print('ACTL:', y_single)
                print()
        print(cnt, "sentences missclasified")

if __name__ == "__main__":
    # utils.time_log(main)
    utils.time_log(get_wrong_preds)