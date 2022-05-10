
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.core.exceptions import ValidationError

import diana.abstract.models as abstract

from polymorphic.models import PolymorphicModel

def tag_case_insensitive_validator(value):
    if Tag.objects.filter(name=value.lower()).exists():
        raise ValidationError('This tag already exists.')
    return value

############################################

class Tag(abstract.AbstractBaseModel):

    name = abstract.CINameField(unique=True, max_length=64) 

    def __str__(self) -> str:
        return f"{self.name}"


    class Meta:
        abstract = True
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='%(class)s_name_unique',
            ),
        ]

    def __str__(self) -> str:
        return f"{self.name}"

class Material(Tag):
    pass

class Place(Tag):

    pass

class ArtworkSubcategory(Tag):
    pass

class PhotographSubcategory(Tag):
    pass

class LetterSubcategory(Tag):
    pass

class DocumentCategory(Tag):
    pass

class DocumentSubcategory(Tag):
    pass

class RelicSubcategory(Tag):
    pass

class ImageContent(Tag):
    pass


##############################################
class Museum(abstract.AbstractBaseModel):

    name = models.CharField(unique=True, max_length=64) 

    def __str__(self) -> str:
        return f"{self.name}"


    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='%(class)s_name_unique',
            ),
        ]

    def __str__(self) -> str:
        return f"{self.name}"


class Person(abstract.AbstractBaseModel):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('-', 'Other'),
        ('X', 'Unknown'),
    )

    name = models.CharField(unique=True, max_length=64)
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


############################################

class Artifact(PolymorphicModel, abstract.AbstractBaseModel):

    title = models.CharField(unique=True, max_length=64, blank=True, null=True)
    subtitle = models.CharField(max_length=64, blank=True, null=True)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, blank=True, null=True)
    date_human = models.CharField(max_length=20, blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Legacy fields
    legacy_acquisition = models.CharField(max_length=128, blank=True, null=True)
    legacy_content = models.CharField(max_length=128, blank=True, null=True)
    legacy_inscription = models.CharField(max_length=128, blank=True, null=True)
    legacy_literature = models.CharField(max_length=64, blank=True, null=True)
    legacy_exhibitions = models.CharField(max_length=64, blank=True, null=True)
    legacy_reproductions = models.CharField(max_length=64, blank=True, null=True)
    legacy_bundle = models.CharField(max_length=32, blank=True, null=True)
    legacy_bundle_order = models.IntegerField(blank=True, null=True)
    legacy_bundle_side = models.CharField(max_length=32, blank=True, null=True)

    materials = models.ManyToManyField(Material, blank=True)
    places = models.ManyToManyField(Place, blank=True)
    persons = models.ManyToManyField(Person, blank=True)


    def __str__(self) -> str:
        if self.subtitle:
            return f"{self.title}: {self.subtitle}"
        else:
            return f"{self.title}"

    def __repr__(self) -> str:
        return str(self)

############################################

class Collection(abstract.AbstractBaseModel):

    title = models.CharField(unique=True, max_length=64, blank=True, null=True)
    subtitle = models.CharField(max_length=64, blank=True, null=True)
    objects = models.ManyToManyField(Artifact)

    def __str__(self) -> str:
        if self.subtitle:
            return f"{self.title}: {self.subtitle}"
        else:
            return f"{self.title}"

    def __repr__(self) -> str:
        return str(self)

class Artwork(Artifact):

    creator = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)

class Photograph(Artifact):

    creator = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    subcategories = models.ManyToManyField(PhotographSubcategory, blank=True)


class Letter(Artifact):    

    sender          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sender", blank=True, null=True)
    recipient       = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receiver", blank=True, null=True)
    transcription   = models.TextField(blank=True, null=True)
    subcategories   = models.ManyToManyField(LetterSubcategory, blank=True)


class Document(Artifact):

    categories = models.ForeignKey(DocumentCategory, null=True, blank=True, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(DocumentSubcategory, blank=True)


class Relic(Artifact):

    subcategories = models.ManyToManyField(RelicSubcategory, blank=True)

class Image(abstract.AbstractTIFFImageModel):

    SIDE_CHOICES = (
        ('F', 'Front'),
        ('B', 'Back'),
        ('C', 'Colour target')
    )

    # An image is associated with only one object
    artifact  = models.ForeignKey(Artifact, on_delete=models.CASCADE)

    # An optional title
    title = models.CharField(max_length=64, blank=True, null=True)
    motif   = models.TextField(default="", blank=True, null=True)

    # Image properties
    inner_width     = models.IntegerField(blank=True, null=True)
    inner_height    = models.IntegerField(blank=True, null=True)
    outer_width     = models.IntegerField(blank=True, null=True)
    outer_height    = models.IntegerField(blank=True, null=True)

    tags = models.ManyToManyField(ImageContent, related_name="images", blank=True)

    page = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], default=1)
    side = models.CharField(max_length=1, choices=SIDE_CHOICES, default=SIDE_CHOICES[0])



################################################

