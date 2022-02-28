# Generated by Django 4.0.2 on 2022-02-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_cuestionarioedimburgo_pregunta1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta1',
            field=models.IntegerField(blank=True, choices=[(3, 'Mucho menos ahora'), (1, 'Tanto como siempre'), (2, 'No tanto ahora'), (4, 'No, Nada')], default='', null=True, verbose_name='1. He sido capaz de reír y ver el lado bueno de las cosas'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta10',
            field=models.IntegerField(blank=True, choices=[(4, 'No, nunca'), (1, 'Sí, bastante a menudo'), (3, 'Casi nunca'), (2, 'A veces')], default='', null=True, verbose_name='10. He pensado en hacerme daño a mí misma'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta2',
            field=models.IntegerField(blank=True, choices=[(2, 'Meno que antes'), (1, 'Tanto como siempre'), (3, 'Mucho menos que antes'), (4, 'Casi nada')], default='', null=True, verbose_name='2. He mirado el futuro con placer'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta3',
            field=models.IntegerField(blank=True, choices=[(3, 'No muy a menudo'), (4, 'No, nunca'), (1, 'Sí, la mayoría de las veces'), (2, 'Sí, algunas veces')], default='', null=True, verbose_name='3. Me he culpado sin necesidad cuando las cosas no salían bien'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta4',
            field=models.IntegerField(blank=True, choices=[(1, 'No, para nada'), (4, 'Sí, a menudo'), (3, 'Sí, a veces'), (2, 'Casi nada')], default='', null=True, verbose_name='4. He estado ansiosa y preocupada sin motivo'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta5',
            field=models.IntegerField(blank=True, choices=[(3, 'No, no mucho'), (4, 'No, nada'), (2, 'Sí, a veces'), (1, 'Sí, bastante')], default='', null=True, verbose_name='5. He sentido miedo y pánico sin motivo alguno'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta6',
            field=models.IntegerField(blank=True, choices=[(4, 'No, nada'), (2, 'Sí, a veces'), (1, 'Sí, la mayor parte de las veces'), (3, 'No, casi nunca')], default='', null=True, verbose_name='6. Las cosas me oprimen o agobian'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta7',
            field=models.IntegerField(blank=True, choices=[(3, 'No muy a menudo'), (4, 'No, nada'), (2, 'Sí, a veces'), (1, 'Sí, la mayoría de las veces')], default='', null=True, verbose_name='7. Me he sentido tan infeliz que he tenido dificultad para dormir'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta8',
            field=models.IntegerField(blank=True, choices=[(3, 'No muy a menudo'), (4, 'No, nada'), (1, 'Sí, casi siempre'), (2, 'Sí, bastante a menudo')], default='', null=True, verbose_name='8. Me he sentido triste y desgraciada'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta9',
            field=models.IntegerField(blank=True, choices=[(4, 'No, nunca'), (1, 'Sí, casi siempre'), (2, 'Sí, bastante a menudo'), (3, 'Sólo en ocasiones')], default='', null=True, verbose_name='9. He sido tan infeliz que he estado llorando'),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='apoyo_de_familia',
            field=models.IntegerField(choices=[(2, 'No'), (1, 'Si'), ('', 'Apoyo actual de la familia')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='embarazo_planeado',
            field=models.IntegerField(choices=[('', 'Embarazo planeado'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='escolaridad',
            field=models.IntegerField(choices=[(4, 'Licenciatura'), (1, 'Primaria'), ('', 'Escolaridad'), (3, 'Bachillerato'), (5, 'Posgrado'), (2, 'Secundaria')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='estado_civil',
            field=models.IntegerField(choices=[(1, 'Casada'), (2, 'Union libre'), (3, 'Soltera'), ('', 'Estado civil'), (4, 'Viuda')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='ocupacion',
            field=models.IntegerField(choices=[(1, 'Ama de casa'), (3, 'Estadiante'), (4, 'Desempleada'), ('', 'Ocupacion'), (2, 'Empleada')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='paridad',
            field=models.IntegerField(choices=[(2, 'Multigesta'), ('', 'Paridad'), (1, 'Primigesta')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='status_economico',
            field=models.IntegerField(choices=[(1, 'Baja baja'), ('', 'Status economico'), (3, 'Media baja'), (2, 'Baja alta'), (4, 'Media alta')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_anestesia',
            field=models.IntegerField(choices=[(0, 'Otra'), (1, 'Anestesia inhalatoria'), (2, 'Anestesia general'), ('', 'Tipos de anestesia')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_parto',
            field=models.IntegerField(choices=[('', 'Tipos de parto'), (2, 'Cesarea'), (1, 'vaginal')], default=''),
        ),
    ]
