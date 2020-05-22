import numpy as np

def gradient_descent(X, y, theta, alpha, num_iters):
    m = y.shape[0]
    theta = theta.copy()

    # add a column of ones to estimate line intercept
    X = np.stack([np.ones(y.size), X], axis=1)

    for i in range(num_iters):
        theta = theta - (alpha / m) * ((X @ theta) - y).dot(X)
    
    return theta


