import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle


def app():
    st.title("Churn Prediction")

    model = tf.keras.models.load_model("model.h5")
    with open("preprocessor.pkl", "rb") as f:
        preprocessor = pickle.load(f)

    st.write("Basic Data")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("Customer Gender", ["Male", "Female"])
    with col2:
        seniorCitizen = st.selectbox("Senior Citizen", ["Yes", "No"])
    with col3:
        partner = st.selectbox("Do the customer has partner?", ["Yes", "No"])
    with col4:
        dependent = st.selectbox("Does the customer has dependent?", ["Yes", "No"])
    tenure = st.number_input(
        "How many months the customer has been a customer?", min_value=1
    )

    st.write("Phone Service")
    col5, col6 = st.columns(2)
    with col5:
        phoneService = st.selectbox("Phone Service", ["No", "Yes"])
    if phoneService == "Yes":
        with col6:
            multipleLines = st.selectbox("Multiple Lines", ["No", "Yes"])
    else:
        multipleLines = "No phone service"

    st.write("Internet Service")
    internetService = st.selectbox(
        "Internet Service Provider", ["No", "DSL", "Fiber optic"]
    )
    if internetService != "No":
        col7, col8, col9, col10 = st.columns(4)
        with col7:
            onlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
        with col8:
            onlineBackup = st.selectbox("Online Backup", ["Yes", "No"])
        with col9:
            deviceProtection = st.selectbox("Device Protection", ["Yes", "No"])
        with col10:
            techSupport = st.selectbox("Tech Support", ["Yes", "No"])
        st.write("Streaming Service")
        col11, col12 = st.columns(2)
        with col11:
            streamingTV = st.selectbox("Streaming TV", ["Yes", "No"])
        with col12:
            streamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"])
    else:
        onlineSecurity = (
            onlineBackup
        ) = (
            deviceProtection
        ) = techSupport = streamingTV = streamingMovies = "No internet service"

    st.write("Contract")
    col13, col14, col15 = st.columns(3)
    with col13:
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    with col14:
        paperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    with col15:
        paymentMethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)",
            ],
        )

    st.write("Charges")
    col16, col17 = st.columns(2)
    with col16:
        monthlyCharges = st.number_input("Monthly Charges", min_value=20)
    with col17:
        totalCharges = st.number_input("Total Charges", min_value=0)

    predict = st.button("Predict")
    if predict:
        data = {
            "gender": gender,
            "SeniorCitizen": seniorCitizen,
            "Partner": partner,
            "Dependents": dependent,
            "tenure": tenure,
            "PhoneService": phoneService,
            "MultipleLines": multipleLines,
            "InternetService": internetService,
            "OnlineSecurity": onlineSecurity,
            "OnlineBackup": onlineBackup,
            "DeviceProtection": deviceProtection,
            "TechSupport": techSupport,
            "StreamingTV": streamingTV,
            "StreamingMovies": streamingMovies,
            "Contract": contract,
            "PaperlessBilling": paperlessBilling,
            "PaymentMethod": paymentMethod,
            "MonthlyCharges": monthlyCharges,
            "TotalCharges": totalCharges,
        }
        data = pd.DataFrame(data, index=[0])
        data = preprocessor.transform(data)
        prediction = model.predict(data).round()
        if prediction == 1:
            st.write("The customer will leave the company")
        else:
            st.write("The customer will stay in the company")
