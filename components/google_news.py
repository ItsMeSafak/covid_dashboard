from GoogleNews import GoogleNews
import streamlit as st
import random

counter = 0

def main():
    global counter
    googlenews = GoogleNews(lang='nl', region='NL', period='7d')
    googlenews.search('Corona virus')
    print(random.randint(0,9))
    news_dict = googlenews.result()[0]
    print(news_dict)
    st.header(news_dict['title'])
    


