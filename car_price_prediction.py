# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:50:54 2018

@author: Win10 User
"""

import tensorflow as tf

zeros= tf.zeros([3,3])
zeros1= tf.Variable(zeros)
tf.ones([,])
tf.fill([,], 42)
tf.constant([,,])
tf.linspace(start, stop, start)
tf.range(start,limit, delta)
tf.random_uniform([],minval, maxval)
tf.random_normal([], meann, std)
tf.random_trun_normal([], mean, std)
tf.random_crop()
tf.random_shuffle()
sess= tf.Session()
tf.global_variables_initializer()
session.run()
x=tf.placeholder(tf.float32, shape=[2,2])
y= tf.identity(x)
x_vals= np.ramdom.rand(2,2)
sess.run(, feed_dict= {x: x_vals})
id_matrix= tf.diag([1,1,1])
a= tf.truncated_normal([2,3])
b= tf.fill([2,3], 5)
run
print (sess.run(id_matrix))
print (sess.run(a))
print (sess.run(c))
print (sess.run(b))
print (sess.run(tf.self_adjoint_eig(b)))

from sklearn import datasets
iris= datasets.load_iris()
len(iris)
len(iris.data)
print (set(iris.target[0]))
print(len(iris.target))
print(iris.target[0][1])
import requests
birthdata_url = 'https://www.umass.edu/statdata/statdata/data/lowbwt.dat'
birth_file= requests.get(birthdata_url)
birth_data= birth_file.text.split('\'r\n')
birth_header= [x for x in birth_data[0].split(' ') if len(x)>=1]
birth_data= [[float(x) for x in y.split(' ') if len(x)>=1] for y in birth_data[1:] if len(y)>=1]

print(len(birth_data[0]))




import requests
housing_url = 'https://archive.ics.uci.edu/ml/machine-learningdatabases/housing/housing.data'
housing_url= 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing_header = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM','AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV0']
housing_file= requests.get(housing_url)
housing_data= [[float(x) for x in y.split(' ') if len(x)>=1] for y in housing_file.text.split('\n') if len(y)>=1]
housing_data = [[float(x) for x in y.split(' ') if len(x)>=1] for y in housing_file.text.split('\n') if len(y)>=1]


housing_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing_header = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
cols_used = ['CRIM', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'B', 'LSTAT']
num_features = len(cols_used)
housing_file = requests.get(housing_url)
housing_data = [[float(x) for x in y.split(' ') if len(x)>=1] for y in housing_file.text.split('\n') if len(y)>=1]

import requests
housing_url = 'https://archive.ics.uci.edu/ml/machine-learningdatabases/housing/housing.data'
housing_header = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV0']
housing_file = requests.get(housing_url)
housing_data = [[float(x) for x in y.split(' ') if len(x)>=1] for y in housing_file.text.split('\n') if len(y)>=1]
