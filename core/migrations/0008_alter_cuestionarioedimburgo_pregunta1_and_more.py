# Generated by Django 4.0.2 on 2022-02-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_cuestionarioedimburgo_pregunta1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta1',
            field=models.IntegerField(blank=True, choices=[(2, 'Mucho menos ahora'), (0, 'Tanto como siempre'), (3, 'No, Nada'), (1, 'No tanto ahora')], default='', null=True, verbose_name='1. He sido capaz de reír y ver el lado bueno de las cosas'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta10',
            field=models.IntegerField(blank=True, choices=[(2, 'Casi nunca'), (0, 'Sí, bastante a menudo'), (1, 'A veces'), (3, 'No, nunca')], default='', null=True, verbose_name='10. He pensado en hacerme daño a mí misma'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta2',
            field=models.IntegerField(blank=True, choices=[(0, 'Tanto como siempre'), (3, 'Casi nada'), (1, 'Meno que antes'), (2, 'Mucho menos que antes')], default='', null=True, verbose_name='2. He mirado el futuro con placer'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta3',
            field=models.IntegerField(blank=True, choices=[(0, 'Sí, la mayoría de las veces'), (1, 'Sí, algunas veces'), (2, 'No muy a menudo'), (3, 'No, nunca')], default='', null=True, verbose_name='3. Me he culpado sin necesidad cuando las cosas no salían bien'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta4',
            field=models.IntegerField(blank=True, choices=[(0, 'No, para nada'), (1, 'Casi nada'), (2, 'Sí, a veces'), (3, 'Sí, a menudo')], default='', null=True, verbose_name='4. He estado ansiosa y preocupada sin motivo'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta5',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí, a veces'), (0, 'Sí, bastante'), (2, 'No, no mucho'), (3, 'No, nada')], default='', null=True, verbose_name='5. He sentido miedo y pánico sin motivo alguno'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta6',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí, a veces'), (2, 'No, casi nunca'), (0, 'Sí, la mayor parte de las veces'), (3, 'No, nada')], default='', null=True, verbose_name='6. Las cosas me oprimen o agobian'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta7',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí, a veces'), (0, 'Sí, la mayoría de las veces'), (2, 'No muy a menudo'), (3, 'No, nada')], default='', null=True, verbose_name='7. Me he sentido tan infeliz que he tenido dificultad para dormir'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta8',
            field=models.IntegerField(blank=True, choices=[(3, 'No, nada'), (0, 'Sí, casi siempre'), (2, 'No muy a menudo'), (1, 'Sí, bastante a menudo')], default='', null=True, verbose_name='8. Me he sentido triste y desgraciada'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta9',
            field=models.IntegerField(blank=True, choices=[(0, 'Sí, casi siempre'), (1, 'Sí, bastante a menudo'), (2, 'Sólo en ocasiones'), (3, 'No, nunca')], default='', null=True, verbose_name='9. He sido tan infeliz que he estado llorando'),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='abortos',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Abortos previos al parto actual'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='anestesia',
            field=models.IntegerField(choices=[('', 'Anestesia'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='apoyo_de_familia',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Apoyo actual de la familia'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='apoyo_de_pareja',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Apoyo actual de la Pareja'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='embarazo_deseado',
            field=models.IntegerField(choices=[('', 'Embarazo deseado'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='embarazo_planeado',
            field=models.IntegerField(choices=[(2, 'No'), ('', 'Embarazo planeado'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='enfermedad_del_neonato',
            field=models.IntegerField(choices=[('', 'Enfermedad el neonato'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='escolaridad',
            field=models.IntegerField(choices=[(4, 'Licenciatura'), ('', 'Escolaridad'), (5, 'Posgrado'), (3, 'Bachillerato'), (2, 'Secundaria'), (1, 'Primaria')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='estado_civil',
            field=models.IntegerField(choices=[('', 'Estado civil'), (3, 'Soltera'), (1, 'Casada'), (4, 'Viuda'), (2, 'Union libre')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='ocupacion',
            field=models.IntegerField(choices=[('', 'Ocupacion'), (4, 'Desempleada'), (3, 'Estadiante'), (1, 'Ama de casa'), (2, 'Empleada')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='paridad',
            field=models.IntegerField(choices=[(2, 'Multigesta'), ('', 'Paridad'), (1, 'Primigesta')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='status_economico',
            field=models.IntegerField(choices=[(2, 'Baja alta'), (4, 'Media alta'), (1, 'Baja baja'), (3, 'Media baja'), ('', 'Status economico')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_anestesia',
            field=models.IntegerField(choices=[(2, 'Anestesia general'), (1, 'Anestesia inhalatoria'), ('', 'Tipos de anestesia'), (0, 'Otra')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_parto',
            field=models.IntegerField(choices=[(2, 'Cesarea'), (1, 'vaginal'), ('', 'Tipos de parto')], default=''),
        ),
    ]
