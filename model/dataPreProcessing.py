"""Reads in the train.csv and processes to right format for sentiment analysis"""

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

import plotly.offline as pyo

train_csv = pd.read_csv('../dataset/train.csv',  usecols=['drug','sentiment'])
drug_name = Counter(train_csv.drug)
drug_names = list(drug_name.keys())
pyo.plot([{'x': list(drug_name.keys()),'y':list(drug_name.values())}])


