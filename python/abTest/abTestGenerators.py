"""
    Test generator performace with different call methods
"""


import time


# ---------------------------------------------------------------------------------------------- #
def test_generator(number_list):
    for item in number_list:
        if (item % 2) == 0:
            yield item
# ---------------------------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------------------------- #
def test_any(number_list):
    if any(test_generator(number_list)):
        return True

    return False


def test_if(number_list):
    for item in test_generator(number_list):
        if item:
            return True

    return False
# ---------------------------------------------------------------------------------------------- #


if __name__ == '__main__':
    t0 = time.time()
    print(test_any(range(1, 1000000000)))
    t1 = time.time()

    t2 = time.time()
    print(test_if(range(1, 1000000000)))
    t3 = time.time()

    print("any:", t1 - t0)
    print(" if:", t3 - t2)
