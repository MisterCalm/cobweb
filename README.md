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

the second layer has 8 neurons with **tanh** activation 

the third layer has 4 neurons with the **relu** activation function

and the last layer has 3 neuron with the **softmax** activation functin and our inputs are 1*3 arrays.

our model will be created like this:

```m = MLP(3,[(12,'tanh'),(8,"tanh"),(4,"relu"),(3,"softmax")])```

> [!TIP]
> the default activation is relu so if you just pass a number or a tuple just with one elemnt like these are valid!
> 
>```m = MLP(3,[(12,'tanh'),(8,"tanh"),(4,),(3,"softmax")])```
> 
>```m = MLP(3,[(12,'tanh'),(8,"tanh"),4,(3,"softmax")])```

### list of activations
you can pass these as activatins
```
"relu"
"tanh"
"softmax"
```

> [!WARNING]
> make sure you are always using the **softmax activation** with the **cross_entropy** loss and as the last layer!
> 
> because of the backpropagation of softmax and cross_entropy loss if you use it in other ways maybe lead to error or your network doesn't learn.
>
> in other activations and losses you are totally free.

### training the NN
