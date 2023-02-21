from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello():
    return "SSBT College TE-A Section is Ravas!"
  
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)