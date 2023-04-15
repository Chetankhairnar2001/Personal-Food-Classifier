from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/Chetan007/Personal-Food-Classifier"
headers = {"Authorization": "Bearer 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"}


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
  # Check if the image file was uploaded
  if 'image' not in request.files:
    return redirect(url_for('index'))

  image = request.files['image']
  # Check if the image file has a valid extension
  if image.filename.split('.')[-1] not in {'jpg', 'jpeg', 'png'}:
    return redirect(url_for('index'))

  # Pass the image to the Hugging Face API
  response = requests.post(API_URL, headers=headers, data=image.read())

  prediction = response.json()
  ans = ((prediction[0]['label']))
  prediction_string = json.dumps(ans)

  # Display the result in a new page
  return render_template('result.html', prediction_string=prediction_string)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000, debug=True)
