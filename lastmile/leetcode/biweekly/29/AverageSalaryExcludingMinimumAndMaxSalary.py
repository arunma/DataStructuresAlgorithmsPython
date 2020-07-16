from typing import List


class AverageSalaryExcludingMinimumAndMaxSalary:
    def average(self, salary: List[int]) -> float:
        if len(salary)<=2:
            return 0
        salary.sort()
        slice=salary[1:-1]
        return sum(slice)/len(slice)


if __name__ == '__main__':
    init = AverageSalaryExcludingMinimumAndMaxSalary()
    print(init.average([4000,3000,1000,2000]))
