from django.test import SimpleTestCase


class FooTest(TestCase):
     def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(1, 100)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(1, 200)
    def setUp(self):
        pass

    def test_tearDown(self):
        pass

    def this_wont_run(self):
        print 'Fail'

    def test_this_will(self):
        print 'Win'
