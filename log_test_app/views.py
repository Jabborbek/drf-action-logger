from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SampleLogAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "GET request successful"})

    def post(self, request):
        return Response({
            "message": "POST request successful",
            "data": request.data
        })

    def put(self, request):
        return Response({"message": "PUT request successful"})

    def delete(self, request):
        return Response({"message": "DELETE request successful"})
