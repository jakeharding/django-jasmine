from django.test import TestCase

example_specs = ['PlayerSpec.js', 'SpecHelper.js']

class TestView(TestCase):

    def setUp(self):
        self.rsp = self.client.get('')

    def test_view_success(self):
        self.assertEqual(self.rsp.status_code, 200)

    def test_spec_files_served(self):
        for spec in example_specs:
            self.assertTrue(spec in str(self.rsp.content), '%s not in %s' % (spec, self.rsp.content))

    # def test_jasmine_version(self):
    #     import pdb; pdb.set_trace()
