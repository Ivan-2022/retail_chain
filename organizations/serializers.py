from rest_framework import serializers

from .models import Factory, Retail, Entrepreneur, Contact, Product


class FactorySerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class RetailSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Retail
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class EntrepreneurSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Entrepreneur
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
