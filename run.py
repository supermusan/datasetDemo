import pickle
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

with open("pkls/datadict_vox2.pkl", "rb") as fp:
    datadict = pickle.load(fp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search', methods=['post'])
def search():
    name = request.form.get('name')
    if name not in datadict.keys():
        return redirect(url_for('voxceleb2'))
    else:
        return redirect(url_for('voxceleb2', videoname=name))



@app.route('/voxceleb2')
@app.route('/voxceleb2/<string:videoname>')
def voxceleb2(videoname=None):
    if videoname==None or videoname not in datadict.keys():
        return render_template('vox2.html', all_videonames=list(datadict.keys()), 
                            videoname=videoname,
                            videopath=None, 
                            framelist=[])
    else:
        return render_template('vox2.html', all_videonames=list(datadict.keys()), 
                            videoname=videoname,
                            videopath=datadict[videoname]["video"], 
                            framelist=datadict[videoname]["frame"])
    

