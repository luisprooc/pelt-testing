from package import Pelt


def equal_values(value1,value2):

    return Pelt.is_equal_type(value1,value2)

multy_dict = {
    Pelt.gt_int(): Pelt.gt_dict(4), 
    Pelt.gt_str(): Pelt.gt_str(5)
}

print(multy_dict)