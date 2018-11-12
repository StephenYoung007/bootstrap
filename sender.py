import requests



url = 'http://localhost:8000/post'
d = {'key1': 'value1', 'key2': 'value2'}
msg = requests.post(url, data=d)


if __name__ == '__main__':
    print(msg.text)