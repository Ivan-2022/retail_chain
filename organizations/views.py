from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated

from organizations.models import Retail, Factory, Entrepreneur, Contact, Product
from organizations.serializers import FactorySerializer, RetailSerializer, EntrepreneurSerializer, ContactSerializer, \
    ProductSerializer


class FactoryCreateView(CreateAPIView):
    model = Factory
    permission_classes = [IsAuthenticated]
    serializer_class = FactorySerializer


class FactoryView(RetrieveUpdateDestroyAPIView):
    model = Factory
    permission_classes = [IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryListView(ListAPIView):
    model = Factory
    permission_classes = [IsAuthenticated]
    serializer_class = FactorySerializer

    def get_queryset(self):
        queryset = Factory.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contact__country__contains=country)
        return queryset


class RetailCreateView(CreateAPIView):
    model = Retail
    permission_classes = [IsAuthenticated]
    serializer_class = RetailSerializer


class RetailListView(ListAPIView):
    model = Retail
    permission_classes = [IsAuthenticated]
    serializer_class = RetailSerializer

    def get_queryset(self):
        queryset = Retail.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contact__country__contains=country)
        return queryset


class RetailView(RetrieveUpdateDestroyAPIView):
    model = Retail
    permission_classes = [IsAuthenticated]
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()


class EntrepreneurCreateView(CreateAPIView):
    model = Entrepreneur
    permission_classes = [IsAuthenticated]
    serializer_class = EntrepreneurSerializer


class EntrepreneurListView(ListAPIView):
    model = Entrepreneur
    permission_classes = [IsAuthenticated]
    serializer_class = EntrepreneurSerializer

    def get_queryset(self):
        queryset = Entrepreneur.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contact__country__contains=country)
        return queryset


class EntrepreneurView(RetrieveUpdateDestroyAPIView):
    model = Entrepreneur
    permission_classes = [IsAuthenticated]
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()


class ContactCreateView(CreateAPIView):
    model = Contact
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer


class ContactListView(ListAPIView):
    model = Contact
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactView(RetrieveUpdateDestroyAPIView):
    model = Contact
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ProductCreateView(CreateAPIView):
    model = Product
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    model = Product
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductView(RetrieveUpdateDestroyAPIView):
    model = Product
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
