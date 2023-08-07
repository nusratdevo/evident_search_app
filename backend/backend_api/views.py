
# Create your views here.
import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes



from .models import CustomUser, SortedInput
from .serializers import UserLoginSerializer , UserRegistrationSerializer,ProfileSerializer, SortedInputSerializer, SortedSerializer

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class UserRegistrationView(APIView):
  def post(self, request, *args, **kwargs):
    data = {
            'name': request.data.get('name'), 
            'username': request.data.get('username'), 
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            "image":  request.FILES.get('image')
        }
    serializer = UserRegistrationSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
  
  def post(self, request, *args, **kwargs):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success', 
                       }, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_401_UNAUTHORIZED)
    

class UserProfileView(APIView):
     permission_classes = [IsAuthenticated]
     def get(self, request, *args, **kwargs):
        
        userdata = CustomUser.objects.filter(pk = request.user.id)
        #todos = Todo.objects.all()
        if userdata:
             serializer = ProfileSerializer(userdata,many=True)
             payload = serializer.data
             response_data = {
                'status': 'success',
                'user_id': request.user.id,
                'payload': payload
        }
             return Response(serializer.data, status=status.HTTP_200_OK)
        


class SortedInputView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [IsAuthenticated]
    # 2. Create
    def post(self, request, *args, **kwargs):
        
         input_values = request.data.get('inputValue')
         search_value = request.data.get('searchValue')
         if not (search_value and input_values):
                return Response(
                         {
                            'meg': 'search_value and input_values are required.'
                         }, 
                        status=status.HTTP_400_BAD_REQUEST)
          # Sorting the input values in descending order
        
         sorted_values = sorted(map(int, input_values.split(',')), reverse=True)
        #  int_search_value = int(request.data.get('search_value'))

         # Storing the sorted input values along with the user ID and timestamp
        #  sorted_string= (' ').join(sorted_values)
         sorted_string = ' '.join([str(elem) for elem in sorted_values])

         input_data=SortedInput.objects.create(user=request.user, input_values=sorted_string, search_value=search_value)

         
         # Check if the search value is in the sorted input values
         is_found = str(search_value) in sorted_string

         return Response({'result': is_found,
                     'status': 'success',
                     'user_id': request.user.id,
                     'payload': SortedInputSerializer(input_data).data
					 },status=status.HTTP_201_CREATED)

class AllInputView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        khujobj = SortedInput.objects.filter(user = request.user.id)
        print('data',khujobj )
        if khujobj:
            serializer = SortedSerializer(khujobj, many=True)
            # wanted_fields = {'input_values', 'timestamp'}
            # all_fields = set(serializer.fields)
            # for field in all_fields:
            #     if field not in wanted_fields:
            #         serializer.fields.pop(field)
            payload = serializer.data
            response_data = {
            'payload': payload,
            'status': 'success',
            'user_id': request.user.id,
        }
            #return Response(response_data)
            return Response(response_data,status=status.HTTP_200_OK)
        