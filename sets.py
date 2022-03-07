# unique collection of immutable unordered elements


# Union
my_set1 = {2, 3, 4}
my_ser2 = {4, 5, 6, 7}
my_set3 = my_set1 | my_ser2  # {2, 3, 4, 5, 6, 7}


# insertion
# only the elements in common remain
my_set1 = {2, 3, 4}
my_ser2 = {4, 5, 6, 7, 3}
my_set3 = my_set1 & my_ser2  # {3, 4}


# difference /subtraction
my_set1 = {2, 3, 4}
my_ser2 = {4, 5, 6, 7}
my_set3 = my_set1 - my_ser2  # {2, 3}
my_set3 = my_ser2 - my_set1  # {5, 6, 7}

# asymmetric difference
my_set1 = {2, 3, 4}
my_ser2 = {4, 5, 6, 7}
my_set3 = my_set1 ^ my_ser2  # {2, 3, 5, 6, 7}