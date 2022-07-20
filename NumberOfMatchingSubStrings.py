
from typing import List

class NumOfMatchingSubStr:
    def number_of_matching_substr(self, s: str, words: List[str]) -> int:
        # I am looking for a data structure to show the relation between two words
        # stack idea space: O(s.length), time: O((s.length + word.length) * list_length)

        # will insert every position into a hashmap and got through every word searching for the least possible index

        # inserting the s into the hasmap
        hashmap = {}
        for index, character in enumerate(s):
            if hashmap.get(character):
                hashmap[character].append(index)
            else:
                hashmap[character] = [index]

        count_of_matching_substr = 0
        for word in words:
            if self.is_matching_substr(word, hashmap):
                count_of_matching_substr += 1

        return count_of_matching_substr

    def is_matching_substr(self, word, hashmap) -> bool:
        min_index = -1
        for character in word:
            if hashmap.get(character):
                prev_min_index = min_index
                for index in hashmap[character]:
                    if index > min_index:
                        min_index = index
                        break
                if min_index == prev_min_index:
                    return False
            else:
                return False
        return True



if __name__ == "__main__":
    print(NumOfMatchingSubStr().number_of_matching_substr("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))