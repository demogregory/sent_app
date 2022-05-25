#### Sentiment analysis application

#### Import packages
import streamlit as st
from textblob import TextBlob


#### Add header to describe app
st.markdown("# Welcome to my sentiment analysis app!") 
st.markdown("---") 
st.markdown("#### Please enter a word or phrase below and we will determine the sentiment for you!")

#### Create text input box and save incoming text to variable called text
text = st.text_input("Please tell us how you feel:", value = "Enter text here")

#### TextBlob to analyze input text
score = TextBlob(text).sentiment.polarity

# Create label (called sent) from TextBlob polarity score to use in summary below
if score > 0.0:
    sent = "positive"
elif score == 0.0:
    sent = "neutral"
else:
    sent = "negative"

#### Print sentiment score and sent label
st.markdown(f"We have determined that your score of {round(score, 2)} exhibits a **{sent}** sentiment")
st.markdown(f"Note: sentiment scores range from -1 (negative) to 1 (positive)")

st.markdown("### Thank you for using our app.")
st.markdown("#### Please keep in touch!")