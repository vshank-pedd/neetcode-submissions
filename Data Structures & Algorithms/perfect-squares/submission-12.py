import math
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, math.isqrt(n) + 1)]
        seen = {n}
        queue = deque([n])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                rem = queue.popleft()
                for s in squares:
                    nxt = rem - s
                    if nxt == 0:
                        return steps
                    if nxt < 0:
                        break
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
        return steps