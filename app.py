from flask import Flask, request, render_template



app = Flask(__name__)



@app.route('/1')
def index1():
    return "<p>hello world</p>"


@app.route('/2')
def Raj ():
    return "<P>He is a ML Eng</P>" 

@app.route('/greet/<name>')
def greet(name):
    return f'hello,{name}'
    
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'num1 + num2 = {num1+num2}'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'you have request a get method \n'
    elif request.method == 'POST':
        return'you have requested a post method \n'
    else:
        return'Invalid request made'
   

@app.route('/3')
def index():
    Ayush = 'My lovely'
    Aditya = 'My lovely son lovely brother'
    
    return render_template('index.html', Ayush = Ayush, Aditya = Aditya)

@app.route('/4')
def other():
    myname = ['Raj', 'Rajiv', "Rakesh"]
    return render_template('other.html', myname = myname)

if __name__== '__main__':
    app.run(host="0.0.0.0", port = 5000, debug = True) 


   
    