# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Locations(models.Model):
    wellsiteid = models.BigIntegerField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    gatheringsiteid = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    userdata4 = models.TextField(blank=True, null=True)
    pumpstatus = models.TextField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    api = models.TextField(blank=True, null=True)
    propnum = models.TextField(blank=True, null=True)
    cygnetoverride = models.FloatField(blank=True, null=True)
    finaldate = models.DateTimeField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    gasalert = models.TextField(blank=True, null=True)
    maint = models.CharField(max_length=10, blank=True, null=True)
    pstatic_alarm = models.IntegerField(blank=True, null=True)
    pstatic_alarm_string = models.TextField(blank=True, null=True)
    rgas_alarm = models.IntegerField(blank=True, null=True)
    rgas_alarm_string = models.TextField(blank=True, null=True)
    facilityid = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'locations'

class Ptsmeterpt(models.Model):
    meterptid = models.BigIntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    wellsiteid = models.BigIntegerField(blank=True, null=True)
    gatheringsiteid = models.BigIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    productid = models.BigIntegerField(blank=True, null=True)
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    purchaserid = models.BigIntegerField(blank=True, null=True)
    purchasermeternum = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    chemicaldata = models.BooleanField(blank=True, null=True)
    fdstatus = models.BigIntegerField(blank=True, null=True)
    dataflag = models.BooleanField(blank=True, null=True)
    linesize = models.BigIntegerField(blank=True, null=True)
    wetdrybtuflag = models.BooleanField(blank=True, null=True)
    temperaturebase = models.BigIntegerField(blank=True, null=True)
    pressurebase = models.BigIntegerField(blank=True, null=True)
    pressurediff = models.BigIntegerField(blank=True, null=True)
    staticpressurerange = models.BigIntegerField(blank=True, null=True)
    serialnumber = models.TextField(blank=True, null=True)
    metertype = models.BigIntegerField(blank=True, null=True)
    metersize = models.BigIntegerField(blank=True, null=True)
    referencenumber = models.TextField(blank=True, null=True)
    userdata0 = models.TextField(blank=True, null=True)
    userdata1 = models.TextField(blank=True, null=True)
    userdata2 = models.TextField(blank=True, null=True)
    userdata3 = models.TextField(blank=True, null=True)
    userdata4 = models.TextField(blank=True, null=True)
    userdata5 = models.TextField(blank=True, null=True)
    userdata6 = models.TextField(blank=True, null=True)
    userdata7 = models.TextField(blank=True, null=True)
    userdata8 = models.TextField(blank=True, null=True)
    userdata9 = models.TextField(blank=True, null=True)
    userdata10 = models.TextField(blank=True, null=True)
    userdata11 = models.TextField(blank=True, null=True)
    userdata12 = models.TextField(blank=True, null=True)
    userdata13 = models.TextField(blank=True, null=True)
    userdata14 = models.TextField(blank=True, null=True)
    userdata15 = models.TextField(blank=True, null=True)
    userdata16 = models.TextField(blank=True, null=True)
    userdata17 = models.TextField(blank=True, null=True)
    userdata18 = models.TextField(blank=True, null=True)
    userdata19 = models.TextField(blank=True, null=True)
    metermetalid = models.BigIntegerField(blank=True, null=True)
    orificemetalid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ptsmeterpt'

