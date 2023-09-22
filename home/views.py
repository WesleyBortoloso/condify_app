from django.shortcuts import render
from setup.utils.count_records import count_records_in_tables

def homepage(request):
    counts = count_records_in_tables()

    context = {
        'counts': counts,
    }

    return render(request, 'homepage/home.html', context)
