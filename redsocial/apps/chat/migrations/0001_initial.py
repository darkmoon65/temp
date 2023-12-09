# Generated by Django 4.2.6 on 2023-12-08 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('usuario1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_usuario1', to='usuarios.usuario')),
                ('usuario2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_usuario2', to='usuarios.usuario')),
            ],
            options={
                'ordering': ['usuario1', 'usuario2', 'fecha_inicio'],
            },
        ),
        migrations.CreateModel(
            name='MensajeChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('mensaje_text', models.TextField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'ordering': ['usuario', 'fecha', 'mensaje_text'],
            },
        ),
    ]
