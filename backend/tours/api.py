from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Tour
from .serializer import TourListSerializer, TourDetailSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def tour_list(request):
    tours = Tour.objects.filter(active=True)
    serializer = TourListSerializer(tours, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def tour_detail(request, slug):
    tour = Tour.objects.select_related().get(slug=slug)
    # tour = tour.tour_day_quota.filter(active=True)

    serializer = TourDetailSerializer(tour)

    return JsonResponse({
        'data': serializer.data
    })