#-*- coding: utf-8 -*-
''' Import theano and numpy '''
import theano
import numpy as np
execfile('00_readingInput.py')

''' set the size of mini-batch and number of epochs'''
batch_size = 16
nb_epoch = 30

''' Import keras to build a DL model '''
from keras.models import Sequential
from keras.layers.core import Dense, Activation

print 'Building a model whose optimizer=RMSprop, activation function=softplus'
model_rmsprop = Sequential()
model_rmsprop.add(Dense(128, input_dim=200))
model_rmsprop.add(Activation('softplus'))
model_rmsprop.add(Dense(256))
model_rmsprop.add(Activation('softplus'))
model_rmsprop.add(Dense(5))
model_rmsprop.add(Activation('softmax'))

''' Setting optimizer as RMSprop '''
from keras.optimizers import  RMSprop
# (Do!) 請在 compile model_adam 時使用 'Adam' 當作 optimizer
model_rmsprop.compile(loss='categorical_crossentropy',
				optimizer='RMSprop',
				metrics=['accuracy'])

'''Fit models and use validation_split=0.1 '''
history_rmsprop = model_rmsprop.fit(X_train, Y_train,
							batch_size=batch_size,
							nb_epoch=nb_epoch,
							verbose=0,
							shuffle=True,
                    		validation_split=0.1)

loss_RMSprop= history_rmsprop.history.get('loss')
acc_RMSprop = history_rmsprop.history.get('acc')


print 'Building a model whose optimizer=adam, activation function=softplus'
model_adam = Sequential()
model_adam.add(Dense(128, input_dim=200))
model_adam.add(Activation('softplus'))
model_adam.add(Dense(256))
model_adam.add(Activation('softplus'))
model_adam.add(Dense(5))
model_adam.add(Activation('softmax'))

''' Setting optimizer as Adam '''
from keras.optimizers import  Adam
# (Do!) 請在 compile model_adam 時使用 'Adam' 當作 optimizer
model_adam.compile(loss='categorical_crossentropy',
				optimizer='Adam',
				metrics=['accuracy'])

'''Fit models and use validation_split=0.1 '''
history_adam = model_adam.fit(X_train, Y_train,
							batch_size=batch_size,
							nb_epoch=nb_epoch,
							verbose=0,
							shuffle=True,
                    		validation_split=0.1)

loss_adam= history_adam.history.get('loss')
acc_adam = history_adam.history.get('acc')

print 'Building a model whose optimizer=sgd, activation function=softplus'
model_sgd = Sequential()
model_sgd.add(Dense(128, input_dim=200))
model_sgd.add(Activation('softplus'))
model_sgd.add(Dense(256))
model_sgd.add(Activation('softplus'))
model_sgd.add(Dense(5))
model_sgd.add(Activation('softmax'))

''' Setting optimizer as SGD '''
model_sgd.compile(loss='categorical_crossentropy',
				optimizer='SGD',
				metrics=['accuracy'])

history_sgd = model_sgd.fit(X_train, Y_train,
							batch_size=batch_size,
							nb_epoch=nb_epoch,
							verbose=0,
							shuffle=True,
                    		validation_split=0.1)

loss_sgd= history_sgd.history.get('loss')
acc_sgd = history_sgd.history.get('acc')

''' Visualize the loss and accuracy of both models'''
import matplotlib.pyplot as plt
plt.figure(4)
plt.subplot(121)
plt.plot(range(len(loss_RMSprop)), loss_RMSprop,label='RMSprop')
plt.plot(range(len(loss_adam)), loss_adam,label='Adam')
plt.plot(range(len(loss_sgd)), loss_sgd,label='SGD')
plt.title('Loss')
plt.legend(loc='upper left')
plt.subplot(122)
plt.plot(range(len(acc_RMSprop)), acc_RMSprop,label='RMSprop')
plt.plot(range(len(acc_adam)), acc_adam,label='Adam')
plt.plot(range(len(acc_sgd)), acc_sgd,label='SGD')
plt.title('Accuracy')
# plt.show()
plt.savefig('04_optimizerSelection.png',dpi=300,format='png')

print 'Result saved into 04_optimizerSelection.png'