from flask import views
from . import admin



@admin.route("/")
def index():
    return "admin Test Demo"

class Index(views.View):
    def __init__(self):
        super(Index,self).__init__()

    def dispatch_request(self):
        return "wo shi Class"

admin.add_url_rule('/Index/',endpoint='Index',view_func=Index.as_view('Index'),methods=['GET','POST'])