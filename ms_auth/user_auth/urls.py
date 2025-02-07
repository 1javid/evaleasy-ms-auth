from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('create/institution/', CreateInstitution.as_view(), name='create_institution'),
    path('institutions/', ListInstitutions.as_view(), name='list_institutions'),
    path('create/representative/', CreateRepresentative.as_view(), name='create_representative'),
    path('users/representatives/', ListRepresentatives.as_view(), name='list_representatives'),
    path('create/instructor/', CreateInstructor.as_view(), name='create_instructor'),
    path('users/instructors/', ListInstructors.as_view(), name='list_instructors'),
]