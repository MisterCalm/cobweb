from cobweb.engine import Value
from numpy import shape , log2

def cross_entropy(y,y_,soft_inps):

# y and y_ should be matrices with the same size ,
#contain one hot values for each sample(each row is one sample)!

    assert shape(y)==shape(y_)
    rows = shape(y)[0]
    columns = shape(y)[1]
    childs = []
    loss = 0


    for i in range(rows):
        for j in range(columns):

            childs.append(soft_inps[i][j])
            soft_inps[i][j].grad += y_[i][j].data-y[i][j]


            if(y_[i][j].data<=1e-7):y_[i][j].data = 1e-7
            elif(y_[i][j].data>=1-1e-7):y_[i][j].data = 1-1e-7

            loss -= y[i][j]*(log2(y_[i][j].data))

    l = Value(loss/rows , _children=childs)

    return l
