from flask import Flask,request,render_template
import requests

app = Flask(__name__)

url =' https://api.thecatapi.com/v1/images/search'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    nome = request.form.get('nome', None)

    if not nome:
        return render_template('index.html', erro='Você precisa informar um nome!')
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        url_img = data[0]['url']
        return render_template('index.html', nome=nome, url_img=url_img)
    else:
        return render_template('index.html', erro='Erro no sistema, o gato sumiu!')




if __name__ == '__main__':
    app.run(debug=True)