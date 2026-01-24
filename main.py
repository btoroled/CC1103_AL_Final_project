import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


brca_dataset = load_breast_cancer()

X = pd.DataFrame(brca_dataset.data, columns=brca_dataset.feature_names)
Y = pd.Series(brca_dataset.target, name='clase')

