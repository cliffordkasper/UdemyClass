from flask import Flask, request, render_template, redirect, url_for, flash
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if valid_login(request.form.get('username'),
		   request.form.get('password')
		   ):
      flash("Succesfully logged in")
      flash("Thanks for coming")
      return redirect(url_for('welcome', username=request.form.get('username')))
    else:
      error = "Incorrect username and password"
  return render_template('login.html', error=error)

@app.route('/welcome/<username>')
def welcome(username):
  return render_template('welcome.html', username=username)

def valid_login(username, password):
  #checks on the db if the username and password are correct
  if username == password:
    return True
  else:
    return False

if __name__ == '__main__':
  app.secret_key = 'SuperSecretPassword1234!@#$'
  app.debug = True
  app.run(host='0.0.0.0')
