def are_they_equal(array_a, array_b):
    # Write your code here
    if array_a==array_b:
        return True
    first = None
    for i in range(len(array_a)):
        if array_a[i] == array_b[i]:
            continue
        elif not first:
            first = array_a[i]
        else:
            return first == array_b[i]
    return False


if __name__ == '__main__':
    print(are_they_equal([1, 2, 3, 4],[1, 4, 3, 2]))
    print(are_they_equal([1, 2, 3, 4],[1, 2, 3, 5]))
    print(are_they_equal([1, 2, 3, 4],[1, 2, 3, 4]))


