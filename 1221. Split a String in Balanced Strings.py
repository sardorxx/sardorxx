class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_count = 0
        l_count = 0
        r_count = 0

        for char in s:
            if char == 'L':
                l_count += 1
            if char == 'R':
                r_count += 1

            if l_count == r_count:
                max_count += 1
                l_count = 0
                r_count = 0

        return max_count