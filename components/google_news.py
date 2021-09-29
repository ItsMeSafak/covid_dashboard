from GoogleNews import GoogleNews
import streamlit as st
import random


def main():
    googlenews = GoogleNews(lang='nl', region='NL', period='7d')
    googlenews.search('Corona virus')
    news_dict = googlenews.result()
    if (len(news_dict) > 0):
        news_dict = news_dict[random.randint(0,9)]
        st.image('assets/google_log.png', width=50)
        st.header(news_dict['title'])
        st.caption(news_dict['media'] + ' - ' + news_dict['date'])
        st.write(news_dict['desc'])
        st.markdown('*Referentie: ' + news_dict['link'] + '*')
    


