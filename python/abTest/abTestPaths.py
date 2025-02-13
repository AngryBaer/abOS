import os

if __name__ == "__main__":
    TEST_PATH = os.path.relpath(
        "/common/root/file/path.ext",
        "/common/root"
    )
    print(TEST_PATH)
    # >>> "file/path.ext"
