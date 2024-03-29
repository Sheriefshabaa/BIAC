from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('classification_model', views.PredictMarkView)
urlpatterns = [
	path('form/', views.MyForm, name='myform'),
    path('api/', include(router.urls)),
    path('status/', views.predictmark),
 
] 