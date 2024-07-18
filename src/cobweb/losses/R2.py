from cobweb.engine import Value

def r2(y,y_):
    
    n = Value(len(y))
    mean_t = sum(y)/n
    rss = sum([(y[i]-y_[i])**2 for i in range(n.data)])
    tss = sum([(yi-mean_t)**2 for yi in y ])
    return (rss/tss)-1