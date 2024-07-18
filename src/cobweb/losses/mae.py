from cobweb.engine import Value

def MAE(y,y_):
    n = len(y)
    return sum([(y[0]-y[1]).abs() for y in zip(y,y_)])/n
