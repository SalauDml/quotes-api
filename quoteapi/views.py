from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

quotes = []
class QuoteEndpoint(APIView):

    def get(self,request):
        return Response(quotes,status=status.HTTP_200_OK)
    
    def post(self,request):
        quote = request.data.get("quote")
        if type(quote) is not str:
            return Response({"Invalid data": "Only Type String"},status=status.HTTP_400_BAD_REQUEST)
        else:
            quotes.append(quote)
            return Response({"Valid":"Proper Data Sent"},status=status.HTTP_200_OK)



