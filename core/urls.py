from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [

   path('', list_companys, name='companys'),
   path('cadastrar-empresa/', register_company, name='register_company'),
   path('cadastrar-colaborador/', create_employee, name='create_employee'),
   path('empresa/<uuid:id>/', company_page, name='company_page'),
   path('editar-empresa/<uuid:id>/', edit_company, name='edit_company'),
   path('empresa/<uuid:id>/delete', delete_company, name='delete_company'),

   # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
   # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
   # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
   # path('process-create', ProcessCreate.as_view(), name='process-create'),
   # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
   # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
   # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),


]