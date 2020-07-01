
class Readiblity:
    """ finding readiblity using Coleman-Liau index """
    def __init__(self, string):
        self.string = [i for i in str(string)]
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.total_sentences = 0
        self.words = 1 # Words = 1 because it does not count last word as there is no space
        self.total_letters = 0

        for i in self.string:
            if i in ['!', '.', '?']:
                self.total_sentences += 1
            elif i == " ":
                self.words += 1
            elif i.upper() in self.alpha:
                self.total_letters += 1

    def main(self):
        print(f"Grade: {self.get_index()}")

    def get_index(self):
        """return the grade"""
        avg_letters = (100 * self.total_letters) / self.words
        avg_sentences = (100 * self.total_sentences) / self.words

        index = round (0.0588 * (avg_letters) - 0.296 * (avg_sentences) - 15.8)
        if int(index) < 1:
            return "Less than Grade 1"
        elif int(index) > 16:
            return "Above Grade 16"
        else:
            return int(index)


text = input("Text: ")
r = Readiblity(text)
r.main()
print(f"Letter(s): {r.total_letters}\nWord(s): {r.words}\nSentence(s): {r.total_sentences}\n")
