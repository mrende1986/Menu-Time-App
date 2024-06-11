import matplotlib.pyplot as plt

class BarChartGenerator:
    def __init__(self, data, labels, title="Bar Chart", xlabel="Categories", ylabel="Values"):
        self.data = data
        self.labels = labels
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def generate_chart(self):
        fig, ax = plt.subplots()
        ax.bar(self.labels, self.data)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title)
        plt.show()
