import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template,send_file
import glob

UPLOAD_FOLDER = 'uploads/'

#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Upload API
@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():  
    if request.method == 'POST':
        file = request.files['file'] 
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/downloadfile/'+ filename)
        
    return render_template('upload.html')

# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

        
@app.route('/view', methods = ['GET'])  
def show(): 
    l=[] 
    if request.method == 'GET':  
        os.chdir('C:\\Users\\user\\Desktop\\try\\uploads')
        types = ('*.pdf', '*.csv','*.docx','.xlsx')
        files_grabbed = []
        for files in types:
            files_grabbed.extend(glob.glob(files))
        files_grabbed.sort(key=os.path.getmtime)

        for file in sorted(files_grabbed,key=os.path.getmtime,reverse=True):
            l.append(file)
    return render_template("show.html", name = l)

# @app.route('/file-downloads/')
# def file_downloads():
#     return render_template('downloads.html')

@app.route('/return-fil/<filename>')
def return_files_tut1(filename):
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, attachment_filename='python.pdf')


if __name__ == "__main__":
    app.run(debug = True,port=5400)