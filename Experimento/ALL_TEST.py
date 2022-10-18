from tests.test_signal_to_binary import test_signal_to_binary
from tests.test_get_threshold_graph import test_get_threshold_graph

if __name__ == '__main__':
    tests = [test_signal_to_binary, test_get_threshold_graph]
    len = len(tests)
    cnt = 1
    for t in tests:
        print(f'Test {cnt}/{len}')
        t()
        cnt += 1
    print('All test passed')