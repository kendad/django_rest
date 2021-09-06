from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiView=[
            "uses a HTTP method as fucntinos",
            'Is similar to traditional Django Views',
            'gives you the most control over your api',
            'is mapped manually to URLS'
        ]

        return Response({'messgae':'Hello!','an_apiView':an_apiView})
