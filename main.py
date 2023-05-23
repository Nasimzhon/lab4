import unittest
from app import app
import io


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_eqwords(self):
        resp = self.app.post('/freq', data={'file': (io.BytesIO(b"first second third"), 'test.txt')},
                             content_type='multipart/form-data')
        assert b'third' in resp.data

    def test_equalwords(self):
        resp = self.app.post('/freq', data={'file': (io.BytesIO(b"first second third third first first third"),
                                                     'test.txt')},
                             content_type='multipart/form-data')
        assert b'third' in resp.data


if __name__ == "__main__":
    unittest.main()