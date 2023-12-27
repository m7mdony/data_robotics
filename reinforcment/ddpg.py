import random
import pandas as pd

import numpy as np
from PIL import Image
from keras.layers import Input, Lambda, Dense, Dropout, Convolution2D, MaxPooling2D

from keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam

from keras.models import Model, load_model, model_from_json
import tensorflow as tf

import gym
import math

import pygame, sys
from tensorflow import keras

from collections import deque
import math

# Renable eager execution in TensorFlow
tf.config.run_functions_eagerly(True)

env = gym.make("Pendulum-v1")

input_shape=(3,)
num_actions=1


def actor_network(input_shape=(3,)):
    model = Sequential()
    model.add(Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.2), input_shape=input_shape))
    model.add(Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.2)))
    model.add(Dense(num_actions, activation='tanh'))
    return model

actor, target_actor = actor_network(), actor_network()
optimizer_actor = Adam(learning_rate=0.001)


def critic_network(state_dim, action_dim):
    # Define the input layers
    state_input = Input(shape=state_dim, dtype=tf.float64)
    action_input = Input(shape=action_dim, dtype=tf.float64)

    state_h1 = Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.2))(state_input)
    state_h2 = Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.2))(state_h1)

    action_h1 = Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.2))(action_input)
    action_h2 = Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.2))(action_h1)

    concat = Concatenate()([state_h2, action_h2])

    # Define the output layer
    densel = Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.2))(concat)
    dense2 = Dense(32, activation=tf.keras.layers.LeakyReLU(alpha=0.2))(densel)
    output = Dense(1, activation='linear')(dense2)

    model = Model(inputs=[state_input, action_input], outputs=output)
    return model

critic, target_critic = critic_network(3, 1), critic_network(3, 1)
optimizer_critic = Adam(learning_rate=0.001)

print("Critic network and target critic network created successfully!")