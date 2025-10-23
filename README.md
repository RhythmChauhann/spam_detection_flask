# Spam or Ham Email Classifier

A machine learning project that classifies email addresses as **Spam** or **Ham** using a combination of **LSTM embeddings** and **Logistic Regression**. The project also includes a **Flask web app** to interact with the model in real-time.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Model Architecture](#model-architecture)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Technologies Used](#technologies-used)  
- [Author](#author)  
- [License](#license)  

---

## Overview

This project demonstrates a practical approach to detecting spam email addresses using deep learning and classical machine learning. The LSTM layer converts email text into embeddings, which are then used by a Logistic Regression model to predict whether an email is spam or not. The model achieves **93% accuracy** on the hand-crafted dataset.

---

## Features

- LSTM-based character embeddings of email addresses.  
- Logistic Regression for binary classification (Spam/Ham).  
- Flask web application for easy user interaction.  
- Models saved using **Joblib** for easy deployment.  
- High accuracy (93%) with a compact, character-level representation.  

---

## Dataset

- Total emails: **10,000**  
- Categories: **Spam** and **Ham**  
- Data Type: Hand-crafted  
- Maximum character length per email: **30**  
- Data split can be customized for training/testing  

---

## Model Architecture

1. **Embedding Layer**: Converts each email address into a sequence of characters.  
2. **LSTM Layer**: Extracts sequential features from the character-level embeddings.  
3. **Logistic Regression**: Classifies the LSTM embeddings into Spam or Ham.  
4. **Max Padding Length**: 30 characters for uniform input size.  

---

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>


2. Create a virtual environment (optional but recommended):

    ```bash
    Copy code
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    
3. Install dependencies:

    ```bash
    Copy code
    pip install -r requirements.txt
---

## Usage

Run the Flask app:

    ```bash
    Copy code
    python app.py
Open your browser and navigate to:http://127.0.0.1:5000/

Enter an email address to classify as Spam or Ham.

---
## Project Structure

 
    spam-ham-classifier/
    ├── app.py                   # Flask application
    ├── models/
    │   ├── lstm_model.h5        # Trained LSTM model
    │   ├── logistic_model.joblib# Trained Logistic Regression model
    │   └── tokenizer.joblib     # Tokenizer used for embedding
    ├── templates/
    │   └── index.html           # Frontend HTML page
    ├── static/                  # CSS/JS if any
    ├── README.md                # Project documentation
    └── requirements.txt         # Python dependencies

---
## Technologies Used
-
  Python 3.x
  Flask
  TensorFlow / Keras
  scikit-learn
  Joblib
---
# Author: Rhythm Chauhan

-
License
This project is licensed under the MIT License. See the LICENSE file for details.
