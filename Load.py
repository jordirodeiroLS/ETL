import csv

from typing import List, Dict

class Load:

    def load_to_csv(self, data:Dict[str, int], headers: List[str], filename:str) -> None:

        with open("data/" + filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for category, amount in data.items():
                writer.writerow([category, amount])