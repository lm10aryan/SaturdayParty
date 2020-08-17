from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView

import json

from django.shortcuts import render
from django.http import JsonResponse
import json
from django.db.models import Q
from rest_framework import status
from rest_framework import generics


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import farmer,fields_info,products_info,CropNames,QuestionSheet
from .serializer import FarmerSerializer,FarmerIdSerializer,FieldSerializer,FieldIdSerializer,ProductsInfoSerializer,CropNamesSerializer,UserCreateSerializer,QuestionSheetSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserCreateSerializer
    authentication_classes=(TokenAuthentication,)

class UserList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserCreateSerializer




@api_view(['GET'])
def trial(request):
    return Response(data=request.user.id,status=status.HTTP_200_OK)

# Create your views here.
@api_view(['POST'])
def feedFarmerInfo(request):
    """ POST personal info of A farmer"""
    user=request.user.id
    serializer=FarmerSerializer(data=request.data)
    info = request.data.get("farmer_id")
    lol=int(info)
    if user != lol:
        return Response({'response':"You are not authorised to do that"})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'response':"Good job!"})


@api_view(['GET'])
def listAllFarmer(request):
    """GET personal info of ALL FARMERS """
    obj=farmer.objects.all()
    serializer=FarmerSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listOneFarmer(request,pk):
    """get info of particular farmer """
    user=request.user.id
    primarykey=int(pk)
    obj=farmer.objects.get(farmer_id=pk)
    serializer=FarmerSerializer(obj,many=False)
    if user != primarykey:
        return Response({'response':"You dont have permission to see buddy :)"})
    return Response(serializer.data)


@api_view(['GET'])
def listIdFarmer(request,pk):
    """get ONLY FARMER ID  of particular farmer """
    user=request.user.id
    primarykey=int(pk)
    obj=farmer.objects.get(farmer_id=pk)
    serializer=FarmerIdSerializer(obj,many=False)
    if user != primarykey:
        return Response({'response':"You dont have permission to see buddy :)"})
    return Response(serializer.data)





"""VIEWS FOR FIELD DETAILS """




@api_view(['POST'])
def listAddField(request):
    """Add field for PARTICULAR  farmer"""
    user=request.user.id
    serializer=FieldSerializer(data=request.data)
    info = request.data.get("farmer")
    lol=int(info)
    if user != lol:
        return Response({'response':"You are not authorised to do that"})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listFieldFarmer(request,pk):
    """Get field adress of PARTICULAR  farmer"""
    user=request.user.id
    primarykey=int(pk)
    obj=fields_info.objects.get(farmer=pk)
    if user != primarykey:
        return Response({'response':"You dont have permission to see buddy :)"})
    serializer=FieldIdSerializer(obj,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def listFieldsFarmer(request):
    """Get field adress of ALL the FARMERS"""
    obj=fields_info.objects.all()
    serializer=FieldSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listIdFieldFarmer(request,pk):
    """get ONLY FARMER ID  of particular farmer """
    user=request.user.id
    primarykey=int(pk)
    obj=fields_info.objects.get(farmer=pk)
    serializer=FarmerIdSerializer(obj,many=False)
    if user != primarykey:
        return Response({'response':"You dont have permission to see buddy :)"})
    return Response(serializer.data)



"""ADD PRODUCT DETAILS OF THE FIELD OF THE FARMER"""




@api_view(['POST'])
def listAddProduct(request):
    """Add crop of the farmer linked with the field """
    serializer=ProductsInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listAllProduct(request):
    """get product of all farmers """
    obj=products_info.objects.all()
    serializer=ProductsInfoSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listProductFarmer(request,pk):
    """get product of SPECIFIC  farmers """
    obj=products_info.objects.get(field=pk)
    serializer=ProductsInfoSerializer(obj,many=False)
    return Response(serializer.data)



""""VIEWS BASED ON CROP FUNCTIONS"""


@api_view(['GET'])
def listCrop(request,pk):
    """Get SPECIFIC CROP """
    obj=CropNames.objects.get(crop_id=pk)
    serializer=CropNamesSerializer(obj,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def listAllCropName(request):
    """get product of all farmers """
    obj=CropNames.objects.all()
    serializer=CropNamesSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def listCropName(request):
    """Add crop of the farmer linked with the field """
    serializer=CropNamesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





"""VIEWS BASED ON QUESTIONS SHEET"""
@api_view(['GET'])
def listquestionsheet(request):
    """get all questions """
    obj=QuestionSheet.objects.all()
    serializer=QuestionSheetSerializer(obj,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def listaddquestion(request):
    serializer=QuestionSheetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def listquestionsheetwise(request):
    """get all questions """
    obj=QuestionSheet.objects.filter(id__gt=1)
    serializer=QuestionSheetSerializer(obj,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listpastcondition(request):
    """get all questions """
    obj=QuestionSheet.objects.get(id__exact=2)
    lala=obj.past_condition
    return Response({'response':lala})
