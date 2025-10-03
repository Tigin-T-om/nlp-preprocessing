from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyCG913HwbuGonb3_DaNKEMTSUIsKBm4QlY"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route('/', methods=['GET', 'POST'])
def index():
    poem = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            data = {
                "contents": [
                    {"parts": [{"text": f"Write a short poem about {prompt}"}]}
                ]
            }
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": API_KEY
            }
            response = requests.post(API_URL, json=data, headers=headers)
            if response.ok:
                result = response.json()
                try:
                    poem = result['candidates'][0]['content']['parts'][0]['text']
                except Exception:
                    poem = "No poem generated."
            else:
                try:
                    error_info = response.json()
                    poem = f"API error: {error_info}"
                except Exception:
                    poem = f"API error: {response.text}"
    return render_template('index.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)
