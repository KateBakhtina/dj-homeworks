from datetime import datetime, date


class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = '%Y-%m-%d'

   def to_python(self, value: str) -> date:
       full_date = datetime.strptime(value, self.format)
       return date(full_date.year, full_date.month, full_date.day)

   def to_url(self, value: date) -> str:
       return value.strftime(self.format)
