from collections import deque


class KSimilarStrings:
    def kSimilarity(self, s1: str, s2: str) -> int:
        A = []
        B = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                A.append(s1[i])
                B.append(s2[i])

        queue = deque([(A, 0)])
        visited=set(tuple(A))
        while queue:
            curr, dist = queue.popleft()
            if curr==B:
                return dist

            visited.add(tuple(curr))

            # get next swap list
            neis=self.get_next_swaps(curr, B, visited)
            for nei in neis:
                if tuple(nei) not in visited:
                    queue.append((nei, dist+1))

        return -1

    def get_next_swaps(self, curr, B, visited):
        neis = []
        i = 0
        while curr[i] == B[i]:
            i += 1

        for j in range(i+1, len(curr)):
            if curr[j] == B[i] and curr[j] != B[j]:
                curr[i], curr[j] = curr[j], curr[i]
                neis.append(curr.copy())
                curr[i], curr[j] = curr[j], curr[i]
        return neis


if __name__ == '__main__':
    init = KSimilarStrings()
    print(init.kSimilarity(s1="ab", s2="ba"))  # 1
    print(init.kSimilarity(s1="abc", s2="bca"))  # 2
    print(init.kSimilarity(s1="abccaacceecdeea", s2="bcaacceeccdeaae"))  # 9
