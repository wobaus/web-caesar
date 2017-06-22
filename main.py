from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
                }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                }}
        </style>
    </head>
    <body>
    <!-- create your form here -->
        <form method = "POST">
            <lable for="rotnum">Rotate by:</lable>
            <input id="rotnum" type="text" name="rot"/> </br>
            <textarea name="text">{0}</textarea> </br>
            <input type="submit" value='Submit Query'/>
            <!--#5. The input element has the default value of 0.-->
    </body>
</html>
"""

@app.route("/")
def index():
    
    return form.format('')

 
@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted = rotate_string(text, rot)    
    return  "<h1>" + form.format(encrypted) + "</h1>"

app.run()