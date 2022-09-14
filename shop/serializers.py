from rest_framework import serializers

class GoodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    purchase_name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()
    create_time = serializers.DateTimeField()
    good = serializers.StringRelatedField()