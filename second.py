from flask import Flask, render_template, request, redirect, flash, url_for, session

from flask_bootstrap import Bootstrap
from forms import PlayerSignUpForm


app = Flask(__name__)
Bootstrap(app)

#config
SECRET_KEY = "a complete secret"

app.config.from_object(__name__)

@app.route('/signup', methods=["GET", "POST"])
def first():
    error = None
    player_sign_up_form = PlayerSignUpForm()

    print session
    print dir(session)

    if request.method == "POST":
        if player_sign_up_form.validate_on_submit():
            print session
            print dir(session)
            flash("you are now signed up")
            return redirect(url_for('show_player_standing'))
        else:
            print session
            print dir(session)
            flash("no valid!")
            print 'no valid'
    return render_template('first.html', player_sign_up_form=PlayerSignUpForm(request.form), error=error)


@app.route('/standing')
def show_player_standing():
    return render_template('show_player_standing.html')



if __name__ == '__main__':
    app.run(debug=True)