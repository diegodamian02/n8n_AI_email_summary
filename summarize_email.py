
from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key="AIzaSyDg2yDd4XKcHdRkDfYDEtYL5mjB02E-PSg")

model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    email_body = data.get("email_body", "")
    response = model.generate_content(
        f"Summarize the following email in 3-4 sentences:\n\n{email_body}"
        )

    return jsonify({"summary:": response.text.strip()})

if __name__ == '__main__':
    app.run(debug=True)


