from flask import views,render_template
from . import admin


@admin.route("/")
def index():
    return "admin Test Demo"

class Index(views.View):
    def __init__(self):
        super(Index,self).__init__()

    def dispatch_request(self):
        return "wo shi Class"

class Template(views.View):
    def __init__(self):
        super(Template,self).__init__()

    def dispatch_request(self):
        #return "WORK"
        return render_template('test.html')

admin.add_url_rule('/Index/',endpoint='Index',view_func=Index.as_view('Index'),methods=['GET','POST'])
admin.add_url_rule('/Template/',endpoint='Template',view_func=Template.as_view('Template'),methods=['GET','POST'])