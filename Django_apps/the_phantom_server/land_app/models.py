from django.contrib.gis.db import models
from django_descope.models import DescopeUser


class LeaseholdTr(models.Model):
    gid = models.AutoField(primary_key=True)
    tr_no = models.CharField(max_length=254, blank=True, null=True)
    tr_gma = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nma_term = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tr_lse = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kj_nri_eff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    first_exp = models.DateField(blank=True, null=True)
    nma_hbp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_id = models.CharField(max_length=254, blank=True, null=True)
    unit = models.CharField(max_length=254, blank=True, null=True)
    unit_trno = models.CharField(max_length=254, blank=True, null=True)
    kj_nma = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kj_trm = models.CharField(max_length=254, blank=True, null=True)
    geometry = models.GeometryField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'leasehold_tr'


class LeaseholdUnit(models.Model):
    gid = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=254, blank=True, null=True)
    unit_no = models.CharField(max_length=254, blank=True, null=True)
    un_gma = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nma_term = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nma_hbp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    comment = models.CharField(max_length=254, blank=True, null=True)
    geometry = models.GeometryField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'leasehold_unit'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class TermAoi(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    desc = models.CharField(max_length=80, blank=True, null=True)
    geometry = models.GeometryField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'term_aoi'

# Create your models here.

# class store_zip_file(models.Model):
#     user = models.ForeignKey(DescopeUser, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True)
#     file_id= models.CharField(max_length=255, null=True, blank=True)
#     file_name = models.CharField(max_length=255, null=True, blank=True)
#     is_process = models.BooleanField(default=False)
#     is_complete = models.BooleanField(default=False)
#     process_at = models.DateTimeField(null=True, blank=True)
#     completed_at = models.DateTimeField(null=True, blank=True)
    
#     class Meta:
#         managed = True
#         db_table = 'store_zip_file'

