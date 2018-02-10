from django.db import models
from django.utils.translation import gettext_lazy as _


# queryset search
class DataQuerySet(models.QuerySet):
    # search func
    def search(self, arguments, date, text=None, ranges=None):
        # arguments is dict or None
        # arguments: { title__icontains: 'example' }
        if arguments is not None:
            # create Q object
            q_object = models.Q()
            # add argument to Q object
            # { title__icontains: 'example' } --> title_icontains='example' + OR
            for key, val in arguments.items():
                q_object.add(models.Q(**{key: val}), models.Q.OR)
        else:
            # if arguments is None, default Q object
            q_object = models.Q(title__icontains=text)
        # check date
        # if date is None, filter queryset without date ranges
        # ranges is number, how objects get from db [0:6] --> click load_more button --> [6:12]
        if date is None:
            return self.filter(q_object)[ranges[0]:ranges[1]]
        # with date ranges, gte = great and equal, lt = less
        else:
            return self.filter(q_object).filter(date_created__year__gte=date,
                                                date_created__year__lt=date + 1)[ranges[0]: ranges[1]]


# Manager Data model
class DataManager(models.Manager):
    # return queryset object
    def get_queryset(self):
        return DataQuerySet(self.model, using=self._db)

    # search func
    # set arguments and return queryset.search()
    def search(self, text, ranges, **kwargs):
        # arguments dict
        arguments = {}
        # if search only author field
        if kwargs.get('author'):
            # iexact --> 'Example' = 'Example' and 'Example' = 'example'
            arguments['author__iexact'] = text
        # if search all text, text and title fields, but not author
        if kwargs.get('text_all'):
            # icontains --> where value like '%text%'
            arguments['text__icontains'] = text
        # if search in date ranges
        # ALL = without ranges
        if kwargs.get('date') != 'ALL':
            date = int(kwargs.get('date'))
        else:
            date = None
        # call func queryset.search()
        # with arguments
        if arguments:
            return self.get_queryset().search(arguments, date, ranges=ranges)
        # without arguments
        else:
            return self.get_queryset().search(None, date, text=text, ranges=ranges)


# Data model
class Data(models.Model):
    # id field, auto_increment
    id = models.AutoField(_('id'), primary_key=True, auto_created=True)
    # title, varchar(130)
    title = models.CharField(_('title'), max_length=130, db_column='title')
    # author, varchar(30)
    author = models.CharField(_('author'), max_length=30, db_column='author')
    # text, longtext
    text = models.TextField(_('text'), max_length=10000, db_column='text')
    # rating, int(11)
    rating = models.IntegerField(_('rating'), db_column='rating')
    # datetime(6)
    date_created = models.DateTimeField(_('date created'), db_column='date_created', auto_now_add=True)
    # set manager
    objects = DataManager()

    class Meta:
        db_table = 'data'

    # __str__ func
    def __str__(self):
        return 'Data object ' + str(self.id)



