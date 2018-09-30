from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!doctype html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form method='POST'>
                <label>Rotate by:
                <input name="rot" type="text" value='0' />
                </label>
                <textarea rows="250" cols="20" name="text" type="text" >
                </textarea>
                <input type="submit" />
            </form>
        </body>
    </html>
    """


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    return '<h1>' + rotate_string(text, rot) + '</h1>'

app.run()
