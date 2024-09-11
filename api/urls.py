from django.urls import path
from .views import SoilTypeListCreateView, SoilTypeDetailView

urlpatterns = [
    path('soil-types/', SoilTypeListCreateView.as_view(), name='soiltype-list-create'),
    path('soil-types/<int:pk>/', SoilTypeDetailView.as_view(), name='soiltype-detail'),
    
]
