import csv
from sys import argv, exit
import re

class DnaTest:
    """CLASS HELP: the DNA test, simply give DNA sequence to the program, and it searches in the database to
       determine the person who owns the sample.

    type the following in cmd to run the program:
    python dna.py databases/small.csv sequences/1.txt """
    def __init__(self):
        # Reading database and sequence files
        dna_seq_path = argv[-1]
        try:
            open(dna_seq_path)
        except FileNotFoundError:
            print("DNA Sequence File not Found")
            exit(1)
        else:
            with open(dna_seq_path, 'r') as f:
                self.seq_file = f.read()  # Reads txt file and store the sequence as a string
                self.seq_file = "".join(str(x) for x in self.seq_file)

        csv_path = argv[-2]
        try:
            open(csv_path)
        except FileNotFoundError:
            print("Database File not Found")
            exit(1)
        else:
            with open(csv_path, 'r') as f:
                self.database_file = f.readlines()

        # Read CSV file as a dictionary,
        self.dict_database = csv.reader(self.database_file)
        # Read CSV file to take its first row, get_str_list()
        self.reader = csv.reader(self.database_file)
         # Temporary dictionary to select maximum
        self.select_max = {}
         # Dictionary containing max STR sequence count
        self.dict_from_sequence = {}

    # returns the first row of the CSV file (database file)
    def get_str_list(self):
        """ returns STR list """
        # get first row from CSV file
        keys = next(self.reader)

        # remove 'name' from list, get STR only.
        keys.remove('name')
        return keys

    def get_max(self, str_key):
        """ Return max value that STR appear in a sequence  """
        # Iteration values [0:5] if the word has 5 letters
        i = 0
        j = len(str_key)

        # Counter of maximum number of time STR is repeated
        max, temp = 0, 0
        # Saves DNA sequence
        dna_seq = self.seq_file

        for x in range(len(dna_seq)):
            if dna_seq[i:j] == str_key:
                # When a match is found start to count the consecutive matches until there's no match.
                while dna_seq[i:j] == str_key:
                    temp += 1
                    # Updates the iteration values so that it keeps searching
                    i += len(str_key)
                    j += len(str_key)

                # Checks if temp is greater than max then it is the new max
                if temp > max:
                    max = temp

            # If there's no match in that substring, update values to keep seaching.
            else:
                i += 1
                j += 1
        return max

    # returns dictionary of computed STRs from the sequence file (key(STR): value(count))
    def get_str_count_from_sequence(self):
        """ returns a dictionary of STR counts in sequence"""
        for str_key in self.get_str_list():
            regex = rf"({str_key})+"
            matches = re.finditer(regex, self.seq_file, re.MULTILINE)

            # my code
            for match in matches:
                match_len = len(match.group())
                key_len = len(str_key)
                self.select_max[match] = match_len
                #  select max value from results dictionary (select_max)
                max_values = max(self.select_max.values())

                if max_values >= key_len:
                    result = int(max_values / key_len)
                    self.select_max[str_key] = result
                    self.dict_from_sequence[str_key] = result

            # clear compare dictionary to select new key
            self.select_max.clear()

        return self.dict_from_sequence

    def get_str_count_db(self):
        """ returns STR counts list-DATABASE """
        str_counts_db = []
        # Stores each str counts of database in list
        for row in self.reader:
            str_counts_db.append(row)

        # Returns string list
        return str_counts_db

    def get_str_count_seq_list(self):
        """ Returns a list of number of time a STR appears in sequence"""
        # Temp list to save STR counts
        temp = []
        for str_count in self.get_str_count_from_sequence().values():
            temp.append(str(str_count))
        return temp

    def compare_database_with_seq(self):
        """ Compares lists of str counts of database and of str counts of sequence"""
        str_counts_seq = self.get_str_count_seq_list()
        str_counts_db = self.get_str_count_db()

        matched_name = ""
        # Loop that will compare values in database and processed values
        for i in str_counts_db:
            if str_counts_seq == i[1:]:
                matched_name = i[0]
            else:
                pass

        if matched_name != "":
            return matched_name
        else:
            return "Not found"

# run the class and its functions (Program control)
if __name__ == '__main__':
    if len(argv) != 3:
        print("Invalid Command\nUsage: python dna.py database_path sequence_path")
        exit(1)

    RunTest = DnaTest()
    print(RunTest.compare_database_with_seq())
