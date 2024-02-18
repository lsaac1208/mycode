from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('add/', views.add_record, name='add_record'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('view-resources/', views.view_resources, name='view_resources'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True, next_page=reverse_lazy('admin:index')), name='login'),
]

