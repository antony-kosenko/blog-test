from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from accounts.models import CustomUser


class Comment(MPTTModel):
    """ The base model represents comment object in db. """

    user = models.ForeignKey(CustomUser, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
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

    RATE_OPTIONS = (
        ("L", "Like"),
        ("D", "Dislike")
    )

    comment = models.ForeignKey(Comment, related_name="rates", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="rates", null=True, on_delete=models.SET_NULL)
    rating = models.CharField(max_length=1, choices=RATE_OPTIONS)

    class Meta:
        unique_together = ('comment', 'user')

    def __str__(self):
        return f"{self.comment} {self.rating}d by {self.user}"
