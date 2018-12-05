from flask import Flask, request, render_template
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/send/', methods=['POST'])
def send_result():
    data = request.form.to_dict()

    if data['agree'] == 'Agree':
        agree = True
    else:
        agree = False
    mac = request.remote_addr
    out = {'mac_adress': mac,
           'agree': agree}
    requests.post('http://127.0.0.1:5002/api/', json=out)
    return 'Data send!'


if __name__ == '__main__':
    app.run()
