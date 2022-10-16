from tests.utils_test import test_signal_to_binary

if __name__ == '__main__':
    tests = [test_signal_to_binary]
    len = len(tests)
    cnt = 1
    for t in tests:
        print(f'Test {cnt}/{len}')
        t()
        cnt += 1
    print('All test passed')