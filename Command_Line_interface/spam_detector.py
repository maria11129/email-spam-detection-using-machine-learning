import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
import joblib  # For saving and loading the model
import sys
import os  # To check if files exist


# Function to train and save the model
def train_model():
    # Load and preprocess data
    df = pd.read_csv('spam.csv', encoding='latin1')
    df.rename(columns={'v1': 'Category', 'v2': 'Message'}, inplace=True)
    data = df.where(pd.notnull(df), '')
    data.loc[data['Category'] == 'spam', 'Category'] = 0
    data.loc[data['Category'] == 'ham', 'Category'] = 1

    X = data['Message']
    Y = data['Category'].astype('int')
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

    # Feature extraction and oversampling
    feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    X_train_features = feature_extraction.fit_transform(X_train)
    X_test_features = feature_extraction.transform(X_test)

    smote = SMOTE(random_state=42)
    X_train_resampled, Y_train_resampled = smote.fit_resample(X_train_features, Y_train)

    # Train the model
    model = LogisticRegression()
    model.fit(X_train_resampled, Y_train_resampled)

    # Evaluate
    print(f"Training Accuracy: {accuracy_score(Y_train_resampled, model.predict(X_train_resampled)) * 100:.2f}%")
    print(f"Testing Accuracy: {accuracy_score(Y_test, model.predict(X_test_features)) * 100:.2f}%")

    # Save the model and vectorizer
    joblib.dump(model, 'spam_model.pkl')
    joblib.dump(feature_extraction, 'tfidf_vectorizer.pkl')

    print("Model and vectorizer saved successfully!")


# Function to load the model and predict
def predict_email(email):
    if not os.path.exists('spam_model.pkl') or not os.path.exists('tfidf_vectorizer.pkl'):
        print("Error: Trained model or vectorizer not found. Train the model first!")
        sys.exit(1)

    model = joblib.load('spam_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    email_features = vectorizer.transform([email])
    prediction = model.predict(email_features)
    return 'Ham' if prediction[0] == 1 else 'Spam'


if __name__ == "__main__":
    # If no email is provided as an argument, show an error
    if len(sys.argv) < 2:
        print("Error: Please provide an email to classify.")
        sys.exit(1)

    # Train the model if files are missing
    if not os.path.exists('spam_model.pkl') or not os.path.exists('tfidf_vectorizer.pkl'):
        print("Model files not found. Training the model...")
        train_model()

    # Classify the provided email
    email = sys.argv[1]
    result = predict_email(email)
    print(f"The email is classified as: {result}")
