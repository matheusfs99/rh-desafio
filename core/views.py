from django.shortcuts import render, redirect
from .models import Company, Department
from .forms import CompanyForm
from django.core.paginator import Paginator
from django.http.response import Http404

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
    form = CompanyForm(request.POST or None, request.FILES or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'core/register_company.html', context)


def company_page(request, id):
    context = {}
    company = Company.objects.get(id=id)
    context['company'] = company
    departments = Department.objects.filter(company__exact=id)
    context['departments'] = departments
    return render(request, 'core/company_page.html', context)


def edit_company(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, request.FILES or None, instance=company)
    context = {'form': form}
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/empresa/{}'.format(id))
    return render(request, 'core/register_company.html', context)


def delete_company(request, id):
    try:
        company = Company.objects.get(id=id)
        company.delete()
    except Exception:
        raise Http404()
    return redirect('/')


def create_employee(request):
    return render(request, 'core/user_form.html')
