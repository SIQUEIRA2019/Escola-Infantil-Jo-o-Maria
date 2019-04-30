# Generated by Django 2.1.7 on 2019-04-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecadastro', models.CharField(max_length=50, verbose_name='nomecadastro')),
                ('siglacadastro', models.CharField(max_length=5, verbose_name='siglacadastro')),
                ('emailcadastro', models.SlugField(verbose_name='emailcadastro')),
            ],
        ),
    ]