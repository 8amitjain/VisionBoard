from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from. import views

urlpatterns = [
    path('basic-upload/<int:pk>/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('vision/view/all/', views.all_list_view, name='vision-view-all'),
    path('vision/view/detail/<int:pk>/', views.detail_view, name='popup-detail-view'),
    path('vision/view/<int:pk>/', views.vision_view, name='vision-view'),
    path('vision/create/', views.CreateVision.as_view(), name='vision-create'),
    path('vision/<int:pk>/update/', views.UpdateVision.as_view(), name='vision-update'),
    path('vision/<int:pk>/delete/', views.VisionDeleteView.as_view(), name='vision-delete'),
    path('vision/<int:pk>/image/delete/', views.VisionImageDeleteView.as_view(), name='vision-image-delete'),

]
# MEDIA_URL = '\media\\'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

