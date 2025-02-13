"""
    Testing how to find the next increment of a numbered name.
"""
import re


def increment_name(name: str, name_list: list) -> str:
    search_pattern = re.compile(f"{name}(\\d*)")
    name_set = set(x for x in name_list if search_pattern.match(x))

    if name not in name_set:
        name_list.append(name)
        return name

    def find_next():
        increment = 1
        while f'{name}{increment}' in name_set:
            increment += 1
        return increment

    new_name = f'{name}{find_next()}'
    name_list.append(new_name)
    return new_name


if __name__ == "__main__":
    TEST_NAME1 = "name"
    TEST_NAME2 = "otherName"
    TEST_NAME3 = "test"
    TEST_NAME4 = "something"
    TEST_NAME5 = "anything"
    TEST_LIST = ['name', 'otherName1', 'otherName2', "test", "test2", "something", "something1"]

    assert increment_name(TEST_NAME1, TEST_LIST) == "name1"
    assert increment_name(TEST_NAME2, TEST_LIST) == "otherName"
    assert increment_name(TEST_NAME2, TEST_LIST) == "otherName3"
    assert increment_name(TEST_NAME3, TEST_LIST) == "test1"
    assert increment_name(TEST_NAME4, TEST_LIST) == "something2"
    assert increment_name(TEST_NAME5, TEST_LIST) == "anything"
    print(TEST_LIST)
