from django.utils.translation import gettext_lazy as _
from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Policy(models.Model):
    class Meta:
        verbose_name_plural = "policies"
    class Types(models.TextChoices):
        SIGNATURE = 'sgn', _('Signature')
        WHITEFILE = 'wls', _('Whitelist')
        BLACKFILE = 'bls', _('Blacklist')
        CONTROL   = 'cgr', _('Control group')
    categories = models.ManyToManyField(Category, blank=True)
    signature = models.OneToOneField(
        'Signature',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
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
    def __str__(self):
        return '.'.join([str(i) for i in ['Sprinthost', self.issue, self.type, self.name] if i])

class File(models.Model):
    class Types(models.TextChoices):
        MALWARE = 'mlw', _('Malware file')
        LEGITIMATE = 'lgt', _('Legitimate file')
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    hash = models.CharField(max_length=128)
    file = models.FileField(upload_to='infected')

class Signature(models.Model):
    options = models.ManyToManyField('Option')
    subsigns = models.ManyToManyField('SubSign')
    logic = models.CharField(
        max_length=128,
        default='1')
    @property
    def prefix(self):
        try:
            return str(self.policy)
        except:
            return 'FREE'
    @property
    def optstring(self):
        return ','.join([f'{opt.get_key_display()}:{opt.value}' for opt in self.options.all()])
    @property
    def value(self):
        return ';'.join([subsign.value for subsign in self.subsigns.all()])

    def __str__(self):
        return f'{self.prefix};{self.optstring};{self.logic};{self.value}'
    

class SubSign(models.Model):
    class SubTypes(models.TextChoices):
        REGEXP    = 'REG', _('Regular expression')
        HEXSTRING = 'HEX', _('Hex string')
    type = models.CharField(
        max_length = 3,
        choices = SubTypes.choices,
        default = SubTypes.HEXSTRING,
    )
    value = models.CharField(max_length=1024, default='3c3f706870')
    
    def __str__(self):
        return f'{self.type} :: {self.value}'

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
        default = Keywords.ENGINE,
    )
    value = models.CharField(max_length=128, default='81-255')
    def __str__(self):
        return f'{self.get_key_display()}:{self.value}'
