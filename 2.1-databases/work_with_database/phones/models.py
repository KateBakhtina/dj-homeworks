from django.db import models



class Phone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return (f"{self.id}: "
                f"("
                f"{self.name}, {self.image}, {self.price},"
                f"{self.release_date}, {self.lte_exists}, {self.slug}"
                f")")






