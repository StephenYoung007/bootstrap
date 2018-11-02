from flask import (
    Flask,
    render_template,
    request,
)
import random

app = Flask(__name__)

from mongo import find, insert
from regular import *


@app.route('/')
def hello_world():
    return render_template('index.html')

def generate():
    a = []
    for i in range(10):
        num = random.randint(10,100)
        a.append(num)
    return a



@app.route('/test',methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        # data = str(find())
        # index = [int(i) for i in data.split(",")]
        index = generate()
        print(index)
        return render_template("test.txt", a = index)
    elif request.method == 'POST':
        data = request.args.get('index', '')
        my = request.form.get('index')

        # data = request.form.get('index', '')
        print(data)
        insert(data)
        return ''
    else:
        return 'nothing'

@app.route('/figure', methods=['GET', 'POST'])
def figure():
    if request.method == 'POST':
        data = request.form
        before = data.get('before')
        after = data.get("after")
        if ret(before) and ret(after):
            print(group(before+','+after))
            a = final(before)
            percent_a = percent(a)
            b = final(after)
            percent_b = percent(b)
            print(b)
            insert("before",a)
            insert("after", b)
            insert("percent_before", percent_a)
            insert("percent_after", percent_b)
            name = ["CO2","甲醛","湿度","温度","PM2.5"]
            insert("index", name)
            print("before: {}; after: {}".format(a, b))
            print('*'*30)
            # return render_template('re.txt', seq = find())
            return render_template('re.txt')
        else:
            print("data form is wrong")
            return "invalid data form"
    elif request.method == "GET":
        before = find("before")
        print("before", before)
        after = find("after")
        percent_before = find("percent_before")
        percent_after = find("percent_after")
        name = find("index")
        return render_template("test.txt", before = before, after = after, percent_before = percent_before, percent_after = percent_after, name = name)

# return render_template("index.html")

# @app.route('/figure',methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         data = request.args.get('index', '')
#         print(data)
#         return ''
#         # insert(data)

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
