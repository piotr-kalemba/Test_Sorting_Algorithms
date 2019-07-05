# Test_Sorting_Algorithms
Project uses Django and Pygal to compare classic sorting algorithms.

A) The goal of this project is to compare and visualize efficiency of classic sorting algorithms, i.e.
bubble sort, select sort, merge sort, quick sort and heap sort. The code for the algorithms is an
adaptation of the pseudo code from the Wikipedia entries concerning relevant sorting algorithms.

B) The algorithms are analyzed in two ways:
1. First (way) fixes a random list of one of the lengths: 10, 100, 1000, 10000 (the user chooses the length)
and the application creates data consisting of the sorting times (by individual algorithms). The
data is recorded in the database and a histogram using pygal library is created. Moreover, the user
can see in another histogram the average results of all the tests he has run (for a given list length).
2. The other compares the performance of a single algorithm for four random lists of the lengths:
10, 100, 1000, 10000 respectively. When the user runs the test a line plot is created to show the sorting
times for the individual lists and the data set is recorded in the database.
The plot contains two graphs - for the current test and for the tests the user has run so far (for given
algorithm).

Since all the user tests' data are kept in the database the user can view sorting times (in milliseconds)
presented in a table for any given test.


C) Installation Guide:
1. Go to the directory with the program:
cd path/to/the program
2. create a virtual environment:
virtualenv -p python3 env
3. install dependencies:
python3 install -r requirements.py
4. create database ‘test_sorting’
>> sudo su - postgres
>> psql
>> CREATE DATABASE test_sorting;
5. Open the file settings.py (Test_Sorting_Algorithms/Sorting_Algorithms/settings.py).
Find the dictionary 'DATABASES' and change the values of the keys 'USER' and 'PASSWORD' adequately.


D) Some information about files that are not usually a part of a standard Django project:

The file Test_Sorting/sorting_algorithms/sorting_times.py contains functions that accept a list
as an argument and return the time the computer needed to sort the list by given algorithm.

The file Test_Sorting/create_test_sorting_data.py contains functions that return dictionaries with
the revelant data depending on which test the user has chosen.

The file Test_Sorting/render_test_chart.py is the only file in application that uses Pygal library and
renders charts visualizing data sets.

