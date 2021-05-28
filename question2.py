

class FindPoint:
    def __init__(self, take_array):
        self.take_array = take_array
        self.checkBondries(self.take_array)

    def checkBondries(self, take_arry):
        if len(take_arry) == 1:
            print("{} is equilibrium point".format(take_arry[0]))
        elif len(take_arry) == 2:
            print("{} is your array Length. Length of array must be great then 2".format(len(take_arry)))
        elif len(take_arry) > 2:
            if self.equilibriumPoint(self.take_array) == -1:
                print("{} | Sorry, The List of array don't have equilibriumPoint".format(self.equilibriumPoint(self.take_array)))
            else:
                print("{} is  equilibriumPoint".format(
                    self.equilibriumPoint(self.take_array)))

    def equilibriumPoint(self, list_of_values):

        left_side_sum = 0
        right_side_sum = 0
        index = -1

        for elem in list_of_values:
            right_side_sum = right_side_sum + elem

        for values in list_of_values:
            right_side_sum = right_side_sum - values

            if right_side_sum == left_side_sum:
                return values
            else:
                left_side_sum = left_side_sum + values
        return index


if __name__ == "__main__":
    list_of_array = list()
    number = input("Enter length of array = ")
    legth_of_N = int(number)
    for values in range(1, legth_of_N+1):
        array_value = input("Enter Array Elements = ")
        number_list = int(array_value)
        list_of_array.append(number_list)
    FindPoint(list_of_array)
