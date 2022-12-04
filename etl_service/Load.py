import csv
import os

from typing import List, Dict

class Load:

    def load_to_csv(self, data:Dict[str, int], headers: List[str], filename:str) -> None:

        if os.path.exists("data/" + filename):
            os.remove("data/" + filename)
            print("File deleted")
        else:
            print("File does not exist.")

        with open("data/" + filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for category, amount in data.items():
                writer.writerow([category, amount])

    def create_csv(self, filename) -> None:
        if os.path.exists("data/" + filename):
            os.remove("data/" + filename)

    def append_to_csv(self, data:Dict[str, int], headers: List[str], filename:str, option:str) -> None:

        with open("data/" + filename, option, newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for category, amount in data.items():
                writer.writerow([category, amount])