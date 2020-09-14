from itertools import chain


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self):
        return "{}{}".format(self.start, self.end)

class EmployeeFreeTime:
    def employeeFreeTime(self, schedule: [[Interval]]) -> [Interval]:
        ssched=sorted(chain(*schedule), key=lambda i: i.start)
        prev=ssched[0]

        result=[]

        for curr in ssched[1:]:
            if prev.end<curr.start:
                result.append(Interval(prev.end, curr.start))
            else:
                prev.start=min(prev.start, curr.start)
                prev.end=max(prev.end, curr.end)

        return result


if __name__ == '__main__':
    init = EmployeeFreeTime()
    print(init.employeeFreeTime([[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]))
