import pandas as pd
import re
import sqlite3

import nltk #Natural Language Tool Kit for pre-processing
# nltk.download('omw-1.4')
# nltk.download('stopwords') #Stopwords removal
# nltk.download('wordnet') #To find Synonyme & Antonyme
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
stopwords.extend(['advanced', 'intelligent', 'multidisciplinary', 'systems', 'aims', 'lab'])
from nltk.stem import WordNetLemmatizer #Lemmatization
lemmatizer = WordNetLemmatizer()

import spacy
# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en_core_web_lg')

