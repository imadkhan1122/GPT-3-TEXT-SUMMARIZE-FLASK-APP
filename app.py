#!python3

from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok
from transformers import pipeline
ngrok.set_auth_token('23oXDCziYTCYX2pL2NkkqrVJkhW_6zaph3KXRPv8WuqA7Ag62')
summarizer = pipeline("summarization")

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    if request.method == 'POST' and 'Text' in request.form:
        Text = str(request.form.get('Text'))
        No = int(request.form.get('number'))
        
        txt = summarize_text(Text, No)
        text = txt[0]['summary_text']
    return render_template("index.html",
	                        text=text)

def summarize_text(Text, No):
  summary = summarizer(Text, min_length=75, max_length=No)

  return summary

if __name__ == '__main__':
    app.run()