from flask import (
    Flask,
    render_template,
    request,
)

app = Flask(__name__)

from mongo import find, insert


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test',methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        data = str(find())
        print(data)
        return '{' + data + '}'
    elif request.method == 'POST':
        data = request.args.get('index', '')
        my = request.form.get('index')
        print('my',my)
        # data = request.form.get('index', '')
        print(data)
        insert(data)
        return ''
    else:
        return 'nothing'

@app.route('/figure',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        data = request.args.get('index', '')
        print(data)
        return ''
        # insert(data)

@app.route('/tool')
def tool():
    return render_template('form.html')


if __name__ == '__main__':
    config = dict(
        host ='0.0.0.0',
        port = 80,
        debug = True,
    )
    app.run()
