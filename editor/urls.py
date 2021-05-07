from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.create,name='editor'),
    path('<unique_id>',views.show,name='show_text'),
    path('edit/<unique_id>',views.edit,name='edit_text')
]
