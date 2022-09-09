from flask import Flask, url_for, render_template
from helpers import listAll, random, generate, build

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['TESTING'] = True

@app.route("/")

def main():
    code = random()
    im = generate(code)
    imgUrl = url_for('static', filename='art.png')
    return render_template('index.html', code=code)

@app.route("/all")

def all():
    items = listAll()
    return render_template('all.html',items=items)


@app.route("/code/<code>")
def bycode(code=None):
    if code:
        im = generate(code)
        imgUrl = url_for('static', filename='art.png')
        return render_template('simple.html', imgUrl=imgUrl)
        
    return "null"


@app.route("/build")
def buildLib():
    return build() 