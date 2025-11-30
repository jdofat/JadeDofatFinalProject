# django to web middleman, sends requests --> django sends response back
# https://www.reddit.com/r/learnpython/comments/1dboq9h/i_am_not_able_to_understand_what_is_wsgi_and_why/


import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internshipfinder.settings")
application = get_wsgi_application()
