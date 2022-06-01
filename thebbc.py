from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/41.0.2228.0 Safari/537.3'}
        res1 = requests.get('https://github.com/', headers=headers)
        res2 = requests.get('https://ria.ru/', headers=headers)
        res3 = requests.get('https://google.com', headers=headers)
        
        return f'''hello
        Github = {str(res1.status_code)} 
        Ria = {str(res2.status_code)}
        Google = {str(res3.status_code)}
        '''
    except:
        return 'Error'

if __name__=="__main__":
    app.run(debug=True)
    
