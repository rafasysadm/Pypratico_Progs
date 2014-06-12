class Anagrama():

    def test_anagrama(self, word1, word2):

        word1 = word1.replace(' ', '').lower()
        word2 = word2.replace(' ', '').lower()



        word1 = sorted([i for i in word1])
        word2 = sorted([i for i in word2])


        if len(word1) != len(word2):
            return False

        else:

            if word1 == word2:
                return True

            else:
                return False



if __name__ == '__main__':
    anagrama = Anagrama()
    #anagrama.test_anagrama('The alias men', 'alan smithee')

