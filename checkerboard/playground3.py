from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play/<x>/<color>')
def index(x, color):
    return render_template("index.html", message="Welcome!", numBoxes=int(x), nameColor=color)



if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)

