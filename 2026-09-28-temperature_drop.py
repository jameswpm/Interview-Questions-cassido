"""
Given an array of daily temperatures and a number drop, return an array where each element is how many days you'd wait until it's at least drop degrees colder than that day. If that never happens, put 0.

Examples:

> firstFrost([70, 68, 72, 60, 65, 55], 5)
> [3, 2, 1, 2, 1, 0]

> firstFrost([50, 49, 48], 5)
> [0, 0, 0]

> firstFrost([40, 30, 45, 20], 10)
> [1, 2, 1, 0]
"""

def firstFrost(temperatures,drop):
    count = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[i] - temperatures[j] >= drop:
                count[i] = j - i
                break

    return count


if __name__ == "__main__":
    assert firstFrost([70, 68, 72, 60, 65, 55], 5) == [3, 2, 1, 2, 1, 0]

    assert firstFrost([50, 49, 48], 5) == [0, 0, 0]
    
    assert firstFrost([40, 30, 45, 20], 10) == [1, 2, 1, 0]

    # ## Chat GPT generated test
    assert firstFrost([10], 5) == [0]

    assert firstFrost([10, 5], 5) == [1, 0]

    assert firstFrost([10, 6, 5], 5) == [2, 0, 0]

    assert firstFrost([10, 8, 7, 4], 6) == [3, 0, 0, 0]

    assert firstFrost([20, 15, 14, 13, 10], 5) == [1, 3, 0, 0, 0]

    assert firstFrost([5, 10, 3, 8, 1], 4) == [4, 1, 0, 1, 0]

    assert firstFrost([100, 99, 98, 97, 96], 1) == [1, 1, 1, 1, 0]

    assert firstFrost([30, 20, 25, 10, 15], 10) == [1, 2, 1, 0, 0]
    print("All tests passed")

