"""Politician

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N4sUvPxKTYP1x4Bdp5KSNSZgwS_0-Qut
"""

#!git clone https://github.com/Inyrkz/Politician-db.git

import pandas as pd
METADATA = pd.read_csv('Politician DS.csv', encoding = 'latin-1')
# METADATA.head(3)

#Removing NaN values
METADATA = METADATA.fillna('')

#Convert the post column string
METADATA["Elected"] = METADATA["Elected"].astype(int).astype(str)

#Joining the other columns into one 
METADATA["General"] = METADATA["Position"] + " " + METADATA["Political Party"] + " " +  METADATA["Elected"]+ " " +  METADATA["Posts"]
# METADATA["General"].head()

#Importing Libraries
from sklearn.feature_extraction.text import TfidfVectorizer

#Define a TF-IDF Vectorizer object. Remove all english stopwords
TFIDF = TfidfVectorizer(stop_words = 'english')

#Construct the required TF-IDF matrix by fitting and transforming the data
TFIDF_MATRIX = TFIDF.fit_transform(METADATA["General"])

#Let's see the output shape of the matrix
# TFIDF_MATRIX.shape

#Importing liinear_kernel
from sklearn.metrics.pairwise import linear_kernel

#computing the cosine similarity matrix
COSINE_SIM = linear_kernel(TFIDF_MATRIX, TFIDF_MATRIX)

#Construct a reverse map of the indices and name
indices = pd.Series(METADATA.index, index = METADATA['Name']).drop_duplicates()
#print(indices)

def get_recommendations(name, COSINE_SIM = COSINE_SIM):
  '''Function that takes in a politician's name as input and output similar politicians'''

  #Get the index of the name
  idx = indices[name]

  #Get the pairwise similarity score of all names with that name
  sim_scores = list(enumerate(COSINE_SIM[idx]))

  #sort the names based on similarity scores
  sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)

  #Get the scores of the 10 most similar politicians
  sim_scores = sim_scores[1:11]

  #Get the names
  names = [i[0] for i in sim_scores] 

  #Return the top 10 similar politicians
  return list(METADATA['Name'].iloc[names].values[:])
    
#PNAME = input("Search Politician's name: ")
#print(get_recommendations('Moses Ekpo'))
