from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list_counter = Counter(list(s))
        t_list_counter = Counter(list(t))

        return s_list_counter == t_list_counter

