import pygal


class TestAllAlgorithmsChart():

    def __init__(self, title, y_title, x_title="Algorytm sortowania"):
        self.chart = pygal.Bar()
        self.chart.title = title
        self.chart.x_title = x_title
        self.chart.y_title = y_title

    def generate(self, chart_data):
        for key, value in chart_data.items():
            self.chart.add(key, value)

        return self.chart.render(is_unicode=True)


class TestAlgorithmChart():

    def __init__(self, algorithm):
        self.chart = pygal.Line()
        self.chart.title = "Wynik testu pomiaru czasów sortowania za pomocą {} sort.".format(algorithm)
        self.chart.x_title = "Liczba kluczy w liście"
        self.chart.y_title = "Czas sortowania (w milisekundach)"

    def generate(self, chart_data_1, chart_data_2):
        self.chart.x_labels = ['n=10', 'n=100', 'n=1000','n=10000']
        self.chart.add('bieżący test', [chart_data_1['10'], chart_data_1['100'], chart_data_1['1000'],
                                                   chart_data_1['10000']])
        self.chart.add('wynik średni', [chart_data_2['10'], chart_data_2['100'],
                                                                          chart_data_2['1000'], chart_data_2['10000']])

        return self.chart.render(is_unicode=True)

