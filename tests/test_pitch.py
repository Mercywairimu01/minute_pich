from app.models import Pitch,User
from app import db
import unittest


class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_user = Pitch(category = 'puns')

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
    def test_instance(self):
        self.assertIsInstance(self.new_pitch, Pitch)    
