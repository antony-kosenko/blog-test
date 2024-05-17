from django.db.models import Model

from accounts.models import CustomUser
from comments.models import Rate


class RateService:
    """ Represents bundle of Rate model services. """

    # rate allowed values
    ALLOWED_ACTIONS = ("like", "dislike")

    @classmethod
    def set_rate(cls, instance: Model, user: CustomUser, action: str) -> Rate:
        """ Rates up valid instance. """
        if not action or action.lower() not in cls.ALLOWED_ACTIONS:
            raise ValueError(
                "Not valid 'action' provided. "
                "Valid actions: ['like', 'dislike']."
            )
        else:
            rate = Rate.objects.create(
                user=user,
                comment=instance,
                rating=action.upper()[0]
            )
            return rate
