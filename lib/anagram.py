# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

        self.sorted_word = sorted(word.lower())
        
    
    def match(self, candidates):
        
        matches = []

        for candidate in candidates:

            candidate_lower = candidate.lower()


            if candidate_lower == self.word.lower():
                continue

            if sorted(candidate_lower) == self.sorted_word:
                matches.append(candidate)

        return matches