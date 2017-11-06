
from os import path
import numpy as np
import argparse

import sys
parent_path = path.abspath('..')
sys.path.insert(0, parent_path)
from machine_learning.prediction.new_algorithm import dfFunctions
import machine_learning.prediction.new_algorithm.recommender as re

import os
from definitions import root_dir


def initialize():
    # path = parent_path + '\\ml-1m\\ratings.dat'

    filename = os.path.join(
        root_dir,
        'machine_learning/prediction/new_algorithm/ml-1m/ratings.dat')
    path = os.path.abspath(os.path.realpath(filename))

    parser = argparse.ArgumentParser()

    parser.add_argument('-p',
                        '--path',
                        type=str,
                        default=path,
                        help=('ratings path\n'
                              '(default=pwd/movielens/ml-1m/ratings.dat)'))

    parser.add_argument('-e',
                        '--example',
                        type=str,
                        default='1',
                        help=('movielens dataset\n'
                              'examples (only 1, 10 or 20) (default=1)'))

    parser.add_argument('-b',
                        '--batch',
                        type=int,
                        default=700,
                        help='batch size (default=700)')

    parser.add_argument('-s',
                        '--steps',
                        type=int,
                        default=2000,
                        help='number of training steps (default=7000)')

    parser.add_argument('-d',
                        '--dimension',
                        type=int,
                        default=12,
                        help='embedding vector size (default=12)')

    parser.add_argument('-r',
                        '--reg',
                        type=float,
                        default=0.0003,
                        help=('regularizer constant for\n'
                              'the loss function  (default=0.0003)'))

    parser.add_argument('-l',
                        '--learning',
                        type=float,
                        default=0.001,
                        help='learning rate (default=0.001)')

    parser.add_argument('-m',
                        '--momentum',
                        type=float,
                        default=0.926,
                        help='momentum factor (default=0.926)')

    parser.add_argument('-i',
                        '--info',
                        type=str,
                        default='True',
                        help=('Training information.\n'
                              'Only True or False (default=True)'))

    parser.add_argument('-M',
                        '--model',
                        type=str,
                        default='svd',
                        help='models: either svd or nsvd (default=svd)')

    parser.add_argument('-S',
                        '--nsvd_size',
                        type=str,
                        default='mean',
                        help=('size of the vectors of the nsvd model:\n'
                              'either max, mean or min (default=mean)'))

    args = parser.parse_args()

    if args.example == '20':
        path = parent_path + '/movielens/ml-20m/ratings.csv'
    elif args.example == '10':
        path = parent_path + '/movielens/ml-10m/ratings.dat'
    elif args.example == '1':
        pass
    else:
        print('Wrong parameter passed to the example option. '
              'Running default=1\n')

    df = dfFunctions.load_dataframe(args.path)
    if args.model == 'svd':
        model = re.SVDmodel(df, 'User', 'item', 'Rating')
    else:
        model = re.SVDmodel(df,
                            'User',
                            'item',
                            'Rating',
                            args.model,
                            args.nsvd_size)

    dimension = args.dimension
    regularizer_constant = args.reg
    learning_rate = args.learning
    batch_size = args.batch
    num_steps = args.steps
    momentum_factor = args.momentum
    if args.info == 'True':
        info = True
    else:
        info = False

    model.training(dimension,
                   regularizer_constant,
                   learning_rate,
                   momentum_factor,
                   batch_size,
                   num_steps,
                   info)

    prediction = model.valid_prediction()
    print('\nThe mean square error of the whole valid dataset is ', prediction)
    # user_example = np.array(model.valid['User'])[0:10]
    # movies_example = np.array(model.valid['item'])[0:10]
    # actual_ratings = np.array(model.valid['Rating'])[0:10]
    # predicted_ratings = model.prediction(user_example, movies_example)
    # print('''\nUsing our model for 10 specific users and 10
    # movies we predicted the following score:''')
    # print(predicted_ratings)
    # print('\nAnd in reality the scores are:')
    # print(actual_ratings)
    return model
