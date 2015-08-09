#!/usr/bin/env python

import numpy
import theano
import theano.tensor as T
import theano.printing as pr
rng = numpy.random


# Training data
N = 400
feats = 784
D = (rng.randn(N, feats).astype(theano.config.floatX),
     rng.randint(size=N,low=0, high=2).astype(theano.config.floatX)
     )
training_steps = 10000

# Declare Theano symbolic variables
x = T.matrix("x")
y = T.vector("y")
w = theano.shared(rng.randn(feats).astype(theano.config.floatX), name="w")
b = theano.shared(numpy.asarray(0., dtype=theano.config.floatX), name="b")
x.tag.test_value = D[0]
y.tag.test_value = D[1]

# Construct Theano expression graph
p_1 = 1 / (1 + T.exp(-T.dot(x, w)-b)) # Probability of having a one
prediction = p_1 > 0.5 # The prediction that is done: 0 or 1

# Compute gradients
xent = -y*T.log(p_1) - (1-y)*T.log(1-p_1) # Cross-entropy
cost = xent.mean() + 0.01*(w**2).sum() # The cost to optimize
gw,gb = T.grad(cost, [w,b])

# Training and prediction function
train = theano.function(inputs=[x,y], outputs=[prediction, xent], updates=[[w, w-0.01*gw], [b, b-0.01*gb]], name = "train")
predict = theano.function(inputs=[x], outputs=prediction, name = "predict")

X, y = D
train(X, y)
p = predict(X)

