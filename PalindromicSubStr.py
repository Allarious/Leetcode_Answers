
class PalidromicSubStr:
    def longest_palindrome(self, s: str) -> str:
        string = self.alpha_numeric_str(s)

        if len(string) == 0:
            return ""
        if len(string) == 1:
            return string

        max_palindrome_substr = ""
        palindrome = ""
        start_index = ""
        end_index = ""
        counter = 0

        while counter < len(string):
            if palindrome == "":
                start_index = counter
                end_index = counter
                palindrome = string[counter]
            elif start_index == end_index and start_index < len(string) - 1 and string[start_index + 1] == string[
                start_index]:
                while string[start_index] == string[end_index]:
                    if end_index >= len(string) - 1:
                        if len(palindrome) > len(max_palindrome_substr):
                            max_palindrome_substr = palindrome
                        palindrome = ""
                        counter += 1
                        break
                    end_index += 1
                    if string[start_index] == string[end_index]:
                        palindrome += string[end_index]
                end_index -= 1
            else:
                if start_index <= 0 or end_index >= len(string) - 1 or string[start_index - 1] != string[end_index + 1]:
                    if len(palindrome) > len(max_palindrome_substr):
                        max_palindrome_substr = palindrome
                    palindrome = ""
                    counter += 1
                    continue
                else:
                    start_index -= 1
                    end_index += 1
                    palindrome = string[start_index] + palindrome + string[end_index]

        return max_palindrome_substr

    def alpha_numeric_str(self, s: str) -> str:
        result = ""
        for c in s:
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
                result += c

        return result


if __name__ == "__main__":
    print(PalidromicSubStr().longest_palindrome("tattarrattat"))