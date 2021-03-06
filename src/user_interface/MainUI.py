from src.user_interface.Part1UI import Part1UI
from src.user_interface.Part2UI import Part2UI
from src.user_interface.Part3UI import Part3UI
from src.user_interface.Part4UI import Part4UI
from src.user_interface.Part5UI import Part5UI
from src.user_interface.UI import UI


class MainUI(UI):
    def start_UI(self):
        print("Welcome to Our Search Engine,")
        while True:
            self.print_help()
            input_str = int(input())
            if input_str == 1:
                Part1UI(self.english_indexer, self.persian_indexer).start_UI()
            elif input_str == 2:
                Part2UI(self.english_indexer, self.persian_indexer).start_UI()
            elif input_str == 3:
                Part3UI(self.english_indexer, self.persian_indexer).start_UI()
            elif input_str == 4:
                Part4UI(self.english_indexer, self.persian_indexer).start_UI()
            elif input_str == 5:
                Part5UI(self.english_indexer, self.persian_indexer).start_UI()
            elif input_str == 6:
                print("Thank You For Using Our Search Engine")
                return

    def print_help(self):
        print("Please Select the Part of Project You Want To Test:")
        print("1- Part 1 Pre_Processing")
        print("2- Part 2 Indexing")
        print("3- Part 3 Compressing")
        print("4- Part 4 Spell Correction")
        print("5- Part 5 Search & Retrieval")
        print("6- Exit")
