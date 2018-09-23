from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
  <head>
    <style>
      form{{
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
    <form action="/"  method="post">
      <label for="rot">Rotate by: 
        <input type="text" name="rot" value=0 />
      </label>
      <textarea type="text" name="text" > {0} </textarea>
        <input type= "submit" value="SUBMIT" />  
    </form>
  </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
  intake=str(request.form['text'])
  rotation=int(request.form['rot'])
  output= str(rotate_string(intake, rotation))
  return form.format(output)    

@app.route("/")
def index():
    return form.format('')

app.run()