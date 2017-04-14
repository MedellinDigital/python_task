import string


class Del:
    def __init__(self, keep=string.digits):
        self.comp = dict((ord(c), c) for c in keep)

    def __getitem__(self, k):
        return self.comp.get(k)


def return_int(input_value):
    DD = Del()
    x = input_value.translate(DD)
    return int(x)

day_number = 0
smallest_temperature_spread = 10000
line_number = 0
for i in open('weather.dat').readlines():
    value = i.strip().split()
    if line_number > 1:
        maximum_temperature = return_int(value[1])
        minimum_temperature = return_int(value[2])
        temperature_spread = maximum_temperature - minimum_temperature
        if temperature_spread < smallest_temperature_spread:
            smallest_temperature_spread = temperature_spread
            line_number_for_smallest_temperature_spread = line_number
            day_number = return_int(value[0])

    line_number += 1

print('Day number with the smallest temperature spread is: ', day_number)
