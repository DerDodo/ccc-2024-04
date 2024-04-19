from util import read_file

level = 0


def level0(file_id: int, is_test: bool) -> int:
    lines = read_file(level, file_id, is_test)
    return sum(map(int, lines))


if __name__ == '__main__':
    assert level0(1, True) == 5
    print(f"Solution data 1: {level0(1, False)}")
