# cobweb
# first picture
the cobweb is a tiny neural network library that I created to gain deeper understanding of how neural nets are working underneath.
## Installation
first of all checkout the *requirements.txt*
and simply use  `pip install cobweb` command
## basics
let's create a simple NN using *cobweb*
first you need to import MLP (model)

```from cobweb.mlp import MLP```

now we will create our model object.

you should pass your input (your training data) size as the first argument

and a list of tuples for each layer input size and it's activation function name

for instance imagine we want a NN with 4 layers such that the first layer has 12 neurons with *tanh* activation

the second layer has 8 neurons with *tanh* activation 

the third layer has 4 neurons with the *relu* activation function

and the last layer has 3 neuron with the *softmax* activation functin and our inputs are 1*3 arrays.

our model will be created like this:
```m = MLP(```

