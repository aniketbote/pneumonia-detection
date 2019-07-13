from flask import Flask, request, render_template
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from support import pneumonia_predictor as p

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/",methods=['GET'])
def index():
    return "<h1> Working </h1>"

@app.route('/uploader', methods = ['POST'])
def upload_file():
    print('started')
    if request.method == 'POST':
        if 'file' not in request.files:
            return "nani?"
        else:
          f = request.files['file']
          type = secure_filename(f.filename).split('.')[1]
          if type not in ALLOWED_EXTENSIONS:
              return "invalid"
          if f :
              filename = os.path.join(
                                    app.config['UPLOAD_FOLDER'],
                                    f"temp.{type}"
                                    # secure_filename(f.filename)
                                    )
              f.save(filename)
              value = p.my_pne_predictor(filename).predict()
              if value == 0:
                  value = "pneumonia not detected"
              else:
                  value = "pnemonia detected"
              return render_template(
                                    "done.html",
                                    user_image = filename,
                                    result = value
                                    )
if __name__ == '__main__':
   app.run(debug = True)
