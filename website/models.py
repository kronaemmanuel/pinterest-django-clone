from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile object associated with a User when the User's save signal is received
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Pin(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='images/')
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    saved_by = models.ManyToManyField(Profile, related_name='saved')
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(Profile, related_name='liked')

    def __str__(self):
        return self.title

    def has_user_saved_pin(self, user):
        profile = Profile.objects.get(user=user)
        user_count = Pin.objects.filter(id=self.id, saved_by=profile).count()
        if user_count == 1:
            return True
        return False

    def has_user_liked_pin(self, user):
        profile = Profile.objects.get(user=user)
        user_count = Pin.objects.filter(id=self.id, liked_by=profile).count()
        if user_count == 1:
            return True
        return False

