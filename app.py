from flask import (
    Flask,
    render_template,
    request,
)
import random

app = Flask(__name__)

from mongo import find_, insert_, insert_new
from regular import *


@app.route('/')
def hello_world():
    id = 27017
    before = find_(id, "before")
    after = find_(id, "after")
    percent_before = find_(id, "percent_before")
    percent_after = find_(id, "percent_after")
    name = find_(id, "index")
    return render_template('index.html', before = before, after = after, percent_before = percent_before, percent_after = percent_after, name = name)

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
        # insert(data)
        return ''
    else:
        return 'nothing'

@app.route('/figure', methods=['GET', 'POST'])
def figure():
    li = int(request.args.get("id"))
    id = li
    if request.method == 'POST':
        insert_new(id)
        data = request.form
        print(data)
        before = data.get('before')
        after = data.get("after")
        print("*"*30)
        print("before", before)
        print("after", after)
        if ret(before) and ret(after):
            # print(group(before+','+after))
            a = final(before)
            percent_a = percent(a)
            b = final(after)
            percent_b = percent(b)
            # print(b)
            insert_(id, "before",a)
            insert_(id, "after", b)
            insert_(id, "percent_before", percent_a)
            insert_(id, "percent_after", percent_b)
            print("before: {}; after: {}".format(a, b))
            print('*'*30)
            # return render_template('re.txt', seq = find())
            return render_template('re.txt')
        else:
            print("data form is wrong")
            return "invalid data form"
    elif request.method == "GET":
        # id = 17017
        before = find_(id, "before")
        # print("before", before)
        after = find_(id, "after")
        percent_before = find_(id, "percent_before")
        percent_after = find_(id, "percent_after")
        name = find_(id, "index")
        return render_template("test.txt", before = before, after = after, percent_before = percent_before, percent_after = percent_after, name = name)

# return render_template("index.html")

# @app.route('/figure',methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         data = request.args.get('index', '')
#         print(data)
#         return ''
#         # insert(data)

@app.route("/index", methods=['GET', 'POST'])
def index():
    id = 17017
    before = find_(id, "before")
    # print("before", before)
    after = find_(id, "after")
    import json
    list = after + before
    # result = [{value * 2: value for value in i} for i in list]
    return (json.dumps(list))







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
