from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    
    return render_template("index.html", message="Welcome!", numBoxes=3)


if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)

