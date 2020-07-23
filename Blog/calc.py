from django.shortcuts import render
from django.http import HttpResponse


def try_addition_compute(request):
    num_1 = request.GET['num_1']
    num_2 = request.GET['num_2']
    result_count = int(num1) + int(num2)
    return HttpResponse("[CONSOLE] The Result Count Number => [  %s  ]" % str(result_count))
