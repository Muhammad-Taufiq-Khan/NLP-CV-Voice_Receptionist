from flask import Flask, render_template, Response, request
from face_verification import Video, gen, face_authenticated


app=Flask(__name__)


"""Home Page"""
@app.route('/')
def index():
    return render_template('index.html')

"""Face Authentication"""
@app.route('/video')
def video():
    return Response(gen(Video()), mimetype='multipart/x-mixed-replace; boundary=frame')

"""Conversation"""
@app.route('/conversation')
def verify():
    authenticated = face_authenticated()
    return render_template('conversation.html', verification = authenticated)

"""Similarity Check"""

app.run(debug=True, threaded = True)