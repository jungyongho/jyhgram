from django.db import models
from nomadgram.users import models as user_models

class TimeStampModel(models.Model):
    """Timestamp Model"""
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    class Meta:
        abstract=True

class Image(TimeStampModel):
    """Image Model"""
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=True)

class Comment(TimeStampModel):
    """Comment Model"""
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=True)
    image = models.ForeignKey(Image, null=True, on_delete=True)

class Like(TimeStampModel):
    """Like Model"""
    creator = models.ForeignKey(user_models.User, null=True, on_delete=True)
    image = models.ForeignKey(Image, null=True, on_delete=True)