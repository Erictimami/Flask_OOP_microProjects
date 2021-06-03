from flask import Flask, render_template, request, redirect, session # import a session first
app = Flask(__name__)

app.secret_key = "sskdfkjsdf" # second, We need to have the key of the app. for securing the cookies in sessions



@app.route('/')
def home():
    if 'count' not in session:
        session['count']=0
    return render_template("index.html", count_times=session['count'])

@app.route('/increase', methods=['POST'])
def counter_by_2():
    count = session['count']
    count += 2
    session['count'] = count
    print(session['count'])
    return render_template("index.html", count_times=count)

@app.route('/reset', methods=['POST'])
def reset():
    session['count']=1
    count = session['count']
    session['count'] = count
    print(session['count'])
    return render_template("index.html", count_times=count)


@app.route('/destroy_session', methods=['POST'])
def detroy():
    session.clear()
    return redirect('/')


if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)


