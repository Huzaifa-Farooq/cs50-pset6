from sys import argv

class Checksum:
    """ Class to perform checksum algorithm"""
    def __init__(self, number=""):
        self.number = [number]
        self.number = list(self.number)
        self.index_list_1 = []
        self.index_list_2 = []

    def main(self):
        self.get_list_1()
        self.get_list_2()
        self.get_sum()
        self.validity()
        print(self.card_type())

    def get_list_1(self):
        """ Seprate the number into two parts for verification """
        self.num_list_1 = []

        # Seprate the numbers that are to be multiplies by 2 by indexes
        self.index_list_1 = [i for i in range(0, len(self.number), 2)]


        for i in self.index_list_1:
            item = self.number[i]
            if item in range(0, 10): # Checks if the item is a number
                self.num_list_1.append(item)
            else:
                continue

    def get_list_2(self):
        """  """
        self.index_list_2 = [i for i in range(1, len(self.number), 2)]

        self.num_list_2 = []
        for item in self.index_list_2:
            item = self.number[i]
            if item in range(0, 10):     # Checks if the item is a number
                self.num_list_2.append(item)
            else:
                continue

    def get_sum(self):
        """ finds product of first list items """
        product = []
        for i in self.num_list_1:
            product.append(2 * int(i))

        self.sum_list = []
        sum_1, sum_2 = 0, 0
        # Seprate two-digit int to one digit int
        self.sum_list = [i for i in ''.join(str(x) for x in product)]
        self.sum_list.
        for j in self.sum_list:
            sum_1 += int(j)

        for i in self.num_list_2:
            sum_2 += int(i)

        self.total_sum = sum_1 + sum_2
        return [self.total_sum]


    def card_type(self):
        """ Verify type of number """
        if self.number [0:1] == 34 or 37:
            return "American Express\n"
        elif self.number [0:1] in range(51, 56):
            return "MasterCard\n"
        elif self.number [-1] == 4:
            return "Visa\n"

    def validity(self):
        if self.get_sum()[-1] == 0:
            return True
        else:
            raise Exception("Invalid Card number")
number = input("Number: ")
Checksum(number).main()
