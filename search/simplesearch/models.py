from django.db import models
from django.utils.translation import gettext_lazy as _


class DataQuerySet(models.QuerySet):
    def search(self, arguments=None, text=None):
        if arguments is not None:
            q_object = models.Q()
            for key, val in arguments.items():
                q_object.add(models.Q(**{key: val}), models.Q.OR)
        else:
            q_object = models.Q(title__icontains=text)
        return self.filter(q_object)


class DataManager(models.Manager):
    def get_queryset(self):
        return DataQuerySet(self.model, using=self._db)

    def search(self, text, **kwargs):
        arguments = {}
        if kwargs.get('exact', False):
            arguments['title__exact'] = text
        if kwargs.get('text_all', False):
            arguments['text_one__icontains'] = text
            arguments['text_two__icontains'] = text

        if arguments:
            return self.get_queryset().search(arguments)
        else:
            return self.get_queryset().search(None, text)


class Data(models.Model):
    id = models.AutoField(_('id'), primary_key=True, auto_created=True)

    title = models.CharField(_('title'), max_length=130, db_column='title')

    text_one = models.TextField(_('text one'), max_length=10000, db_column='text_one')

    text_two = models.TextField(_('text two'), max_length=1000, db_column='text_two')

    date_created = models.DateTimeField(_('date created'), db_column='date_created', auto_now_add=True)

    objects = DataManager()

    class Meta:
        db_table = 'data'



