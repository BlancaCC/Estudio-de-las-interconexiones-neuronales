from utils import signal_to_binary

def test_signal_to_binary():
    signal = [0,1.2, 1.3, -0.2,1.3,-1, 0,1.2,0]
    expect_result = [0,0,1,0,0,0,1,0]
    assert signal_to_binary(signal=signal, lower_threshold=-0.5, upper_threshold=1) == expect_result, "Incorrect output"


if __name__ == "__main__":
    test_signal_to_binary()
    print('All test passed')