def li_2010_case1(x1, x2, x3, x4, x5):
    """An incorrect implementation of Li et al. (2010) example case #1.

    `y` should be the sum of all inputs, but here an inadvertent typo subtracts x5.

    References
    ----------
    .. [1] Li, G., Rabitz, H., Yelvington, P.E., Oluwole, O.O., Bacon, F., 
           Kolb, C.E., Schoendorf, J., 2010. 
           Global Sensitivity Analysis for Systems with Independent and/or 
           Correlated Inputs. 
           J. Phys. Chem. A 114, 6022–6032. 
           https://doi.org/10.1021/jp9096919
    """
    y = x1 + x2 + x3 + x4 - x5

    return y


def li_2010_case1_inactive(x1, x2, x3, x4, x5):
    """An implementation of Li et al. (2010) example case #1 with an inactive parameter.

    `y` should be the sum of all inputs but x5 is essentially ignored.

    References
    ----------
    .. [1] Li, G., Rabitz, H., Yelvington, P.E., Oluwole, O.O., Bacon, F., 
           Kolb, C.E., Schoendorf, J., 2010. 
           Global Sensitivity Analysis for Systems with Independent and/or 
           Correlated Inputs. 
           J. Phys. Chem. A 114, 6022–6032. 
           https://doi.org/10.1021/jp9096919
    """
    y = x1 + x2 + x3 + x4 - x5 + x5

    return y
