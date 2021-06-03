from flask import Flask  # Import Flask to allow us to create our app. 
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file. Creation of a instance (an object) from the class Flask
                         # directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function. 
                         # @app.route means all the lines below is mine
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.


@app.route('/<name>')
def namefunction(name):
  return name

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    print(name)   # we can print it in the terminal if we want. specially for debugging
    return "Hi "+name

@app.route('/repeat/<numTimes>/<message>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def RepeatMessage(message, numTimes):
    print(message)
    print(numTimes)
    return (message+'\n') * int(numTimes)

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app with a debug mode, if we wanna see the errors messages. It's mandatory.
