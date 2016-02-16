
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Season(models.Model):
    """
    """
    title = models.CharField(_('title'), max_length=100)

    description = models.CharField(_('description'), max_length=300)

    order = models.PositiveIntegerField(_('order'), default=0)

    class Meta:
        verbose_name = _('season')
        verbose_name_plural = _('seasons')
        ordering = ['order']

    def __str__(self):
        return self.title
