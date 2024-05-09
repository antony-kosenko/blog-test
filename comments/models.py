from django.db import models

from accounts.models import CustomUser


class Comment(models.Model):
    """ The base model represents comment object in db. """

    user = models.ForeignKey(CustomUser, related_name="comments", on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children",
        on_delete=models.SET_NULL
    )
    date_created = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True,
        blank=True,
        null=True
    )
    text = models.TextField(max_length=500)

    class Meta:
        ordering = ("-date_created",)
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment[{self.id}] | {self.text[0:40]}"

    def get_rating(self) -> int:
        """ Returns comment's rating """
        likes: int = self.rates.filter(rating='L').count()
        dislikes: int = self.rates.filter(rating='D').count()
        return likes - dislikes


class Rate(models.Model):
    """ Comment rating model."""

    RATE_OPTIONS = {
        "L": "Like",
        "D": "Dislike"
    }

    comment = models.ForeignKey(Comment, related_name="rates", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="rates", null=True, on_delete=models.SET_NULL)
    rating = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.user} {self.RATE_OPTIONS.get(self.rating)} Comment[{self.id}]"
