from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index_Service.as_view(), name='index_service'),
    path('new', views.New_Service.as_view(), name='new_service'),
    path('<int:id>/edit',views.Edit.as_view(), name='edit_service'),
    path('<int:id>/delete', views.Delete_service.as_view(), name='delete_service'),
    path('<int:id>', views.Show_Service.as_view(), name='show_service'),
    path('<int:id>/register', views.Register_Service.as_view(), name='register_service'),
    path('register/', views.List_Register_Service.as_view(), name='list_register_service'),
    path('register/<int:id>/destroy', views.Destroy_Service.as_view(), name='destroy_service'),
    path('register/<int:id>/activate', views.Activate_Service.as_view(), name='activate_service'),

    # path('notification/', include('Notification.urls'))
]