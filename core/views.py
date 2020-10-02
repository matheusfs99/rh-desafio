from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    pass

def list_companys(request):
    context = {}
    auto_complete = Company.objects.all()
    context['auto_complete'] = auto_complete
    search = request.GET.get('search')
    if search:
        companys_list = Company.objects.filter(name__icontains=search).order_by('name')
    else:
        companys_list = Company.objects.all()
    paginator = Paginator(companys_list, 10)
    page = request.GET.get('page')
    companys = paginator.get_page(page)
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


def company_page(request, id):
    context = {}
    company = Company.objects.get(id=id)
    context['company'] = company
    return render(request, 'core/company_page.html', context)




def create_employee(request):
    return render(request, 'core/user_form.html')
