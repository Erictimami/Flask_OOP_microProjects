from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods = ["POST"])
def display_info_form():
                
    count=int(0)
    result = request.form
    for value in result.values():
        count += int(value)
    import datetime
    now = datetime.datetime.now()
    return render_template("checkout.html", Num = count, instant=now, result = request.form)

@app.route('/fruit')
def redirect_danger():
    print("A user tried to visit /fruit.  We have redirected the user to /")
    return redirect('/')

if __name__=="__main__":   #we run own app and with debugging activecount
    app.run(debug=True)


