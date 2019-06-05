from flask import Flask, request, Response
import os
from werkzeug.utils import secure_filename
from pneumonia_predictor import my_pne_predictor

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

app = Flask(__name__)


@app.route('/uploader', methods = ['POST'])
def upload_file():
    print('started')
    if request.method == 'POST':
        if 'file' not in request.files:
            return "file not found"
        else:
          f = request.files['file']
          type = secure_filename(f.filename).split('.')[1]
          if type not in ALLOWED_EXTENSIONS:
              return "invalid"
          if f :
              filename = os.path.join(
                                    UPLOAD_FOLDER,
                                    f"temp_sto.{type}"
                                    )
              f.save(filename)
              value = my_pne_predictor(filename).predict()
              if value == 0:
                  value = "pneumonia not detected"
              else:
                  value = "pnemonia detected"
              return Response(response = value, status=200, mimetype='application/json')
if __name__ == '__main__':
   app.run()
