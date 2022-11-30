from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response  # note used here.
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from .serializers import UserLoginSerializer, UserRegistrationSerializer
#  return Response({'profiles': queryset})


class UserRegistrationView(APIView):
    '''
        Registering a user with Post email, name, tc and password
    '''

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.is_valid(raise_exception=True)
            serializer.save()
            # return Response({'msg': 'This user created'}, status=HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.data, status=HTTP_201_CREATED)
    # return response({'msg': 'All are Not ok here'})
    # return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.data.get(email)
            password = request.data.get(password)
            print('............. email', email)
            print('............. email', password)
            user = authenticate(email=email, password=password)
            if user is not None:
                # A backend authenticated the credentials
                return Response({'msg': 'This user is Loged in Successfully!'}, status=HTTP_200_OK)
            else:
                return Response({'msg': 'This user is Not Loged in Successfully!'}, status=HTTP_400_BAD_REQUEST)
