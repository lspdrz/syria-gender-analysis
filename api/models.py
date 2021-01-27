from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FacebookPost(Base):
    page_name = models.CharField(max_length=128)
    post_id = models.CharField(max_length=128)
    text = models.TextField()
    shared_text = models.TextField()
    time = models.DateTimeField()
    image = models.TextField()
    video = models.TextField()
    num_reacts = models.IntegerField()
    like_react = models.IntegerField()
    sorry_react = models.IntegerField()
    anger_react = models.IntegerField()
    love_react = models.IntegerField()
    wow_react = models.IntegerField()
    support_react = models.IntegerField()
    haha_react = models.IntegerField()
    comments = models.IntegerField()
    shares = models.IntegerField()
    post_url = models.CharField(max_length=255)
