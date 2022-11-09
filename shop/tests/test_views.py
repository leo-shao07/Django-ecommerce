from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_1(self):
        self.assertEquals(1,1)

    def test_2(self):
        self.assertEquals(1,2)