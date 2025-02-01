from django.urls import path
from .views import CreateInstitution, CreateRepresentative, CustomTokenObtainPairView

urlpatterns = [
    path('create/institution/', CreateInstitution.as_view(), name='create_institution'),
    path('create/representative/', CreateRepresentative.as_view(), name='create_representative'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]