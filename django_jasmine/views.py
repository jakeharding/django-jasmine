import logging
import os

from django.conf import settings
from django.shortcuts import render_to_response
from django.utils import simplejson

logger = logging.getLogger("django_jasmine")


def run_tests(request, path):
    """Run the jasmine tests and render index.html"""
    full_path = os.path.join(settings.JASMINE_TEST_DIRECTORY, path)
    full_path, directories, files = os.walk(full_path).next()
    for file_name in os.walk(os.path.join(full_path, 'spec')).next()[2]:
        files.append(file_name)

    suite = {}

    # defaults
    suite['js_files'] = []
    suite['media_files'] = []

    # load files.json if present
    if 'files.json' in files:
        file = open(os.path.join(full_path, 'files.json'), 'r')
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

    return render_to_response('jasmine/index.html', {
        'files': [path + file for file in files if file.endswith('js')],
        'suite': suite,
    })
