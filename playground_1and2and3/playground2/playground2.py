from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play/<x>')
def index(x):
    return render_template("index.html", message="Welcome!", numBoxes=int(x))



if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)

