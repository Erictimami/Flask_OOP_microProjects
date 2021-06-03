from flask import Flask, render_template, request, redirect, session # import a session first
app = Flask(__name__)

app.secret_key = "sskdfkjsdf" # second, We need to have the key of the app. for securing the cookies in sessions



@app.route('/') ############ IMPOSSIBLE TO POST SOMETHING INTO THE HOME PAGE . I HAVE TO TO CREATE MANY ROUTES (AND FORMS INTO HTML FILE) AND REDIRECT THE TO THE INDEX
def home():
    if 'count' not in session:
        session['count']=0
    # if 'values' not in session:
    #     session['values']=[]
    if 'to_guess' not in session:
        import random
        session['to_guess']=random.randrange(0, 101)
        print(session['to_guess'])
        print(session['to_guess'])
        print(session['to_guess'])
        print(session['to_guess'])

    if 'guess' not in session:
        class_result="low"
        result="Too low!"
        class_button="b_submit"
        text_button="Submit"
        type_input="text" #or hidden
        display_result=None #or block

    else:
        print(request.form)
        session['guess']=50   # TEST HERE.    we should have request.form to have guess value
        if session['guess'] < session['to_guess']:               
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['guess'])
            print(session['guess'])
            print(session['guess'])
            print(session['guess'])

            class_result="low"
            result="Too low!"
            class_button="b_submit"
            text_button="Submit"
            type_input="text" #or hidden
            display_result="block" #or None

        if session['guess'] > session['to_guess']:
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['guess'])
            print(session['guess'])
            print(session['guess'])
            print(session['guess'])

            class_result="high"
            result="Too high!"
            class_button="b_submit"
            text_button="Submit"
            type_input="text" #or hidden
            display_result="block" #or None

        if session['guess'] == session['to_guess']:
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['to_guess'])
            print(session['guess'])
            print(session['guess'])
            print(session['guess'])
            print(session['guess'])

            class_result="egal"
            result=str(session['guess']) +" was the number!"
            class_button="b_play"
            text_button="Play again!"
            type_input="hidden" #or text
            display_result="block" #or None

            # session.clear()
            # return redirect('/')



    return render_template("index.html", class_result=class_result, display_result=display_result, text_button=text_button, type_input=type_input, class_button=class_button, result=result)

if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)


