from flask import Flask, render_template
import os
app = Flask(__name__)
IMAGE_FOLDER = os.path.join('images')
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/image')
def image():
    full_filename = os.path.join(app.config['IMAGE_FOLDER'], 'ProfilePicture2020.jpg')
    return render_template("index.html", user_image = full_filename)