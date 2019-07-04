from rest_framework import serializers
from .models import Saledata
from django.contrib.auth.models import User 

class SaledataSerializer(serializers.ModelSerializer):
	reseller = serializers.ReadOnlyField(source='reseller.username')
	class Meta:
		model = Saledata
		fields = ('id','lnochar', 'lnoint','reseller', 'cname', 'cadress', 'ccontact', )


class UserSerializer(serializers.ModelSerializer):
	
	saledatas = serializers.PrimaryKeyRelatedField(many=True,queryset=Saledata.objects.all())
	class Meta:
		model = User
		fields = ('id','username','saledatas')