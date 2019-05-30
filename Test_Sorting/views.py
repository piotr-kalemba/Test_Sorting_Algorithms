from django.shortcuts import render
from django.views import View
from .create_test_sorting_data import create_test_sorting_data
from .render_test_chart import TestChart
from .forms import TestForm
from .models import TestInstance, AverageTimes

class IndexView(View):

    def get(self, request):

        form = TestForm()
        return render(request, 'test_view.html', {'form': form})

    def post(self, request):

        form = TestForm(request.POST)

        if form.is_valid():

            list_length = int(form.cleaned_data['list_length'])
            unique_keys = int(form.cleaned_data['unique_keys'])

            if form.cleaned_data['action'] == 'test':

                times_data = create_test_sorting_data(list_length, unique_keys)
                test = TestInstance.objects.get_or_create(list_length=list_length, unique_keys=bool(unique_keys))[0]
                test.set_data(times_data)
                test.save()
                avg_times = AverageTimes.objects.get_or_create(test=test)[0]
                avg_times.update_data()
                avg_times.save()
                title = "Wynik testu pomiaru czasów sortowania"
                y_title = "Czas sortowania (w milisekundach)"
                chart = TestChart(title=title, y_title=y_title)
                hist = chart.generate(times_data)

                return render(request, 'test_hist.html', {'hist': hist})

            else:

                if TestInstance.objects.filter(list_length=list_length).filter(unique_keys=bool(unique_keys)):

                    test = TestInstance.objects.filter(list_length=list_length).filter(unique_keys=bool(unique_keys))[0]
                    avg_times = AverageTimes.objects.get_or_create(test=test)[0]
                    test_number = avg_times.test_number
                    avg_times_data = avg_times.get_data()
                    title = "Średnie wyniki z {} testów".format(test_number) if test_number != 1 else "Średnie wyniki z 1 testu"
                    y_title = "Średni czas sortowania (w milisekundach) "
                    chart = TestChart(title=title, y_title=y_title)
                    hist = chart.generate(avg_times_data)

                    return render(request, 'avg_hist.html', {'hist': hist})

                else:

                    return render(request, 'no_data.html')






