import unittest
import main

class TestMain(unittest.TestCase):
  def test_do_stuff(self):
    num = 10
    result = main.do_stuff(num)
    self.assertEqual(result, 15)

  def test_do_stuff2(self):
    num = 'hello'
    result = main.do_stuff(num)
    self.assertTrue(isinstance(result, ValueError))
    
unittest.main()