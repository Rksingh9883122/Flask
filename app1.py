from flask import Flask, request, render_template

app = Flask(__name__)


@app.route(rule='/', methods = ['GET', 'POST'])            ##through get get the form and through post post the form

def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return render_template("")
        
    


    
    
if __name__== '__main__':
    app.run(host="0.0.0.0", port = 5000, debug = True) 