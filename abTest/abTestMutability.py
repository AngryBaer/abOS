"""
    Test for utilizing mutability without return values
"""


from pprint import pprint


def test_dicts():
    # test pre-mutation
    test_dict = dict()
    pprint(test_dict)

    # test post-mutation
    mutating_dict(test_dict)
    pprint(test_dict)


def test_lists():
    # test pre-mutation
    test_list = list()
    pprint(test_list)

    # test post-mutation
    mutating_list(test_list)
    pprint(test_list)


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
