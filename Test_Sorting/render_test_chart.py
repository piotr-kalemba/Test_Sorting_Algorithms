import pygal


class TestChart():

    def __init__(self, title, y_title, x_title="Algorytm sortowania"):
        self.chart = pygal.Bar()
        self.chart.title = title
        self.chart.x_title = x_title
        self.chart.y_title = y_title

    def generate(self, chart_data):
        for key, value in chart_data.items():
            self.chart.add(key, value)

        return self.chart.render(is_unicode=True)



