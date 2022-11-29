from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    description = models.TextField(verbose_name="Description",null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.titulo + ' - ' + self.description

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()