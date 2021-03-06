from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")
    user_choice = request.args.get("play")

    compliment = choice(AWESOMENESS)

    if user_choice == "yes":
        return render_template("game.html",
                                player="person")
    
    else:
        return render_template("goodbye.html")

@app.route('/game')
def show_madlib_form():
    """Show the madlibs form"""

    color_choice = request.args.get("color")
    noun_choice = request.args.get("noun")
    adjective_choice = request.args.get("adjective")

    return render_template("/madlibs")

#     player_answer = request.args.get("play")

#     if player_answer == "no":
#         return render_template("goodbye.html",
#                                 player_answer=play)
@app.route("/madlibs")

def madlib_results():
    """Madlib completed form"""
    return render_template("/hello")

#     color_choice = request.args.get("color")
#     noun_choice = request.args.get("noun")
#     adjective_choice = request.args.get("adjective")

  

# @app.route("/goodbye")
# def say_goodbye():
#     """Tells user goodbye
#     """
#     return render_template("goodbye.html")

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
