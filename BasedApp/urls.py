from django.urls import path,include
from . import views

app_name="BasedApp"

urlpatterns = [
    path('',views.DataList.as_view(),name='home'),
    path('create/',views.CreateData.as_view(),name='create'),
    path('about/',views.MyView.as_view()),
    path('update/<pk>',views.UpdateData.as_view(),name='update'),
    path('delete/<pk>',views.DeleteData.as_view(),name='delete'),
    path('/form',views.DataFormView.as_view()),
    path('<pk>',views.DataDetailView.as_view(),name='detail'),

]
