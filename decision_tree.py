from typing import List, Dict, Any
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class MultiNodeCategoricalDecisionTree(BaseEstimator, ClassifierMixin):
    """
    A multi-node categorical decision tree classifier.
    
    This classifier is designed to work with categorical features and can have
    multiple branches at each node, unlike binary decision trees.
    
    Parameters
    ----------
    max_depth : int, optional (default=None)
        The maximum depth of the tree. If None, the tree will expand until all
        leaves are pure or until all leaves contain less than min_samples_split samples.
    
    min_samples_split : int, optional (default=2)
        The minimum number of samples required to split an internal node.
    
    Attributes
    ----------
    tree_ : dict
        The tree structure stored as a nested dictionary.
    
    n_classes_ : int
        The number of classes.
    
    classes_ : array-like of shape (n_classes,)
        The class labels.
    
    n_features_ : int
        The number of features when `fit` is performed.
    
    feature_importances_ : array-like of shape (n_features,)
        The feature importances based on the amount of criterion reduction achieved.
    """

    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'MultiNodeCategoricalDecisionTree':
        """
        Build a multi-node categorical decision tree classifier from the training set (X, y).

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The training input samples.
        y : array-like of shape (n_samples,)
            The target values (class labels).

        Returns
        -------
        self : object
            Fitted estimator.
        """
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        
        # Store the classes seen during fit
        self.classes_ = np.unique(y)
        self.n_classes_ = len(self.classes_)
        self.n_features_ = X.shape[1]

        # Build the tree
        self.tree_ = self._build_tree(X, y)

        # Calculate feature importances
        self.feature_importances_ = self._calculate_feature_importances()

        return self

    def _build_tree(self, X: np.ndarray, y: np.ndarray, depth: int = 0) -> Dict[str, Any]:
        
        pass

    def _best_split(self, X: np.ndarray, y: np.ndarray) -> Dict[str, Any]:
        """
        Find the best split for a node.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The training input samples.
        y : array-like of shape (n_samples,)
            The target values (class labels).

        Returns
        -------
        best_split : dict
            A dictionary containing information about the best split.
        """
        # TODO: Implement the best split selection logic
        pass

    def _calculate_feature_importances(self) -> np.ndarray:
        """
        Calculate feature importances based on the tree structure.

        Returns
        -------
        feature_importances : array-like of shape (n_features,)
            The feature importances.
        """
        # TODO: Implement feature importance calculation
        pass

    def _calculate_entropy(self, y: np.ndarray) -> float:
        val,counts = np.unique(y, return_counts=True)
        all = counts.sum()
        probabilities = counts / all
    
        result = -np.sum(probabilities * np.log2(probabilities))
        return result


    def _calculate_gini(self, y: np.ndarray) -> float:
        val,counts = np.unique(y ,return_counts=True)
        all = counts.sum()
        probabilities = counts / all
    
        result = 1 - np.sum(np.pow(probabilities , 2))
        return result
     
    def _calculate_feature_entropy(self, X: np.ndarray, y: np.ndarray, feature_idx: int) -> float:
        feature = X[:,feature_idx]
        vals,counts = np.unique(feature , return_counts=True)
        all = counts.sum()
        result = 0.0
        
        for val,count in zip(vals , counts):
            cur_y = y[val]
            cur_entropy = self._calculate_entropy(cur_y)
            result += (count / all) * cur_entropy
        
            return result

    def _calculate_feature_gini(self, X: np.ndarray, y: np.ndarray, feature_idx: int) -> float:
        feature = X[:,feature_idx]
        vals,counts = np.unique(feature , return_counts=True)
        all = counts.sum()
        result = 0.0
        
        for val,count in zip(vals , counts):
            cur_y = y[val]
            cur_entropy = self._calculate_gini(cur_y)
            result += (count / all) * cur_entropy
        
            return result


    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class for X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y : array-like of shape (n_samples,)
            The predicted classes.
        """
        check_is_fitted(self)
        X = check_array(X)
        return np.array([self._predict_single(x) for x in X])

    def _predict_single(self, x: np.ndarray) -> Any:
        """
        Predict class for a single sample.

        Parameters
        ----------
        x : array-like of shape (n_features,)
            The input sample.

        Returns
        -------
        y : Any
            The predicted class.
        """
        # TODO: Implement the prediction logic for a single sample
        pass