import sae
from MessageBoard import wsgi
application = sae.create_wsgi_app(wsgi.application)
