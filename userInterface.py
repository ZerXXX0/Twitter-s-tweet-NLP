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
    result_nb, result_svm, acuracy_nb, acuracy_svm = predict_word(textToPredict)
    # Display the predictions
    st.write(f"Predicted Sentiment (Naive Bayes) - {acuracy_nb} : {result_nb}")
    st.write(f"Predicted Sentiment (Linear SVM) - {acuracy_svm} : {result_svm}")