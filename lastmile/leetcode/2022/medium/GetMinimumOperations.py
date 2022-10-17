def getMinOperations(kValues):
    result = []
    if not kValues:
        return result

    for each in kValues:
        if each<0:
            result.append(-1)
        if each <= 1:
            result.append(each)
        else:
            result.append(getMinOperationsForOne(each))

    return result


def getMinOperationsForOne(kvalue):
    count = 0
    while kvalue:
        if (kvalue % 2 == 0):
            kvalue /= 2
        else:
            kvalue-=1
        count+=1
    return count


if __name__ == "__main__":
    print(getMinOperations(kValues=[5, 3]))  # [4,3]
    print(getMinOperations(kValues=[3]))  # [3]
    print(getMinOperations(kValues=[]))  # []
    print(getMinOperations(kValues=[0]))  # [0]
    print(getMinOperations(kValues=[8]))  # [4]
    print(getMinOperations(kValues=[6]))  # [2]
    print(getMinOperations(kValues=[14]))  # [6]
