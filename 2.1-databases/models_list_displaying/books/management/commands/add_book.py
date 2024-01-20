from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Введите название')
        parser.add_argument('author', type=str, help='Введите автора')
        parser.add_argument('pub_date', type=str, help='Дата публикации')

    def handle(self, *args, **options):
        Book(
            name=options['name'],
            author=options['author'],
            pub_date=options['pub_date'],
        ).save()
        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены'))

