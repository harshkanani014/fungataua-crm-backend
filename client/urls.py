from django.urls import path

from .views import *

urlpatterns = [
      path('add-status', AddStatus.as_view()),
      path('edit-status/<int:id>', EditStatus.as_view()),
      path('get-status', GetStatus.as_view()),
      path('add-service', AddService.as_view()),
      path('edit-service/<int:id>', EditService.as_view()),
      path('get-service', GetService.as_view()),
      path('add-subcategory', AddSubCategory.as_view()),
      path('edit-subcategory/<int:id>', EditSubCategory.as_view()),
      path('get-subcategory', GetSubCategory.as_view()),
      path('add-category', AddCategory.as_view()),
      path('edit-category/<int:id>', EditCategory.as_view()),
      path('get-category', GetCategory.as_view()),
      path('add-client', AddClient.as_view()),
      path('edit-client/<int:id>', EditClient.as_view()),
      path('get-client', GetClient.as_view()),
      path('get-client/<int:id>', GetEachClient.as_view()),
      path('add-client-service', AddClientService.as_view()),
      path('edit-client-service/<int:id>', EditClientService.as_view()),
      path('get-client-service/<int:id>', GetClientService.as_view())

]