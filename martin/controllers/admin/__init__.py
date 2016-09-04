from flask_security import login_required
from flask_admin import helpers, expose
from flask_admin.admin import AdminIndexView

# Customized index view class that handles login & registration
class MartinAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return super(MartinAdminIndexView, self).index()
