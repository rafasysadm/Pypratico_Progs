class Anagrama():

    def test_anagrama(self, word1, word2):

        word1 = word1.replace(' ', '').lower()
        word2 = word2.replace(' ', '').lower()



        word1 = sorted([i for i in word1])
        word2 = sorted([i for i in word2])


        if len(word1) != len(word2):
           # print(word1)
           # print(word2)
            return False
        else:
           # print(word1)
           # print(word2)
            if word1 == word2:
              #  print("TRUE")
                return True
            else:
               # print("FALSE")
                return False



if __name__ == '__main__':
    anag = Anagrama()
    anag.test_anagrama('The alias men', 'alan smithee')
    #anag = None
    #anag = Anagrama()

    anag.test_anagrama('naa', 'abn')

