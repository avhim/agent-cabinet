from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Agency
from .serializers import AgencyDetailSerializer



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def agency_detail(request):
    agent = Agency.objects.get(user__name = request.get.user.name)