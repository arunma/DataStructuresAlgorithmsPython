class RabinKarp:
    def search(self, search: str, pat: str) -> int:
        D = 257
        M = len(pat)
        N = len(search)
        Q = 11
        h = pow(D, M - 1) % Q
        p = 0
        t = 0
        # preprocessing
        for i in range(M):
            p = (p * D + ord(pat[i])) % Q
            t = (t * D + ord(search[i])) % Q

        for s in range(N - M + 1):
            if p == t:
                match = True
                for i in range(M):
                    if pat[i] != search[i + s]:
                        match = False
                if match:
                    return s
            if s < (N - M):
                t = (t - h * ord(search[s])) % Q
                t = (t * D + ord(search[s + M])) % Q
                t = (t + Q) % Q


if __name__ == '__main__':
    init = RabinKarp()
    print(init.search("3141592653589793", "26"))  # 10
