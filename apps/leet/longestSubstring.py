from typing import List


from typing import List

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_index = 0
        hashmap = {}
        max_len = len(s)
        result_len = 0

        for i in range(max_len):
            if s[i] in hashmap and start_index <= hashmap[s[i]]:
                start_index = hashmap[s[i]] + 1
            else:
                result_len = max(result_len, i-start_index+1)
            hashmap[s[i]] = i
        return result_len

    
    """
        for x in input_list:
            #if(current_list.index(x) != 0):
            strIndex = current_list.count(x) if (current_list.count(x) != None) else -1
            if (strIndex > 0):
                return len(current_list*)
            current_list.append(x)
            print(current_list)
            i += 1
        return 0
    def check(self, start: int, end: int, s: str):
        for i in range(start, end+1):
            c = s[i]
    """ 

solution = Solution()
input: str = "pwwkpw"
print("Result: " + str(solution.lengthOfLongestSubstring(input)))