from rest_framework import serializers
from suggestions.models import CategorySuggestion, SubCategorySuggestion



class CategorySuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySuggestion
        fields = '__all__'




class SubCategorySuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategorySuggestion
        fields = '__all__'
        