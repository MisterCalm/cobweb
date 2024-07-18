from cobweb.engine import Value
# because of dying gradient I implemented leaky_relu as relu!

def relu(val):

    out = Value(max(0.01*val.data,val.data),_children=(val,))

    def _backwrad():

        if(val.data>0): val.grad += out.grad
        else: val.grad += 0.01 * out.grad

    out._backward = _backwrad

    return out