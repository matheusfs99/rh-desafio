from django.shortcuts import render
from .models import Company

# Create your views here.
def index(request):
    pass


def list_companys(request):
    context = {}
    companys = Company.objects.all()
    context['companys'] = companys
    return render(request, 'core/companys.html', context)


def create_employee(request):
    return render(request, 'core/user_form.html')
