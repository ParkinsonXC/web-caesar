from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
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
            <form method="POST">
                <label for="rot">Rotate by: <input type="text" name="rot"></label> 
                <input type="textarea" name="text" />
                <input type="submit" value="Encode" />
        </body>
    </html>
"""




@app.route("/")
def index():
    return form

app.run()