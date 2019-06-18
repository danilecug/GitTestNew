import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pdb
import pickle as pkl
import scipy as sp 

def plot_figure(list_data):
    index = [i for i in range(len(list_data))]
    plt.plot(index, list_data, 'r-')
    plt.show()


