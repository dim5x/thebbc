from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    try:
        res1 = requests.get('https://github.com/')
        res2 = requests.get('https://ria.ru/')
        res3 = requests.get('https://google.com')
        return 'hello' + str(res1.status_code) + str(res2.status_code) + str(res3.status_code)
    except:
        return 'Error'

if __name__=="__main__":
    app.run(debug=True)
    
