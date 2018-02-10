from django.db import models
from django.utils.translation import gettext_lazy as _


class DataQuerySet(models.QuerySet):
    def search(self, arguments, date, text=None, ranges=None):
        if arguments is not None:
            q_object = models.Q()
            for key, val in arguments.items():
                q_object.add(models.Q(**{key: val}), models.Q.OR)
        else:
            q_object = models.Q(title__icontains=text)
        if date is None:
            return self.filter(q_object)[ranges[0]:ranges[1]]
        else:
            return self.filter(q_object).filter(date_created__year__gte=date,
                                                date_created__year__lt=date + 1)[ranges[0]: ranges[1]]


class DataManager(models.Manager):
    def get_queryset(self):
        return DataQuerySet(self.model, using=self._db)

    def search(self, text, ranges, **kwargs):
        arguments = {}
        print(kwargs)
        if kwargs.get('author'):
            arguments['author__iexact'] = text
        if kwargs.get('text_all'):
            arguments['text__icontains'] = text
        if kwargs.get('date') != 'ALL':
            date = int(kwargs.get('date'))
        else:
            date = None

        if arguments:
            return self.get_queryset().search(arguments, date, ranges=ranges)
        else:
            return self.get_queryset().search(None, date, text=text, ranges=ranges)


class Data(models.Model):
    id = models.AutoField(_('id'), primary_key=True, auto_created=True)

    title = models.CharField(_('title'), max_length=130, db_column='title')

    author = models.CharField(_('author'), max_length=30, db_column='author')

    text = models.TextField(_('text'), max_length=10000, db_column='text')

    rating = models.IntegerField(_('rating'), db_column='rating')

    date_created = models.DateTimeField(_('date created'), db_column='date_created', auto_now_add=True)

    objects = DataManager()

    class Meta:
        db_table = 'data'



