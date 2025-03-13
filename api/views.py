from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from restaurant.models import Menu, Booking
from .serializers import bookingSerializer,menuSerializer

from django.http import JsonResponse


""" class bookingview(APIView):
    def get(self,request):
        items = Booking_table.objects.all()
        serializer = bookingSerializer(items , many = True)
        return Response(serializer.data)

class menuview(APIView):
    def post(self, request):
        serializer = menuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
 """

class MenuViewListCreateAPIView (ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class MenuRetrieveUpdateView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

@permission_classes([IsAuthenticated])
class BookingViewSet(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

@permission_classes([IsAuthenticated])
class BookingRetrieveUpdateView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer


