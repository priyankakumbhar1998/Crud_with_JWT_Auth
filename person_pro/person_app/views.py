from .models import Person
from .serializers import PersonSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes ,permission_classes
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(http_method_names=['POST',])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_person(request):
    try:
        serializer = PersonSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        # return Response(data=serializer.errors)
        return Response(data={'detail': 'ERROR in processing request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def show_person(request):
    try:
        person = Person.objects.all()
        serializer = PersonSerializers(person, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error in Fetching data'}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(http_method_names=['GET'])
def retrieve_person(request, pk=None):
    serializer = PersonSerializers(request)
    try:
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializers(person)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error in Fetching data'}, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(http_method_names=['PUT','PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_person(request, pk=None):
    try:
        person =get_object_or_404(Person, pk=pk)
        if request.method == 'PUT':
            serializer = PersonSerializers(data=request.data, instance=person)
        if request.method == 'PATCH':
            serializer = PersonSerializers(data=request.data, instance=person, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error in updating data'}, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(http_method_names=['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_person(request, pk=None):
    try:
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response(data={'detail': 'Person deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error in deleting person'}, status=status.HTTP_400_BAD_REQUEST)
    
    

    
  


    
    
