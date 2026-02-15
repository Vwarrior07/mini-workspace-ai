from django.db import models


class Run(models.Model):
    question = models.TextField()
    answer = models.TextField()
    source_document = models.CharField(max_length=255, null=True, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Run at {self.created_at}"
