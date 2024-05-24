# your code here!
class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
 
    def match(self, words):
        match_words = []
        for word in words:
            if sorted([letter for letter in word]) == self.word_letters:
                match_words.append(word)

        return match_words        