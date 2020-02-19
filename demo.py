from flask import Flask
from flask import views
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

class Index(views.View):
    def __init__(self):
        super(Index,self).__init__()

    def dispatch_request(self):
        return "HaHa"

def add_url_rule(app):
    app.add_url_rule('/Index/',endpoint='Index',view_func=Index.as_view('Index'),methods=['GET','POST'])


if __name__ == '__main__':
    add_url_rule(app)
    app.run(host='0.0.0.0',port='8899',debug=True)

