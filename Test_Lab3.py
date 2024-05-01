import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_more_than_or_equal_to_10_numbers(): 
    input_arr = [64, 34, 25, 12, 22, 11, 90, 0, 15, 69, 42] # 11 elements

    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == 1) 

def test_bubble_sort_0_numbers():
    input_arr = []

    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == 0) 

def test_bubble_sort_not_int():
    input_arr = [64, 3.4, 25, 'a', 22, "hello", 90]

    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == 2)  

    