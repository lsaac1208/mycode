from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContactRecord
from .forms import ContactRecordForm
from django.db.models import Q
from datetime import datetime

@login_required
def record_list(request):
    records = ContactRecord.objects.all()
    return render(request, 'crm/record_list.html', {'records': records})

@login_required
def add_record(request):
    if request.method == 'POST':
        form = ContactRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = ContactRecordForm()
    return render(request, 'crm/add_record.html', {'form': form})

@login_required
def view_resources(request):
    resources = Resource.objects.all()
    if 'start_date' in request.GET and 'end_date' in request.GET:
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            resources = resources.filter(Q(date__range=(start_date, end_date)))

    return render(request, 'crm/view_resources.html', {'resources': resources})
