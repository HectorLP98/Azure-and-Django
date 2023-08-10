# Generated by Django 4.2.3 on 2023-08-02 00:21

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "description",
                    models.CharField(max_length=250, verbose_name="Descripcion"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
            ],
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias",},
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="titulo")),
                ("content", ckeditor.fields.RichTextField(verbose_name="contenido")),
                (
                    "image",
                    models.ImageField(
                        default="null", upload_to="", verbose_name="imagen"
                    ),
                ),
                ("public", models.BooleanField(verbose_name="¿Publicado?")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="creado"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="actualizado"),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        to="blog.category",
                        verbose_name="Categorias",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="usuario",
                    ),
                ),
            ],
            options={"verbose_name": "Articulo", "verbose_name_plural": "Articulos",},
        ),
    ]
