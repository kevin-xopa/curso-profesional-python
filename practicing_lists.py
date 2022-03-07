# [1, 1, 2, 3, 4, 4] -> [1, 2, 3, 4]

# receive list as parameter
def remove_duplicates(some_list):
    # create an empty list
    without_duplicates = []
    # loop through the list passed as a parameter
    for element in some_list:
        # we ask is not in the created list
        if element not in without_duplicates:
            # add to created without_duplicates
            without_duplicates.append(element)
    # return without_duplicates
    return without_duplicates


def run():
    random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]

    print(remove_duplicates(random_list))

if __name__ == "__main__":
    run()