class Ptsproductionpt(models.Model):
    productionptid = models.BigIntegerField(db_column='ProductionPtID', primary_key=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    wellsiteid = models.BigIntegerField(db_column='WellSiteID', blank=True, null=True)
    propertyid = models.BigIntegerField(db_column='PropertyID', blank=True, null=True)
    api = models.TextField(db_column='API', blank=True, null=True)
    primaryproductid = models.BigIntegerField(db_column='PrimaryProductID', blank=True, null=True)
    status = models.BigIntegerField(db_column='Status', blank=True, null=True)
    formationname = models.TextField(db_column='FormationName', blank=True, null=True)
    reservoirname = models.TextField(db_column='ReservoirName', blank=True, null=True)
    fieldname = models.TextField(db_column='FieldName', blank=True, null=True)
    topperf = models.BigIntegerField(db_column='TopPerf', blank=True, null=True)
    bottomperf = models.BigIntegerField(db_column='BottomPerf', blank=True, null=True)
    shotsperfoot = models.BigIntegerField(db_column='ShotsPerFoot', blank=True, null=True)
    producingmethodcode = models.BigIntegerField(db_column='ProducingMethodCode', blank=True, null=True)
    workingint = models.FloatField(db_column='WorkingInt', blank=True, null=True)
    netrevoilint = models.FloatField(db_column='NetRevOilInt', blank=True, null=True)
    netrevgasint = models.FloatField(db_column='NetRevGasInt', blank=True, null=True)
    allowableoil = models.BigIntegerField(db_column='AllowableOil', blank=True, null=True)
    allowablewater = models.BigIntegerField(db_column='AllowableWater', blank=True, null=True)
    allowablegas = models.BigIntegerField(db_column='AllowableGas', blank=True, null=True)
    startdate = models.TextField(db_column='StartDate', blank=True, null=True)
    enddate = models.TextField(db_column='EndDate', blank=True, null=True)
    firstproddate = models.TextField(db_column='FirstProdDate', blank=True, null=True)
    lastproddate = models.TextField(db_column='LastProdDate', blank=True, null=True)
    liquidgatherername = models.TextField(db_column='LiquidGathererName', blank=True, null=True)
    gasgatherername = models.TextField(db_column='GasGathererName', blank=True, null=True)
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)
    userdata0 = models.TextField(db_column='UserData0', blank=True, null=True,unique=True)
    userdata1 = models.TextField(db_column='UserData1', blank=True, null=True)
    userdata2 = models.TextField(db_column='UserData2', blank=True, null=True)
    userdata3 = models.TextField(db_column='UserData3', blank=True, null=True)
    userdata4 = models.TextField(db_column='UserData4', blank=True, null=True)
    userdata5 = models.TextField(db_column='UserData5', blank=True, null=True)
    userdata6 = models.TextField(db_column='UserData6', blank=True, null=True)
    userdata7 = models.TextField(db_column='UserData7', blank=True, null=True)
    userdata8 = models.TextField(db_column='UserData8', blank=True, null=True)
    userdata9 = models.TextField(db_column='UserData9', blank=True, null=True)
    userdata10 = models.TextField(db_column='UserData10', blank=True, null=True)
    userdata11 = models.TextField(db_column='UserData11', blank=True, null=True)
    userdata12 = models.TextField(db_column='UserData12', blank=True, null=True)
    userdata13 = models.TextField(db_column='UserData13', blank=True, null=True)
    userdata14 = models.TextField(db_column='UserData14', blank=True, null=True)
    userdata15 = models.TextField(db_column='UserData15', blank=True, null=True)
    userdata16 = models.TextField(db_column='UserData16', blank=True, null=True)
    userdata17 = models.TextField(db_column='UserData17', blank=True, null=True)
    userdata18 = models.TextField(db_column='UserData18', blank=True, null=True)
    userdata19 = models.TextField(db_column='UserData19', blank=True, null=True)
    chemicaldata = models.BooleanField(db_column='ChemicalData', blank=True, null=True)
    fdstatus = models.BigIntegerField(db_column='fdStatus', blank=True, null=True)
    dataflag = models.BooleanField(db_column='DataFlag', blank=True, null=True)
    stamp = models.DateTimeField(db_column='Stamp', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)
    createdate = models.TextField(db_column='CreateDate', blank=True, null=True)
    county = models.CharField(max_length=50, db_column='County', blank=True, null=True)
    dripalloc = models.CharField(max_length=50, db_column='DripAlloc', blank=True, null=True)
    dripalloc2 = models.CharField(max_length=50, db_column='DripAlloc2', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ptsproductionpt'



class Alerts(models.Model):
    alertid = models.BigAutoField(primary_key=True)
    category = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    docdate = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    notify = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'alerts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING,null=True)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING,null=True)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING,null=True)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING,null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING,null=True)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)





class Btu(models.Model):
    id = models.AutoField(primary_key=True)
    productionptid = models.BigIntegerField()
    btu = models.DecimalField(max_digits=28, decimal_places=5)
    effectivedate = models.DateField(blank=True, null=True)
    expireddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'btu'


class Chemical(models.Model):
    chemicalid = models.AutoField(primary_key=True)
    chemicalname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'chemical'


class Compressors(models.Model):
    id = models.AutoField(primary_key=True)
    compressorid = models.BigIntegerField(blank=True, null=True)
    entityid = models.BigIntegerField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compressors'


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    route = models.CharField(max_length=50, blank=True, null=True)
    carrierid = models.IntegerField(blank=True, null=True)
    production = models.IntegerField()
    afe = models.IntegerField()
    drilling = models.IntegerField()
    completion = models.IntegerField()
    dcdailyreport = models.IntegerField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    activestatus = models.IntegerField()
    approverid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contacts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Doccompressors(models.Model):
    docidcompressors = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    compressorid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField(blank=True, null=True)
    suctionpressure = models.FloatField(blank=True, null=True)
    suctiontemperature = models.FloatField(blank=True, null=True)
    dischargepressure = models.FloatField(blank=True, null=True)
    dischargetemperature = models.FloatField(blank=True, null=True)
    rpm = models.FloatField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    ambienttemp = models.FloatField(blank=True, null=True)
    interstage1press = models.FloatField(blank=True, null=True)
    interstage2press = models.FloatField(blank=True, null=True)
    interstage3press = models.FloatField(blank=True, null=True)
    interstage4press = models.FloatField(blank=True, null=True)
    interstage1temp = models.FloatField(blank=True, null=True)
    interstage2temp = models.FloatField(blank=True, null=True)
    interstage3temp = models.FloatField(blank=True, null=True)
    interstage4temp = models.FloatField(blank=True, null=True)
    oilpressure = models.FloatField(blank=True, null=True)
    oiltemp = models.FloatField(blank=True, null=True)
    watertemp = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    entityid = models.BigIntegerField(blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'doccompressors'


class Docdowntime(models.Model):
    dociddowntime = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    entityid = models.IntegerField(blank=True, null=True)
    entitytypeid = models.SmallIntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    hrsdown = models.FloatField(blank=True, null=True)
    downtimecode = models.SmallIntegerField(blank=True, null=True)
    oildown = models.BooleanField(blank=True, null=True)
    gasdown = models.BooleanField(blank=True, null=True)
    waterdown = models.BooleanField(blank=True, null=True)
    stamp = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docdowntime'


class Docfluidlevels(models.Model):
    docidfluidlevels = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    productionptid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    pumpdepth = models.FloatField(blank=True, null=True)
    fluidlevel = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docfluidlevels'


class Docgasdispositions(models.Model):
    docidgasdispositions = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    meterptid = models.ForeignKey(Ptsmeterpt,on_delete=models.CASCADE)
    docdate = models.DateTimeField()
    differential = models.FloatField(blank=True, null=True)
    static = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    reasoncode = models.SmallIntegerField(blank=True, null=True)
    startreading = models.FloatField(blank=True, null=True)
    endreading = models.FloatField(blank=True, null=True)
    meterfactor = models.FloatField(blank=True, null=True)
    purchaserid = models.SmallIntegerField(blank=True, null=True)
    transporterid = models.SmallIntegerField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docgasdispositions'


class Docgasmeterreadings(models.Model):
    docidgasmeterreadings = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    meterptid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    differential = models.FloatField(blank=True, null=True)
    static = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    avgtemp = models.FloatField(blank=True, null=True)
    mintemp = models.FloatField(blank=True, null=True)
    maxtemp = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    flowhours = models.FloatField(blank=True, null=True)
    linepressure = models.FloatField(blank=True, null=True)
    avglinepress = models.FloatField(blank=True, null=True)
    minlinepress = models.FloatField(blank=True, null=True)
    maxlinepress = models.FloatField(blank=True, null=True)
    startreading = models.FloatField(blank=True, null=True)
    endreading = models.FloatField(blank=True, null=True)
    meterfactor = models.FloatField(blank=True, null=True)
    orificesize = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.FloatField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    propertyid = models.FloatField(blank=True, null=True)
    wellsiteid = models.FloatField(blank=True, null=True)
    gatheringsiteid = models.FloatField(blank=True, null=True)
    chemical_inventory = models.TextField(blank=True, null=True)
    chemical_delivery = models.TextField(blank=True, null=True)
    maintanance_item = models.TextField(blank=True, null=True)
    location_notes = models.TextField(blank=True, null=True)
    pdiff = models.FloatField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    new = models.FloatField(blank=True, null=True)
    datasource = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docgasmeterreadings'


class Docinjectionreports(models.Model):
    docidinjectionreports = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    injectionptid = models.IntegerField(blank=True, null=True)
    meterptid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    productid = models.SmallIntegerField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    wellheadpressure = models.FloatField(blank=True, null=True)
    casingpressure = models.FloatField(blank=True, null=True)
    injectiontime = models.FloatField(blank=True, null=True)
    startreading = models.FloatField(blank=True, null=True)
    endreading = models.FloatField(blank=True, null=True)
    meterfactor = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    wellsiteid = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docinjectionreports'


class Doclacttickets(models.Model):
    docidlacttickets = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    meterptid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    meterstart = models.FloatField(blank=True, null=True)
    meterend = models.FloatField(blank=True, null=True)
    ticketnum = models.CharField(max_length=50, blank=True, null=True)
    transporterid = models.SmallIntegerField(blank=True, null=True)
    purchaserid = models.IntegerField(blank=True, null=True)
    gravity = models.FloatField(blank=True, null=True)
    onseal = models.CharField(max_length=50, blank=True, null=True)
    offseal = models.CharField(max_length=50, blank=True, null=True)
    starttemp = models.FloatField(blank=True, null=True)
    endtemp = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    bsw = models.FloatField(blank=True, null=True)
    meterfactor = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    netsalesvolume = models.FloatField(blank=True, null=True)
    correctedgravity = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'doclacttickets'


class Docliquidtransfer(models.Model):
    docidliquidtransfer = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    tankfromid = models.IntegerField(blank=True, null=True)
    tanktoid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    reasoncode = models.SmallIntegerField(blank=True, null=True)
    tankfrom_startlevel = models.FloatField(blank=True, null=True)
    tankfrom_endlevel = models.FloatField(blank=True, null=True)
    tankto_startlevel = models.FloatField(blank=True, null=True)
    tankto_endlevel = models.FloatField(blank=True, null=True)
    productid = models.SmallIntegerField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docliquidtransfer'


class Docoildispositions(models.Model):
    docidoildispositions = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    tankid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    volume = models.FloatField(blank=True, null=True)
    reasoncode = models.SmallIntegerField(blank=True, null=True)
    startlevel = models.FloatField(blank=True, null=True)
    endlevel = models.FloatField(blank=True, null=True)
    onseal = models.CharField(max_length=50, blank=True, null=True)
    offseal = models.CharField(max_length=50, blank=True, null=True)
    valvetype = models.CharField(max_length=50, blank=True, null=True)
    valvetypeid = models.SmallIntegerField(blank=True, null=True)
    purchaserid = models.SmallIntegerField(blank=True, null=True)
    transporterid = models.SmallIntegerField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docoildispositions'


class Docplungerlift(models.Model):
    docidplungerlift = models.IntegerField(primary_key=True)
    plungerliftid = models.IntegerField(blank=True, null=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    docdate = models.DateTimeField(blank=True, null=True)
    initcasingpress = models.FloatField(blank=True, null=True)
    finalcasingpress = models.FloatField(blank=True, null=True)
    initflowpress = models.FloatField(blank=True, null=True)
    finalflowpress = models.FloatField(blank=True, null=True)
    initshutinpress = models.FloatField(blank=True, null=True)
    finalshutinpress = models.FloatField(blank=True, null=True)
    shutintubingpress = models.FloatField(blank=True, null=True)
    shutincasingpress = models.FloatField(blank=True, null=True)
    shutintime = models.FloatField(blank=True, null=True)
    venttime = models.FloatField(blank=True, null=True)
    flowtime = models.FloatField(blank=True, null=True)
    afterflowtime = models.FloatField(blank=True, null=True)
    plungertraveltime = models.FloatField(blank=True, null=True)
    cycles = models.FloatField(blank=True, null=True)
    arrivals = models.FloatField(blank=True, null=True)
    ventgas = models.FloatField(blank=True, null=True)
    delay = models.FloatField(blank=True, null=True)
    daysinhole = models.IntegerField(blank=True, null=True)
    inspected = models.BooleanField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    plungersize = models.FloatField(blank=True, null=True)
    plungertypeid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docplungerlift'


class Docpumpingunits(models.Model):
    docidpumpingunits = models.IntegerField(primary_key=True)
    pumpingunitid = models.IntegerField(blank=True, null=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    docdate = models.DateTimeField(blank=True, null=True)
    strokespeed = models.FloatField(blank=True, null=True)
    strokelength = models.FloatField(blank=True, null=True)
    cycleontime = models.FloatField(blank=True, null=True)
    cycleofftime = models.FloatField(blank=True, null=True)
    cyclepumptime = models.FloatField(blank=True, null=True)
    maxrodstress = models.IntegerField(blank=True, null=True)
    minrodstress = models.IntegerField(blank=True, null=True)
    pumpinguniteff = models.FloatField(blank=True, null=True)
    theoreticaloutput = models.FloatField(blank=True, null=True)
    pumpdowntime = models.FloatField(blank=True, null=True)
    pumpoffflag = models.BooleanField(blank=True, null=True)
    pumpstatusflag = models.BooleanField(blank=True, null=True)
    pumpcard1 = models.CharField(max_length=1, blank=True, null=True)
    pumpcard2 = models.CharField(max_length=1, blank=True, null=True)
    quality = models.CharField(max_length=1, blank=True, null=True)
    pumpintakepressure = models.FloatField(blank=True, null=True)
    pumpfillage = models.FloatField(blank=True, null=True)
    netstrokelength = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docpumpingunits'


class Docruntickets(models.Model):
    docidruntickets = models.BigIntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    tankid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField(blank=True, null=True)
    upinches = models.FloatField(blank=True, null=True)
    lowinches = models.FloatField(blank=True, null=True)
    ticketnum = models.CharField(max_length=50, blank=True, null=True)
    gravity = models.FloatField(blank=True, null=True)
    onseal = models.CharField(max_length=50, blank=True, null=True)
    offseal = models.CharField(max_length=50, blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    uptemp = models.FloatField(blank=True, null=True)
    lowtemp = models.FloatField(blank=True, null=True)
    bsw = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    grcorrsalesvol = models.FloatField(blank=True, null=True)
    netsalesvol = models.FloatField(blank=True, null=True)
    gropenvol = models.FloatField(blank=True, null=True)
    grclosevol = models.FloatField(blank=True, null=True)
    grcorropenvol = models.FloatField(blank=True, null=True)
    grcorrclosevol = models.FloatField(blank=True, null=True)
    bswvolume = models.FloatField(blank=True, null=True)
    rvpfactor = models.FloatField(blank=True, null=True)
    correctedgravity = models.FloatField(blank=True, null=True)
    incrustfactor = models.FloatField(blank=True, null=True)
    purchaserid = models.TextField(blank=True, null=True)
    transporterid = models.FloatField(blank=True, null=True)
    trucknumber = models.CharField(max_length=50, blank=True, null=True)
    valvetypeid = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.FloatField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    inchfactor = models.FloatField(blank=True, null=True)
    gatheringsiteid = models.BigIntegerField(blank=True, null=True)
    wellsiteid = models.BigIntegerField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    tankname = models.TextField(blank=True, null=True)
    tanknumber = models.TextField(blank=True, null=True)
    start_ft = models.FloatField(blank=True, null=True)
    start_inch = models.FloatField(blank=True, null=True)
    start_qtr = models.FloatField(blank=True, null=True)
    end_ft = models.FloatField(blank=True, null=True)
    end_inch = models.FloatField(blank=True, null=True)
    end_qtr = models.FloatField(blank=True, null=True)
    new = models.FloatField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docruntickets'


class Doctankgauges(models.Model):
    docidtankgauges = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=4, blank=True, null=True)
    tankid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    productid = models.SmallIntegerField(blank=True, null=True)
    inches = models.FloatField(blank=True, null=True)
    inches_initial = models.FloatField(blank=True, null=True)
    inches_mid = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_initial = models.FloatField(blank=True, null=True)
    volume_mid = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    bsw = models.FloatField(blank=True, null=True)
    gravity = models.FloatField(blank=True, null=True)
    esttankfull = models.DateTimeField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    gatheringsiteid = models.IntegerField(blank=True, null=True)
    wellsiteid = models.IntegerField(blank=True, null=True)
    inchfactor = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    tankname = models.TextField(blank=True, null=True)
    tanknumber = models.TextField(blank=True, null=True)
    start_ft = models.FloatField(blank=True, null=True)
    start_inch = models.FloatField(blank=True, null=True)
    start_qtr = models.FloatField(blank=True, null=True)
    end_ft = models.FloatField(blank=True, null=True)
    end_inch = models.FloatField(blank=True, null=True)
    end_qtr = models.FloatField(blank=True, null=True)
    product_number = models.FloatField(blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    waterdispbbl = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'doctankgauges'


class Docwaterdisposition(models.Model):
    docidwaterdisposition = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    tankid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    volume = models.FloatField(blank=True, null=True)
    reasoncode = models.SmallIntegerField(blank=True, null=True)
    startlevel = models.FloatField(blank=True, null=True)
    endlevel = models.FloatField(blank=True, null=True)
    onseal = models.CharField(max_length=50, blank=True, null=True)
    offseal = models.CharField(max_length=50, blank=True, null=True)
    valvetypeid = models.SmallIntegerField(blank=True, null=True)
    disposalsiteid = models.SmallIntegerField(blank=True, null=True)
    transporterid = models.SmallIntegerField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docwaterdisposition'


class Docwellheadpressures(models.Model):
    docidwellheadpressures = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    productionptid = models.IntegerField(blank=True, null=True)
    docdate = models.DateTimeField()
    tubingpressure = models.FloatField(blank=True, null=True)
    avgtubingpress = models.FloatField(blank=True, null=True)
    mintubingpress = models.FloatField(blank=True, null=True)
    maxtubingpress = models.FloatField(blank=True, null=True)
    casingpressure = models.FloatField(blank=True, null=True)
    avgcasingpress = models.FloatField(blank=True, null=True)
    mincasingpress = models.FloatField(blank=True, null=True)
    maxcasingpress = models.FloatField(blank=True, null=True)
    chokesize = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.FloatField(blank=True, null=True)
    api = models.CharField(max_length=14, blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    wellsiteid = models.BigIntegerField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docwellheadpressures'


class Docwellstatus(models.Model):
    docidwellstatus = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    entityid = models.IntegerField(blank=True, null=True)
    entitytypeid = models.SmallIntegerField(blank=True, null=True)
    docdate = models.DateTimeField(blank=True, null=True)
    statusid = models.SmallIntegerField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docwellstatus'


class Docwelltests(models.Model):
    docidwelltests = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    docdate = models.DateTimeField()
    wellsiteid = models.IntegerField(blank=True, null=True)
    entityid = models.IntegerField(blank=True, null=True)
    entitytypeid = models.SmallIntegerField(blank=True, null=True)
    hourson = models.FloatField(blank=True, null=True)
    runtimeperc = models.FloatField(blank=True, null=True)
    chokesize = models.FloatField(blank=True, null=True)
    notforallocation = models.BooleanField(blank=True, null=True)
    testmethod = models.SmallIntegerField(blank=True, null=True)
    oil = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    water = models.FloatField(blank=True, null=True)
    shutintubingpressure = models.FloatField(blank=True, null=True)
    shutincasingpressure = models.FloatField(blank=True, null=True)
    flowingtubingpressure = models.FloatField(blank=True, null=True)
    flowingcasingpressure = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    inputbyid = models.CharField(max_length=50, blank=True, null=True)
    docsourcecode = models.SmallIntegerField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'docwelltests'


class Eqpcompressors(models.Model):
    compressorid = models.IntegerField(primary_key=True)
    entityid = models.IntegerField(blank=True, null=True)
    entitytypeid = models.SmallIntegerField(blank=True, null=True)
    pmentityid = models.IntegerField(blank=True, null=True)
    pmentitytypeid = models.SmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    leasingcompany = models.CharField(max_length=50, blank=True, null=True)
    serialnumber = models.CharField(max_length=50, blank=True, null=True)
    horsepower = models.IntegerField(blank=True, null=True)
    stages = models.SmallIntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    chemicaldata = models.BooleanField(blank=True, null=True)
    fdstatus = models.SmallIntegerField(blank=True, null=True)
    dataflag = models.BooleanField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    userdata0 = models.CharField(max_length=50, blank=True, null=True)
    userdata1 = models.CharField(max_length=50, blank=True, null=True)
    userdata2 = models.CharField(max_length=50, blank=True, null=True)
    userdata3 = models.CharField(max_length=50, blank=True, null=True)
    userdata4 = models.CharField(max_length=50, blank=True, null=True)
    userdata5 = models.CharField(max_length=50, blank=True, null=True)
    userdata6 = models.CharField(max_length=50, blank=True, null=True)
    userdata7 = models.CharField(max_length=50, blank=True, null=True)
    userdata8 = models.CharField(max_length=50, blank=True, null=True)
    userdata9 = models.CharField(max_length=50, blank=True, null=True)
    userdata10 = models.CharField(max_length=50, blank=True, null=True)
    userdata11 = models.CharField(max_length=50, blank=True, null=True)
    userdata12 = models.CharField(max_length=50, blank=True, null=True)
    userdata13 = models.CharField(max_length=50, blank=True, null=True)
    userdata14 = models.CharField(max_length=50, blank=True, null=True)
    userdata15 = models.CharField(max_length=50, blank=True, null=True)
    userdata16 = models.CharField(max_length=50, blank=True, null=True)
    userdata17 = models.CharField(max_length=50, blank=True, null=True)
    userdata18 = models.CharField(max_length=50, blank=True, null=True)
    userdata19 = models.CharField(max_length=50, blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'eqpcompressors'


class Eqpmeter(models.Model):
    compid = models.IntegerField(primary_key=True)
    linesize = models.FloatField(blank=True, null=True)
    orificediameter = models.FloatField(blank=True, null=True)
    orificefactor = models.FloatField(blank=True, null=True)
    specificgravity = models.FloatField(blank=True, null=True)
    temperaturebase = models.FloatField(blank=True, null=True)
    pressurediff = models.FloatField(blank=True, null=True)
    staticpressurerange = models.FloatField(blank=True, null=True)
    serialnumber = models.CharField(max_length=50, blank=True, null=True)
    metertype = models.SmallIntegerField(blank=True, null=True)
    referencenumber = models.CharField(max_length=50, blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'eqpmeter'


class Eqpplungerlift(models.Model):
    plungerliftid = models.IntegerField(primary_key=True)
    productionptid = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    controller = models.CharField(max_length=50, blank=True, null=True)
    controllermodel = models.CharField(max_length=50, blank=True, null=True)
    controllersn = models.CharField(max_length=50, blank=True, null=True)
    fdstatus = models.SmallIntegerField(blank=True, null=True)
    dataflag = models.BooleanField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'eqpplungerlift'


class Eqptank(models.Model):
    compid = models.BigIntegerField(primary_key=True)
    gatheringsiteid = models.BigIntegerField(blank=True, null=True)
    wellsiteid = models.BigIntegerField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    tanknumber = models.TextField(blank=True, null=True)
    tankname = models.TextField(blank=True, null=True)
    tankcapacity = models.BigIntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    diameter = models.BigIntegerField(blank=True, null=True)
    calculatedvol = models.FloatField(blank=True, null=True)
    tanktype = models.BigIntegerField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    manufacturersn = models.TextField(blank=True, null=True)
    productid = models.BigIntegerField(blank=True, null=True)
    secondproductid = models.BigIntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    fdstatus = models.BigIntegerField(blank=True, null=True)
    dataflag = models.BooleanField(blank=True, null=True)
    chemicaldata = models.BooleanField(blank=True, null=True)
    userdata0 = models.TextField(blank=True, null=True)
    userdata1 = models.TextField(blank=True, null=True)
    userdata2 = models.TextField(blank=True, null=True)
    userdata3 = models.TextField(blank=True, null=True)
    userdata4 = models.TextField(blank=True, null=True)
    userdata5 = models.TextField(blank=True, null=True)
    userdata6 = models.TextField(blank=True, null=True)
    userdata7 = models.TextField(blank=True, null=True)
    userdata8 = models.TextField(blank=True, null=True)
    userdata9 = models.TextField(blank=True, null=True)
    userdata10 = models.TextField(blank=True, null=True)
    userdata11 = models.TextField(blank=True, null=True)
    userdata12 = models.TextField(blank=True, null=True)
    userdata13 = models.TextField(blank=True, null=True)
    userdata14 = models.TextField(blank=True, null=True)
    userdata15 = models.TextField(blank=True, null=True)
    userdata16 = models.TextField(blank=True, null=True)
    userdata17 = models.TextField(blank=True, null=True)
    userdata18 = models.TextField(blank=True, null=True)
    userdata19 = models.TextField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    product_number = models.IntegerField(blank=True, null=True)
    cal_id = models.ForeignKey(Locations,on_delete=models.CASCADE)        #ForeignKey(Locations,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'eqptank'


class Eqptubing(models.Model):
    tubingid = models.IntegerField(primary_key=True)
    entityid = models.IntegerField(blank=True, null=True)
    entitytypeid = models.SmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    footage = models.FloatField(blank=True, null=True)
    tubingsize = models.FloatField(blank=True, null=True)
    tubingweight = models.FloatField(blank=True, null=True)
    tubinggrade = models.CharField(max_length=50, blank=True, null=True)
    tubingconnection = models.CharField(max_length=50, blank=True, null=True)
    fdstatus = models.SmallIntegerField(blank=True, null=True)
    dataflag = models.BooleanField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'eqptubing'


class FdSysgatheringsite(models.Model):
    gatheringsiteid = models.BigIntegerField(primary_key=True)
    sitename = models.TextField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    createdate = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    fdstatus = models.BigIntegerField(blank=True, null=True)
    userdata0 = models.TextField(blank=True, null=True)
    userdata1 = models.TextField(blank=True, null=True)
    userdata2 = models.TextField(blank=True, null=True)
    userdata3 = models.TextField(blank=True, null=True)
    userdata4 = models.TextField(blank=True, null=True)
    userdata5 = models.TextField(blank=True, null=True)
    userdata6 = models.TextField(blank=True, null=True)
    userdata7 = models.TextField(blank=True, null=True)
    userdata8 = models.TextField(blank=True, null=True)
    userdata9 = models.TextField(blank=True, null=True)
    userdata10 = models.TextField(blank=True, null=True)
    userdata11 = models.TextField(blank=True, null=True)
    userdata12 = models.TextField(blank=True, null=True)
    userdata13 = models.TextField(blank=True, null=True)
    userdata14 = models.TextField(blank=True, null=True)
    userdata15 = models.TextField(blank=True, null=True)
    userdata16 = models.TextField(blank=True, null=True)
    userdata17 = models.TextField(blank=True, null=True)
    userdata18 = models.TextField(blank=True, null=True)
    userdata19 = models.TextField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    pumperlat = models.FloatField(blank=True, null=True)
    pumperlong = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fd_sysgatheringsite'


class FdSysproperties(models.Model):
    propertyid = models.BigIntegerField(primary_key=True)
    propertyname = models.TextField(blank=True, null=True)
    admincorpid = models.BigIntegerField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    county = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    api = models.TextField(blank=True, null=True)
    checkedout = models.TextField(blank=True, null=True)
    userdata0 = models.TextField(blank=True, null=True)
    userdata1 = models.TextField(blank=True, null=True)
    userdata2 = models.TextField(blank=True, null=True)
    userdata3 = models.TextField(blank=True, null=True)
    userdata4 = models.TextField(blank=True, null=True)
    userdata5 = models.TextField(blank=True, null=True)
    userdata6 = models.TextField(blank=True, null=True)
    userdata7 = models.TextField(blank=True, null=True)
    userdata8 = models.TextField(blank=True, null=True)
    userdata9 = models.TextField(blank=True, null=True)
    userdata10 = models.TextField(blank=True, null=True)
    userdata11 = models.TextField(blank=True, null=True)
    userdata12 = models.TextField(blank=True, null=True)
    userdata13 = models.TextField(blank=True, null=True)
    userdata14 = models.TextField(blank=True, null=True)
    userdata15 = models.TextField(blank=True, null=True)
    userdata16 = models.TextField(blank=True, null=True)
    userdata17 = models.TextField(blank=True, null=True)
    userdata18 = models.TextField(blank=True, null=True)
    userdata19 = models.TextField(blank=True, null=True)
    fdstatus = models.BigIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fd_sysproperties'


class FdSyswellsite(models.Model):
    wellsiteid = models.IntegerField(primary_key=True)
    wellname = models.CharField(max_length=51, blank=True, null=True)
    operatorname = models.CharField(max_length=24, blank=True, null=True)
    propertyid = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    api = models.CharField(max_length=14, blank=True, null=True)
    totaldepth = models.IntegerField(blank=True, null=True)
    pbtotaldepth = models.IntegerField(blank=True, null=True)
    basincode = models.SmallIntegerField(blank=True, null=True)
    spuddate = models.DateTimeField(blank=True, null=True)
    finishdrilldate = models.DateTimeField(blank=True, null=True)
    completiondate = models.DateTimeField(blank=True, null=True)
    abandondate = models.DateTimeField(blank=True, null=True)
    texasrrdist = models.CharField(max_length=16, blank=True, null=True)
    surveynamesurface = models.CharField(max_length=60, blank=True, null=True)
    abstractnumbersurface = models.CharField(max_length=12, blank=True, null=True)
    blocksurface = models.CharField(max_length=6, blank=True, null=True)
    townshipsurface = models.CharField(max_length=4, blank=True, null=True)
    townshipdirsurface = models.CharField(max_length=12, blank=True, null=True)
    rangesurface = models.CharField(max_length=4, blank=True, null=True)
    rangedirsurface = models.CharField(max_length=12, blank=True, null=True)
    sectionsurface = models.CharField(max_length=6, blank=True, null=True)
    qqsurface = models.CharField(max_length=8, blank=True, null=True)
    nsdistsurface = models.CharField(max_length=7, blank=True, null=True)
    ewdistsurface = models.CharField(max_length=7, blank=True, null=True)
    nsdirsurface = models.CharField(max_length=4, blank=True, null=True)
    ewdirsurface = models.CharField(max_length=4, blank=True, null=True)
    offshorearea = models.CharField(max_length=29, blank=True, null=True)
    surveynamebh = models.CharField(max_length=60, blank=True, null=True)
    abstractnumberbh = models.CharField(max_length=12, blank=True, null=True)
    blockbh = models.CharField(max_length=6, blank=True, null=True)
    townshipbh = models.CharField(max_length=4, blank=True, null=True)
    townshipdirbh = models.CharField(max_length=12, blank=True, null=True)
    rangebh = models.CharField(max_length=4, blank=True, null=True)
    rangedirbh = models.CharField(max_length=12, blank=True, null=True)
    sectionbh = models.CharField(max_length=6, blank=True, null=True)
    qqbh = models.CharField(max_length=8, blank=True, null=True)
    nsdistbh = models.CharField(max_length=7, blank=True, null=True)
    ewdistbh = models.CharField(max_length=7, blank=True, null=True)
    nsdirbh = models.CharField(max_length=4, blank=True, null=True)
    ewdirbh = models.CharField(max_length=4, blank=True, null=True)
    elevationkb = models.SmallIntegerField(blank=True, null=True)
    elevationground = models.SmallIntegerField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    createdate = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitudebh = models.FloatField(blank=True, null=True)
    longitudebh = models.FloatField(blank=True, null=True)
    userdata0 = models.CharField(max_length=50, blank=True, null=True)
    userdata1 = models.CharField(max_length=50, blank=True, null=True)
    userdata2 = models.CharField(max_length=50, blank=True, null=True)
    userdata3 = models.CharField(max_length=50, blank=True, null=True)
    userdata4 = models.CharField(max_length=50, blank=True, null=True)
    userdata5 = models.CharField(max_length=50, blank=True, null=True)
    userdata6 = models.CharField(max_length=50, blank=True, null=True)
    userdata7 = models.CharField(max_length=50, blank=True, null=True)
    userdata8 = models.CharField(max_length=50, blank=True, null=True)
    userdata9 = models.CharField(max_length=50, blank=True, null=True)
    userdata10 = models.CharField(max_length=50, blank=True, null=True)
    userdata11 = models.CharField(max_length=50, blank=True, null=True)
    userdata12 = models.CharField(max_length=50, blank=True, null=True)
    userdata13 = models.CharField(max_length=50, blank=True, null=True)
    userdata14 = models.CharField(max_length=50, blank=True, null=True)
    userdata15 = models.CharField(max_length=50, blank=True, null=True)
    userdata16 = models.CharField(max_length=50, blank=True, null=True)
    userdata17 = models.CharField(max_length=50, blank=True, null=True)
    userdata18 = models.CharField(max_length=50, blank=True, null=True)
    userdata19 = models.CharField(max_length=50, blank=True, null=True)
    isswb = models.BooleanField(blank=True, null=True)
    fdstatus = models.SmallIntegerField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fd_syswellsite'


class Field(models.Model):
    fieldid = models.AutoField(primary_key=True)
    fieldname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'field'


class Gatheringrate(models.Model):
    productionptid = models.BigIntegerField()
    effectivedate = models.DateField()
    expireddate = models.DateField(blank=True, null=True)
    capitalmcfrate = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    operatingmcfrate = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    totalmcfrate = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gatheringrate'


class Ldgtank(models.Model):
    tankid = models.IntegerField(primary_key=True)  # The composite primary key (tankid, refdocid, refdoctype, productid) found, that is not supported. The first column is selected.
    ldgdate = models.DateTimeField()
    refdocid = models.IntegerField()
    refdoctype = models.SmallIntegerField()
    productid = models.SmallIntegerField()
    increase = models.FloatField(blank=True, null=True)
    decrease = models.FloatField(blank=True, null=True)
    currentvolume = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ldgtank'
        unique_together = (('tankid', 'refdocid', 'refdoctype', 'productid'),)


class Leaseholder(models.Model):
    id = models.BigIntegerField(primary_key=True)
    leaseholder_group = models.CharField(db_column='LEASEHOLDER GROUP', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wellsiteid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'leaseholder'


class Lifttype(models.Model):
    lifttypeid = models.AutoField(primary_key=True)
    lifttypename = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lifttype'





class Maintcapstring(models.Model):
    wellsiteid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'maintcapstring'


class Maintenance(models.Model):
    index = models.IntegerField(primary_key=True)
    description = models.TextField()
    interval = models.BigIntegerField(db_column='Interval')  # Field name made lowercase.
    cost = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    prodmin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maintenance'


class Mainthotoil(models.Model):
    wellsiteid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'mainthotoil'


class Measurement(models.Model):
    feet = models.IntegerField(blank=True, null=True)
    inches = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    number_1_4in = models.FloatField(db_column='1/4In', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = True
        db_table = 'measurement'


class Nextdate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nextpumpdate = models.DateTimeField(blank=True, null=True)
    capstring_maint = models.DateTimeField(db_column='Capstring Maint', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dump_valve = models.DateTimeField(db_column='Dump Valve', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_battery = models.DateTimeField(db_column='New Battery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plunger_lift = models.DateTimeField(db_column='Plunger Lift', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trido_pin = models.DateTimeField(db_column='Trido Pin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fulldate = models.DateTimeField(blank=True, null=True)
    loaddate = models.DateTimeField(blank=True, null=True)
    nextoildate = models.DateTimeField(blank=True, null=True)
    finaldate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nextdate'


class Ngl(models.Model):
    activitydate = models.DateField()
    metric = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = True
        db_table = 'ngl'

entityid = models.ForeignKey(Ptsproductionpt,db_column='entity', on_delete=models.CASCADE)
class OilLedger(models.Model):
    id = models.AutoField(primary_key=True)
    tankid = models.ForeignKey(Eqptank,on_delete=models.CASCADE)
    docdatedate = models.TextField(blank=True, null=True)
    rtvolume = models.FloatField(blank=True, null=True)
    oildisp = models.FloatField(blank=True, null=True)
    final_gauge = models.FloatField(blank=True, null=True)
    prior_gauge = models.FloatField(db_column='Prior Gauge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    production = models.FloatField(blank=True, null=True)
    dsource = models.TextField(blank=True, null=True)
    lastupdate = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'oil_ledger'


class Propertymaster(models.Model):
    propname = models.TextField(blank=True, null=True)
    dbskey = models.TextField(blank=True, null=True)
    propnum = models.TextField(blank=True, null=True)
    seqnum = models.BigIntegerField(blank=True, null=True)
    wellno = models.TextField(blank=True, null=True)
    welltype = models.TextField(blank=True, null=True)
    propcode = models.TextField(blank=True, null=True)
    opertype = models.TextField(blank=True, null=True)
    apinum = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    countyname = models.TextField(blank=True, null=True)
    fieldname = models.TextField(blank=True, null=True)
    prospect = models.TextField(blank=True, null=True)
    reservoir = models.TextField(blank=True, null=True)
    major = models.TextField(blank=True, null=True)
    resclass = models.TextField(blank=True, null=True)
    drill_yr = models.TextField(blank=True, null=True)
    opername = models.TextField(blank=True, null=True)
    pbtd = models.BigIntegerField(blank=True, null=True)
    spud = models.TextField(blank=True, null=True)
    proj_start_date = models.TextField(blank=True, null=True)
    first_prod = models.DateTimeField(blank=True, null=True)
    loc_misc = models.TextField(blank=True, null=True)
    loc_lat = models.TextField(blank=True, null=True)
    loc_long = models.TextField(blank=True, null=True)
    hole_direction = models.TextField(blank=True, null=True)
    tx_rrc_dis = models.TextField(blank=True, null=True)
    ihs_id = models.TextField(blank=True, null=True)
    di_code = models.TextField(blank=True, null=True)
    btu_fact = models.TextField(blank=True, null=True)
    de_min = models.BigIntegerField(blank=True, null=True)
    tax_adv = models.BigIntegerField(blank=True, null=True)
    no_frac_stages = models.BigIntegerField(blank=True, null=True)
    avg_frac_stage_len = models.BigIntegerField(blank=True, null=True)
    lateral_length = models.BigIntegerField(blank=True, null=True)
    corp03 = models.BigIntegerField(blank=True, null=True)
    payout = models.TextField(blank=True, null=True)
    adval_start = models.TextField(blank=True, null=True)
    trans_cost_date = models.TextField(blank=True, null=True)
    lpc_gas_diff = models.FloatField(blank=True, null=True)
    lpc_oil_diff = models.TextField(blank=True, null=True)
    lpc_ngl_diff = models.TextField(blank=True, null=True)
    lpc_ngl_yield = models.TextField(blank=True, null=True)
    rig_relse = models.TextField(blank=True, null=True)
    lpc_opcost = models.TextField(blank=True, null=True)
    lpc_insurance = models.BigIntegerField(blank=True, null=True)
    reworked_date = models.TextField(blank=True, null=True)
    enhanced_date = models.TextField(blank=True, null=True)
    lpc_trnsp = models.TextField(blank=True, null=True)
    lpc_opcwtr = models.TextField(blank=True, null=True)
    plugged_date = models.TextField(blank=True, null=True)
    loc_sec = models.TextField(blank=True, null=True)
    lpc_opcoil = models.BigIntegerField(blank=True, null=True)
    loc_town = models.TextField(blank=True, null=True)
    lpc_opcgas = models.FloatField(blank=True, null=True)
    loc_tn = models.TextField(blank=True, null=True)
    lpc_oh = models.BigIntegerField(blank=True, null=True)
    loc_tn_dir = models.TextField(blank=True, null=True)
    lpc_shrink = models.FloatField(blank=True, null=True)
    loc_range = models.TextField(blank=True, null=True)
    lpc_start_date = models.TextField(blank=True, null=True)
    loc_rn = models.TextField(blank=True, null=True)
    sev_table = models.TextField(blank=True, null=True)
    loc_rn_dir = models.TextField(blank=True, null=True)
    lpc_lease = models.TextField(blank=True, null=True)
    lpc_county = models.TextField(blank=True, null=True)
    lpc_field = models.TextField(blank=True, null=True)
    lpc_state = models.TextField(blank=True, null=True)
    loc_quad = models.TextField(blank=True, null=True)
    lpc_rsv_cat = models.TextField(blank=True, null=True)
    lpc_reservoir = models.TextField(blank=True, null=True)
    mapsqr_ns = models.TextField(blank=True, null=True)
    lpc_group1 = models.TextField(blank=True, null=True)
    mapsqr_ew = models.TextField(blank=True, null=True)
    pipeline = models.TextField(blank=True, null=True)
    prod_start_date = models.TextField(blank=True, null=True)
    gaspurch = models.TextField(blank=True, null=True)
    lpc_upr_perf = models.BigIntegerField(blank=True, null=True)
    lpc_lwr_perf = models.BigIntegerField(blank=True, null=True)
    oilpurch = models.TextField(blank=True, null=True)
    lpc_perf_length = models.BigIntegerField(blank=True, null=True)
    prior_gas = models.TextField(blank=True, null=True)
    lpc_peak_mo_oil = models.TextField(blank=True, null=True)
    prior_oil = models.TextField(blank=True, null=True)
    gas_cum_fr = models.TextField(blank=True, null=True)
    lpc_peak_mo_gas = models.BigIntegerField(blank=True, null=True)
    lpc_first_prod = models.DateTimeField(blank=True, null=True)
    oil_cum_fr = models.TextField(blank=True, null=True)
    lpcsur_lat = models.TextField(blank=True, null=True)
    meternum = models.TextField(blank=True, null=True)
    landlseno = models.TextField(blank=True, null=True)
    lpcsur_long = models.TextField(blank=True, null=True)
    lpcbhl_lat = models.TextField(blank=True, null=True)
    nra_acct_num = models.TextField(blank=True, null=True)
    land_book_acreage = models.TextField(blank=True, null=True)
    lpcbhl_long = models.TextField(blank=True, null=True)
    start_var = models.TextField(blank=True, null=True)
    final_var = models.TextField(blank=True, null=True)
    rrc_lease = models.TextField(blank=True, null=True)
    type5_rate = models.TextField(blank=True, null=True)
    type5_expire = models.DateField(blank=True, null=True)
    type11 = models.TextField(blank=True, null=True)
    work13 = models.TextField(blank=True, null=True)
    work14 = models.TextField(blank=True, null=True)
    work15 = models.TextField(blank=True, null=True)
    orri_int = models.TextField(blank=True, null=True)
    geology_id = models.TextField(blank=True, null=True)
    tltr = models.TextField(blank=True, null=True)
    payout_bal = models.FloatField(blank=True, null=True)
    prod_source = models.TextField(blank=True, null=True)
    prev_db = models.TextField(blank=True, null=True)
    prev_seqnum = models.TextField(blank=True, null=True)
    sort1 = models.TextField(blank=True, null=True)
    sort2 = models.TextField(blank=True, null=True)
    lease_acreage = models.TextField(blank=True, null=True)
    corpnet_div = models.TextField(blank=True, null=True)
    rsv_major = models.TextField(blank=True, null=True)
    rsv_sub = models.TextField(blank=True, null=True)
    rsv_stat = models.TextField(blank=True, null=True)
    cabot_maj = models.TextField(blank=True, null=True)
    cabot_sub = models.TextField(blank=True, null=True)
    recon_typ = models.TextField(blank=True, null=True)
    recon_cls = models.TextField(blank=True, null=True)
    cost_center = models.TextField(blank=True, null=True)
    bpo_wi = models.DecimalField(max_digits=9, decimal_places=8, blank=True, null=True)
    bpo_nri = models.DecimalField(max_digits=9, decimal_places=8, blank=True, null=True)
    apo_wi = models.DecimalField(max_digits=9, decimal_places=8, blank=True, null=True)
    apo_nri = models.DecimalField(max_digits=9, decimal_places=8, blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    swd = models.TextField(blank=True, null=True)
    swd_delivery = models.TextField(blank=True, null=True)
    salespoint = models.TextField(blank=True, null=True)
    tmd = models.BigIntegerField(blank=True, null=True)
    trackpayout = models.IntegerField(blank=True, null=True)
    payoutreached = models.IntegerField(blank=True, null=True)
    payout_act_dt = models.DateField(blank=True, null=True)
    payout_actg_dt = models.DateField(blank=True, null=True)
    gasunit = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'propertymaster'


class Ptsinjectionpt(models.Model):
    injectionptid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    wellsiteid = models.IntegerField()
    propertyid = models.IntegerField(blank=True, null=True)
    api = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    productid = models.SmallIntegerField(blank=True, null=True)
    topperf = models.IntegerField(blank=True, null=True)
    bottomperf = models.IntegerField(blank=True, null=True)
    shotsperfoot = models.SmallIntegerField(blank=True, null=True)
    formationname = models.CharField(max_length=20, blank=True, null=True)
    reservoirname = models.CharField(max_length=20, blank=True, null=True)
    fieldname = models.CharField(max_length=38, blank=True, null=True)
    workinginjint = models.FloatField(blank=True, null=True)
    netrevinjint = models.FloatField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    createdate = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    userdata0 = models.CharField(max_length=50, blank=True, null=True)
    userdata1 = models.CharField(max_length=50, blank=True, null=True)
    userdata2 = models.CharField(max_length=50, blank=True, null=True)
    userdata3 = models.CharField(max_length=50, blank=True, null=True)
    userdata4 = models.CharField(max_length=50, blank=True, null=True)
    userdata5 = models.CharField(max_length=50, blank=True, null=True)
    userdata6 = models.CharField(max_length=50, blank=True, null=True)
    userdata7 = models.CharField(max_length=50, blank=True, null=True)
    userdata8 = models.CharField(max_length=50, blank=True, null=True)
    userdata9 = models.CharField(max_length=50, blank=True, null=True)
    userdata10 = models.CharField(max_length=50, blank=True, null=True)
    userdata11 = models.CharField(max_length=50, blank=True, null=True)
    userdata12 = models.CharField(max_length=50, blank=True, null=True)
    userdata13 = models.CharField(max_length=50, blank=True, null=True)
    userdata14 = models.CharField(max_length=50, blank=True, null=True)
    userdata15 = models.CharField(max_length=50, blank=True, null=True)
    userdata16 = models.CharField(max_length=50, blank=True, null=True)
    userdata17 = models.CharField(max_length=50, blank=True, null=True)
    userdata18 = models.CharField(max_length=50, blank=True, null=True)
    userdata19 = models.CharField(max_length=50, blank=True, null=True)
    chemicaldata = models.BooleanField(blank=True, null=True)
    fdstatus = models.SmallIntegerField(blank=True, null=True)
    dataflag = models.BooleanField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ptsinjectionpt'





class RealTimeData(models.Model):
    location_name = models.TextField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    meter_pt_id = models.BigIntegerField(blank=True, null=True)
    cynget_id = models.TextField(blank=True, null=True)
    plc_type = models.TextField(blank=True, null=True)
    inch_factor = models.FloatField(blank=True, null=True)
    total_water = models.FloatField(blank=True, null=True)
    acc_total_water = models.FloatField(blank=True, null=True)
    water_flow_rate = models.FloatField(blank=True, null=True)
    vol_td_bbl = models.FloatField(blank=True, null=True)
    vol_y_bbl = models.FloatField(blank=True, null=True)
    well_name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    static = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    gas_flow_rate = models.FloatField(blank=True, null=True)
    vol_td_mcf = models.FloatField(blank=True, null=True)
    vol_y_mcf = models.FloatField(blank=True, null=True)
    to_sql = models.FloatField(blank=True, null=True)
    vol_td_mbtu = models.FloatField(blank=True, null=True)
    vol_y_mbtu = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)
    current_volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'real_time_data'

class ResEconomicInputs(models.Model):
    id = models.AutoField(primary_key=True)
    propnum = models.ForeignKey(Ptsproductionpt,db_column='PROPNUM', to_field='userdata0', on_delete=models.CASCADE)
    section = models.TextField(db_column='SECTION', blank=True, null=True)  # Field name made lowercase.
    sequence = models.TextField(db_column='SEQUENCE', blank=True, null=True)  # Field name made lowercase.
    qualifier = models.TextField(db_column='QUALIFIER', blank=True, null=True)  # Field name made lowercase.
    keyword = models.TextField(db_column='KEYWORD', blank=True, null=True)  # Field name made lowercase.
    expression = models.TextField(db_column='EXPRESSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'res_economic_inputs'


class ResForcastMonthlyProduction(models.Model):
    id = models.AutoField(primary_key=True)
    propnum = models.ForeignKey(Ptsproductionpt,db_column='PROPNUM', to_field='userdata0', on_delete=models.CASCADE)
    scenario = models.TextField(db_column='SCENARIO', blank=True, null=True)  # Field name made lowercase.
    outdate = models.TextField(db_column='OUTDATE', blank=True, null=True)  # Field name made lowercase.
    s40 = models.TextField(db_column='S40', blank=True, null=True)  # Field name made lowercase.
    s41 = models.TextField(db_column='S41', blank=True, null=True)  # Field name made lowercase.
    s44 = models.TextField(db_column='S44', blank=True, null=True)  # Field name made lowercase.
    s55 = models.TextField(db_column='S55', blank=True, null=True)  # Field name made lowercase.
    s95 = models.TextField(db_column='S95', blank=True, null=True)  # Field name made lowercase.
    s123 = models.TextField(db_column='S123', blank=True, null=True)  # Field name made lowercase.
    s125 = models.TextField(db_column='S125', blank=True, null=True)  # Field name made lowercase.
    s126 = models.TextField(db_column='S126', blank=True, null=True)  # Field name made lowercase.
    s129 = models.TextField(db_column='S129', blank=True, null=True)  # Field name made lowercase.
    s145 = models.TextField(db_column='S145', blank=True, null=True)  # Field name made lowercase.
    s146 = models.TextField(db_column='S146', blank=True, null=True)  # Field name made lowercase.
    s149 = models.TextField(db_column='S149', blank=True, null=True)  # Field name made lowercase.
    s195 = models.TextField(db_column='S195', blank=True, null=True)  # Field name made lowercase.
    s196 = models.TextField(db_column='S196', blank=True, null=True)  # Field name made lowercase.
    s197 = models.TextField(db_column='S197', blank=True, null=True)  # Field name made lowercase.
    s199 = models.TextField(db_column='S199', blank=True, null=True)  # Field name made lowercase.
    s237 = models.TextField(db_column='S237', blank=True, null=True)  # Field name made lowercase.
    s238 = models.TextField(db_column='S238', blank=True, null=True)  # Field name made lowercase.
    s241 = models.TextField(db_column='S241', blank=True, null=True)  # Field name made lowercase.
    s252 = models.TextField(db_column='S252', blank=True, null=True)  # Field name made lowercase.
    s253 = models.TextField(db_column='S253', blank=True, null=True)  # Field name made lowercase.
    s256 = models.TextField(db_column='S256', blank=True, null=True)  # Field name made lowercase.
    s258 = models.TextField(db_column='S258', blank=True, null=True)  # Field name made lowercase.
    s267 = models.TextField(db_column='S267', blank=True, null=True)  # Field name made lowercase.
    s274 = models.TextField(db_column='S274', blank=True, null=True)  # Field name made lowercase.
    s277 = models.TextField(db_column='S277', blank=True, null=True)  # Field name made lowercase.
    s345 = models.TextField(db_column='S345', blank=True, null=True)  # Field name made lowercase.
    s346 = models.TextField(db_column='S346', blank=True, null=True)  # Field name made lowercase.
    s349 = models.TextField(db_column='S349', blank=True, null=True)  # Field name made lowercase.
    s350 = models.TextField(db_column='S350', blank=True, null=True)  # Field name made lowercase.
    s351 = models.TextField(db_column='S351', blank=True, null=True)  # Field name made lowercase.
    s352 = models.TextField(db_column='S352', blank=True, null=True)  # Field name made lowercase.
    s356 = models.TextField(db_column='S356', blank=True, null=True)  # Field name made lowercase.
    s370 = models.TextField(db_column='S370', blank=True, null=True)  # Field name made lowercase.
    s371 = models.TextField(db_column='S371', blank=True, null=True)  # Field name made lowercase.
    s372 = models.TextField(db_column='S372', blank=True, null=True)  # Field name made lowercase.
    s374 = models.TextField(db_column='S374', blank=True, null=True)  # Field name made lowercase.
    s376 = models.TextField(db_column='S376', blank=True, null=True)  # Field name made lowercase.
    s427 = models.TextField(db_column='S427', blank=True, null=True)  # Field name made lowercase.
    s428 = models.TextField(db_column='S428', blank=True, null=True)  # Field name made lowercase.
    s431 = models.TextField(db_column='S431', blank=True, null=True)  # Field name made lowercase.
    s442 = models.TextField(db_column='S442', blank=True, null=True)  # Field name made lowercase.
    s692 = models.TextField(db_column='S692', blank=True, null=True)  # Field name made lowercase.
    s701 = models.TextField(db_column='S701', blank=True, null=True)  # Field name made lowercase.
    s706 = models.TextField(db_column='S706', blank=True, null=True)  # Field name made lowercase.
    s709 = models.TextField(db_column='S709', blank=True, null=True)  # Field name made lowercase.
    s730 = models.TextField(db_column='S730', blank=True, null=True)  # Field name made lowercase.
    s732 = models.TextField(db_column='S732', blank=True, null=True)  # Field name made lowercase.
    s750 = models.TextField(db_column='S750', blank=True, null=True)  # Field name made lowercase.
    s751 = models.TextField(db_column='S751', blank=True, null=True)  # Field name made lowercase.
    s752 = models.TextField(db_column='S752', blank=True, null=True)  # Field name made lowercase.
    s753 = models.TextField(db_column='S753', blank=True, null=True)  # Field name made lowercase.
    s754 = models.TextField(db_column='S754', blank=True, null=True)  # Field name made lowercase.
    s755 = models.TextField(db_column='S755', blank=True, null=True)  # Field name made lowercase.
    s757 = models.TextField(db_column='S757', blank=True, null=True)  # Field name made lowercase.
    s815 = models.TextField(db_column='S815', blank=True, null=True)  # Field name made lowercase.
    s816 = models.TextField(db_column='S816', blank=True, null=True)  # Field name made lowercase.
    s817 = models.TextField(db_column='S817', blank=True, null=True)  # Field name made lowercase.
    s819 = models.TextField(db_column='S819', blank=True, null=True)  # Field name made lowercase.
    s846 = models.TextField(db_column='S846', blank=True, null=True)  # Field name made lowercase.
    s847 = models.TextField(db_column='S847', blank=True, null=True)  # Field name made lowercase.
    s848 = models.TextField(db_column='S848', blank=True, null=True)  # Field name made lowercase.
    s850 = models.TextField(db_column='S850', blank=True, null=True)  # Field name made lowercase.
    s861 = models.TextField(db_column='S861', blank=True, null=True)  # Field name made lowercase.
    s872 = models.TextField(db_column='S872', blank=True, null=True)  # Field name made lowercase.
    s873 = models.TextField(db_column='S873', blank=True, null=True)  # Field name made lowercase.
    s874 = models.TextField(db_column='S874', blank=True, null=True)  # Field name made lowercase.
    s876 = models.TextField(db_column='S876', blank=True, null=True)  # Field name made lowercase.
    s887 = models.TextField(db_column='S887', blank=True, null=True)  # Field name made lowercase.
    s892 = models.TextField(db_column='S892', blank=True, null=True)  # Field name made lowercase.
    s1018 = models.TextField(db_column='S1018', blank=True, null=True)  # Field name made lowercase.
    s1019 = models.TextField(db_column='S1019', blank=True, null=True)  # Field name made lowercase.
    s1022 = models.TextField(db_column='S1022', blank=True, null=True)  # Field name made lowercase.
    s1024 = models.TextField(db_column='S1024', blank=True, null=True)  # Field name made lowercase.
    s1033 = models.TextField(db_column='S1033', blank=True, null=True)  # Field name made lowercase.
    s1039 = models.TextField(db_column='S1039', blank=True, null=True)  # Field name made lowercase.
    s1040 = models.TextField(db_column='S1040', blank=True, null=True)  # Field name made lowercase.
    s1062 = models.TextField(db_column='S1062', blank=True, null=True)  # Field name made lowercase.
    s1064 = models.TextField(db_column='S1064', blank=True, null=True)  # Field name made lowercase.
    s1065 = models.TextField(db_column='S1065', blank=True, null=True)  # Field name made lowercase.
    s1069 = models.TextField(db_column='S1069', blank=True, null=True)  # Field name made lowercase.
    s1070 = models.TextField(db_column='S1070', blank=True, null=True)  # Field name made lowercase.
    s1094 = models.TextField(db_column='S1094', blank=True, null=True)  # Field name made lowercase.
    m41 = models.TextField(db_column='M41', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'res_forcast_monthly_production'


class ResHistoricalDailyProduction(models.Model):
    id = models.AutoField(primary_key=True)
    propnum = models.ForeignKey(Ptsproductionpt, db_column='PROPNUM', to_field='userdata0', on_delete=models.CASCADE)
    scenario = models.TextField(db_column='SCENARIO', blank=True, null=True)  # Field name made lowercase.
    time_frame = models.TextField(db_column='TIME_FRAME', blank=True, null=True)  # Field name made lowercase.
    s345 = models.TextField(db_column='S345', blank=True, null=True)  # Field name made lowercase.
    s346 = models.TextField(db_column='S346', blank=True, null=True)  # Field name made lowercase.
    s349 = models.TextField(db_column='S349', blank=True, null=True)  # Field name made lowercase.
    s370 = models.TextField(db_column='S370', blank=True, null=True)  # Field name made lowercase.
    s371 = models.TextField(db_column='S371', blank=True, null=True)  # Field name made lowercase.
    s372 = models.TextField(db_column='S372', blank=True, null=True)  # Field name made lowercase.
    s373 = models.TextField(db_column='S373', blank=True, null=True)  # Field name made lowercase.
    s374 = models.TextField(db_column='S374', blank=True, null=True)  # Field name made lowercase.
    s375 = models.TextField(db_column='S375', blank=True, null=True)  # Field name made lowercase.
    s376 = models.TextField(db_column='S376', blank=True, null=True)  # Field name made lowercase.
    s427 = models.TextField(db_column='S427', blank=True, null=True)  # Field name made lowercase.
    s428 = models.TextField(db_column='S428', blank=True, null=True)  # Field name made lowercase.
    s429 = models.TextField(db_column='S429', blank=True, null=True)  # Field name made lowercase.
    s430 = models.TextField(db_column='S430', blank=True, null=True)  # Field name made lowercase.
    s431 = models.TextField(db_column='S431', blank=True, null=True)  # Field name made lowercase.
    s432 = models.TextField(db_column='S432', blank=True, null=True)  # Field name made lowercase.
    s433 = models.TextField(db_column='S433', blank=True, null=True)  # Field name made lowercase.
    s442 = models.TextField(db_column='S442', blank=True, null=True)  # Field name made lowercase.
    s815 = models.TextField(db_column='S815', blank=True, null=True)  # Field name made lowercase.
    s816 = models.TextField(db_column='S816', blank=True, null=True)  # Field name made lowercase.
    s817 = models.TextField(db_column='S817', blank=True, null=True)  # Field name made lowercase.
    s818 = models.TextField(db_column='S818', blank=True, null=True)  # Field name made lowercase.
    s819 = models.TextField(db_column='S819', blank=True, null=True)  # Field name made lowercase.
    s846 = models.TextField(db_column='S846', blank=True, null=True)  # Field name made lowercase.
    s847 = models.TextField(db_column='S847', blank=True, null=True)  # Field name made lowercase.
    s848 = models.TextField(db_column='S848', blank=True, null=True)  # Field name made lowercase.
    s849 = models.TextField(db_column='S849', blank=True, null=True)  # Field name made lowercase.
    s850 = models.TextField(db_column='S850', blank=True, null=True)  # Field name made lowercase.
    s851 = models.TextField(db_column='S851', blank=True, null=True)  # Field name made lowercase.
    s852 = models.TextField(db_column='S852', blank=True, null=True)  # Field name made lowercase.
    s861 = models.TextField(db_column='S861', blank=True, null=True)  # Field name made lowercase.
    s872 = models.TextField(db_column='S872', blank=True, null=True)  # Field name made lowercase.
    s873 = models.TextField(db_column='S873', blank=True, null=True)  # Field name made lowercase.
    s874 = models.TextField(db_column='S874', blank=True, null=True)  # Field name made lowercase.
    s887 = models.TextField(db_column='S887', blank=True, null=True)  # Field name made lowercase.
    s892 = models.TextField(db_column='S892', blank=True, null=True)  # Field name made lowercase.
    s1062 = models.TextField(db_column='S1062', blank=True, null=True)  # Field name made lowercase.
    s1064 = models.TextField(db_column='S1064', blank=True, null=True)  # Field name made lowercase.
    s1065 = models.TextField(db_column='S1065', blank=True, null=True)  # Field name made lowercase.
    s1069 = models.TextField(db_column='S1069', blank=True, null=True)  # Field name made lowercase.
    s1100 = models.TextField(db_column='S1100', blank=True, null=True)  # Field name made lowercase.
    s1101 = models.TextField(db_column='S1101', blank=True, null=True)  # Field name made lowercase.
    s1183 = models.TextField(db_column='S1183', blank=True, null=True)  # Field name made lowercase.
    s1184 = models.TextField(db_column='S1184', blank=True, null=True)  # Field name made lowercase.
    s1185 = models.TextField(db_column='S1185', blank=True, null=True)  # Field name made lowercase.
    s1186 = models.TextField(db_column='S1186', blank=True, null=True)  # Field name made lowercase.
    s1187 = models.TextField(db_column='S1187', blank=True, null=True)  # Field name made lowercase.
    s1301 = models.TextField(db_column='S1301', blank=True, null=True)  # Field name made lowercase.
    s1302 = models.TextField(db_column='S1302', blank=True, null=True)  # Field name made lowercase.
    s1303 = models.TextField(db_column='S1303', blank=True, null=True)  # Field name made lowercase.
    s1305 = models.TextField(db_column='S1305', blank=True, null=True)  # Field name made lowercase.
    s1306 = models.TextField(db_column='S1306', blank=True, null=True)  # Field name made lowercase.
    s1134 = models.TextField(db_column='S1134', blank=True, null=True)  # Field name made lowercase.
    s1182 = models.TextField(db_column='S1182', blank=True, null=True)  # Field name made lowercase.
    s1236 = models.TextField(db_column='S1236', blank=True, null=True)  # Field name made lowercase.
    s1208 = models.TextField(db_column='S1208', blank=True, null=True)  # Field name made lowercase.
    s1261 = models.TextField(db_column='S1261', blank=True, null=True)  # Field name made lowercase.
    s1262 = models.TextField(db_column='S1262', blank=True, null=True)  # Field name made lowercase.
    s1263 = models.TextField(db_column='S1263', blank=True, null=True)  # Field name made lowercase.
    s1264 = models.TextField(db_column='S1264', blank=True, null=True)  # Field name made lowercase.
    s1265 = models.TextField(db_column='S1265', blank=True, null=True)  # Field name made lowercase.
    s1266 = models.TextField(db_column='S1266', blank=True, null=True)  # Field name made lowercase.
    s1269 = models.TextField(db_column='S1269', blank=True, null=True)  # Field name made lowercase.
    s1270 = models.TextField(db_column='S1270', blank=True, null=True)  # Field name made lowercase.
    s1307 = models.TextField(db_column='S1307', blank=True, null=True)  # Field name made lowercase.
    s1308 = models.TextField(db_column='S1308', blank=True, null=True)  # Field name made lowercase.
    s1314 = models.TextField(db_column='S1314', blank=True, null=True)  # Field name made lowercase.
    s1315 = models.TextField(db_column='S1315', blank=True, null=True)  # Field name made lowercase.
    s1316 = models.TextField(db_column='S1316', blank=True, null=True)  # Field name made lowercase.
    s1317 = models.TextField(db_column='S1317', blank=True, null=True)  # Field name made lowercase.
    s1318 = models.TextField(db_column='S1318', blank=True, null=True)  # Field name made lowercase.
    s350 = models.TextField(db_column='S350', blank=True, null=True)  # Field name made lowercase.
    s750 = models.TextField(db_column='S750', blank=True, null=True)  # Field name made lowercase.
    s751 = models.TextField(db_column='S751', blank=True, null=True)  # Field name made lowercase.
    s1081 = models.TextField(db_column='S1081', blank=True, null=True)  # Field name made lowercase.
    s1038 = models.TextField(db_column='S1038', blank=True, null=True)  # Field name made lowercase.
    s1018 = models.TextField(db_column='S1018', blank=True, null=True)  # Field name made lowercase.
    s1019 = models.TextField(db_column='S1019', blank=True, null=True)  # Field name made lowercase.
    s1033 = models.TextField(db_column='S1033', blank=True, null=True)  # Field name made lowercase.
    s1034 = models.TextField(db_column='S1034', blank=True, null=True)  # Field name made lowercase.
    s1035 = models.TextField(db_column='S1035', blank=True, null=True)  # Field name made lowercase.
    s686 = models.TextField(db_column='S686', blank=True, null=True)  # Field name made lowercase.
    s687 = models.TextField(db_column='S687', blank=True, null=True)  # Field name made lowercase.
    s706 = models.TextField(db_column='S706', blank=True, null=True)  # Field name made lowercase.
    s730 = models.TextField(db_column='S730', blank=True, null=True)  # Field name made lowercase.
    s753 = models.TextField(db_column='S753', blank=True, null=True)  # Field name made lowercase.
    s754 = models.TextField(db_column='S754', blank=True, null=True)  # Field name made lowercase.
    s757 = models.TextField(db_column='S757', blank=True, null=True)  # Field name made lowercase.
    s1092 = models.TextField(db_column='S1092', blank=True, null=True)  # Field name made lowercase.
    s1093 = models.TextField(db_column='S1093', blank=True, null=True)  # Field name made lowercase.
    s1094 = models.TextField(db_column='S1094', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'res_historical_daily_production'


class ResHistoricalMonthlyProduction(models.Model):
    id = models.AutoField(primary_key=True)
    propnum = models.ForeignKey(Ptsproductionpt,db_column='PROPNUM', to_field='userdata0', on_delete=models.CASCADE)
    p_date = models.TextField(db_column='P_DATE', blank=True, null=True)  # Field name made lowercase.
    oil = models.TextField(db_column='OIL', blank=True, null=True)  # Field name made lowercase.
    gas = models.TextField(db_column='GAS', blank=True, null=True)  # Field name made lowercase.
    water = models.TextField(db_column='WATER', blank=True, null=True)  # Field name made lowercase.
    wells = models.TextField(db_column='WELLS', blank=True, null=True)  # Field name made lowercase.
    oil_sales = models.TextField(db_column='OIL_SALES', blank=True, null=True)  # Field name made lowercase.
    gas_sales = models.TextField(db_column='GAS_SALES', blank=True, null=True)  # Field name made lowercase.
    ngl = models.TextField(db_column='NGL', blank=True, null=True)  # Field name made lowercase.
    btu = models.TextField(db_column='BTU', blank=True, null=True)  # Field name made lowercase.
    wtr_inj = models.TextField(db_column='WTR_INJ', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.
    days_on = models.TextField(db_column='DAYS_ON', blank=True, null=True)  # Field name made lowercase.
    line_pres = models.TextField(db_column='LINE_PRES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'res_historical_monthly_production'


class ResOnelineSummary(models.Model):
    id = models.AutoField(primary_key=True)
    propnum = models.ForeignKey(Ptsproductionpt,db_column='PROPNUM', to_field='userdata0', on_delete=models.CASCADE)  # Field name made lowercase.
    scenario = models.TextField(db_column='SCENARIO', blank=True, null=True)  # Field name made lowercase.
    c351 = models.TextField(db_column='C351', blank=True, null=True)  # Field name made lowercase.
    c352 = models.TextField(db_column='C352', blank=True, null=True)  # Field name made lowercase.
    c356 = models.TextField(db_column='C356', blank=True, null=True)  # Field name made lowercase.
    c370 = models.TextField(db_column='C370', blank=True, null=True)  # Field name made lowercase.
    c371 = models.TextField(db_column='C371', blank=True, null=True)  # Field name made lowercase.
    c374 = models.TextField(db_column='C374', blank=True, null=True)  # Field name made lowercase.
    c815 = models.TextField(db_column='C815', blank=True, null=True)  # Field name made lowercase.
    c817 = models.TextField(db_column='C817', blank=True, null=True)  # Field name made lowercase.
    c819 = models.TextField(db_column='C819', blank=True, null=True)  # Field name made lowercase.
    c816 = models.TextField(db_column='C816', blank=True, null=True)  # Field name made lowercase.
    c846 = models.TextField(db_column='C846', blank=True, null=True)  # Field name made lowercase.
    c847 = models.TextField(db_column='C847', blank=True, null=True)  # Field name made lowercase.
    c850 = models.TextField(db_column='C850', blank=True, null=True)  # Field name made lowercase.
    c861 = models.TextField(db_column='C861', blank=True, null=True)  # Field name made lowercase.
    c887 = models.TextField(db_column='C887', blank=True, null=True)  # Field name made lowercase.
    c892 = models.TextField(db_column='C892', blank=True, null=True)  # Field name made lowercase.
    c1062 = models.TextField(db_column='C1062', blank=True, null=True)  # Field name made lowercase.
    c1064 = models.TextField(db_column='C1064', blank=True, null=True)  # Field name made lowercase.
    c1065 = models.TextField(db_column='C1065', blank=True, null=True)  # Field name made lowercase.
    c1069 = models.TextField(db_column='C1069', blank=True, null=True)  # Field name made lowercase.
    c1092 = models.TextField(db_column='C1092', blank=True, null=True)  # Field name made lowercase.
    c1093 = models.TextField(db_column='C1093', blank=True, null=True)  # Field name made lowercase.
    c1094 = models.TextField(db_column='C1094', blank=True, null=True)  # Field name made lowercase.
    c1100 = models.TextField(db_column='C1100', blank=True, null=True)  # Field name made lowercase.
    c1101 = models.TextField(db_column='C1101', blank=True, null=True)  # Field name made lowercase.
    c1183 = models.TextField(db_column='C1183', blank=True, null=True)  # Field name made lowercase.
    c1184 = models.TextField(db_column='C1184', blank=True, null=True)  # Field name made lowercase.
    c1185 = models.TextField(db_column='C1185', blank=True, null=True)  # Field name made lowercase.
    c1186 = models.TextField(db_column='C1186', blank=True, null=True)  # Field name made lowercase.
    c1187 = models.TextField(db_column='C1187', blank=True, null=True)  # Field name made lowercase.
    c1208 = models.TextField(db_column='C1208', blank=True, null=True)  # Field name made lowercase.
    c1263 = models.TextField(db_column='C1263', blank=True, null=True)  # Field name made lowercase.
    c1264 = models.TextField(db_column='C1264', blank=True, null=True)  # Field name made lowercase.
    c1265 = models.TextField(db_column='C1265', blank=True, null=True)  # Field name made lowercase.
    c1269 = models.TextField(db_column='C1269', blank=True, null=True)  # Field name made lowercase.
    c1270 = models.TextField(db_column='C1270', blank=True, null=True)  # Field name made lowercase.
    c1301 = models.TextField(db_column='C1301', blank=True, null=True)  # Field name made lowercase.
    c1302 = models.TextField(db_column='C1302', blank=True, null=True)  # Field name made lowercase.
    c1303 = models.TextField(db_column='C1303', blank=True, null=True)  # Field name made lowercase.
    c1305 = models.TextField(db_column='C1305', blank=True, null=True)  # Field name made lowercase.
    c1306 = models.TextField(db_column='C1306', blank=True, null=True)  # Field name made lowercase.
    c1308 = models.TextField(db_column='C1308', blank=True, null=True)  # Field name made lowercase.
    c1317 = models.TextField(db_column='C1317', blank=True, null=True)  # Field name made lowercase.
    c1318 = models.TextField(db_column='C1318', blank=True, null=True)  # Field name made lowercase.
    m1 = models.TextField(db_column='M1', blank=True, null=True)  # Field name made lowercase.
    m4 = models.TextField(db_column='M4', blank=True, null=True)  # Field name made lowercase.
    m6 = models.TextField(db_column='M6', blank=True, null=True)  # Field name made lowercase.
    m7 = models.TextField(db_column='M7', blank=True, null=True)  # Field name made lowercase.
    m8 = models.TextField(db_column='M8', blank=True, null=True)  # Field name made lowercase.
    m11 = models.TextField(db_column='M11', blank=True, null=True)  # Field name made lowercase.
    m16 = models.TextField(db_column='M16', blank=True, null=True)  # Field name made lowercase.
    m17 = models.TextField(db_column='M17', blank=True, null=True)  # Field name made lowercase.
    m18 = models.TextField(db_column='M18', blank=True, null=True)  # Field name made lowercase.
    m19 = models.TextField(db_column='M19', blank=True, null=True)  # Field name made lowercase.
    m21 = models.TextField(db_column='M21', blank=True, null=True)  # Field name made lowercase.
    m22 = models.TextField(db_column='M22', blank=True, null=True)  # Field name made lowercase.
    m23 = models.TextField(db_column='M23', blank=True, null=True)  # Field name made lowercase.
    m24 = models.TextField(db_column='M24', blank=True, null=True)  # Field name made lowercase.
    m25 = models.TextField(db_column='M25', blank=True, null=True)  # Field name made lowercase.
    m27 = models.TextField(db_column='M27', blank=True, null=True)  # Field name made lowercase.
    m28 = models.TextField(db_column='M28', blank=True, null=True)  # Field name made lowercase.
    m31 = models.TextField(db_column='M31', blank=True, null=True)  # Field name made lowercase.
    m32 = models.TextField(db_column='M32', blank=True, null=True)  # Field name made lowercase.
    m33 = models.TextField(db_column='M33', blank=True, null=True)  # Field name made lowercase.
    m34 = models.TextField(db_column='M34', blank=True, null=True)  # Field name made lowercase.
    m35 = models.TextField(db_column='M35', blank=True, null=True)  # Field name made lowercase.
    m36 = models.TextField(db_column='M36', blank=True, null=True)  # Field name made lowercase.
    m41 = models.TextField(db_column='M41', blank=True, null=True)  # Field name made lowercase.
    m42 = models.TextField(db_column='M42', blank=True, null=True)  # Field name made lowercase.
    m65 = models.TextField(db_column='M65', blank=True, null=True)  # Field name made lowercase.
    m67 = models.TextField(db_column='M67', blank=True, null=True)  # Field name made lowercase.
    m75 = models.TextField(db_column='M75', blank=True, null=True)  # Field name made lowercase.
    m77 = models.TextField(db_column='M77', blank=True, null=True)  # Field name made lowercase.
    m111 = models.TextField(db_column='M111', blank=True, null=True)  # Field name made lowercase.
    m133 = models.TextField(db_column='M133', blank=True, null=True)  # Field name made lowercase.
    e1 = models.TextField(db_column='E1', blank=True, null=True)  # Field name made lowercase.
    e2 = models.TextField(db_column='E2', blank=True, null=True)  # Field name made lowercase.
    e3 = models.TextField(db_column='E3', blank=True, null=True)  # Field name made lowercase.
    e4 = models.TextField(db_column='E4', blank=True, null=True)  # Field name made lowercase.
    e5 = models.TextField(db_column='E5', blank=True, null=True)  # Field name made lowercase.
    e6 = models.TextField(db_column='E6', blank=True, null=True)  # Field name made lowercase.
    e7 = models.TextField(db_column='E7', blank=True, null=True)  # Field name made lowercase.
    e8 = models.TextField(db_column='E8', blank=True, null=True)  # Field name made lowercase.
    e11 = models.TextField(db_column='E11', blank=True, null=True)  # Field name made lowercase.
    p1 = models.TextField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.TextField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.TextField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.TextField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.TextField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
    p6 = models.TextField(db_column='P6', blank=True, null=True)  # Field name made lowercase.
    p7 = models.TextField(db_column='P7', blank=True, null=True)  # Field name made lowercase.
    p8 = models.TextField(db_column='P8', blank=True, null=True)  # Field name made lowercase.
    p9 = models.TextField(db_column='P9', blank=True, null=True)  # Field name made lowercase.
    p10 = models.TextField(db_column='P10', blank=True, null=True)  # Field name made lowercase.
    p11 = models.TextField(db_column='P11', blank=True, null=True)  # Field name made lowercase.
    p12 = models.TextField(db_column='P12', blank=True, null=True)  # Field name made lowercase.
    p13 = models.TextField(db_column='P13', blank=True, null=True)  # Field name made lowercase.
    p14 = models.TextField(db_column='P14', blank=True, null=True)  # Field name made lowercase.
    p15 = models.TextField(db_column='P15', blank=True, null=True)  # Field name made lowercase.
    b1 = models.TextField(db_column='B1', blank=True, null=True)  # Field name made lowercase.
    b2 = models.TextField(db_column='B2', blank=True, null=True)  # Field name made lowercase.
    b3 = models.TextField(db_column='B3', blank=True, null=True)  # Field name made lowercase.
    b4 = models.TextField(db_column='B4', blank=True, null=True)  # Field name made lowercase.
    b5 = models.TextField(db_column='B5', blank=True, null=True)  # Field name made lowercase.
    b6 = models.TextField(db_column='B6', blank=True, null=True)  # Field name made lowercase.
    b7 = models.TextField(db_column='B7', blank=True, null=True)  # Field name made lowercase.
    b8 = models.TextField(db_column='B8', blank=True, null=True)  # Field name made lowercase.
    b9 = models.TextField(db_column='B9', blank=True, null=True)  # Field name made lowercase.
    b10 = models.TextField(db_column='B10', blank=True, null=True)  # Field name made lowercase.
    b11 = models.TextField(db_column='B11', blank=True, null=True)  # Field name made lowercase.
    b12 = models.TextField(db_column='B12', blank=True, null=True)  # Field name made lowercase.
    b13 = models.TextField(db_column='B13', blank=True, null=True)  # Field name made lowercase.
    b14 = models.TextField(db_column='B14', blank=True, null=True)  # Field name made lowercase.
    b15 = models.TextField(db_column='B15', blank=True, null=True)  # Field name made lowercase.
    a18 = models.TextField(db_column='A18', blank=True, null=True)  # Field name made lowercase.
    bfit_ror_interp = models.TextField(db_column='BFIT_ROR_INTERP', blank=True, null=True)  # Field name made lowercase.
    bfit_payout = models.TextField(db_column='BFIT_PAYOUT', blank=True, null=True)  # Field name made lowercase.
    bfit_n_to_inv = models.TextField(db_column='BFIT_N_TO_INV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'res_oneline_summary'


class Sumdailyinjection(models.Model):
    entityid = models.IntegerField(primary_key=True)  # The composite primary key (entityid, entitytype, productid, docdate) found, that is not supported. The first column is selected.
    entitytype = models.SmallIntegerField()
    api = models.CharField(max_length=20, blank=True, null=True)
    productid = models.SmallIntegerField()
    docdate = models.DateTimeField()
    injectionvolume = models.FloatField()
    stamp = models.DateTimeField(blank=True, null=True)
    datasource = models.CharField(max_length=50, blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sumdailyinjection'
        unique_together = (('entityid', 'entitytype', 'productid', 'docdate'),)


class Sumdailyproduction(models.Model):
    entityid = models.ForeignKey(Ptsproductionpt, db_column='entityid', on_delete=models.CASCADE)  # The composite primary key (entityid, entitytype, docdate) found, that is not supported. The first column is selected.
    entitytype = models.IntegerField()
    api = models.CharField(max_length=20, blank=True, null=True)
    docdate = models.DateTimeField()
    oil = models.FloatField()
    water = models.FloatField()
    gas = models.FloatField()
    swd_oil = models.FloatField(db_column='SWD Oil', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gasprodvol = models.FloatField(blank=True, null=True)
    gassalesvol = models.FloatField(blank=True, null=True)
    gasleasevol = models.FloatField(blank=True, null=True)
    stamp = models.DateTimeField(blank=True, null=True)
    datasource = models.CharField(max_length=20, blank=True, null=True)
    noru = models.CharField(max_length=1, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'sumdailyproduction'
        unique_together = (('entityid', 'entitytype', 'docdate'),)


class Swd(models.Model):
    swdid = models.AutoField(primary_key=True)
    swdname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'swd'


class Type11Rate(models.Model):
    date = models.DateField()
    credit = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'type11rate'

class modem(models.Model):
    name = models.CharField(max_length=50)
    iccid = models.CharField(primary_key=True,max_length=20)

    class Meta:
        managed = True
        db_table = 'modem'
        
    @classmethod
    def get_all_modems(cls):
        return cls.objects.all()
    
    def __str__(self):
        return self.name

class device(models.Model):
    #id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100) #this is well name
    device_id = models.CharField(primary_key=True)
    unit_slave = (models.CharField(max_length=50))
    plc_type = models.CharField(max_length=50)
    station = models.ForeignKey(modem, on_delete=models.CASCADE)
    station_location = models.CharField(max_length=100)
    baud_rate = models.IntegerField()
    run_status = models.BooleanField(default=False)

    class Meta:
        managed = True  # Set to False if you want to manage the table outside Django's migration system
        #db_table = 'tower_map'  # Specify the custom table name here

    def __str__(self):
        return self.device_name

class flow_controller_data(models.Model):
    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(device,on_delete=models.CASCADE, null=True, blank=True)
    current_output = models.IntegerField(null=True, blank=True)
    line_pressure = models.IntegerField(null=True, blank=True)
    well_pressure = models.IntegerField(null=True, blank=True)
    current_day_production = models.IntegerField(null=True, blank=True) # yesterday is just the current day from today
    spot_rate = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    line_pressure_high = models.IntegerField(null=True, blank=True)
    well_pressure_high = models.IntegerField(null=True, blank=True)
    line_pressure_low = models.IntegerField(null=True, blank=True)
    well_pressure_low = models.IntegerField(null=True, blank=True)
    last_action = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    well_pressure_mean = models.IntegerField(null=True, blank=True)
    well_pressure_max = models.IntegerField(null=True, blank=True)
    well_pressure_min = models.IntegerField(null=True, blank=True)
    line_pressure_max = models.IntegerField(null=True, blank=True)
    line_pressure_min = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = True  # Set to False if you want to manage the table outside Django's migration system
        #db_table = 'tower_map'  # Specify the custom table name here

    #def __str__(self):
    #    return self.device_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    parent_tag = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    device = models.ForeignKey(device, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50)
    units = models.CharField(max_length=50)
    description = models.TextField()
    modbus_address = models.IntegerField()
    modbus_function_code = models.IntegerField()
    modbus_data_type = models.CharField(max_length=50)
    modbus_unit_identifier = models.IntegerField(null=True, blank=True)
    modbus_tcp_ip = models.BooleanField(default=True)
    modbus_baud_rate = models.IntegerField(null=True, blank=True)
    modbus_data_bits = models.IntegerField(null=True, blank=True)
    modbus_stop_bits = models.IntegerField(null=True, blank=True)
    modbus_parity = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.tag_name


class Welltype(models.Model):
    welltypeid = models.AutoField(primary_key=True)
    welltypename = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'welltype'

class Device_inputs(models.Model):
    current_production = models.IntegerField(blank=True, null=True)
    hour_production_limit = models.IntegerField(blank=True, null=True)
    k_factor = models.FloatField(blank=True, null=True)
    kill_switch = models.CharField(blank=True, null=True)
    low_line_pressure = models.IntegerField(blank=True, null=True)
    max_output = models.IntegerField(blank=True, null=True)
    max_pressure = models.IntegerField(blank=True, null=True)
    min_output = models.IntegerField(blank=True, null=True)
    min_pressure = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    output_channel = models.IntegerField(blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    start_casing_pressure = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'device_inputs'
  


