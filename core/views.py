from django.shortcuts import render, redirect
from .models import Company, Department, Employee
from .forms import CompanyForm, DepartmentForm, EmployeeForm
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/empresas')
        else:
            messages.error(request, 'Usuário e/ou senha inválida')
    return render(request, 'core/index.html')


def cadastro_user(request):
    if request.POST:
        nome = request.POST.get('first-name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(first_name=nome,
                                 username=username,
                                 password=password)
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/empresas')
        else:
            messages.error(request, 'Preencha todos os campos')
    return render(request, 'core/cadastro_user.html')


def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def list_companys(request):
    context = {}
    user = request.user
    context['user'] = user
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


@login_required(login_url='/')
def register_company(request):
    form = CompanyForm(request.POST or None, request.FILES or None)
    user = request.user
    context = {'form': form, 'user': user}
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/empresas')
    return render(request, 'core/register_company.html', context)


@login_required(login_url='/')
def company_page(request, id):
    user = request.user
    company = Company.objects.get(id=id)
    search = request.GET.get('search')
    if search:
        departments = Department.objects.filter(company__exact=id).filter(name__icontains=search)
    else:
        departments = Department.objects.filter(company__exact=id)
    paginator = Paginator(departments, 10)
    page = request.GET.get('page')
    departments = paginator.get_page(page)
    context = {'company': company, 'departments': departments, 'user': user}
    return render(request, 'core/company_page.html', context)


@login_required(login_url='/')
def edit_company(request, id):
    user = request.user
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, request.FILES or None, instance=company)
    context = {'form': form, 'user': user}
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/empresa/{}'.format(id))
    return render(request, 'core/register_company.html', context)


@login_required(login_url='/')
def delete_company(request, id):
    try:
        company = Company.objects.get(id=id)
        company.delete()
    except Exception:
        raise Http404()
    return redirect('/empresas')


@login_required(login_url='/')
def create_department(request, company_id):
    user = request.user
    company = Company.objects.get(id=company_id)
    form = DepartmentForm(request.POST or None)
    context = {'form': form, 'company': company, 'user': user}
    if request.POST:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = get_object_or_404(Company, id=company_id)
            obj.admin = request.user
            obj.save()
            return redirect('/empresa/{}'.format(company_id))
    return render(request, 'core/create_department.html', context)


@login_required(login_url='/')
def department_page(request, id):
    user = request.user
    department = Department.objects.get(id=id)
    employees = Employee.objects.filter(department__exact=id)
    context = {'department': department, 'employees': employees, 'user': user}
    return render(request, 'core/department_page.html', context)


@login_required(login_url='/')
def edit_department(request, id):
    user = request.user
    department = Department.objects.get(id=id)
    company = Company.objects.get(id=department.company.id)
    form = DepartmentForm(request.POST or None, instance=department)
    context = {'form': form, 'department': department, 'company': company, 'user': user}
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/departamento/{}'.format(id))
    return render(request, 'core/create_department.html', context)


@login_required(login_url='/')
def delete_department(request, id):
    try:
        department = Department.objects.get(id=id)
        department.delete()
    except Exception:
        raise Http404()
    return redirect('/empresa/{}'.format(department.company.id))


@login_required(login_url='/')
def create_employee(request, department_id):
    user = request.user
    department = Department.objects.get(id=department_id)
    form = EmployeeForm(request.POST or None)
    context = {'form': form, 'department': department, 'user': user}
    if request.POST:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.department = Department.objects.get(id=department.id)
            obj.company = Company.objects.get(id=department.company.id)
            obj.save()
            return redirect('/departamento/{}'.format(department_id))
    return render(request, 'core/user_form.html', context)


@login_required(login_url='/')
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
    except Exception:
        raise Http404()
    return redirect('/empresa/{}'.format(employee.department.company.id))