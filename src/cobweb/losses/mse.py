def MSE(y,y_):
    
    n = len(y)
    return sum([(y_i - yi)**2 for y_i,yi in zip(y_,y)])/n