import sys
import json
import google.generativeai as genai

email_body = sys.stdin.read()

genai.configure(api_key="AIzaSyACVKbyIjtXbf_e6QzX_r17bTKVx6fougs")

model = genai.GenerativeModel("gemini-2.0-flash")

#prompt
response = model.generate_content(
    f"Summarize the following email in 3-4 sentences:\n\n{email_body}"
)

#extract the generated summary

summary = response.text.strip()

#output as JSON
print(json.dumps({"summary": summary}))
