import Formulas as f
import numpy as np

def test_entropia():
    X = np.array([0,1,0,0,0,1,1,0])
    expect_result = 2
    bits = 2
    assert f.entropia(X,bits) == expect_result, "Incorrect output "


if __name__ == '__main__':
    test_entropia()
    print('All test passed')