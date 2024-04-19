def read_file(level: int, file_id: int, is_test: bool) -> list[str]:
    test_or_data = 'test' if is_test else 'data'
    with open(f'data/level-{level}-{test_or_data}-{file_id}.txt') as f:
        return f.read().splitlines()
