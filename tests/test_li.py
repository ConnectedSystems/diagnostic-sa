import numpy as np

from diagnostic_sa.li_2010 import li_2010_case1, li_2010_case1_inactive


def test_li_2010():
    expected_result = 0.0

    # Run the model
    result = li_2010_case1(0.0, 0.0, 0.0, 0.0, 0.0)

    assert result == expected_result, "Result should be zero"
    

def test_li_2010_property_small():
    np.random.seed(101)
    inputs = np.random.randint(-100.0, 100.0, size=(5, 5))
    for i in inputs:
        result = li_2010_case1(*i)
        if np.sum(i[i >= 0]) >= np.abs(np.sum(i[i < 0])):
            assert result >= 0.0, "Result should be positive" 
        else:
            assert result < 0.0, "Result should be negative"


def test_li_2010_positive_property_larger():
    np.random.seed(101)
    inputs = np.random.randint(-100.0, 100.0, size=(10, 5))
    for i in inputs:
        result = li_2010_case1(*i)
        if np.sum(i[i >= 0]) >= np.abs(np.sum(i[i < 0])):
            assert result >= 0.0, "Result should be positive" 
        else:
            assert result < 0.0, "Result should be negative" 


def test_li_2010_parameter_active():
    """Testing for parameter activity.

    This is equivalent to conducting an OAT sensitivity analysis.
    """
    np.random.seed(101)

    base = [-100.0, -100.0, -100.0, -100.0, -100.0]
    nominal_result = li_2010_case1_inactive(*base)  # run model at nominal position

    for idx, x_i in enumerate([100.0, 100.0, 100.0, 100.0, 100.0]):
        tmp = base[:]  # copy nominal values
        tmp[idx] = x_i  # perturb parameter value
        result = li_2010_case1_inactive(*tmp)  # run model

        x_diff = np.abs(base[idx] - tmp[idx])
        y_diff = np.abs(nominal_result - result)

        # Test sensitivity measure
        assert (y_diff / x_diff) != 0.0, f"Perturbing parameter x_{idx+1} should affect SA metric!"

        # Alternative test for inactivity
        assert result != nominal_result, f"Perturbing parameter x_{idx+1} should affect results!"
