import unittest

from app import __version__
from app import create_app


class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.client = self.app.test_client()

    def test_hello_world(self):
        response = self.client.get('/robot_demo', follow_redirects=True)
        self.assertTrue('The Art of Computer Programming' in response.data)

    def test_version(self):
        response = self.client.get('/robot_demo/version', follow_redirects=True)
        self.assertTrue(__version__ in response.data)

    def test_faq(self):
        response = self.client.get('/robot_demo/faq.htm')
        self.assertEqual('<!--Newegg-->', response.data)
