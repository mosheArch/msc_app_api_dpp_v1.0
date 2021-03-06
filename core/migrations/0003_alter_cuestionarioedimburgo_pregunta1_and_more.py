# Generated by Django 4.0.2 on 2022-02-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cuestionarioedimburgo_pregunta1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta1',
            field=models.CharField(blank=True, choices=[('Tanto como siempre', 'Tanto como siempre'), ('Mucho menos', 'Mucho menos'), ('No, no he podido', 'No, no he podido'), ('No tanto ahora', 'No tanto ahora')], default='', max_length=100, null=True, verbose_name='1. He sido capaz de reír y ver el lado bueno de las cosas'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta10',
            field=models.CharField(blank=True, choices=[('Sí, bastante a menudo', 'Sí, bastante a menudo'), ('No, nunca', 'No, nunca'), ('Casi nunca', 'Casi nunca'), ('A veces', 'A veces')], default='', max_length=100, null=True, verbose_name='10. He pensado en hacerme daño a mí misma'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta2',
            field=models.CharField(blank=True, choices=[('No, nada ', 'No, nada'), ('Tanto como siempre', 'Tanto como siempre'), ('Algo menos de lo que solía hacer', 'Algo menos de lo que solía hacer'), ('Definitivamente menos', 'Definitivamente menos')], default='', max_length=100, null=True, verbose_name='2. He mirado el futuro con placer'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta3',
            field=models.CharField(blank=True, choices=[('Sí, la mayoría de las veces', 'Sí, la mayoría de las veces'), ('No muy a menudo', 'No muy a menudo'), ('No, nunca', 'No, nunca'), ('Sí, algunas veces', 'Sí, algunas veces')], default='', max_length=100, null=True, verbose_name='3. Me he culpado sin necesidad cuando las cosas no salían bien'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta4',
            field=models.CharField(blank=True, choices=[('Casi nada', 'Casi nada'), ('Sí, a menudo', 'Sí, a menudo'), ('No, para nada', 'No, para nada'), ('Sí, a veces', 'Sí, a veces')], default='', max_length=100, null=True, verbose_name='4. He estado ansiosa y preocupada sin motivo'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta8',
            field=models.CharField(blank=True, choices=[('No muy a menudo', 'No muy a menudo'), ('Sí, casi siempre', 'Sí, casi siempre'), ('Sí, bastante a menudo', 'Sí, bastante a menudo'), ('No, nada', 'No, nada')], default='', max_length=100, null=True, verbose_name='8. Me he sentido triste y desgraciada'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta9',
            field=models.CharField(blank=True, choices=[('Sí, casi siempre', 'Sí, casi siempre'), ('Sí, bastante a menudo', 'Sí, bastante a menudo'), ('No, nunca', 'No, nunca'), ('Sólo en ocasiones', 'Sólo en ocasiones')], default='', max_length=100, null=True, verbose_name='9. He sido tan infeliz que he estado llorando'),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='abortos',
            field=models.IntegerField(choices=[('', 'Abortos previos al parto actual'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='anestesia',
            field=models.IntegerField(choices=[('', 'Anestesia'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='apoyo_de_familia',
            field=models.IntegerField(choices=[('', 'Apoyo actual de la familia'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='apoyo_de_pareja',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Apoyo actual de la Pareja'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='embarazo_deseado',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Embarazo deseado'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='embarazo_planeado',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Embarazo planeado'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='enfermedad_del_neonato',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Enfermedad el neonato'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='escolaridad',
            field=models.IntegerField(choices=[(5, 'Posgrado'), (2, 'Secundaria'), (1, 'Primaria'), ('', 'Escolaridad'), (4, 'Licenciatura'), (3, 'Bachillerato')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='estado_civil',
            field=models.IntegerField(choices=[(4, 'Viuda'), (3, 'Soltera'), (1, 'Casada'), (2, 'Union libre'), ('', 'Estado civil')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='lactancia',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Lactancia'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='ocupacion',
            field=models.IntegerField(choices=[(2, 'Empleada'), (4, 'Desempleada'), (3, 'Estadiante'), (1, 'Ama de casa'), ('', 'Ocupacion')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='paridad',
            field=models.IntegerField(choices=[('', 'Paridad'), (1, 'Primigesta'), (2, 'Multigesta')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='parto_termino',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Parto término'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='status_economico',
            field=models.IntegerField(choices=[(2, 'Baja alta'), ('', 'Status economico'), (3, 'Media baja'), (1, 'Baja baja'), (4, 'Media alta')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_anestesia',
            field=models.IntegerField(choices=[(0, 'Otra'), (2, 'Anestesia general'), ('', 'Tipos de anestesia'), (1, 'Anestesia inhalatoria')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_parto',
            field=models.IntegerField(choices=[(2, 'Cesarea'), (1, 'vaginal'), ('', 'Tipos de parto')], default=''),
        ),
    ]
