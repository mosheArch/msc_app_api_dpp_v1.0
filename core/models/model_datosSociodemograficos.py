#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class DatosSociodemograficos(models.Model):

#Choice de datos definidos
    choice_estadoCivil = {('', 'Estado civil'),
                          (1, 'Casada'),
                          (2, 'Union libre'),
                          (3, 'Soltera'),
                          (4, 'Viuda')}

    choice_escolaridad = {('', 'Escolaridad'),
                          (1, 'Primaria'),
                          (2, 'Secundaria'),
                          (3, 'Bachillerato'),
                          (4, 'Licenciatura'),
                          (5, 'Posgrado')}

    choice_ocupacion = {('', 'Ocupacion'),
                        (1, 'Ama de casa'),
                        (2, 'Empleada'),
                        (3, 'Estadiante'),
                        (4, 'Desempleada')}

    choice_statusEconomico = {('', 'Status economico'),
                              (1, 'Baja baja'),
                              (2, 'Baja alta'),
                              (3, 'Media baja'),
                              (4, 'Media alta')}

    choice_embarazoDeseado = {('', 'Embarazo deseado'),
                              (1, 'Si'),
                              (2, 'No')}

    choice_embarazoPlaneado = {('', 'Embarazo planeado'),
                               (1, 'Si'),
                               (2, 'No')}


    choice_partoTermino = {('', 'Parto término'),
                           (1, 'Si'),
                           (2, 'No')}

    choice_paridad = {('', 'Paridad'),
                           (1, 'Primigesta'),
                           (2, 'Multigesta')}

    choice_lactancia = {('', 'Lactancia'),
                        (1, 'Si'),
                        (2, 'No')}

    choice_enfermedadNeonato = {('', 'Enfermedad el neonato'),
                                (1, 'Si'),
                                (2, 'No')}

    choice_anetesia = {('', 'Anestesia'),
                       (1, 'Si'),
                       (2, 'No')}

    choice_tipoAnetesia = {('', 'Tipos de anestesia'),
                           (1, 'Anestesia inhalatoria'),
                           (2, 'Anestesia general'),
                           (0, 'Otra')
                           }

    choice_tipoParto = {('', 'Tipos de parto'),
                        (1, 'vaginal'),
                        (2, 'Cesarea')}

    choice_apoyoFamilia = {('', 'Apoyo actual de la familia'),
                           (1, 'Si'),
                           (2, 'No')}

    choice_apoyoPareja = {('', 'Apoyo actual de la Pareja'),
                          (1, 'Si'),
                          (2, 'No')}

    choice_abortosPrevios = {('', 'Abortos previos al parto actual'),
                             (1, 'Si'),
                             (2, 'No')}



#Datos sociodemograficos

    #fecha_de_nacimiento = models.DateField()
    edad = models.IntegerField()
    estado_civil = models.IntegerField(
        choices=choice_estadoCivil,
        default='',)
    escolaridad = models.IntegerField(
        choices=choice_escolaridad,
        default='',)
    ocupacion = models.IntegerField(
        choices=choice_ocupacion,
        default='',)
    status_economico = models.IntegerField(
        choices=choice_statusEconomico,
        default='',)
    ingreso_mensual = models.IntegerField()
    embarazo_deseado = models.IntegerField(
        choices=choice_embarazoDeseado,
        default='',)
    embarazo_planeado = models.IntegerField(
        choices=choice_embarazoPlaneado,
        default='',)

    parto_termino = models.IntegerField(
        choices=choice_partoTermino,
        default='',)
    paridad = models.IntegerField(
        choices=choice_paridad,
        default='',)


    numero_de_hijos = models.IntegerField()

    lactancia = models.IntegerField(
        choices=choice_lactancia,
        default='',)
    tiempo_de_lactancia = models.IntegerField()

    enfermedad_del_neonato = models.IntegerField(
        choices=choice_enfermedadNeonato,
        default='',)
    tipo_de_enfermedad_neonato = models.CharField(max_length=150)

    anestesia = models.IntegerField(
        choices=choice_anetesia,
        default='',)
    tipo_de_anestesia = models.IntegerField(
        choices=choice_tipoAnetesia,
        default='',)
    tipo_de_parto = models.IntegerField(
        choices=choice_tipoParto,
        default='',)
    edad_del_bebe = models.IntegerField()
    lugar_de_atencion = models.CharField(max_length=150)
    apoyo_de_familia = models.IntegerField(
        choices=choice_apoyoFamilia,
        default='',)
    apoyo_de_pareja = models.IntegerField(
        choices=choice_apoyoPareja,
        default='',)
    abortos = models.IntegerField(
        choices=choice_abortosPrevios,
        default='',)
    numero_de_bortos = models.IntegerField()



    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #active = models.BooleanField(default=True)
    #
    def __str__(self):
        return self.user.name
