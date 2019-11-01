from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        balance = [gas[i] - cost[i] for i in range(l)]
        cache_positive_balance_block = dict()
        tank = 0
        start = 0
        for i in range(l):
            tank += balance[i]
            if tank >= 0:
                cache_positive_balance_block[start] = [i - start, tank]
            else:
                tank = 0
                start = i + 1
        for res in cache_positive_balance_block:
            tank = 0
            i = res
            while i < res + l:
                if (i % l) in cache_positive_balance_block.keys():
                    tank += cache_positive_balance_block[i % l][1]
                    i += cache_positive_balance_block[i % l][0] + 1
                else:
                    tank += balance[i % l]
                    i += 1
                if tank < 0:
                    break
            if tank >= 0:
                return res
        return -1


gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))

gas  = [1,2,3,4,5]
cost = [6,6,5,1,6]
print(Solution().canCompleteCircuit(gas, cost))