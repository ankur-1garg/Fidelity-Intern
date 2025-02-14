from django.db import models


class QuestionPaper(models.Model):
    question_name = models.CharField(max_length=255)
    question_number = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject} - Q{self.question_number}: {self.question_name}"

    class Meta:
        ordering = ['question_number']
