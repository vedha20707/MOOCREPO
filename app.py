from flask import Flask

app = Flask(__name__)
@route('/')
def index():
    return render_template('index.html', student=student)  
mooc_agencies = ["ABC",DFB",GFD"];
