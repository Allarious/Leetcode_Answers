
class LongestSubStr:
    def length_of_longest_substring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        max_length = 1
        hashmap = {s[0]: 0}
        i = 0
        j = 0
        while j < length:
            if j - i > max_length:
                max_length = j - i

            if i >= j or hashmap.get(s[j]) is None or hashmap.get(s[j]) < i:
                hashmap[s[j]] = j
                j += 1
            else:
                tmp = hashmap[s[i]]
                hashmap[s[i]] = None
                i = tmp + 1

        return max(max_length, j - i)

if __name__ == "__main__":
    print(LongestSubStr().length_of_longest_substring("bbbb"))