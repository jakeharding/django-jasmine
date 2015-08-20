from django.test import TestCase


class TestView(TestCase):
    def test_run_tests_view(self):
        rsp = self.client.get('')
        self.assertEqual(rsp.status_code, 200)
