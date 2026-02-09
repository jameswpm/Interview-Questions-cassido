"""
Given an integer array and a number n, move all of the ns to the end of the array while
maintaining the relative order of the non-ns. Bonus: do this without making a copy of the array!

Example:

$ moveNums([0,2,0,3,10], 0)
$ [2,3,10,0,0]
"""

def move_nums(arr: list, num_to_move: int):
    list_to_end = list(filter(lambda x : x == num_to_move, arr))
    return list(filter(lambda x : x != num_to_move, arr)) + list_to_end


if __name__ == "__main__":
    assert move_nums([0,2,0,3,10], 0) == [2,3,10,0,0]

    assert move_nums([], 0) == []

    assert move_nums([5], 5) == [5]

    assert move_nums([5], 0) == [5]

    assert move_nums([1, 2, 3], 0) == [1, 2, 3]

    assert move_nums([0, 0, 0], 0) == [0, 0, 0]

    assert move_nums([0, 1, 2, 3], 0) == [1, 2, 3, 0]

    assert move_nums([1, 2, 3, 0], 0) == [1, 2, 3, 0]

    assert move_nums([1, 0, 2, 3], 0) == [1, 2, 3, 0]

    assert move_nums([0, 2, 0, 3, 10], 0) == [2, 3, 10, 0, 0]

    assert move_nums([1, 0, 1, 0, 1], 0) == [1, 1, 1, 0, 0]

    assert move_nums([-1, 0, -2, 0, -3], 0) == [-1, -2, -3, 0, 0]

    print("All tests passed")