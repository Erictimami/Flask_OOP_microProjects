from flask import Flask, render_template
app = Flask(__name__)

# users = [1,3,4,5]
users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

@app.route('/')
def index():
    return render_template("index.html", tableOfUsers=users)



if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)

