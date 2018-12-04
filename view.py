from flask import Blueprint, request, render_template
from flask.views import MethodView
from flask import jsonify
import models


users = Blueprint('users', __name__, template_folder='templates')


class IndexView(MethodView):
    def get(self):
        return render_template('index.html')


class DetailView(MethodView):

    def get(self, mac):
        """Return """
        return jsonify(models.User.objects(mac_adress=mac).exclude())


class AgreeView(MethodView):
    """View for save agree=True/false and mac-adress"""

    def get(self):
        if request.args.get('agree'):
            agree = True
        else:
            agree = False

        mac = request.remote_addr

        if models.User.objects(mac_adress=mac):
            models.User.objects(mac_adress=mac).update(agree=agree)
        else:
            models.User.objects.create(mac_adress=mac, agree=agree)
        return render_template('result.html')


# Register the urls
users.add_url_rule('/', view_func=IndexView.as_view('index'))
users.add_url_rule('/<mac>/', view_func=DetailView.as_view('detail'))
users.add_url_rule('/save/', view_func=AgreeView.as_view('agree'))
