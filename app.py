from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/<name>/<age>')
def index(name, age):
    url = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-12-15&sortBy=publishedAt&apiKey=######'
   
    response = requests.get(url)
    content = response.json()
    return render_template('index.html',
                           name=name,
                           age=age,
                           news=content['articles'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)