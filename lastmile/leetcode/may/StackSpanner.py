import collections

StockEntry = collections.namedtuple('StockEntry', 'price count')

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.merge_counts(price)
        return self.stack[-1].count

    def merge_counts(self, price: int):
        count = 1
        while self.stack and self.stack[-1].price <= price:
            count = count + self.stack.pop().count
        merged_entry = StockEntry(price, count)
        self.stack.append(merged_entry)


if __name__ == '__main__':
    S = StockSpanner()
    print(S.next(100))  # is called and returns 1,
    print(S.next(80))  # is called and returns 1,
    print(S.next(60))  # is called and returns 1,
    print(S.next(70))  # is called and returns 2,
    print(S.next(60))  # is called and returns 1,
    print(S.next(75))  # is called and returns 4,
    print(S.next(85))  # is called and returns 6.
