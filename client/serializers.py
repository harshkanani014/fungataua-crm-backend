from rest_framework import serializers
from .models import Status, Services, SubCategory, Category, Client, Client_images, client_service_records

# Serializer to create and update status
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'status',) 
        extra_kwargs = {
            'id': {'read_only': True}
        }
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# Serializer to create and update services
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'service_name', 'is_enabled')
        extra_kwargs = {
            'id': {'read_only': True}
        }
    

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# Serializer to create and update subcategory
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'subcategory_name', 'is_enabled')
        extra_kwargs = {
            'id': {'read_only': True}
        }
    

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# Serializer to create and update category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'is_enabled', 'subcategory')
        extra_kwargs = {
            'id': {'read_only': True}
        }
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# # Serializer to create and update Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# Serializer to create and update Client Image
class ClientImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_images
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'date_of_add':{'read_only': True}
        }
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# Serializer to create and update Client Service Records
class client_service_records_serializer(serializers.ModelSerializer):
    class Meta:
        model = client_service_records
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'date_of_visit': {'read_only':True}
        }
      
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance