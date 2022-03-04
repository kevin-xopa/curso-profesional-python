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
    # repeat_5 = make_repeater_of(5)
    # print(repeat_5("Jelow "))
    # repeat_5 = make_repeater_of(4)
    # print(repeat_5("xopita "))
    division = make_division_by(7)
    print(division(70))


if __name__ == "__main__":
    run()
