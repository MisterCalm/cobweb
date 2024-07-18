import random
from cobweb.engine import Value
from cobweb.activations.tanh_activation import tanh
from cobweb.activations.relu_activation import relu
from cobweb.activations.softmax_activation import softmax , linear

class Neuron():

    def __init__(self, number_of_ins , _activation):
        self.w = [Value(random.uniform(-1,1)) for _ in range(number_of_ins)]
        self.b = Value(random.uniform(-1,1))
        self.activation = _activation
        

    def __call__(self, x):

        act = sum((wi*xi for wi,xi in zip(self.w, x)), self.b)

        activations = {"tanh":tanh,
                       "relu":relu,
                       "linear":linear}
        
        if(self.activation=="softmax"):self.activation="linear"
        act = activations[self.activation](act)
        return act

    def parameters(self):
        return self.w + [self.b]


class Layer():

    def __init__(self, number_of_ins, number_of_outs , _activation="relu"):
        self.activation = _activation

        self.neurons = [Neuron(number_of_ins , _activation) for _ in range(number_of_outs)]

    def __call__(self, x):

        out = [n(x) for n in self.neurons]

        if(self.activation=="softmax"):
            softm_inps.append(out)
            return softmax(out)

        return out[0] if len(out) == 1 else out

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

class MLP():

    def __init__(self, number_of_ins, outs):
        self.layers = []
        sz = [(number_of_ins,)] + outs    

        global softm_inps
        softm_inps = []

        #handling different shapes of inputs
        for i in range(len(outs)):

            if (isinstance(sz[i],tuple) and isinstance(sz[i+1],tuple)):

                if(len(sz[i+1])==1): sz[i+1] = (sz[i+1][0],"relu")
                self.layers.append(Layer(sz[i][0], sz[i+1][0] , sz[i+1][1]))

            elif(isinstance(sz[i],int) and isinstance(sz[i+1],tuple)):

                if(len(sz[i+1])==1): sz[i+1][1] = "relu"
                self.layers.append(Layer(sz[i], sz[i+1][0] , sz[i+1][1]))
            
            elif(isinstance(sz[i],tuple) and isinstance(sz[i+1],int)):

                sz[i+1] = (sz[i+1],"relu")
                self.layers.append(Layer(sz[i][0], sz[i+1][0] , sz[i+1][1]))
            
            elif(isinstance(sz[i],int) and isinstance(sz[i+1],int)):
                sz[i+1] = (sz[i+1],"relu")
                self.layers.append(Layer(sz[i], sz[i+1][0] , sz[i+1][1]))

        

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):

        return [p for layer in self.layers for p in layer.parameters()]
       

    def update(self,x,y,loss_function="mse",epochs=100,learning_rate=0.01):
        #importing losses
        from cobweb.losses.mse import MSE
        from cobweb.losses.mae import MAE
        from cobweb.losses.R2 import r2
        from cobweb.losses.cross_entropy_loss import cross_entropy
 
        loss_functions = {"mse":MSE,
                          "mae":MAE,
                          "r2":r2,
                          "cross_entropy":cross_entropy}
        
        loss_func = loss_functions[loss_function]

        # ready for forward!
        y_ = [self(xi) for xi in x]

        print("first predictions")
        for yi in y_ : print(yi)

        print('-----Training-----')

        for k in range(epochs):

            global softm_inps

            y_ = [self(xi) for xi in x]

            if (loss_function!="cross_entropy") : loss = loss_func(y,y_)
            else : loss = loss_func(y,y_,softm_inps)

            for p in self.parameters():
                p.grad = 0
            
            #backward is coming ...
            
            loss.backward()

            for p in self.parameters():
                p.data += -learning_rate * p.grad

            softm_inps  = []

            print(k,loss)

            
        print("----finished----")
        print("new predictions")
        for xi in x:print(self(xi))


