# Generated by Django 4.0.4 on 2022-05-10 08:39

import diana.abstract.models
import diana.storages
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=64, null=True)),
                ('date_human', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('legacy_acquisition', models.CharField(blank=True, max_length=128, null=True)),
                ('legacy_content', models.CharField(blank=True, max_length=128, null=True)),
                ('legacy_inscription', models.CharField(blank=True, max_length=128, null=True)),
                ('legacy_literature', models.CharField(blank=True, max_length=64, null=True)),
                ('legacy_exhibitions', models.CharField(blank=True, max_length=64, null=True)),
                ('legacy_reproductions', models.CharField(blank=True, max_length=64, null=True)),
                ('legacy_bundle', models.CharField(blank=True, max_length=32, null=True)),
                ('legacy_bundle_order', models.IntegerField(blank=True, null=True)),
                ('legacy_bundle_side', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ArtworkSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('file', models.ImageField(storage=diana.storages.OriginalFileStorage, upload_to=diana.abstract.models.get_original_path)),
                ('iiif_file', models.ImageField(blank=True, null=True, storage=diana.storages.IIIFFileStorage, upload_to=diana.abstract.models.get_iiif_path)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('motif', models.TextField(blank=True, default='', null=True)),
                ('inner_width', models.IntegerField(blank=True, null=True)),
                ('inner_height', models.IntegerField(blank=True, null=True)),
                ('outer_width', models.IntegerField(blank=True, null=True)),
                ('outer_height', models.IntegerField(blank=True, null=True)),
                ('page', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('side', models.CharField(choices=[('F', 'Front'), ('B', 'Back'), ('C', 'Colour target')], default=('F', 'Front'), max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LetterSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
                ('death_year', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('-', 'Other'), ('X', 'Unknown')], max_length=1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhotographSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RelicSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('name', diana.abstract.models.CINameField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('artifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='arosenius.artifact')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('arosenius.artifact',),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('artifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='arosenius.artifact')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('arosenius.artifact',),
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('artifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='arosenius.artifact')),
                ('transcription', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('arosenius.artifact',),
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('artifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='arosenius.artifact')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('arosenius.artifact',),
        ),
        migrations.CreateModel(
            name='Relic',
            fields=[
                ('artifact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='arosenius.artifact')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('arosenius.artifact',),
        ),
        migrations.AddConstraint(
            model_name='relicsubcategory',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='relicsubcategory_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='place',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='place_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='photographsubcategory',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='photographsubcategory_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='museum',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='museum_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='material',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='material_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='lettersubcategory',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='lettersubcategory_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='imagecontent',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='imagecontent_name_unique'),
        ),
        migrations.AddField(
            model_name='image',
            name='artifact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arosenius.artifact'),
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='images', to='arosenius.imagecontent'),
        ),
        migrations.AddConstraint(
            model_name='documentsubcategory',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='documentsubcategory_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='documentcategory',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='documentcategory_name_unique'),
        ),
        migrations.AddField(
            model_name='collection',
            name='objects',
            field=models.ManyToManyField(to='arosenius.artifact'),
        ),
        migrations.AddConstraint(
            model_name='artworksubcategory',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='artworksubcategory_name_unique'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='materials',
            field=models.ManyToManyField(blank=True, to='arosenius.material'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='museum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arosenius.museum'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='persons',
            field=models.ManyToManyField(blank=True, to='arosenius.person'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='places',
            field=models.ManyToManyField(blank=True, to='arosenius.place'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='relic',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='arosenius.relicsubcategory'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arosenius.person'),
        ),
        migrations.AddField(
            model_name='photograph',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='arosenius.photographsubcategory'),
        ),
        migrations.AddField(
            model_name='letter',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='arosenius.person'),
        ),
        migrations.AddField(
            model_name='letter',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='arosenius.person'),
        ),
        migrations.AddField(
            model_name='letter',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='arosenius.lettersubcategory'),
        ),
        migrations.AddField(
            model_name='document',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arosenius.documentcategory'),
        ),
        migrations.AddField(
            model_name='document',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='arosenius.documentsubcategory'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arosenius.person'),
        ),
    ]
