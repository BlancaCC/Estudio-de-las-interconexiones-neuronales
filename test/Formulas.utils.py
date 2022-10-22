import Formulas as f
import numpy as np

def test_entropy():
    X = np.array([0,1,0,0,0,1,1,0])
    expect_result = 2
    bits = 3
    stride = 4
    assert f.entropy(X,bits,stride) == expect_result, "Incorrect output "


if __name__ == '__main__':
    test_entropy()
    print('All test passed')