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
        "<h1 style='text-align: center'>☎️ Telco Customer Churn Prediction ☎️</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="text-align: center">This simple app is a project about customer churn prediction using <strong>Artificial Neural Network</strong>🤖.<br><br></p>',
        unsafe_allow_html=True,
    )

    # CUSTOMER BASIC INFORMATION SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Basic Customer Information</h3>',
        unsafe_allow_html=True,
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("👩 Customer Gender 👨", ["Male", "Female"])
    with col2:
        seniorCitizen = st.selectbox(
            "👵 Is the customer a senior citizen? 👴", ["No", "Yes"]
        )
    with col3:
        partner = st.selectbox("🧍 Do the customer has partner? 👫", ["No", "Yes"])
    with col4:
        dependent = st.selectbox(
            " 🙍‍♂️Does the customer has dependent? 👨‍👩‍👧‍👦", ["No", "Yes"]
        )
    tenure = st.number_input(
        "How many months the customer has been a customer? 📅", min_value=1
    )

    # CUSTOMER PHONE SERVICE SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Phone Service</h3>', unsafe_allow_html=True
    )
    col5, col6 = st.columns(2)
    with col5:
        phoneService = st.selectbox("Phone Service 📞", ["No", "Yes"])
    if phoneService == "Yes":
        with col6:
            multipleLines = st.selectbox("Multiple Lines 📠", ["No", "Yes"])
    else:
        multipleLines = "No phone service"

    # CUSTOMER INTERNET SERVICE SECTION
    st.markdown(
        '<hr><h3 style="text-align: center">Internet Service</h3>',
        unsafe_allow_html=True,
    )
    internetService = st.selectbox(
        "Internet Service Provider 🌐 ", ["No", "DSL", "Fiber optic"]
    )

    # CUSTOMER ADDITIONAL SERVICE SECTION
    if internetService != "No":
        st.markdown(
            '<hr><h4 style="text-align: center">Protection Service</h4>',
            unsafe_allow_html=True,
        )
        col7, col8, col9, col10 = st.columns(4)
        with col7:
            onlineSecurity = st.selectbox("Online Security 👮", ["No", "Yes"])
        with col8:
            onlineBackup = st.selectbox("Online Backup 🗄️", ["No", "Yes"])
        with col9:
            deviceProtection = st.selectbox("Device Protection 📱", ["No", "Yes"])
        with col10:
            techSupport = st.selectbox("Tech Support 👨‍🔧", ["No", "Yes"])
        st.markdown(
            '<hr><h4 style="text-align: center">Streaming Service</h4>',
            unsafe_allow_html=True,
        )
        col11, col12 = st.columns(2)
        with col11:
            streamingTV = st.selectbox("Streaming TV 📺", ["No", "Yes"])
        with col12:
            streamingMovies = st.selectbox("Streaming Movies 🍿", ["No", "Yes"])
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
            "Contract 📜", ["Month-to-month", "One year", "Two year"]
        )
    with col14:
        paperlessBilling = st.selectbox("Paperless Billing 📄", ["Yes", "No"])
    with col15:
        paymentMethod = st.selectbox(
            "Payment Method 💳",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)",
            ],
        )
    col16, col17 = st.columns(2)
    with col16:
        monthlyCharges = st.number_input("Monthly Charges 💵", min_value=20)
    with col17:
        totalCharges = st.number_input("Total Charges 💰", min_value=0)

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
        predict = st.button("Predict 🧠")

    # PREDICTION SECTION
    if predict:
        data_df = pd.DataFrame(data, index=[0])  # convert dict to dataframe

        data_df = preprocessor.transform(data_df)  # preprocess data

        prediction = model.predict(data_df).round()  # predict

        if prediction == 1:
            # if customer is likely to churn
            st.markdown(
                '<h2 style="text-align: center">🚨 The customer will <span style="color: red">leave</span> the company! 🚨</h2>',
                unsafe_allow_html=True,
            )
        else:
            # if customer is likely to stay
            st.markdown(
                '<h2 style="text-align: center">🎊 The customer will <span style="color: green">stay</span> in the company! 🎊</h2>',
                unsafe_allow_html=True,
            )

    # note:
    # 1 is likely to churn
    # 0 is likely to stay
