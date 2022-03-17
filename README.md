# Milestone 1

Milestones ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Full Time Program khususnya pada Artificial Neural Network.

---

By [Rifky Aliffa](https://github.com/Penzragon)

![Image](https://atrium.ai/wp-content/uploads/2021/07/What-stops-customer-churn-Having-a-centralized-data-hub-does-and-heres-why.jpeg)

## Dashboard

Untuk melihat halaman dashboard dari project, dapat ditekan pada tombol di bawah ini.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://rifkyaliffa-churn-prediction.herokuapp.com/)

Atau

```
https://rifkyaliffa-churn-prediction.herokuapp.com
```

## Dataset

Pada project ini dataset yang digunakan data customer dari sebuah perusahaan telephone. Dataset ini berisi 7043 baris dengan 21 kolom yang diantaranya adalah customerID, gender, seniorCitizen, partner, dependents, dan masih banyak lagi. Dataset dapat dilihat di [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn).

Keterangan dari kolom dataset adalah:

| Feature          | Description                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| customerID       | Customer ID                                                                                                        |
| gender           | Whether the customer is a male or a female                                                                         |
| SeniorCitizen    | Whether the customer is a senior citizen or not (1, 0)                                                             |
| Partner          | Whether the customer has a partner or not (Yes, No)                                                                |
| Dependents       | Whether the customer has dependents or not (Yes, No)                                                               |
| tenure           | Number of months the customer has stayed with the company                                                          |
| PhoneService     | Whether the customer has a phone service or not (Yes, No)                                                          |
| MultipleLines    | Whether the customer has multiple lines or not (Yes, No, No phone service)                                         |
| InternetService  | Customer’s internet service provider (DSL, Fiber optic, No)                                                        |
| OnlineSecurity   | Whether the customer has online security or not (Yes, No, No internet service)                                     |
| OnlineBackup     | Whether the customer has online backup or not (Yes, No, No internet service)                                       |
| DeviceProtection | Whether the customer has device protection or not (Yes, No, No internet service)                                   |
| TechSupport      | Whether the customer has tech support or not (Yes, No, No internet service)                                        |
| StreamingTV      | Whether the customer has streaming TV or not (Yes, No, No internet service)                                        |
| StreamingMovies  | Whether the customer has streaming movies or not (Yes, No, No internet service)                                    |
| Contract         | The contract term of the customer (Month-to-month, One year, Two year)                                             |
| PaperlessBilling | Whether the customer has paperless billing or not (Yes, No)                                                        |
| PaymentMethod    | The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) |
| MonthlyCharges   | The amount charged to the customer monthly                                                                         |
| TotalCharges     | The total amount charged to the customer                                                                           |
| Churn            | Whether the customer churned or not (Yes or No)                                                                    |

## Objectives

**Milestones 1** ini dibuat guna mengevaluasi Pembelajaran Phase 2 :

- Mampu memahami konsep Artificial Neural Network.
- Mampu mempersiapkan data untuk digunakan dalam model Artificial Neural Network.
- Mampu mengimplementasikan Artificial Neural Network dengan data yang diberikan.
- Mampu menganalisis dan menjelaskan layer yang dibuat.
