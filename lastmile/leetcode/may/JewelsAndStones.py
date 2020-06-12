class JewelsAndStones:

    def numJewelsInStones(self, J, S):
        freq_map = {}

        for s in S:
            if s not in freq_map:
                freq_map[s] = 0
            freq_map[s] += 1

        count = 0
        for j in J:
            if j in freq_map:
                count += freq_map.get(j)

        return count


if __name__ == '__main__':
    j = JewelsAndStones()
    print(j.numJewelsInStones("aA", "aAAbbbb")) # 3
    print(j.numJewelsInStones("z", "ZZ")) # 0
