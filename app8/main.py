from cProfile import label
import streamlit as st
import glob
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

analyser=SentimentIntensityAnalyzer()

filepaths=sorted(glob.glob("diary/*.txt"))

pos=[]

neg=[]

for filepath in filepaths:
    print(filepath)
    with open(filepath,"r") as file:
        content=file.read()
    scores=analyser.polarity_scores(content)
    pos.append(scores['pos'])
    print(scores)
    neg.append(scores['neg'])

dates=[filepath.strip('.txt').strip("diary\\") for filepath in filepaths]


st.header("Diary Tone")

print(pos,neg)

st.subheader("Positivity Across Days")

plotly=px.line(x=dates,y=pos,labels={'x':'Dates','y':'Positivity'})

st.plotly_chart(plotly)


st.subheader("Negativity Across Days")

plotly=px.line(x=dates,y=neg,labels={'x':"Dates",'y':"negativity"})

st.plotly_chart(plotly)