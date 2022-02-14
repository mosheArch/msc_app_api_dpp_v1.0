#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class CuestionarioEdimburgo(models.Model):

#Campos de selección para cada pregunta, se agrega en cada campo del modelo o tabla.
    choice_pregunta1 = {
                        ('Tanto como siempre', 'Tanto como siempre'),
                        ('No tanto ahora', 'No tanto ahora'),
                        ('Mucho menos', 'Mucho menos'),
                        ('No, no he podido', 'No, no he podido')}

    choice_pregunta2 = {
                        ('Tanto como siempre', 'Tanto como siempre'),
                        ('Algo menos de lo que solía hacer', 'Algo menos de lo que solía hacer'),
                        ('Definitivamente menos', 'Definitivamente menos'),
                        ('No, nada ', 'No, nada')}

    choice_pregunta3 = {
                        ('Sí, la mayoría de las veces', 'Sí, la mayoría de las veces'),
                        ('Sí, algunas veces', 'Sí, algunas veces'),
                        ('No muy a menudo', 'No muy a menudo'),
                        ('No, nunca', 'No, nunca')}

    choice_pregunta4 = {
                        ('No, para nada', 'No, para nada'),
                        ('Casi nada', 'Casi nada'),
                        ('Sí, a veces', 'Sí, a veces'),
                        ('Sí, a menudo', 'Sí, a menudo')}

    choice_pregunta5 = {
                        ('Sí, bastante', 'Sí, bastante'),
                        ('Sí, a veces', 'Sí, a veces'),
                        ('No, no mucho', 'No, no mucho'),
                        ('No, nada', 'No, nada')}

    choice_pregunta6 = {
                        ('Sí, la mayor parte de las veces', 'Sí, la mayor parte de las veces'),
                        ('Sí, a veces', 'Sí, a veces'),
                        ('No, casi nunca', 'No, casi nunca'),
                        ('No, nada', 'No, nada')}

    choice_pregunta7 = {
                        ('Sí, la mayoría de las veces', 'Sí, la mayoría de las veces'),
                        ('Sí, a veces', 'Sí, a veces'),
                        ('No muy a menudo', 'No muy a menudo'),
                        ('No, nada', 'No, nada')}

    choice_pregunta8 = {
                        ('Sí, casi siempre', 'Sí, casi siempre'),
                        ('Sí, bastante a menudo', 'Sí, bastante a menudo'),
                        ('No muy a menudo', 'No muy a menudo'),
                        ('No, nada', 'No, nada')}

    choice_pregunta9 = {
                        ('Sí, casi siempre', 'Sí, casi siempre'),
                        ('Sí, bastante a menudo', 'Sí, bastante a menudo'),
                        ('Sólo en ocasiones', 'Sólo en ocasiones'),
                        ('No, nunca', 'No, nunca')}

    choice_pregunta10 = {
                         ('Sí, bastante a menudo', 'Sí, bastante a menudo'),
                         ('A veces', 'A veces'),
                         ('Casi nunca', 'Casi nunca'),
                         ('No, nunca', 'No, nunca')}


#Creación de campos para el modelo (tablas de BD)

    pregunta1 = models.CharField(
        "1. He sido capaz de reír y ver el lado bueno de las cosas",
        choices=choice_pregunta1,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta2 = models.CharField(
        "2. He mirado el futuro con placer",
        choices=choice_pregunta2,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta3 = models.CharField(
        "3. Me he culpado sin necesidad cuando las cosas no salían bien",
        choices=choice_pregunta3,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta4 = models.CharField(
        "4. He estado ansiosa y preocupada sin motivo",
        choices=choice_pregunta4,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta5 = models.CharField(
        "5. He sentido miedo y pánico sin motivo alguno",
        choices=choice_pregunta5,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta6 = models.CharField(
        "6. Las cosas me oprimen o agobian",
        choices=choice_pregunta6,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta7 = models.CharField(
        "7. Me he sentido tan infeliz que he tenido dificultad para dormir",
        choices=choice_pregunta7,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta8 = models.CharField(
        "8. Me he sentido triste y desgraciada",
        choices=choice_pregunta8,
        default='',
        max_length=100,
        blank=True,
        null=True)
    pregunta9 = models.CharField(
        "9. He sido tan infeliz que he estado llorando",
        choices=choice_pregunta9,
        default='', max_length=100,
        blank=True, null=True)
    pregunta10 = models.CharField(
        "10. He pensado en hacerme daño a mí misma",
        choices=choice_pregunta10,
        default='',
        max_length=100,
        blank=True,
        null=True)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.name


