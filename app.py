from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)


def most_frequent_word(x):
    f = Counter(x.replace('\n', ' ').replace('\r', ' ').split())
    max_value = 0
    max_word = ""
    for word in f:
        if max_value <= f[word]:
            max_value = f[word]
            max_word = word

    return max_word


@app.route('/')
@app.route('/index.htm')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/freq', methods=['post'])
def freq():
    file = request.files['file']
    file_data = ' '.join(x.decode('utf-8') for x in file.stream.readlines())
    word = most_frequent_word(file_data)
    return render_template('freq.html', freq_word=word)


if __name__ == "__main__":
    app.run()
