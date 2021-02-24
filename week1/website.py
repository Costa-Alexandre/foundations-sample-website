from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/code')
def code():
    return render_template('code.html', page_title="CODE University")


@app.route('/author')
def author():
    return render_template('author.html', page_title="About the Author")


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title="Contact the Author")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
