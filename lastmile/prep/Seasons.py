import sys


def calc_amplitude(S):
    mini = abs(min(S))
    maxi = abs(max(S))
    return abs(maxi - mini)

def solution(T):
    if not T:
        return "INVALID_INPUT"

    N = len(T)
    if N <= 4 or N % 4 != 0:
        return "INVALID_INPUT"
    length_of_season = N // 4

    max_amplitude = float('-inf')
    max_season = "INVALID_INPUT"

    seasons = ["WINTER", "SPRING", "SUMMER", "AUTUMN"]

    for season, partition in zip(seasons, list(range(4))):
        start = partition * length_of_season
        end = (partition + 1) * length_of_season
        S = T[start:end]
        amplitude = calc_amplitude(S)
        if max_amplitude < amplitude:
            max_amplitude = amplitude
            max_season = season

    return max_season


if __name__ == '__main__':
    print(solution([-3, -14, -5, 7, 8, 42, 8, 3]))  # SUMMER
    print(solution([2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18]))  # AUTUMN
    print(solution([]))
    print(solution([1, 2, 3, 4]))
    print(solution([-3, -14, -5, -7, -8, -42, -8, -3]))
    print(solution([3, 14, 5, 7, 8, 42, 8, 3]))
    print(solution([-1, -2, -3, -4]))
    print(solution([-1, -2, -3]))
    print(solution([-1, -2]))
    print(solution([-1]))
    print(solution([2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18, 9]))  # INVALID
