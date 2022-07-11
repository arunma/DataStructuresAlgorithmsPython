from typing import List


class TwentyFourGame_24:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.dfs(cards)

    def dfs(self, cards):
        if len(cards) == 1 and abs(cards[0] - 24) <= 0.001:
            return True

        for i in range(len(cards)):
            card1 = cards[i]
            for j in range(i + 1, len(cards)):
                card2 = cards[j]
                next = []
                for k in range(len(cards)):
                    if k != i and k != j:
                        next.append(cards[k])

                computed = self.get_computed(card1, card2)
                for comp in computed:
                    if self.dfs(next + [comp]):
                        return True
        return False

    def get_computed(self, card1, card2):
        computed = [card1 - card2, card2 - card1, card1 + card2, card1 * card2]
        if card1 != 0:
            computed.append(float(card2) / float(card1))
        if card2 != 0:
            computed.append(float(card1) / float(card2))

        return computed


if __name__ == '__main__':
    init = TwentyFourGame_24()
    #print(init.judgePoint24(cards=[4, 1, 8, 7]))
    #print(init.judgePoint24(cards=[8, 4, 7, 1])) #True
    print(init.judgePoint24(cards=[1, 2, 1, 2])) #False
