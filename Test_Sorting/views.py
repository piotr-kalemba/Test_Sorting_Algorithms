from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Avg
from .create_test_sorting_data import create_all_alg_data, create_single_alg_data
from .render_test_chart import TestSingleChart, TestAllChart
from .forms import AllAlgForm, SingleAlgForm, UserLoginForm, UserCreateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import AllAlgTest, SingleAlgTest
from django.contrib.auth.mixins import LoginRequiredMixin


class SingleAlgTestView(LoginRequiredMixin, View):

    def get(self, request):

        form = SingleAlgForm()
        return render(request, 'algorithm_view.html', {'form': form})

    def post(self, request):

        form = SingleAlgForm(request.POST)
        user = request.user

        if form.is_valid():

            algorithm = form.cleaned_data['algorithm']
            unique_keys = bool(int(form.cleaned_data['unique_keys']))

            times_data = create_single_alg_data(algorithm, unique_keys)
            test = SingleAlgTest(algorithm=algorithm, unique_keys=unique_keys, user=user)
            test.set_data(times_data)
            test.save()

            test_objects = SingleAlgTest.objects.filter(algorithm=algorithm).filter(user=user).\
                filter(unique_keys=unique_keys)

            avg_times_data = {}
            avg_times_data['10'] = test_objects.aggregate(Avg('time_10'))['time_10__avg']
            avg_times_data['100'] = test_objects.aggregate(Avg('time_100'))['time_100__avg']
            avg_times_data['1000'] = test_objects.aggregate(Avg('time_1000'))['time_1000__avg']
            avg_times_data['10000'] = test_objects.aggregate(Avg('time_10000'))['time_10000__avg']

            chart = TestSingleChart(algorithm)
            plot = chart.generate(times_data, avg_times_data)
            return render(request, 'algorithm_plot.html', {'plot': plot})

class AllAlgTestView(LoginRequiredMixin, View):

    def get(self, request):

        form = AllAlgForm()
        return render(request, 'test_view.html', {'form': form})

    def post(self, request):

        form = AllAlgForm(request.POST)
        user = request.user

        if form.is_valid():

            list_length = int(form.cleaned_data['list_length'])
            unique_keys = bool(int(form.cleaned_data['unique_keys']))

            if form.cleaned_data['action'] == 'test':

                times_data = create_all_alg_data(list_length, unique_keys)
                test = AllAlgTest(list_length=list_length, unique_keys=unique_keys, user=user)
                test.set_data(times_data)
                test.save()
                title = "Wynik testu pomiaru czasów sortowania"
                y_title = "Czas sortowania (w milisekundach)"
                chart = TestAllChart(title=title, y_title=y_title)
                hist = chart.generate(times_data)

                return render(request, 'test_hist.html', {'hist': hist})

            else:

                test_objects = AllAlgTest.objects.filter(list_length=list_length).\
                    filter(unique_keys=unique_keys).filter(user=user)

                if test_objects:

                    avg_times_data = {}
                    test_number = test_objects.count()
                    avg_times_data['bubble'] = test_objects.aggregate(Avg('bubble'))['bubble__avg']
                    avg_times_data['select'] = test_objects.aggregate(Avg('select'))['select__avg']
                    avg_times_data['merge'] = test_objects.aggregate(Avg('merge'))['merge__avg']
                    avg_times_data['heap'] = test_objects.aggregate(Avg('heap'))['heap__avg']
                    avg_times_data['quick'] = test_objects.aggregate(Avg('quick'))['quick__avg']

                    title = "Średnie wyniki z {} testów".format(
                        test_number) if test_number != 1 else "Średnie wyniki z 1 testu"
                    y_title = "Średni czas sortowania (w milisekundach) "
                    chart = TestAllChart(title=title, y_title=y_title)
                    hist = chart.generate(avg_times_data)

                    return render(request, 'avg_hist.html', {'hist': hist})

                else:

                    return render(request, 'no_data.html')


class CreateUser(View):

    def get(self, request):

        form = UserCreateForm()
        return render(request, 'new_user.html', {'form': form})

    def post(self, request):

        form = UserCreateForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password != password2:
                return render(request, 'passwords_not_matching.html', {'form': form})
            user = User.objects.create_user(password=password, username=username)
            user.save()
            login(request, user)
            return redirect('tests')

        else:
            return render(request, 'new_user.html', {'form': form})


class LoginUser(View):

    def get(self, request):
        form = UserLoginForm()

        return render(request, 'login_user.html', {'form': form})

    def post(self, request):

        form = UserLoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                return redirect('tests')

            else:

                return render(request, 'invalid_login_user.html', {'form': form})


class TestsView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        if user is not None:
            all_algorithms_tests = AllAlgTest.objects.filter(user=user)
            single_algorithm_tests = SingleAlgTest.objects.filter(user=user)
        else:
            all_algorithms_tests = []
            single_algorithm_tests = []

        return render(request, 'tests.html', {'all_algorithms_tests' : all_algorithms_tests, 'single_algorithm_tests':\
                                              single_algorithm_tests})

class AllAlgTestTable(LoginRequiredMixin, View):

    def get(self, request, pk):
        test = AllAlgTest.objects.get(pk=pk)
        return render(request, 'all_test_table.html', {'test' : test})

class SingleAlgTestTable(LoginRequiredMixin, View):

    def get(self, request, pk):
        test = SingleAlgTest.objects.get(pk=pk)
        return render(request, 'single_test_table.html', {'test': test})

class WelcomeView(View):

    def get(self, request):
        return render(request, 'base.html')

