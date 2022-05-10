from pydoc import Doc
from django.contrib import admin
from django.contrib.gis.db import models
from .models import *
import diana.abstract.models
from diana.abstract.models import DEFAULT_EXCLUDE, DEFAULT_FIELDS, get_many_to_many_fields
from django.contrib.gis import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter, PolymorphicInlineSupportMixin, StackedPolymorphicInline

def get_fields(model: models.Model):

    exclude = DEFAULT_EXCLUDE + ['artifact_ptr',]
    fields  = [field for field in diana.abstract.models.get_fields(model) if ((not field.startswith('legacy')) and field not in exclude)]

    return fields

def get_list_display_fields(model: models.Model):

    m2m = get_many_to_many_fields(model)
    exclude = DEFAULT_EXCLUDE + ['artifact_ptr',]
    fields  = [field for field in diana.abstract.models.get_fields(model) if ((not field.startswith('legacy')) and field not in exclude and field not in m2m)]

    return fields + DEFAULT_FIELDS


##########################################
class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

class ImageInline(admin.StackedInline):
    model = Image
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    exclude = ('iiif_file',)
    extra = 1


@admin.register(ImageContent)
class ImageContentTagAdmin(admin.ModelAdmin):

    fields = get_fields(ImageContent)
    list_display = get_fields(ImageContent) + DEFAULT_FIELDS


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):

    fields = get_fields(Material)
    list_display = get_fields(Material) + DEFAULT_FIELDS

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    fields = get_fields(Place)
    list_display = get_fields(Place) + DEFAULT_FIELDS


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    fields = get_fields(Person)
    list_display = get_fields(Person) + DEFAULT_FIELDS 
    search_fields = ('name',)

@admin.register(Image)
class ImageModel(admin.ModelAdmin):
    
    fields = get_fields(Image)
    readonly_fields = ['uuid', 'iiif_file']
    list_display = get_list_display_fields(Image)
    filter_horizontal = ('tags',)

@admin.register(Museum)
class MuseumAdmin(admin.ModelAdmin):

    fields = get_fields(Museum)
    list_display = get_fields(Museum) + DEFAULT_FIELDS 
    search_fields = ('name',)

##################################################


class ArtifactAdminModel(PolymorphicInlineSupportMixin, PolymorphicChildModelAdmin):

    base_model = Artifact
    search_fields = ['title']
    show_in_index = True
    inlines = [ImageInline,]
    filter_horizontal = ('materials', 'persons', 'places')

@admin.register(Artwork)
class ArtworkAdmin(ArtifactAdminModel):
    base_model = Artwork
    fields = get_fields(Artwork)
    list_display = get_list_display_fields(Artwork)
    # filter_horizontal = ('materials',)
    autocomplete_fields = ('creator', 'museum')


@admin.register(Photograph)
class PhotographAdmin(ArtifactAdminModel):
    base_model = Photograph
    fields = get_fields(Photograph)

    list_display = get_list_display_fields(Photograph)
    autocomplete_fields = ('creator', 'museum')


@admin.register(Letter)
class LetterAdmin(ArtifactAdminModel):
    base_model = Letter
    fields = get_fields(Letter)

    list_display = get_list_display_fields(Letter)
    autocomplete_fields = ('sender', 'recipient', 'museum')


@admin.register(Document)
class DocumentAdmin(ArtifactAdminModel):
    base_model = Document
    fields = get_fields(Document)
    list_display = get_list_display_fields(Document)
    autocomplete_fields = ('museum',)


@admin.register(Relic)
class RelicAdmin(ArtifactAdminModel):
    base_model = Relic
    fields = get_fields(Relic)
    list_display = get_list_display_fields(Relic)
    autocomplete_fields = ('museum',)


@admin.register(Artifact)
class ArtifactParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Artifact  # Optional, explicitly set here.
    child_models = (Artwork, Photograph, Letter, Document, Relic)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.