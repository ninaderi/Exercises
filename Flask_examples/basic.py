from flask import Flask
# from gevent.pywsgi import WSGIServer
# from flask import info
# export FLASK_ENV=development

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello Kitty!</h1>"

@app.route('/inform')
def info():
    return "<h1>Kitties are cuties!</h1>"

@app.route('/kitty/<name>')
def kitty(name):
    return "<h1>This is a page for {}</h1>".format(name)

@app.route('/kitty3/<name>')
def kitty3(name):
    return "Upper case: {}".format(name.upper())

if __name__ == '__main__':
    app.run(debug=True)
