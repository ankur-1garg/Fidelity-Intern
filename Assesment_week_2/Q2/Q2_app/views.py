from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import QuestionPaper
from .serializers import QuestionPaperSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class QuestionPaperViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing question papers
    """
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer
    # Removed permission_classes to allow unauthenticated access

    @swagger_auto_schema(
        operation_description="List all question papers",
        responses={200: QuestionPaperSerializer(many=True)}
    )
    def list(self, request):
        return super().list(request)

    @swagger_auto_schema(
        operation_description="Create a new question paper",
        request_body=QuestionPaperSerializer,
        responses={201: QuestionPaperSerializer()}
    )
    def create(self, request):
        return super().create(request)

    @swagger_auto_schema(
        operation_description="Retrieve a specific question paper",
        responses={
            200: QuestionPaperSerializer(),
            404: "Question paper not found"
        }
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

    @swagger_auto_schema(
        operation_description="Update a question paper",
        request_body=QuestionPaperSerializer,
        responses={
            200: QuestionPaperSerializer(),
            404: "Question paper not found"
        }
    )
    def update(self, request, pk=None):
        return super().update(request, pk=pk)

    @swagger_auto_schema(
        operation_description="Partially update a question paper",
        request_body=QuestionPaperSerializer(partial=True),
        responses={
            200: QuestionPaperSerializer(),
            404: "Question paper not found"
        }
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @swagger_auto_schema(
        operation_description="Delete a question paper",
        responses={
            204: "Question paper deleted successfully",
            404: "Question paper not found"
        }
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)
