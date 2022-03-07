import time


def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    if max == None:
        while True:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
    else:
        while True:
            if counter == 0 and counter < max:
                counter += 1
                yield n1
            elif counter == 1 and counter < max:
                counter += 1
                yield n2
            else:
                if counter < max:
                    aux = n1 + n2
                    n1, n2 = n2, aux
                    counter += 1
                    yield aux
                else:
                    break


if __name__ == '__main__':
    for element in fibo_gen(4):
        print(element)
        time.sleep(0.5)
