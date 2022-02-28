#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class CuestionarioEdimburgo(models.Model):

#Campos de selección para cada pregunta, se agrega en cada campo del modelo o tabla.
    choice_pregunta1 = {
                        (0, 'Tanto como siempre'),
                        (1, 'No tanto ahora'),
                        (2, 'Mucho menos ahora'),
                        (3, 'No, Nada')}

    choice_pregunta2 = {
                        (0, 'Tanto como siempre'),
                        (1, 'Meno que antes'),
                        (2, 'Mucho menos que antes'),
                        (3, 'Casi nada')}

    choice_pregunta3 = {
                        (0, 'Sí, la mayoría de las veces'),
                        (1, 'Sí, algunas veces'),
                        (2, 'No muy a menudo'),
                        (3, 'No, nunca')}

    choice_pregunta4 = {
                        (0, 'No, para nada'),
                        (1, 'Casi nada'),
                        (2, 'Sí, a veces'),
                        (3, 'Sí, a menudo')}

    choice_pregunta5 = {
                        (0, 'Sí, bastante'),
                        (1, 'Sí, a veces'),
                        (2, 'No, no mucho'),
                        (3, 'No, nada')}

    choice_pregunta6 = {
                        (0, 'Sí, la mayor parte de las veces'),
                        (1, 'Sí, a veces'),
                        (2, 'No, casi nunca'),
                        (3, 'No, nada')}

    choice_pregunta7 = {
                        (0, 'Sí, la mayoría de las veces'),
                        (1, 'Sí, a veces'),
                        (2, 'No muy a menudo'),
                        (3, 'No, nada')}

    choice_pregunta8 = {
                        (0, 'Sí, casi siempre'),
                        (1, 'Sí, bastante a menudo'),
                        (2, 'No muy a menudo'),
                        (3, 'No, nada')}

    choice_pregunta9 = {
                        (0, 'Sí, casi siempre'),
                        (1, 'Sí, bastante a menudo'),
                        (2, 'Sólo en ocasiones'),
                        (3, 'No, nunca')}

    choice_pregunta10 = {
                         (0, 'Sí, bastante a menudo'),
                         (1, 'A veces'),
                         (2, 'Casi nunca'),
                         (3, 'No, nunca')}
    choice_Estado_actual= {
             ('Embarazo', 'Embarazo'),
            ('Posparto', 'Posparto'),
    }

#Creación de campos para el modelo (tablas de BD)

    pregunta1 = models.IntegerField(
        "1. He sido capaz de reír y ver el lado bueno de las cosas",
        choices=choice_pregunta1,
        default='',
        blank=True,
        null=True)
    pregunta2 = models.IntegerField(
        "2. He mirado el futuro con placer",
        choices=choice_pregunta2,
        default='',
        blank=True,
        null=True)
    pregunta3 = models.IntegerField(
        "3. Me he culpado sin necesidad cuando las cosas no salían bien",
        choices=choice_pregunta3,
        default='',
        blank=True,
        null=True)
    pregunta4 = models.IntegerField(
        "4. He estado ansiosa y preocupada sin motivo",
        choices=choice_pregunta4,
        default='',
        blank=True,
        null=True)
    pregunta5 = models.IntegerField(
        "5. He sentido miedo y pánico sin motivo alguno",
        choices=choice_pregunta5,
        default='',
        blank=True,
        null=True)
    pregunta6 = models.IntegerField(
        "6. Las cosas me oprimen o agobian",
        choices=choice_pregunta6,
        default='',
        blank=True,
        null=True)
    pregunta7 = models.IntegerField(
        "7. Me he sentido tan infeliz que he tenido dificultad para dormir",
        choices=choice_pregunta7,
        default='',
        blank=True,
        null=True)
    pregunta8 = models.IntegerField(
        "8. Me he sentido triste y desgraciada",
        choices=choice_pregunta8,
        default='',
        blank=True,
        null=True)
    pregunta9 = models.IntegerField(
        "9. He sido tan infeliz que he estado llorando",
        choices=choice_pregunta9,
        default='',
        blank=True,
        null=True)
    pregunta10 = models.IntegerField(
        "10. He pensado en hacerme daño a mí misma",
        choices=choice_pregunta10,
        default='',
        blank=True,
        null=True)
    estadoActual = models.CharField(
        "¿Está embarazada o hace poco tuvo un bebé?",
        choices=choice_Estado_actual,
        default='',
        max_length=50,
        blank=True,
        null=True)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.name


class resultdoEdimburgo(models.Model):


    resultado = models.IntegerField()
    comentarios = models.CharField(max_length=500, blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name