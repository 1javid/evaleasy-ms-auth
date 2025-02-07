from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import *
import random

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CreateInstitution(APIView):
    def post(self, request):
        serializer = InstitutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateRepresentative(APIView):
    def post(self, request):
        user_type = UserType.objects.get(id=2)  # Assuming user_type id 2 is for Representative
        data = request.data.copy()
        data['user_type'] = user_type.id
        data['user_id'] = random.randint(10000, 99999)  # Generate random user_id
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateInstructor(APIView):
    def post(self, request):
        user_type = UserType.objects.get(id=3)  # Assuming user_type id 3 is for Instructor
        data = request.data.copy()
        data['user_type'] = user_type.id
        data['user_id'] = random.randint(10000, 99999)  # Generate random user_id
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListInstructors(APIView):
    def get(self, request):
        institution_id = request.query_params.get('institution_id')
        if institution_id:
            instructors = User.objects.filter(user_type__name__iexact='instructor', institution_id=institution_id)
        else:
            instructors = User.objects.filter(user_type__name__iexact='instructor')
        serializer = UserSerializer(instructors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListInstitutions(APIView):
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListRepresentatives(APIView):
    def get(self, request):
        institution_id = request.query_params.get('institution_id')
        if institution_id:
            representatives = User.objects.filter(user_type__name__iexact='institution representative', institution_id=institution_id)
        else:
            representatives = User.objects.filter(user_type__name__iexact='institution representative')
        serializer = UserSerializer(representatives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)