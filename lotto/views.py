from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.response import Response 
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Saledata
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import SaledataSerializer
from .pagination import CustomPagination

class get_delete_update_sale(RetrieveUpdateDestroyAPIView):
	serializer_class = SaledataSerializer
	permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

	def get_queryset(self,pk):
		try:
			saledata = Saledata.objects.get(pk=pk)
		except Saledata.DoesNotExit:
			content = {
			'status':'Not Found'
			}
			return Response(content,status=status.HTTP_404_NOT_FOUND)
		return saledata

	
	def get(self,request,pk):

		saledata = self.get_queryset(pk)
		serializer = SaledataSerializer(saledata)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,pk):
		saledata = self.get_queryset(pk)
		if(request.user==saledata.reseller):
			serializer = SaledataSerializer(saledata,data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data,status=status.HTTP_201_CREATED)
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		else:
			content={
			'status':'UNAUTHORIZED'
			}
			return Response(content,status=status.HTTP_401_UNAUTHORIZED)

	def delete(self,request,pk):
		saledata = self.get_queryset(pk)
		if(request.user == saledata.reseller):
			saledata.delete()
			content={
			'status':'NO CONTENT'
			}
			return Response(content,status=status.HTTP_204_NO_CONTENT)
		else:
			content ={
			'status':'UNAUTHORIZED'
			}
			return Response(content,status=status.HTTP_401_UNAUTHORIZED)




class get_post_sale(ListCreateAPIView):
	serializer_class = SaledataSerializer
	permission_classes = (IsAuthenticated,)
	pagination_class = CustomPagination
	def get_queryset(self):

		saledatas = Saledata.objects.filter(reseller=self.request.user)
		return saledatas

	def get(self,request):
		saledatas = self.get_queryset()
		paginate_queryset = self.paginate_queryset(saledatas)
		serializer = self.serializer_class(paginate_queryset,many=True)
		return self.get_paginated_response(serializer.data)
	def post(self,request):
		serializer = SaledataSerializer(data=request.data)
		if  serializer.is_valid():
			serializer.save(reseller=request.user)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
			Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
