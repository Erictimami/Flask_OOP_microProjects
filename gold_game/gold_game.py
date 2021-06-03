from flask import Flask, render_template, request, redirect, session # import a session first
app = Flask(__name__)

app.secret_key = "sskdfkjsdf" # second, We need to have the key of the app. for securing the cookies in sessions

def random_earn(a,b):
    import random
    return random.randrange(a,b)
def activ_datetime():
    import datetime
    return datetime.datetime.now()

@app.route('/')
def home():
    if 'your_gold' not in session:
        session['your_gold']=0
    if 'activities' not in session:
        session['activities']=""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['place'] == 'farm':   #place is the name of the <input> tag in html file
        gold_earned=random_earn(10, 20) 
        now=activ_datetime()
        session['your_gold'] += gold_earned
        session['activities'] += "<div class='not_casino'> Earned " + str(gold_earned) + " golds from the farm! (" + str(now) + ")</div><b>"

    elif request.form['place'] == 'cave':
        gold_earned=random_earn(5, 10)
        now=activ_datetime()
        session['your_gold'] += gold_earned
        session['activities'] += "<div class='not_casino'> Earned " + str(gold_earned) + " golds from the cave! (" + str(now) + ")</div><b>"

    elif request.form['place'] == 'house':
        gold_earned=random_earn(2, 5)
        now=activ_datetime()
        session['your_gold'] += gold_earned
        session['activities'] += "<div class='not_casino'> Earned " + str(gold_earned)  + " golds from the house! (" + str(now) + ")</div><b>"

    elif request.form['place'] == 'casino':
        gold_earned=random_earn(-50, 50)
        now=activ_datetime()
        session['your_gold'] += gold_earned
        if gold_earned >= 0:
            session['activities'] += "<div class='casino_win'> Entered a casino and earned " + str(gold_earned)  + " golds ... It's amazong (" + str(now) + ")</div><b>"
        else:
            gold_earned = -1 * gold_earned
            session['activities'] += "<div class='casino_loss'> Entered a casino and lost " + str(gold_earned)  + " golds ... Ouch.. (" + str(now)+ ")</div><b>"

    print(session['your_gold'])
    return render_template("index.html", activities=session['activities'], your_gold=session['your_gold'] )


if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)


