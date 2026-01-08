Customer Churn Prediction – AI Assignment

Project Overview : 
This project is a Machine Learning–based Customer Churn Prediction system developed as part of an AI Developer assignment.
The objective is to predict whether a bank customer is likely to leave the service based on their demographic and financial details.
The project demonstrates the complete AI workflow, including data preprocessing, model building, evaluation, explanation, and deployment using a REST API.

Dataset:
Dataset Name: Churn_Modelling.csv
Target Column: Exited
0 → No Churn
1 → Churn

Features Used :
CreditScore
Geography (One-Hot Encoded)
Gender (Label Encoded)
Age
Tenure
Balance
NumOfProducts
HasCrCard
IsActiveMember
EstimatedSalary
The columns RowNumber, CustomerId, and Surname were removed as they do not contribute to churn prediction.

Data Preprocessing : 
Verified and handled missing values
Encoded categorical variables
Applied feature scaling using StandardScaler
Split the dataset into training and testing sets

Models Implemented :
Two classification models were trained and evaluated:
Logistic Regression
Random Forest Classifier

Evaluation Metrics :
Accuracy
Precision
Recall
F1-Score
After comparison, Random Forest was selected as the final model due to its better performance, especially in recall and F1-score.

Model Explanation : 
Why Random Forest?
Random Forest was chosen because:
It handles non-linear relationships effectively
It captures feature interactions better than linear models
It performs well on moderately imbalanced datasets

Feature Impact
Key features that strongly influence churn prediction include:
Age
IsActiveMember
Balance
NumOfProducts
Geography

Possible Improvements :
Handle class imbalance using SMOTE
Perform hyperparameter tuning
Try advanced models such as XGBoost or LightGBM
Additional feature engineering

API Deployment (Flask) :
The trained model is deployed as a REST API using Flask.
 
Available Endpoints
/ → Health check
/predict → Returns churn prediction

Sample Input
{
  "CreditScore": 650,
  "Gender": 1,
  "Age": 40,
  "Tenure": 5,
  "Balance": 60000,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000,
  "Geography_Germany": 0,
  "Geography_Spain": 1
}

Sample Output
{
  "prediction": "No Churn",
  "probability": 0.12
}


Setup Instructions :
1. Clone the Repository
git clone https://github.com/Im-Ashvin/customer-churn-prediction.git
cd customer-churn-prediction

2. Install Dependencies
pip install -r requirements.txt

3. Run the API
python app.py

The API will be available at:
http://127.0.0.1:5000

4. Test the Prediction Endpoint
Send a POST request to:
http://127.0.0.1:5000/predict

Conclusion :
This project presents a complete and practical AI solution for customer churn prediction.
It covers data preprocessing, model development, evaluation, explanation, and deployment in a clean and professional manner using Flask.
