import os
import unittest
from main import app, allowed_file

class TestApp(unittest.TestCase):
    def setUp(self):
        # Define the test directory
        self.test_dir = 'uploads_test'
        self.allowed_files = ["example.txt", "document.pdf", "image.png", "picture.jpg", "photo.jpeg", "animation.gif"]
        self.disallowed_files = ["file.doc", "script.sh"]
        
    def test_allowed_file(self):
        for filename in self.allowed_files:
            path = os.path.join(self.test_dir, filename)
            self.assertTrue(allowed_file(path))

    def test_disallowed_file(self):  
        for filename in self.disallowed_files:
            path = os.path.join(self.test_dir, filename)
            self.assertFalse(allowed_file(path))

    def test_upload_file_no_field(self):
        client = app.test_client()
        # File is sent
        response = client.post('/upload')
        self.assertEqual(response.status_code, 400)

    def test_upload_file_field_empty(self):
        client = app.test_client()
        # Field is empty
        response = client.post('/upload', data={'file': ''})
        self.assertEqual(response.status_code, 400)

    def test_upload_file_allowed(self):
        client = app.test_client()
        # Allowed file is uploaded
        allowed_file_path = os.path.join(self.test_dir, "example.txt")
        with open(allowed_file_path, 'rb') as f:
            data = {'file': (f, 'example.txt')}
            response = client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)

    def test_upload_file_disallowed(self):
        client = app.test_client()
        # Disallowed file is uploaded
        disallowed_file_path = os.path.join(self.test_dir, "script.sh")
        with open(disallowed_file_path, 'rb') as f:
            data = {'file': (f, 'script.sh')}
            response = client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
