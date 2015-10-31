from flask import Flask, url_for
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
  return "User: " + str(username)


@app.route('/')
def show_url_for():
  return url_for('show_user_profile', username='Clifford')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
