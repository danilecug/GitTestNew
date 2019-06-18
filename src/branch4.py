import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pd
import pickle as pkl

def read_file(file_path):
    with open(file_path, 'rb') as f:
        data = pkl.load(f)
    return data

