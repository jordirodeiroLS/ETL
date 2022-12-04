
import matplotlib.pyplot as plt
import Constants

class Show:

    def histogram(self, data, title, x_data, y_data) -> None:

        fig = plt.figure(figsize=(30,15))
        plt.bar(data.keys(), data.values())
        plt.xticks(fontsize=Constants.LABELS_FONT_SIZE, rotation = 45)
        plt.xlabel(x_data, fontweight='bold', fontsize=Constants.AXIS_FONT_SIZE)
        plt.ylabel(y_data, fontweight='bold', fontsize=Constants.AXIS_FONT_SIZE)
        plt.title(title, fontweight='bold', fontsize=Constants.TITLE_FONT_SIZE)
        plt.savefig("data/" + title + '.png', bbox_inches='tight')