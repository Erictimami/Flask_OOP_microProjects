from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play/<x>/<y>/<color>')
def index(x, y, color):
    return render_template("index.html", message="Welcome!", xBoxes=int(x), yBoxes=int(y), nameColor=color)



if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)

