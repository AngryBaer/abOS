"""
    Test for utilizing mutability without return values
"""
from pprint import pprint


def test_dicts():
    # test pre-mutation
    test_dict = {}
    pprint(test_dict)

    # test post-mutation
    mutating_dict(test_dict)
    pprint(test_dict)


def test_lists():
    # test pre-mutation
    test_list = []
    pprint(test_list)

    # test post-mutation
    mutating_list(test_list)
    pprint(test_list)


def test_tuples():
    # test pre-mutation
    tuple_str = "test_string"
    tuple_list = []
    test_tuple = (tuple_str, tuple_list)
    pprint(test_tuple)

    # test post-mutation
    mutating_list(tuple_list)
    pprint(test_tuple)


def mutating_dict(testDict):
    testDict.setdefault("entry1", "data1")
    testDict.setdefault("entry2", "data2")
    testDict.setdefault("entry3", "data3")


def mutating_list(testList):
    testList.append("list_item_1")
    testList.append("list_item_2")
    testList.append("list_item_3")


if __name__ == "__main__":
    test_dicts()
    test_lists()
    test_tuples()
