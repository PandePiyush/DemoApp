from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello():
    return "My Future is an ideal Projection of what i envision now"
  
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)