from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [

   path('', index, name='index'),
   path('logout', logout_user, name='logout'),
   path('cadastrar-usuario/', cadastro_user, name='cadastro_user'),

   path('empresas/', list_companys, name='companys'),
   path('cadastrar-empresa/', register_company, name='register_company'),
   path('empresa/<uuid:id>/', company_page, name='company_page'),
   path('editar-empresa/<uuid:id>/', edit_company, name='edit_company'),
   path('empresa/<uuid:id>/delete', delete_company, name='delete_company'),

   path('cadastrar-departamento/<uuid:company_id>/', create_department, name='create_department'),
   path('departamento/<uuid:id>/', department_page, name='department_page'),
   path('editar-departamento/<uuid:id>/', edit_department, name='edit_department'),
   path('departamento/<uuid:id>/delete', delete_department, name='delete_department'),

   path('cadastrar-colaborador/<uuid:department_id>/', create_employee, name='create_employee'),
   path('colaborador/<uuid:id>/', employee_page, name='employee_page'),
   path('colaborador/<uuid:id>/delete', delete_employee, name='delete_employee'),
   path('editar-colaborador/<uuid:id>/', edit_employee, name='edit_employee'),



   # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
   # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
   # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
   # path('process-create', ProcessCreate.as_view(), name='process-create'),
   # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
   # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
   # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),


]