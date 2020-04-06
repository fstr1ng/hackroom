from django.utils.translation import gettext_lazy as _
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Policy(models.Model):
    class Types(models.TextChoices):
        SIGNATURE = 'SIG', _('Signature')
        WHITEFILE = 'WLS', _('Whitelist')
        BLACKFILE = 'BLS', _('Blacklist')
        CONTROL   = 'CGR', _('Control group')
    categories = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=128)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    issue = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    example = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    type = models.CharField(
        max_length = 3,
        choices = Types.choices,
        default = Types.SIGNATURE
    )
    
    @property
    def full_name(self):
        return f'{self.type}.{self.issue}.{self.name}'
    def __str__(self):
        return self.full_name

class File(models.Model):
    class Types(models.TextChoices):
        MALWARE = 'MLW', _('Malware file')
        LEGITIMATE = 'LGT', _('Legitimate file')
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    hash = models.CharField(max_length=128)
    file = models.FileField(upload_to='infected')

class Signature(models.Model):
    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'SIG'},
        null=True,
        blank=True)
    options = models.ManyToManyField('Option')
    subsigns = models.ManyToManyField('SubSign')
    logic = models.CharField(
        max_length=128,
        default='0')

class SubSign(models.Model):
    class SubTypes(models.TextChoices):
        REGEXP    = 'REG', _('Regular expression')
        HEXSTRING = 'HEX', _('Hex string')
    type = models.CharField(
        max_length = 3,
        choices = SubTypes.choices,
        default = SubTypes.HEXSTRING,
    )
    value = models.CharField(max_length=1024)
    size = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return f'{self.type} :: {self.value}'

    def order(self):
        pass # check subsig's order in relater signature

class Option(models.Model):
    class Keywords(models.TextChoices):
        TARGET = 'TGT', _('Target')
        ENGINE = 'ENG', _('Engine')
        FILESIZE = 'FSZ', _('FileSize')
        ENTRY = 'ENT', _('EntryPoint')
        SECTIONS = 'SEC', _('NumberOfSections')
        CONTAINER = 'CON', _('Container')
        INTERMEDIATES = 'INT', _('Intermediates')
        
    key = models.CharField(
        max_length = 3,
        choices = Keywords.choices,
        default = Keywords.TARGET,
    )
    value = models.CharField(max_length=128, default='0')
    def __str__(self):
        return f'{self.get_key_display()}:{self.value}'
