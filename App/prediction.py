import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle


def app():
    model = tf.keras.models.load_model("model.h5")
    with open("preprocessor.pkl", "rb") as f:
        preprocessor = pickle.load(f)

    # HEADER SECTION
    st.markdown(
        "<h1 style='text-align: center'>βοΈ Telco Customer Churn Prediction βοΈ</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="text-align: center">This simple app is a project about customer churn prediction using <strong>Artificial Neural Network</strong>π€.<br><br></p>',
        unsafe_allow_html=True,
    )

    # CUSTOMER BASIC INFORMATION SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Basic Customer Information</h3>',
        unsafe_allow_html=True,
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("π© Customer Gender π¨", ["Male", "Female"])
    with col2:
        seniorCitizen = st.selectbox(
            "π΅ Is the customer a senior citizen? π΄", ["No", "Yes"]
        )
    with col3:
        partner = st.selectbox("π§ Do the customer has partner? π«", ["No", "Yes"])
    with col4:
        dependent = st.selectbox(
            " πββοΈDoes the customer has dependent? π¨βπ©βπ§βπ¦", ["No", "Yes"]
        )
    tenure = st.number_input(
        "How many months the customer has been a customer? π", min_value=1
    )

    # CUSTOMER PHONE SERVICE SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Phone Service</h3>', unsafe_allow_html=True
    )
    col5, col6 = st.columns(2)
    with col5:
        phoneService = st.selectbox("Phone Service π", ["No", "Yes"])
    if phoneService == "Yes":
        with col6:
            multipleLines = st.selectbox("Multiple Lines π ", ["No", "Yes"])
    else:
        multipleLines = "No phone service"

    # CUSTOMER INTERNET SERVICE SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Internet Service</h3>',
        unsafe_allow_html=True,
    )
    internetService = st.selectbox(
        "Internet Service Provider π ", ["No", "DSL", "Fiber optic"]
    )

    # CUSTOMER ADDITIONAL SERVICE SECTION
    if internetService != "No":
        st.markdown(
            '<hr><h4 style="text-align: center">Protection Service</h4>',
            unsafe_allow_html=True,
        )
        col7, col8, col9, col10 = st.columns(4)
        with col7:
            onlineSecurity = st.selectbox("Online Security π?", ["No", "Yes"])
        with col8:
            onlineBackup = st.selectbox("Online Backup ποΈ", ["No", "Yes"])
        with col9:
            deviceProtection = st.selectbox("Device Protection π±", ["No", "Yes"])
        with col10:
            techSupport = st.selectbox("Tech Support π¨βπ§", ["No", "Yes"])
        st.markdown(
            '<hr><h4 style="text-align: center">Streaming Service</h4>',
            unsafe_allow_html=True,
        )
        col11, col12 = st.columns(2)
        with col11:
            streamingTV = st.selectbox("Streaming TV πΊ", ["No", "Yes"])
        with col12:
            streamingMovies = st.selectbox("Streaming Movies πΏ", ["No", "Yes"])
    else:
        onlineSecurity = (
            onlineBackup
        ) = (
            deviceProtection
        ) = techSupport = streamingTV = streamingMovies = "No internet service"

    # CUSTOMER BILLING INFORMATION SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Billing Information</h3>',
        unsafe_allow_html=True,
    )
    col13, col14, col15 = st.columns(3)
    with col13:
        contract = st.selectbox(
            "Contract π", ["Month-to-month", "One year", "Two year"]
        )
    with col14:
        paperlessBilling = st.selectbox("Paperless Billing π", ["Yes", "No"])
    with col15:
        paymentMethod = st.selectbox(
            "Payment Method π³",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)",
            ],
        )
    col16, col17 = st.columns(2)
    with col16:
        monthlyCharges = st.number_input("Monthly Charges π΅", min_value=20)
    with col17:
        totalCharges = st.number_input("Total Charges π°", min_value=0)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Create dictionary with all customer information
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

    col18, col19, col20 = st.columns([1.7, 1, 1])
    with col19:
        predict = st.button("Predict π§ ")

    # PREDICTION SECTION
    if predict:
        data_df = pd.DataFrame(data, index=[0])  # convert dict to dataframe

        data_df = preprocessor.transform(data_df)  # preprocess data

        prediction = model.predict(data_df).round()  # predict

        if prediction == 1:
            # if customer is likely to churn
            st.markdown(
                '<h2 style="text-align: center">π¨ The customer will <span style="color: red">leave</span> the company! π¨</h2>',
                unsafe_allow_html=True,
            )
        else:
            # if customer is likely to stay
            st.markdown(
                '<h2 style="text-align: center">π The customer will <span style="color: green">stay</span> in the company! π</h2>',
                unsafe_allow_html=True,
            )

    # note:
    # 1 is likely to churn
    # 0 is likely to stay
