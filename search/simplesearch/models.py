from django.db import models
from django.utils.translation import gettext_lazy as _


class Data(models.Model):
    id = models.AutoField(_('id'), primary_key=True, auto_created=True)

    title = models.CharField(_('title'), max_length=130, db_column='title')

    text_one = models.TextField(_('text one'), max_length=10000, db_column='text_one')

    text_two = models.TextField(_('text two'), max_length=1000, db_column='text_two')

    date_created = models.DateTimeField(_('date created'), db_column='date_created', auto_now_add=True)

    class Meta:
        db_table = 'data'



