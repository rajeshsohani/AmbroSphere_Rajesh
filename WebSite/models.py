from django.db import models

# Create your models here.
from django.db import models

class SubjectModel(models.Model):
    name = models.CharField(max_length=255)  # Name of the subject
    description = models.TextField(blank=True, null=True)  # Optional description
    url = models.URLField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

class TopicModel(models.Model):
    subject = models.ForeignKey(SubjectModel, related_name='topics', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name of the topic
    description = models.TextField(blank=True, null=True)  # Optional description
    url = models.URLField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

class SubtopicModel(models.Model):
    topic = models.ForeignKey(TopicModel, related_name='subtopics', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name of the subtopic
    content = models.TextField(blank=True, null=True)  # Optional content for the subtopic
    url = models.URLField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f"{self.name} ({self.topic.name})"
