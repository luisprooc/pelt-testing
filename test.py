from package import Pelt


def equal_values(value1,value2):

    return Pelt.is_equal_type(value1,value2)

equal_values( Pelt.gt_mix(),Pelt.gt_mix() )