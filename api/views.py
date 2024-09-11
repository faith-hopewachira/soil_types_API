from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from soil_types.models import SoilType
from .serializers import SoilTypeSerializer

class SoilTypeListCreateView(APIView):
    """
    This view handles HTTP GET, POST, and DELETE requests for the SoilType model.
    
    - GET request: Retrieves a list of all SoilType objects.
    - POST request: Creates a new SoilType object based on the data provided.
    - DELETE request: Deletes an existing SoilType object based on the ID provided.
    """

    def get(self, request):
        """
        Retrieves a list of all SoilType objects.
        """
        soil_types = SoilType.objects.all()
        serializer = SoilTypeSerializer(soil_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Creates a new SoilType object based on the data provided.
        """
        serializer = SoilTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Deletes a SoilType object based on the ID provided in the URL.
        """
        if pk is None:
            return Response({"error": "ID parameter is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        
        soil_type = get_object_or_404(SoilType, pk=pk)
        soil_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoilTypeDetailView(APIView):
    """
    This view handles HTTP GET, PUT, PATCH, and DELETE requests for a specific SoilType object by ID.
    
    - GET request: Retrieves a SoilType object by its ID.
    - PUT request: Updates a SoilType object based on the ID and provided data.
    - PATCH request: Partially updates a SoilType object based on the ID and provided data.
    - DELETE request: Deletes a SoilType object based on the ID.
    """

    def get(self, request, pk):
        """
        Retrieves a SoilType object by its ID.
        """
        soil_type = get_object_or_404(SoilType, pk=pk)
        serializer = SoilTypeSerializer(soil_type)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Updates a SoilType object based on the ID and provided data.
        """
        soil_type = get_object_or_404(SoilType, pk=pk)
        serializer = SoilTypeSerializer(soil_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Partially updates a SoilType object based on the ID and provided data.
        """
        soil_type = get_object_or_404(SoilType, pk=pk)
        serializer = SoilTypeSerializer(soil_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes a SoilType object based on the ID.
        """
        soil_type = get_object_or_404(SoilType, pk=pk)
        soil_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
