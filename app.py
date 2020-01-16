from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://newsapi.org/v2/top-headlines?country=sa&apiKey=######'

    response = requests.get(url)
    content = response.json()

    return render_template('index.html',
                           news=content['articles'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)