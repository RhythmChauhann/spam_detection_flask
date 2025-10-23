from flask import Flask, render_template, request
from tensorflow.keras.models import load_model,Model
import joblib
import numpy as np


loaded_lstm = load_model("models/lstm_model.h5")
embedding_model = Model(inputs=loaded_lstm.input, outputs=loaded_lstm.get_layer(index=-2).output)
loaded_clf = joblib.load("models/logistic_model.joblib")
loaded_tokenizer = joblib.load("models/tokenizer.joblib")


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']

        seq = loaded_tokenizer.texts_to_sequences([message])
        
        
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        padded_seq = pad_sequences(seq, maxlen=30)  
        
        X_embed = embedding_model.predict(padded_seq)

        
        pred = loaded_clf.predict(X_embed)[0]
        
        result = "SPAM" if pred == 1 else "NOT SPAM"
        return render_template('index.html', prediction_text=result, message=message)

if __name__ == "__main__":
    app.run(debug=True)
