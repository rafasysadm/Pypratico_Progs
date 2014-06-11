import unittest


from anagrama import *

class AnagramaTest(unittest.TestCase):
    def test(self):
        anagrama = Anagrama()
        self.assertTrue(anagrama.test_anagrama('ana', 'naa'))
        self.assertTrue(anagrama.test_anagrama('aaa', 'aaa'))
        self.assertTrue(anagrama.test_anagrama('the Alias Men', 'alan smithee'))

    def not_anagram(self,word1, word2):
         self.assertTrue(anagrama.test_anagrama('ana', 'nia'))
         self.assertTrue(anagrama.test_anagrama('aaa', 'abc'))
         self.assertTrue(anagrama.test_anagrama('the Alias Men', 'alen smithee'))

