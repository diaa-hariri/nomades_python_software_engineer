import os
from uuid import uuid4

from flask import Flask, request

app = Flask(__name__)

CURRENT_DIR = os.path.dirname(__file__)
UPLOAD_DIR = os.path.join(CURRENT_DIR, "uploads")

def save_file(file):
  uuid = uuid4()
  ext = file.filename.split(".")[-1]
  new_filename = f"{str(uuid)}.{ext}"
  file.save(os.path.join(UPLOAD_DIR, new_filename))


@app.route('/form/files', methods=['GET', 'POST'])
def form_files():
  if request.method == 'POST': # request object has attribute method, which is a string informing the method used in the request
    file = request.files['fileInput']
    print(file)
    save_file(file)
    return 'File uploaded successfully'
  return '''
    <form action="" method="POST" enctype="multipart/form-data">
      <input type="file" name="fileInput">
      <input type="submit" value="Envoyer">
    </form>
  '''

@app.route('/form/files/multiple', methods=['GET', 'POST'])
def form_files_multiple():
  if request.method == 'POST': # request object has attribute method, which is a string informing the method used in the request
    files = request.files.getlist('fileInput')
    for file in files:
      save_file(file)
    return 'File uploaded successfully'
  return '''
    <form action="" method="POST" enctype="multipart/form-data">
      <input type="file" name="fileInput" multiple accept="image/*" size="1000000">
      <input type="submit" value="Envoyer">
    </form>
  '''

if __name__ == '__main__':
  app.run(debug=True)