from flask import Flask, render_template, flash, request, redirect
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request
import subprocess
from subprocess import check_output
 
app = Flask(__name__)
 
UPLOAD_FOLDER = '/home/bird/Downloads/Web/app/image'

app.secret_key = "Cairocoders-Ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
##app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def split (x):
    X = x.decode("utf-8")
    Y = X.split("\n")
    return(Y)

def split2 (x):
    Y = x.split(" ")
    return(Y)

def check_txt (x):
    for i in x:
        if "Mean distance" in i:
            Y = i[19:]
    X = split2(Y)
    X = X[3],X[8]
    return(X)

 
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  
@app.route('/')
def upload_form():
 return render_template('upload.html')
 
@app.route('/', methods=["POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the files part
        if 'image[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('image[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        subprocess.run(["/home/bird/Downloads/meshroom-2019.2.0/meshroom_photogrammetry.sh", "--input", "/home/bird/Downloads/Web/app/image", "--output", "/home/bird/Downloads/Web/input_CC", "--pipeline", /home/bird/Downloads/Web/input_CC/config])
        subprocess.check_output(["cloudcompare.CloudCompare", "-silent" ,"-AUTO_SAVE","OFF","-o", "/home/bird/Downloads/Web/input_CC/texturedMesh.obj", "-SAMPLE_MESH", "POINTS","1000000","-C_EXPORT_FMT","BIN","-SAVE_CLOUDS","FILE","/home/bird/Downloads/Web/input_CC/outputCC.bin"])
        out = subprocess.check_output(["cloudcompare.CloudCompare", "-silent","-AUTO_SAVE","OFF" ,"-o", "/home/bird/Downloads/Web/data_t/input_T.bin", "-o", "/home/bird/Downloads/Web/input_CC/outputCC.bin","-ICP", "-c2c_dist"])
        out_CC = split(out)
        out_CC_mean = check_txt(out_CC)
        flash(out_CC_mean)

        return render_template("result2.html",out_CC_mean=out_CC_mean)


@app.route('/result')
def index():
 return render_template('result.html')

@app.route('/web_help')
def web_help():
 return render_template('web_help.html')

@app.route('/result2')
def result2():
 return render_template('result2.html')


if __name__ == '__main__':
 app.run(debug=True)