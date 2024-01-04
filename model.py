# Load Data

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
import re
#import cmudictloss = criteon(logits, y)

import torch
from transformers import BertTokenizer, BertModel, BertConfig,BertForSequenceClassification, AdamW
# from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
from torch.utils.data import DataLoader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler