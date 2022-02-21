from rest_framework import serializers
from suggestions.models import CategorySuggestion, SubCategorySuggestion



class CategorySuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySuggestion
        fields = 'name', 'state', 'user'



class SubCategorySuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategorySuggestion
        fields = 'name', 'state', 'user'
        