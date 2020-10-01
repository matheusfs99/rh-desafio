from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm

# Create your views here.
def index(request):
    pass

def list_companys(request):
    context = {}
    companys = Company.objects.all()
    context['companys'] = companys
    return render(request, 'core/companys.html', context)


def register_company(request):
    context = {}
    form = CompanyForm()
    if request.POST:
        form = CompanyForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context['form'] = form
    return render(request, 'core/register_company.html', context)



def create_employee(request):
    return render(request, 'core/user_form.html')
