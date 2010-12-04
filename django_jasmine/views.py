from django.shortcuts import render_to_response
from django.conf import settings
from django.utils import simplejson

import os

def run_tests(request, path):
    full_path = os.path.join(settings.JASMINE_TEST_DIRECTORY, path)
    full_path, directories, files = os.walk(full_path).next()
    for file_name in os.walk(full_path+'spec/').next()[2]:
        files.append(file_name)

    suite = {}

    # defaults
    suite['js_files'] = []
    suite['media_files'] = []

    # load files.json if present
    if 'files.json' in files:
        file = open(os.path.join(full_path, 'files.json'), 'r')
        json = file.read()
        suite.update(simplejson.loads(json))

    return render_to_response('jasmine/index.html', {
        'files': [path + file for file in files if file.endswith('js')],
        'suite': suite,
    })
