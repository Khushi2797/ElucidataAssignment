import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('C:\Users\Khushboo 13\Desktop\8th SEM\Elucidata\upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploaded_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
   
