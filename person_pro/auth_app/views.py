from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


@api_view(http_method_names=['POST',])
def create_user(request):
    try:
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error saving user'}, status=status.HTTP_400_BAD_REQUEST)