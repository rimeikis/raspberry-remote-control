from flask import Flask, render_template, redirect
from servoControl import controlBoiler

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')  

@app.route('/switch', methods=['GET'])
def switchOnOff(): 
   controlBoiler()
   return redirect("/")

if __name__ == '__main__':
app.run(debug = True)
