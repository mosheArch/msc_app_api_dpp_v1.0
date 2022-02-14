#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class DatosSociodemograficos(models.Model):

#Choice de datos definidos
    choice_estadoCivil = {('', 'Estado civil'),
                          ('Soltera', 'Soltera'),
                          ('Casada', 'Casada'),
                          ('Union libre', 'Union libre'),
                          ('Viuda', 'Viuda')}

    choice_escolaridad = {('', 'Escolaridad'),
                          ('Primaria', 'Primaria'),
                          ('Secundaria', 'Secundaria'),
                          ('Bachillerato', 'Bachillerato'),
                          ('Lienciatura', 'Licenciatura'),
                          ('Posgrado', 'Posgrado')}

    choice_ocupacion = {('', 'Ocupacion'),
                        ('Ama de casa', 'Ama de casa'),
                        ('Empleada tiempo parcial', 'Empleada tiempo parcial'),
                        ('Empleada tiempo completo', 'Empleada tiempo completo'),
                        ('Desempleada', 'Desempleada')}

    choice_embarazoPlaneado = {('', 'Embarazo planeado'), ('Si', 'Si'), ('No', 'No')}

    choice_embarazoDeseado = {('', 'Embarazo deseado'), ('Si', 'Si'), ('No', 'No')}

    choice_partoTermino = {('', 'Parto término'),
                           ('Término temprano', 'Término temprano'),
                           ('Término completo', 'Término completo'),
                           ('Término tardío', 'Término tardío'),
                           ('Postérmino', 'Postérmino')
                           }

    choice_lactancia = {('', 'Lactancia'), ('Si', 'Si'), ('No', 'No')}

    choice_enfermedadNeonato = {('', 'Enfermedad el neonato'), ('Si', 'Si'), ('No', 'No')}

    choice_anetesia = {('', 'Anestesia'), ('Si', 'Si'), ('No', 'No')}

    choice_tipoAnetesia = {('', 'Tipos de anestesia'),
                           ('Anestesia inhalatoria', 'Anestesia inhalatoria'),
                           ('Anestesia general', 'Anestesia general'),
                           ('Analgesia parenteral (intramuscular o intravenosa)',
                            'Analgesia parenteral (intramuscular o intravenosa)'),
                           ('Bloqueo paracervical', 'Bloqueo paracervical'),
                           ('Bloqueo de nervios pudendos', 'Bloqueo de nervios pudendos'),
                           ('Analgesia local', 'Analgesia local'),
                           ('Bloqueo espinal (epidural y subaracnoideo)', 'Bloqueo espinal (epidural y subaracnoideo)'),
                           }

    choice_tipoParto = {('', 'Tipos de parto'),
                        ('Parto espontáneo', 'Parto espontáneo'),
                        ('Parto inducido', 'Parto inducido')}

    choice_apoyoFamilia = {('', 'Apoyo actual de la familia'), ('Si', 'Si'), ('No', 'No')}

    choice_apoyoPareja = {('', 'Apoyo actual de la Pareja'), ('Si', 'Si'), ('No', 'No')}

    choice_abortosPrevios = {('', 'Abortos previos al parto actual'), ('Si', 'Si'), ('No', 'No')}

    choice_statusEconomico = {('', 'Status economico'), ('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')}

#Datos sociodemograficos

    fecha_de_nacimiento = models.DateField()
    edad = models.IntegerField()
    estado_civil = models.CharField(
        choices=choice_estadoCivil,
        default='',
        max_length=20,
        blank=True,
        null=True)
    escolaridad = models.CharField(
        choices=choice_escolaridad,
        default='',
        max_length=50,
        blank=True,
        null=True)
    embarazo_planeado = models.CharField(
        choices=choice_embarazoPlaneado,
        default='',
        max_length=10,
        blank=True,
        null=True)
    embarazo_deseado = models.CharField(
        choices=choice_embarazoDeseado,
        default='',
        max_length=10,
        blank=True,
        null=True)
    parto_termino = models.CharField(
        choices=choice_partoTermino,
        default='',
        max_length=30,
        blank=True,
        null=True)
    paridad = models.IntegerField()
    numero_de_hijos = models.IntegerField()
    lactancia = models.CharField(
        choices=choice_lactancia,
        default='',
        max_length=30,
        blank=True,
        null=True)
    tiempo_de_lactancia = models.IntegerField()
    enfermedad_del_neonato = models.CharField(
        choices=choice_enfermedadNeonato,
        default='',
        max_length=30,
        blank=True,
        null=True)
    tipo_de_enfermedad_neonato = models.CharField(max_length=150)
    anestesia = models.CharField(
        choices=choice_anetesia,
        default='',
        max_length=30,
        blank=True,
        null=True)
    tipo_de_anestesia = models.CharField(
        choices=choice_tipoAnetesia,
        default='',
        max_length=100,
        blank=True,
        null=True)
    tipo_de_parto = models.CharField(
        choices=choice_tipoParto,
        default='',
        max_length=50,
        blank=True,
        null=True)
    edad_del_bebe = models.IntegerField()
    lugar_de_atencion = models.CharField(max_length=150)
    apoyo_de_familia = models.CharField(
        choices=choice_apoyoFamilia,
        default='',
        max_length=50,
        blank=True,
        null=True)
    apoyo_de_pareja = models.CharField(
        choices=choice_apoyoPareja,
        default='',
        max_length=50,
        blank=True,
        null=True)
    abortos_previos = models.CharField(
        choices=choice_abortosPrevios,
        default='',
        max_length=50,
        blank=True,
        null=True)
    numero_de_bortos = models.IntegerField()

    ocupacion = models.CharField(
        choices=choice_ocupacion,
        default='',
        max_length=50,
        blank=True,
        null=True)
    status_economico = models.CharField(
        choices=choice_statusEconomico,
        default='',
        max_length=50,
        blank=True,
        null=True)
    ingreso_mensual = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #active = models.BooleanField(default=True)
    #
    def __str__(self):
        return self.user.name
