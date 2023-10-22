# Here I am showing DevOps Project Day 1 with Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
