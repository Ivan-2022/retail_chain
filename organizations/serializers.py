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


class FactoryCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    product = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='title',
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop("product")
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        factory = Factory.objects.create(**validated_data)

        for product in self._products:
            obj, _ = Product.objects.get_or_create(title=product)
            factory.product.add(obj)

        factory.save()
        return factory

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class FactoryUpdateSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='title'
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop("product")
        super().is_valid(raise_exception=raise_exception)

    def save(self):
        factory = super().save()

        for product in self._products:
            obj, _ = Product.objects.get_or_create(title=product)
            factory.product.add(obj)

        factory.save()
        return factory

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class FactoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ["id"]


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


class RetailCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    product = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='title',
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop("product")
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        retail = Retail.objects.create(**validated_data)

        for product in self._products:
            obj, _ = Product.objects.get_or_create(title=product)
            retail.product.add(obj)

        retail.save()
        return retail

    class Meta:
        model = Retail
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class RetailUpdateSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='title'
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop("product")
        super().is_valid(raise_exception=raise_exception)

    def save(self):
        retail = super().save()

        for product in self._products:
            obj, _ = Product.objects.get_or_create(title=product)
            retail.product.add(obj)

        retail.save()
        return retail

    class Meta:
        model = Retail
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class RetailDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = ["id"]


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


class EntrepreneurCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    product = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='title',
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop("product")
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        entrepreneur = Entrepreneur.objects.create(**validated_data)

        for product in self._products:
            obj, _ = Product.objects.get_or_create(title=product)
            entrepreneur.product.add(obj)

        entrepreneur.save()
        return entrepreneur

    class Meta:
        model = Entrepreneur
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class EntrepreneurUpdateSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Product.objects.all(),
        slug_field='title'
    )

    def is_valid(self, raise_exception=False):
        self._products = self.initial_data.pop("product")
        super().is_valid(raise_exception=raise_exception)

    def save(self):
        entrepreneur = super().save()

        for product in self._products:
            obj, _ = Product.objects.get_or_create(title=product)
            entrepreneur.product.add(obj)

        entrepreneur.save()
        return entrepreneur

    class Meta:
        model = Entrepreneur
        fields = '__all__'
        read_only_fields = ("id", "created", "debt")


class EntrepreneurDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
