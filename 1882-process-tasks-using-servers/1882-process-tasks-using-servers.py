class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        order = sorted(range(n), key=servers.__getitem__) 
        free = list(range(n))  

        ans, busy = [], [] 
        for s, t in enumerate(tasks):
            while busy and busy[0] < (s + 1) * n: 
                heappush(free, heappop(busy) % n)
            start, r = (s, heappop(free)) if free else divmod(heappop(busy), n) 
            heappush(busy, (start + t) * n + r)
            ans.append(order[r])

        return ans