# Generated by Django 4.2.1 on 2023-06-04 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('link_site', models.CharField(default=True, max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('etcs', models.IntegerField()),
                ('coordenador', models.CharField(max_length=100)),
                ('nota', models.CharField(max_length=20)),
                ('rating', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_utilizador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descrição', models.CharField(max_length=1000)),
                ('imagem', models.CharField(max_length=100)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tecnologias', to='portfolioDjango.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=2000)),
                ('linguagem_programacao', models.CharField(max_length=10)),
                ('link_associado', models.CharField(blank=True, default=True, max_length=100)),
                ('cadeira', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cadeira', to='portfolioDjango.cadeira')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='portfolioDjango.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='licenciatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_licenciatura', models.CharField(max_length=100)),
                ('portfolio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='licenciatura', to='portfolioDjango.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='facto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.CharField(max_length=100)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factos', to='portfolioDjango.portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='licenciatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cadeiras', to='portfolioDjango.licenciatura'),
        ),
    ]