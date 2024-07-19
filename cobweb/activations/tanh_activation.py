from cobweb.engine import Value
from math import tanh as th

def tanh(val):

    out = Value(th(val.data) , _children=(val,) , label='tanh')

    def _backward():

        val.grad += (1 - th(val.data)**2) * out.grad

    out._backward = _backward

    return out
