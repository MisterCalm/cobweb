# cobweb
![spider-man](https://github.com/user-attachments/assets/64b0aa17-0c89-466f-ad04-ec445a7ff425)


the cobweb is a tiny neural network library that I created to gain deeper understanding of how neural nets are working underneath.
## Installation
first of all checkout the *requirements.txt*
and simply use  `pip install cubweb` command
## basics
let's create a simple NN using *cobweb*
first you need to import MLP (model)

```from cobweb.model import MLP```

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

* "relu"
* "tanh"
* "softmax"


> [!WARNING]
> make sure you are always using the **softmax activation** with the **cross_entropy** loss and as the last layer!
> 
> because of the backpropagation of softmax and cross_entropy loss if you use it in other ways maybe lead to error or your network doesn't learn.
>
> in other activations and losses you are totally free.

### training the NN

now let's train our NN

for this we will use `**m.update()**`

update method gets these as input:

* training data batch
* target datas
* loss_function (as str)
* number of epochs
* learning rate

by running this line of code our NN will be training:

```m.update(x,y,loss_function="cross_entropy",epochs=100,learning_rate=0.01)```

> [!TIP]
> the default valu for **loss_function** is "mse" which is **MSE**(mean squared error) loss.
>
> the default value for **epochs** is **100**
>
> the default value for **learning rate** is **0.01**

#### list of loss functions

* "mse" for MSE 
* "mae" for MAE
* "cross_entropy" for categorical cross entropy

also even you can use r2 score as loss function by passing "r2"


### sample training for a classification problem
#### a classification problem
![Screenshot (124)](https://github.com/user-attachments/assets/269e9b94-a7eb-4071-8a8d-0d40c579ba2a)

![Screenshot (125)](https://github.com/user-attachments/assets/782ca9ee-8220-41b4-8c40-5e5627255928)

#### a regression problem
![Screenshot (126)](https://github.com/user-attachments/assets/2c5b0e11-c0ef-4c8c-a295-7b85ff0b7781)
![Screenshot (127)](https://github.com/user-attachments/assets/58ffc4d4-42c9-4dc8-aaa6-f3ab0d8d13ae)


## Credit

special tahnks to [Andrej Karpathy](https://github.com/karpathy)

I learned the most of these codes by his [Micro Grad](https://github.com/karpathy/micrograd).
