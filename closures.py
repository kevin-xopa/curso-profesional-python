def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo letritas caballero'
        return string * n
    return repeater


def make_division_by(n):
    def home(x):
        return x / n
    return home


def run():
    division = make_division_by(7)
    print(division(70))


x = 1
def my_num():
    x = 4


if __name__ == "__main__":
    run()
