# Generated by Django 4.0.4 on 2022-04-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero_de_contacto', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Numero_de_contacto',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Numero_de_contacto',
            field=models.ManyToManyField(to='clientes.contactos'),
        ),
    ]