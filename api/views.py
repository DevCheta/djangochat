from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Product, Image
from .serializers import ProductSerializer, ImageSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
#Imports for images 
from django.shortcuts import render, redirect
from .forms import ImageForm
#from django.http import HttpResponse



#get Image


@csrf_exempt
@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['GET'])
def product_detail(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        serializer =  ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def product_create(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT'])
def product_update(request, pk):
    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELETE'])
def product_delete(request, pk):
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=204)
        


#@csrf_exempt
#@api_view(['POST'])
#def image_create(request, pk):
   # product = Product.objects.get(pk=pk)
    #if request.method == 'POST':
      #  form = ImageForm(request.POST, request.FILES)
       # if form.is_valid():
           # image = form.save(commit=False)
         #   image.product = product
         #   image.save()
          #  return redirect('product_detail', pk=product.pk)
    #else:
       # form = ImageForm()
    #return render(request, 'products/image_form.html', {'form': form})
