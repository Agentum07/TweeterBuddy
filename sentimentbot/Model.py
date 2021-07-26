import tweepy
from textblob import TextBlob
from textblob import Word
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re 
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import urllib
import requests
import nltk

def inputs():
    flag = True
    lines2 = []
    while flag:
      val = input("Enter the text: ")
      lines2.append(val)
      ans = input("Do u want to enter another tweet y/n? ")
      flag = ans == 'y'

    df = pd.DataFrame({'Tweets' : lines2})
    
    df['Tweets'] = df['Tweets'].apply(cleanText)
    
    df['Polarity'] = df['Tweets'].apply(getPolarity)
    
    df['Analysis'] = df['Polarity'].apply(getAnalysis)

    sortedDf = printHistory(df, True)
    
    return (str(sortedDf))

def input(text):
    
    lines2 = []
    lines2.append(text)
    df = pd.DataFrame({'Tweets' : lines2})
    
    df['Tweets'] = df['Tweets'].apply(cleanText)
    
    df['Polarity'] = df['Tweets'].apply(getPolarity)
    
    df['Analysis'] = df['Polarity'].apply(getAnalysis)
    
    return (str(df.at[0, 'Analysis']))

#Clean the text
def cleanText(text):
  text = re.sub(r'@[A-za-z0-9]+' , '', text) #Remove mentions
  text = re.sub(r'RT[\s]+', '', text) #remove retweets
  text = re.sub(r'https?:\/\/\S+', '', text) #remove hyperlinks

  return text 

#Create a function to get the subjectivity
def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity 

#Create a function to get polarity
def getPolarity(text):
  return TextBlob(text).sentiment.polarity

#Create a fn to compute the negative, neutral and positive analysis
def getAnalysis(score):
  if score < - 0.2:
    return 'Negative'
  elif score > 0.2:
    return 'Positive'
  else: 
    return 'Neutral'

def printHistory(df, asc = True, num = 5):
  sortedDF = df.sort_values(by = ['Polarity'], axis=0, ascending = asc)
  sortedDF = sortedDF.reset_index(drop=True)
  sortedDF = sortedDF[['Tweets', 'Analysis']].iloc[:num]
  return sortedDF
  
  
inputs()
