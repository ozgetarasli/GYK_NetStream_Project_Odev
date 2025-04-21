"""
Custom implementation of cosine similarity to avoid dependency issues
"""

import numpy as np

def cosine_similarity(X, Y=None):
    """
    Compute cosine similarity between samples in X and Y.
    
    Parameters
    ----------
    X : array-like of shape (n_samples_X, n_features)
        Input data.
    Y : array-like of shape (n_samples_Y, n_features), default=None
        Input data. If None, the output will be the pairwise
        similarities between all samples in X.
        
    Returns
    -------
    similarities : ndarray of shape (n_samples_X, n_samples_Y)
        Cosine similarity matrix.
    """
    # Compute the dot product
    if Y is None:
        Y = X
    
    # Ensure X and Y are numpy arrays
    X = np.asarray(X)
    Y = np.asarray(Y)
    
    # Handle the case when X or Y is a single sample
    if X.ndim == 1:
        X = X.reshape(1, -1)
    if Y.ndim == 1:
        Y = Y.reshape(1, -1)
    
    # Compute the norms
    X_norm = np.sqrt(np.sum(X**2, axis=1))
    Y_norm = np.sqrt(np.sum(Y**2, axis=1))
    
    # Avoid division by zero
    X_norm[X_norm == 0] = 1
    Y_norm[Y_norm == 0] = 1
    
    # Compute cosine similarity
    dot_product = np.dot(X, Y.T)
    similarity = dot_product / np.outer(X_norm, Y_norm)
    
    return similarity 