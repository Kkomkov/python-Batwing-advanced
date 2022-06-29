from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():    
    return "Hi man"

@app.route("/sum/<int:x1>/<int:x2>", methods=['GET'])
def sum(x1,x2):    
    return str(x1+x2)

if __name__ == "__main__":
    app.run(port=5000,  host='0.0.0.0', debug=True)