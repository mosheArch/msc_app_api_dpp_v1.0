# Generated by Django 4.0.2 on 2022-02-28 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_cuestionarioedimburgo_pregunta1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuestionarioedimburgo',
            name='estadoActual',
            field=models.CharField(blank=True, choices=[(0, 'Sí, bastante a menudo'), (2, 'Casi nunca'), (1, 'A veces'), (3, 'No, nunca')], default='', max_length=50, null=True, verbose_name='¿Está embarazada o hace poco tuvo un bebé?'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta1',
            field=models.IntegerField(blank=True, choices=[(0, 'Tanto como siempre'), (3, 'No, Nada'), (1, 'No tanto ahora'), (2, 'Mucho menos ahora')], default='', null=True, verbose_name='1. He sido capaz de reír y ver el lado bueno de las cosas'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta10',
            field=models.IntegerField(blank=True, choices=[(0, 'Sí, bastante a menudo'), (2, 'Casi nunca'), (1, 'A veces'), (3, 'No, nunca')], default='', null=True, verbose_name='10. He pensado en hacerme daño a mí misma'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta2',
            field=models.IntegerField(blank=True, choices=[(2, 'Mucho menos que antes'), (0, 'Tanto como siempre'), (3, 'Casi nada'), (1, 'Meno que antes')], default='', null=True, verbose_name='2. He mirado el futuro con placer'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta4',
            field=models.IntegerField(blank=True, choices=[(0, 'No, para nada'), (2, 'Sí, a veces'), (3, 'Sí, a menudo'), (1, 'Casi nada')], default='', null=True, verbose_name='4. He estado ansiosa y preocupada sin motivo'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta5',
            field=models.IntegerField(blank=True, choices=[(2, 'No, no mucho'), (0, 'Sí, bastante'), (3, 'No, nada'), (1, 'Sí, a veces')], default='', null=True, verbose_name='5. He sentido miedo y pánico sin motivo alguno'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta6',
            field=models.IntegerField(blank=True, choices=[(0, 'Sí, la mayor parte de las veces'), (2, 'No, casi nunca'), (3, 'No, nada'), (1, 'Sí, a veces')], default='', null=True, verbose_name='6. Las cosas me oprimen o agobian'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta7',
            field=models.IntegerField(blank=True, choices=[(0, 'Sí, la mayoría de las veces'), (2, 'No muy a menudo'), (3, 'No, nada'), (1, 'Sí, a veces')], default='', null=True, verbose_name='7. Me he sentido tan infeliz que he tenido dificultad para dormir'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta8',
            field=models.IntegerField(blank=True, choices=[(2, 'No muy a menudo'), (3, 'No, nada'), (0, 'Sí, casi siempre'), (1, 'Sí, bastante a menudo')], default='', null=True, verbose_name='8. Me he sentido triste y desgraciada'),
        ),
        migrations.AlterField(
            model_name='cuestionarioedimburgo',
            name='pregunta9',
            field=models.IntegerField(blank=True, choices=[(3, 'No, nunca'), (1, 'Sí, bastante a menudo'), (0, 'Sí, casi siempre'), (2, 'Sólo en ocasiones')], default='', null=True, verbose_name='9. He sido tan infeliz que he estado llorando'),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='abortos',
            field=models.IntegerField(choices=[('', 'Abortos previos al parto actual'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='apoyo_de_familia',
            field=models.IntegerField(choices=[('', 'Apoyo actual de la familia'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='apoyo_de_pareja',
            field=models.IntegerField(choices=[(2, 'No'), (1, 'Si'), ('', 'Apoyo actual de la Pareja')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='escolaridad',
            field=models.IntegerField(choices=[(3, 'Bachillerato'), (5, 'Posgrado'), (4, 'Licenciatura'), ('', 'Escolaridad'), (2, 'Secundaria'), (1, 'Primaria')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='estado_civil',
            field=models.IntegerField(choices=[(4, 'Viuda'), (1, 'Casada'), ('', 'Estado civil'), (2, 'Union libre'), (3, 'Soltera')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='lactancia',
            field=models.IntegerField(choices=[('', 'Lactancia'), (2, 'No'), (1, 'Si')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='ocupacion',
            field=models.IntegerField(choices=[(2, 'Empleada'), (1, 'Ama de casa'), (3, 'Estadiante'), ('', 'Ocupacion'), (4, 'Desempleada')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='paridad',
            field=models.IntegerField(choices=[(2, 'Multigesta'), (1, 'Primigesta'), ('', 'Paridad')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='parto_termino',
            field=models.IntegerField(choices=[(2, 'No'), (1, 'Si'), ('', 'Parto término')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='status_economico',
            field=models.IntegerField(choices=[(3, 'Media baja'), (4, 'Media alta'), (2, 'Baja alta'), (1, 'Baja baja'), ('', 'Status economico')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_anestesia',
            field=models.IntegerField(choices=[('', 'Tipos de anestesia'), (2, 'Anestesia general'), (0, 'Otra'), (1, 'Anestesia inhalatoria')], default=''),
        ),
        migrations.AlterField(
            model_name='datossociodemograficos',
            name='tipo_de_parto',
            field=models.IntegerField(choices=[('', 'Tipos de parto'), (2, 'Cesarea'), (1, 'vaginal')], default=''),
        ),
        migrations.CreateModel(
            name='resultdoEdimburgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.IntegerField()),
                ('comentarios', models.CharField(blank=True, max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
