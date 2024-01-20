import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone
from main.settings import CSV_FILE



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(CSV_FILE, 'r') as file:
            phones = csv.DictReader(file, delimiter=';')
            for phone in phones:
                Phone(**phone, slug = slugify(phone.get('name', ''))).save()
        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены'))
