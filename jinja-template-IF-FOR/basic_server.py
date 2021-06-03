from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="I am happy to be learning coding at Coding Dojo", times=5) #render_template is a function where we have to pass the first argument as index.html


if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)
