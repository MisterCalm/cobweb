from numpy import clip , shape , mean , log , sum

class CategoricalCrossEntropy:

    def calculate(self,y_pred,y):

        y_pred = clip(y_pred,1e-7,1-1e-7)

        if(len(shape(y))==1):

            n_rows = len(y_pred)
            self.output = mean(-1*log(y_pred[range(n_rows),y]))

        elif(len(shape(y))==2):
           
           self.output = mean(-1*log(sum(y_pred*y,axis=1)))
