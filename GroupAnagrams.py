import collections
from typing import List

class GroupAnagramsNotOptimal:

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap_array = []
        for s in strs:
            hashmap_array.append(self._return_word_hashmap(s))

        length = len(hashmap_array)
        group_anagrams = []
        hashmap_check = [False] * length

        for i in range(length):
            if hashmap_check[i]:
                continue
            group = [strs[i]]
            for j in range(i + 1, length):
                if hashmap_array[i] == hashmap_array[j]:
                    hashmap_check[j] = True
                    group.append(strs[j])
            group_anagrams.append(group)

        return group_anagrams

    def _return_word_hashmap(self, s: str):
        hashmap = {}

        for c in s:
            value = hashmap.get(c)
            if value is None:
                hashmap[c] = 0
            else:
                hashmap[c] += 1
        return hashmap

class GroupAnagramsOptimal:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        base_ascii = ord('a')

        for s in strs:
            array = [0] * 26
            for c in s:
                array[ord(c) - base_ascii] += 1
            hashmap[tuple(array)].append(s)

        return hashmap.values()

if __name__ == "__main__":
    print(GroupAnagramsOptimal().group_anagrams(["eat","tea","tan","ate","nat","bat"]))