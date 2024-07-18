from cobweb.mlp import MLP
x = [[2,3,-1],
     [3,-1,0.5],
     [0.5,1,1],]

y = [[1,0,0],
     [0,1,0],
     [0,0,1],]


#y = [0.7,0.5,0.25]

m = MLP(3,[(12,'tanh'),(8,"tanh"),(4,"relu"),(3,"softmax")])

m.update(x,y,loss_function="cross_entropy",epochs=100,learning_rate=0.01)

