# https://leetcode.com/problems/count-of-matches-in-tournament/
# 2020.12.24, easy

class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        remaining_teams = n
        while remaining_teams > 1:
            if remaining_teams % 2 == 0:
                count += remaining_teams / 2
                remaining_teams /= 2
            else:
                count += (remaining_teams - 1) / 2 + 1
                remaining_teams = (remaining_teams - 1) / 2
        return count
