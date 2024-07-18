import math

class Value():

    def __init__(self,data,_children=(),label=''):

        self.data = data
        self.label = label
        self.grad = 0.0
        self._prev = set(_children)
        self._backward = lambda : None
        

    def __repr__(self):
        return f"Value:{self.data:.4f}"
        
    def __add__(self,other):

        other = other if isinstance(other,Value) else Value(other)
  
        out = Value(self.data + other.data , _children=(self,other))

        def _backward():

            self.grad += out.grad 
            other.grad += out.grad

        out._backward = _backward

        return out
    
    def __radd__(self,other):

        out =  Value(other+self.data, _children=(self,))

        def _backward():

            self.grad += out.grad 

        out._backward = _backward

        return out
    
    def __mul__(self,other):

        other = other if isinstance(other,Value) else Value(other)

        out = Value(self.data*other.data , _children=(self,other))

        def _backward():

            self.grad += other.data * out.grad 
            other.grad += self.data * out.grad

        out._backward = _backward
         
        return out
    
    def __rmul__(self,other):

        out = Value(other*self.data , _children=(self,))

        def _backward():

            self.grad += other * out.grad 

        out._backward = _backward
         
        return out

    def __sub__(self,other):

        other = other if isinstance(other,Value) else Value(other)
         
        out = Value(self.data - other.data , _children=(self,other))

        def _backward():
             
             self.grad += out.grad
             other.grad += -1*(out.grad)

        out._backward = _backward

        return out
    
    def __rsub__(self,other):
        
        out = Value(other-self.data , _children=(self,))

        def _backward():
             
             self.grad += -1*(out.grad)

        out._backward = _backward

        return out
        
    def __truediv__(self,other):

        other = other if isinstance(other,Value) else Value(other)

        out = Value(self.data/other.data,_children=(self,other))

        def _backward():

            self.grad += (1/(other.data)) * out.grad 
            other.grad += ((-1*self.data)/((other.data)**2)) * out.grad

        out._backward = _backward

        return out
    
    def __rtruediv__(self,other):

        out = Value(other/self.data, _children=(self,))

        def _backward():

            self.grad += ((-1*other)/((self.data)**2)) * out.grad

        out._backward = _backward

        return out
    
    def __pow__(self,other):

        other = other if isinstance(other,Value) else Value(other)

        out = Value(self.data**other.data,_children=(self,other))

        def _backward():

            self.grad = ((other.data)*(self.data**((other.data)-1))) * out.grad

            try:
                other.grad = (out.data*(math.log(float(self.data)))) * out.grad

            except: other.grad = other.grad

        out._backward = _backward

        return out
    
    def __rpow__(self,other):

        out = Value(other**(self.data) , _children=(self,))

        def _backward():

            self.grad = (out.data*(math.log(other))) * out.grad

        out._backward = _backward

        return out
    

    def exp(self):

        out = Value(math.exp(self.data),_children=(self,))

        def _backward():
            
            self.grad = out.data * out.grad

        out._backward = _backward

        return out

    def log(self):
         
        out = Value(math.log(self.data),_children=(self,), label="log")

        def _backward():

            self.grad += (1/self.data) * out.grad

        self._backward = _backward

        return out 
    
    def abs(self):

        out = Value(abs(self.data),_children=(self,),label="abs")

        def _backward():
            if(self.data >= 0): self.grad += out.grad
            else: self.grad -= out.grad

        out._backward = _backward
        
        return out
            
    def backward(self):

        self.grad = 1.0

        #using topological sort for implementation backpropagation

        topo = []
        visited = set()

        def topo_sort(v):

            if v not in visited:

                visited.add(v)

                for children in v._prev:

                    topo_sort(children)

            topo.append(v)

        topo_sort(self)

        for node in reversed(topo):
            node._backward()
