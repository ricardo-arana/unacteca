from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django_thumbs.db.models import ImageWithThumbsField

# Create your models here.

class Editorial(models.Model):
	class Meta:
		verbose_name = "Editorial"
		verbose_name_plural = "Editoriales"
	nombre = models.CharField(max_length=100)
	pais = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombre

class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	class Meta:
		verbose_name = "Autor"
		verbose_name_plural = "Autores"

	def __unicode__(self):
		return self.nombre

class Materia(models.Model):
	nombre = models.CharField(max_length=50)
	class Meta:
		verbose_name = "Materia"
		verbose_name_plural = "Materias"
	def __unicode__(self):
		return self.nombre
    

class Idioma(models.Model):
	nombre = models.CharField(max_length=50)
	iniciales = models.CharField(max_length=10)
	class Meta:
		verbose_name = "Idioma"
		verbose_name_plural = "Idiomas"
	def __unicode__(self):
		return self.nombre

class Etiqueta(models.Model):
	nombre = models.CharField(max_length=50)
	class Meta:
		verbose_name = "etiqueta"
		verbose_name_plural = "etiquetas"

	def __unicode__(self):
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=200)
	editorial = models.ForeignKey(Editorial)
	autor = models.ForeignKey(Autor)
	materia = models.ForeignKey(Materia)
	idioma = models.ForeignKey(Idioma)
	cantidad = models.IntegerField()
	descripcion = models.TextField()
	portada = ImageWithThumbsField(upload_to='portadas',null=True, sizes=((250,300),(125,150)))
	calificacion = models.FloatField()
	etiqueta = models.ManyToManyField(Etiqueta)
	slug = models.SlugField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Libro, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Libro"
		verbose_name_plural = "Libros"

	def __unicode__(self):
		return self.titulo

class Ejemplar(models.Model):
	codigo = models.CharField(max_length=50)
	libro = models.ForeignKey(Libro)
	edicion = models.CharField(max_length=50)
	ano = models.CharField(max_length=4)
	estado = models.CharField(max_length=1)
	ingreso = models.DateField()
	baja = models.DateField(null=True, blank=True)
	class Meta:
		verbose_name = "Ejemplar"
		verbose_name_plural = "Ejemplares"
	def __unicode__(self):
		return self.codigo

class Prestamo(models.Model):
	ejemplar = models.ForeignKey(Ejemplar)
	usuario = models.ForeignKey(User)
	fecha_prestamo = models.DateField()
	fecha_devolucion = models.DateField()
	estado = models.CharField(max_length=1)
	dias_mora = models.IntegerField(default=0)
	class Meta:
		verbose_name = "Prestamo"
		verbose_name_plural = "Prestamos"
  
	def __unicode__(self):
		return self.usuario
class Comentario(models.Model):
	titulo = models.CharField(max_length=50)
	usuario = models.ForeignKey(User)
	texto = models.TextField()
	postivos = models.IntegerField()
	negativos = models.IntegerField()
	libro = models.ForeignKey(Libro)
	fecha_publicacion = models.DateField('publicado')
	class Meta:
		verbose_name = "Comentario"
		verbose_name_plural = "Comentarios"

	def __unicode__(self):
		return self.titulo

class Mora(models.Model):
	Usuario = models.ForeignKey(User)
	dias = models.IntegerField()
	costoxdia = models.FloatField()
	estado = models.CharField(max_length=1)
	class Meta:
		verbose_name = "Mora"
		verbose_name_plural = "Moras"

	def __unicode__(self):
		return self.usuario
    
                  
    
        
    


    
    
    

    
		



