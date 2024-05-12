from rest_framework import serializers
from .models import Tour, TourDayQuota, TourDescriptionDay


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = (
            'title',
            'slug',
            'img_url',
            'price',
            'currency'
        )

class TourDayQuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDayQuota
        fields = ('tour_date', 'total_quotas', 'price_adult', 'price_child', )


class TourDescriptionDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDescriptionDay
        fields = ('day', 'description')


class TourDetailSerializer(serializers.ModelSerializer):
    tour_description_day = TourDescriptionDaySerializer(many=True, read_only=True)
    tour_day_quota = TourDayQuotaSerializer(many=True, read_only=True)
    country  = serializers.StringRelatedField(many=True)
    # category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tour
        fields = ('title', 'first_title', 'second_title', 'price', 'old_price', 
                  'currency', 'service_price', 'service_price_child', 'route', 'num_days', 'night_transfer',
                  'description_tour', 'included', 'not_included', 'country', 'tour_day_quota', 'tour_description_day','img_url')