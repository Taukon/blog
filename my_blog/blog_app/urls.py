from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.Index, name='index'),
    path('create/', views.CreateBlog.as_view(), name='create'),
    path('detail/<int:num>', views.Detail, name='detail'),
    path('delete/<int:num>', views.Delete, name='delete'),
    path('update/<int:pk>', views.UpdateBlog.as_view(), name='update'),
]
