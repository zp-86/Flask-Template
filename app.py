from flask import Flask, render_template

app = Flask(__name__)


# Flask Template - @zp86

@app.route('/')
def hello_world():
    pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
