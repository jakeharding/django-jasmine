import logging
import os

import django
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView

if django.VERSION >= (1, 5):
    import json as simplejson
else:
    from django.utils import simplejson

logger = logging.getLogger("django_jasmine")


class DjangoJasmineView(TemplateView):
    template_name = "jasmine/index.html"

    def get_context_data(self, path=None):
        """Run the jasmine tests and render index.html"""
        print(path)
        root = os.path.join(settings.JASMINE_TEST_DIRECTORY, path)
        # Get all files in spec dir and subdirs
        all_files = []
        for curpath, dirs, files in os.walk(os.path.join(root, "spec")):
            for name in files:
                if not name.startswith("."):
                    "We want to avoid .file.js.swp and co"
                    curpath = curpath.replace(os.path.join(root, "spec"), "")
                    all_files.append(os.path.join(curpath, name))

        suite = {}

        # defaults
        suite['js_files'] = []
        suite['static_files'] = []

        # load files.json if present
        if os.path.exists(os.path.join(root, "files.json")):
            file = open(os.path.join(root, 'files.json'), 'r')
            json = file.read()
            try:
                json = simplejson.loads(json)
            except ValueError:
                logger.info("You might have a syntax error in your files.json, "
                    "like a surplus comma")
                # Trick to call back the django handler500, couldn't find a way to
                # customize the Exception Type field in the debug Traceback
                json = simplejson.loads(json)
            suite.update(json)

        data = {
            'files': [path + file for file in all_files if file.endswith('js')],
            'suite': suite,
        }
        return data
