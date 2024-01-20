import json
from django.core.management.base import BaseCommand
from books.models import Book
from main.settings import JSON_FILE


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(JSON_FILE, encoding='utf-8') as file:
            for data in json.load(file):
                Book(**data.get('fields')).save()

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены'))

