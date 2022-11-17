
from Extract import Extract

class Controller:

    def __init__(self) -> None:
        self.extract = Extract()

    def execute(self):
        print("This is the main function.")

        self.extract.extract_data()


ETL = Controller()
ETL.execute()