import unittest

from anagrama import Anagrama

anagram = Anagrama()

class AnagramaTest(unittest.TestCase):



    def test_anag(self):
       # anagramt = Anagrama()
        self.assertTrue(anagram.test_anagrama('sapo', 'posa'))
        self.assertTrue(anagram.test_anagrama('Iracema', 'America'))
        self.assertTrue(anagram.test_anagrama('the Alias Men', 'alan smithee'))


    #Testes nao funcionam se crio objeto dentro da funcao.
    def test_not_anagram(self):

       # anagramF = Anagrama()
       self.assertFalse(anagram.test_anagrama('aqa', 'ata'))
       self.assertFalse(anagram.test_anagrama('aaa', 'aba'))
       self.assertFalse(anagram.test_anagrama('the Alias Men', 'alen smithee'))


