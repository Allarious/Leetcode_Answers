
class LongestSubStr:
    def length_of_longest_substring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        max_length = 1
        hashmap = {s[0]: True}
        i = 0
        j = 0
        while j < length:
            if j - i > max_length:
                max_length = j - i

            if i >= j or not hashmap.get(s[j]):
                hashmap[s[j]] = True
                j += 1
            else:
                hashmap[s[i]] = None
                i += 1

        return max(max_length, j - i)

if __name__ == "__main__":
    print(LongestSubStr().length_of_longest_substring("pwwkew"))