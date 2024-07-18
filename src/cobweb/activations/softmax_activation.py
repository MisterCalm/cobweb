from numpy import exp

def softmax(input):
    n = len(input)
    summ = sum([exp(input[i]) for i in range(n)])
    out = [((exp(input[i]))/summ) for i in range(n)]

    return out


def linear(input):

    return input