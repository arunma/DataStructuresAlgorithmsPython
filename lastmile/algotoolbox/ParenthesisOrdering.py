import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(i, j, ops, min_values, max_values):
    min_value = sys.maxsize
    max_value = -sys.maxsize - 1
    for k in range(i, j):
        a = evalt(min_values[i][k], min_values[k + 1][j], ops[k])
        b = evalt(max_values[i][k], max_values[k + 1][j], ops[k])
        c = evalt(min_values[i][k], max_values[k + 1][j], ops[k])
        d = evalt(max_values[i][k], min_values[k + 1][j], ops[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def get_maximum_value(dataset):
    # write your code here
    ops = []
    digits = []
    for d in dataset:
        if d in {'+', '-', '*'}:
            ops.append(d)
        else:
            digits.append(int(d))
    n = len(digits)
    max_values = [[0] * n for _ in range(n)]
    min_values = [[0] * n for _ in range(n)]
    for i in range(n):
        max_values[i][i] = digits[i]
        min_values[i][i] = digits[i]

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            min_values[i][j], max_values[i][j] = MinMax(i, j, ops, min_values, max_values)
    return max_values[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
    #print(get_maximum_value("5-8+7*4-8+9"))  # 200
