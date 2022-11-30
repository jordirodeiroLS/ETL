
import matplotlib.pyplot as plt

class Show:

    def histogram(self, data, title, x_data, y_data) -> None:

        fig = plt.figure(figsize=(30,10))
        plt.bar(data.keys(), data.values())
        #plt.xticks()
        plt.xlabel(x_data, fontweight='bold', fontsize=20)
        plt.ylabel(y_data, fontweight='bold', fontsize=20)
        # TODO: fontsize in constants.py
        plt.title(title, fontweight='bold', fontsize=20)
        plt.savefig("data/" + title + '.png')