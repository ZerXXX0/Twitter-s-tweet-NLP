import streamlit as st
import requests

def predict_word(text):
    response = requests.post("http://127.0.0.1:8000/docs#/predict_sentiment", json={"text": text})

    result_NB = response.json()["predicted_sentiment_nb"]
    result_SVM = response.json()["predicted_sentiment_svm"]
    accuracy_NB = response.json()["accuracy_nb"]
    accuracy_SVM = response.json()["accuracy_svm"]
    
    return result_NB, result_SVM, accuracy_NB, accuracy_SVM
    
st.title("Test API NLP")
textToPredict = st.text_area("input text","enter your input")

# Button to predict sentiment
if st.button("Predict Sentiment"):
    result_NB, result_SVM, accuracy_NB, accuracy_SVM = predict_word(textToPredict)
    # Display the predictions
    st.write(f"Predicted Sentiment (Naive Bayes) - {accuracy_NB} : {result_NB}")
    st.write(f"Predicted Sentiment (Linear SVM) - {accuracy_SVM} : {result_SVM}")