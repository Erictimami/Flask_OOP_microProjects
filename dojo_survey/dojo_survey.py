from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ["POST"])
def display_info_form():
    return render_template("display_info_form.html", result = request.form)

@app.route('/danger')
def redirect_danger():
    print("A user tried to visit /danger.  We have redirected the user to /")
    return redirect('/')

if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)


