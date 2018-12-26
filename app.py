from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)

app = Flask(__name__)


from mongo import find_, insert_, insert_new, findOrigin
from regular import *
from utilis import format_time





@app.route('/<int:now>/')
def hello_world(now):
    id = now
    before = find_(id, "before")
    after = find_(id, "after")
    percent_before = find_(id, "percent_before")
    percent_after = find_(id, "percent_after")
    name = find_(id, "index")
    return render_template('index.html', before = before, after = after, percent_before = percent_before, percent_after = percent_after, name = name, id = id)


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
            a = final(before)
            percent_a = percent(a)
            b = final(after)
            percent_b = percent(b)
            time = format_time()
            insert_(id, "time", time)
            insert_(id, "before",a)
            insert_(id, "after", b)
            insert_(id, "percent_before", percent_a)
            insert_(id, "percent_after", percent_b)
            print("before: {}; after: {}".format(a, b))
            print('*'*30)
            return render_template('re.txt')
        else:
            print("data form is wrong")
            return "invalid data form"
    elif request.method == "GET":
        before = find_(id, "before")
        after = find_(id, "after")
        percent_before = find_(id, "percent_before")
        percent_after = find_(id, "percent_after")
        name = find_(id, "index")
        return render_template("test.txt", before = before, after = after, percent_before = percent_before, percent_after = percent_after, name = name)


@app.route("/co2/data", methods=['GET', 'POST'])
def co2_data():
    id = int(request.args.get("id"))
    after = findOrigin(id, "after")
    return str(after[2])


@app.route("/co2/<int:id>", methods=['GET', 'POST'])
def co2(id):
    id = int(id)
    after = findOrigin(id, "after")
    data = after[2]
    return render_template("co2.html", id = id, data = data)


@app.route("/index", methods=['GET', 'POST'])
def index():
    id = 2
    before = find_(id, "before")
    after = find_(id, "after")
    import json
    list = before + after
    return (json.dumps(list))


@app.route('/tool')
def tool():
    return render_template('form.html')


@app.route('/myip', methods=['GET'])
def get_my_ip():
    ip = request.headers['X-Forwarded-For']
    return jsonify({'ip': ip}), 200


if __name__ == '__main__':
    config = dict(
        host ='0.0.0.0',
        port = 80,
        debug = True,
    )
    app.run()
