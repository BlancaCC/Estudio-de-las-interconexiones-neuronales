from utils import signal_to_binary

def test_signal_to_binary():
    print('\tSignal to binary list of spikes. Should return a correct list of 0s and 1s.')
    signal =        [0, 1.2, 1.3, -0.2, 1.3, -1, 0,   1.2, 0]
    expect_result = [0, 0,    1,   0,     0,  0,  0,     1,  0]
    output = signal_to_binary(signal=signal, lower_threshold=-0.5, upper_threshold=1)
    assert output == expect_result, f"Incorrect output, expected {expect_result} but {output} arose."
