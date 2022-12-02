from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ads.models import Ads
from ads.permissions import IsOwnerAdOrStaff
from ads.serializers.ad import AdsListSerializer, AdsDetailSeraializer, AdsCreateSerializer, AdsUpdateSerializer, \
    AdsDeleteSerializer


class AdsListView(ListAPIView):
    """Возвращает все объявления"""
    queryset = Ads.objects.all().order_by("-price")
    serializer_class = AdsListSerializer

    def get(self, request, *args, **kwargs):
        """Использование фильтров"""
        category_id = request.GET.getlist("category_id")
        text = request.GET.get("text")
        location = request.GET.get("location")
        price_from = request.GET.get("price_from")
        price_to = request.GET.get("price_to")

        # Возвращает все объявления в переданных ему категориях
        if category_id:
            self.queryset = self.queryset.filter(category_id__in=category_id)
        # Поиск по вхождению слова в название
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)
        # Возвращает все объявления только релевантные нам по месту
        if location:
            self.queryset = self.queryset.filter(author_id__location_id__name__icontains=location)
        # Возвращает все объявления в диапазоне цен
        if price_from and price_to:
            self.queryset = self.queryset.filter(price__range=(price_from, price_to))

        return super().get(self, request, *args, **kwargs)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ad_by_id(request, pk):
    """Возвращает объявление по id"""
    try:
        ad = Ads.objects.get(pk=pk)
    except Ads.DoesNotExist:
        return JsonResponse({"error": "Объявление не найдено"}, status=404)
    return JsonResponse(AdsDetailSeraializer(ad).data)


class AdsCreateView(CreateAPIView):
    """Создает объявление"""
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer


class AdsUpdateView(UpdateAPIView):
    """Обновляет объявление"""
    queryset = Ads.objects.all()
    serializer_class = AdsUpdateSerializer
    permission_classes = [IsOwnerAdOrStaff]


class AdsDeleteView(DestroyAPIView):
    """Удаляет объявление"""
    queryset = Ads.objects.all()
    serializer_class = AdsDeleteSerializer
    permission_classes = [IsOwnerAdOrStaff]


@method_decorator(csrf_exempt, name="dispatch")
class AdsUploadImage(UpdateView):
    """Загружает картинку для объявления"""
    model = Ads
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object = self.get_object()
        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author_id.username,
            "category": self.object.category_id.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None
        }, json_dumps_params={"ensure_ascii": False})
