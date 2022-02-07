import pandas as pd
import numpy as np
import re
import contractions
import nltk

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer

from bs4 import BeautifulSoup

print("This is a text processing script, please input your csv file (don't include .csv): ")
tablename = input()
data = pd.read_csv(f"{tablename}.csv")

print("First 5 lines of your dataframe")
print(data.head(5))

# boolean list for deleted and removed comments
condition = data['body'].str.startswith(
    '[deleted]') & data['body'].str.startswith('[deleted]')
condition2 = data['body'].str.startswith(
    '[removed]') & data['body'].str.endswith('[removed]')

# indices where the comment is deleted
full_idx = np.arange(data.shape[0])
x1_idx = [i for i, j in enumerate(condition) if j]
x2_idx = [i for i, j in enumerate(condition2) if j]

x_idx = np.sort(x1_idx + x2_idx)
# set difference for indexing dataframe
filtered_idx = np.setdiff1d(full_idx, x_idx)

# dataframe with no [deleted] or [removed] comments
data_filter1 = data.iloc[filtered_idx, :]

print(
    "\nFirst 5 lines of your dataframe with no [deleted] or [removed] comments")
print(data_filter1.head())

# Replacing new line
data_filter1['body'] = data_filter1['body'].apply(
    lambda x: re.sub(r'\n', ' ', str(x)))

print("\nFirst 5 lines of your dataframe with no new line")
print(data_filter1.head())


# remove websites
data_filter1['body'] = data_filter1['body'].apply(
    lambda x: re.sub(r'http\S+', '', str(x)))

print("\nFirst 5 lines of your dataframe with no url's")
print(data_filter1.head())

# html parser
data_filter1['body'] = data_filter1['body'].apply(
    lambda x: BeautifulSoup(str(x), "html").text)

print("\nFirst 5 lines of your dataframe with no weird html tags")
print(data_filter1.head())

# removing mentions and emails
data_filter1['body'] = data_filter1['body'].apply(
    lambda x: re.sub(r'\S*@\S*\s?', ' ', str(x)))

print("\nFirst 5 lines of your dataframe with @'s or emails")
print(data_filter1.head())

# expand contraction
data_filter1['body'] = data_filter1['body'].apply(
    lambda x: contractions.fix(x))

print("\nFirst 5 lines of your dataframe with expanded contractions")
print(data_filter1.head())

# remove all that's not a letter
data_filter1['body'] = data_filter1['body'].apply(
    lambda x: re.sub(r'[^A-Za-z]+', ' ', str(x))).str.lower()

print("\nFirst 5 lines of your dataframe with only lowercased letters")
print(data_filter1.head())

# remove multiple spaces
data_filter1['body'] = data_filter1['body'].apply(
    lambda x: " ".join(x.split()))

print("\nFirst 5 lines of your dataframe with removed spaces")
print(data_filter1.head())

# Lemmatization

lemmatizer = WordNetLemmatizer()
wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, 
               "J": wordnet.ADJ, "R": wordnet.ADV}

def word_lemmatizer(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN))
    for word, pos in pos_tagged_text])

data_lemmatized = data_filter1['body'].apply(lambda x: word_lemmatizer(x))

print("\nFirst 5 lines of your dataframe after lemmatization")
print(data_lemmatized.head())

print("\nDone! This is your processed text, what will you name her?")

data_lemmatized.to_csv(f'{tablename}_p.csv', ',')












