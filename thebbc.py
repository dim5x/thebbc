from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    res = requests.get('https://ria.ru/authors/')
    return 'hello' + res.status_code

if __name__=="__main__":
    app.run(debug=True)
    
