import random
import string
import datetime


years = [i for i in range(2007, 2018)]
months = [i for i in range(1, 13)]
days = [i for i in range(1, 26)]
hours = [i for i in range(0, 24)]
minutes = [i for i in range(0, 60)]


def gen_date():
    return datetime.datetime(random.choice(years), random.choice(months), random.choice(days),
                             random.choice(hours), random.choice(minutes))


with open('name.data', 'r', encoding='utf8') as ff:
    a = list([s.replace('\n', '') for s in ff.readlines()])

with open('mysql2.data', 'r+', encoding='utf8') as f:
    f.truncate()

    for i in range(70):
        title = 'title ' + 'a' * random.randint(0, 90) + ' what a joke'
        author = random.choice(a)
        text = ''.join([random.choice(string.ascii_letters + '    ') for i in range(random.randint(100, 6000))])
        rating = random.randint(-50, 45)
        date = gen_date()
        f.write(title + str(i) + '~~' + author + '~~' + text + '~~' + str(rating) + '~~' + str(date) + '\n')





