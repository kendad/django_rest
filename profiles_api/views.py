from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiView=[
            "uses a HTTP method as fucntinos",
            'Is similar to traditional Django Views',
            'gives you the most control over your api',
            'is mapped manually to URLS'
        ]

        return Response({'messgae':'Hello!','an_apiView':an_apiView})

    def post(self,request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name} !!!'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self,request,pk=None):
        """Handles updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handels a partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """Deletes an object"""
        return Response({"method":'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Returns a hello message"""
        a_viewset=[
            'Uses action(list,create,retrieve,update,partial_update,destroy)',
            'automaticallly maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!!','a_viewset':a_viewset})
    
    def create(self,request):
        """Creates a hello Message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self,request,pk=None):
        """Handle gettin an object by it ID"""
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        """Handel updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """Handle updating part of the object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handels creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    #adds a filter to a viewset for searching the database
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')

class UserLoginApiView(ObtainAuthToken):
    """Handel creating user auth tokens"""
    #this line of code to render the login on the browser
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
