from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            return render_template('index.html', message=f'Text "{text}" has been spoken!')
    return render_template('index.html', message=None)

if __name__ == '__main__':
    app.run(debug=True)
