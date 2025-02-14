from rest_framework import serializers
from .models import QuestionPaper

class QuestionPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields = ['id', 'question_name', 'question_number', 'subject']