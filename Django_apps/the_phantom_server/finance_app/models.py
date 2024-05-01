from django.db import models

# Create your models here.
class Coa(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    acct_designation = models.CharField(max_length=4, blank=True, null=True)
    at_coa_type = models.CharField(max_length=8, blank=True, null=True)
    category = models.CharField(max_length=5, blank=True, null=True)
    exp_date = models.DateTimeField(blank=True, null=True)
    inventory_req = models.CharField(max_length=9, blank=True, null=True)
    jib_req = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    normal_bal = models.CharField(max_length=4, blank=True, null=True)
    purpose = models.CharField(max_length=42, blank=True, null=True)
    qty2_req = models.CharField(max_length=4, blank=True, null=True)
    qty_req = models.CharField(max_length=3, blank=True, null=True)
    sl_req = models.CharField(max_length=3, blank=True, null=True)
    sub_co = models.CharField(max_length=4, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'coa'
        indexes = [
            models.Index(fields=['u2_id']),
        ]

class CoaCat(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=34, blank=True, null=True)
    pl_closing_flag = models.CharField(max_length=15, blank=True, null=True)
    revalue_flag = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    wip_flag = models.CharField(max_length=4, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'coa_cat'

class CoaGen(models.Model):
    u2_id = models.IntegerField(primary_key=True)
    acct_designation = models.CharField(max_length=100, blank=True, null=True)
    at_coa_type = models.CharField(max_length=8, blank=True, null=True)
    category = models.CharField(max_length=5, blank=True, null=True)
    exp_date = models.DateTimeField(blank=True, null=True)
    inventory_req = models.CharField(max_length=9, blank=True, null=True)
    jib_req = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    normal_bal = models.CharField(max_length=4, blank=True, null=True)
    qty2_req = models.CharField(max_length=4, blank=True, null=True)
    qty_req = models.CharField(max_length=3, blank=True, null=True)
    sl_req = models.CharField(max_length=3, blank=True, null=True)
    sub_co = models.CharField(max_length=4, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)
    LOS_aggregation = models.IntegerField( null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'coa_gen'
        indexes = [
            models.Index(fields=['u2_id']),
        ]


class Cc(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    api_well_no = models.CharField(max_length=18, blank=True, null=True)
    cc_hier_id = models.CharField(max_length=10, blank=True, null=True)
    coding_flag = models.CharField(max_length=2, blank=True, null=True)
    dflt_company_access = models.CharField(max_length=7, blank=True, null=True)
    exp_date = models.DateTimeField(blank=True, null=True)
    ideas_cost_center = models.CharField(max_length=20, blank=True, null=True)
    manager = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=482, blank=True, null=True)
    rpt_flag = models.CharField(max_length=6, blank=True, null=True)
    shadow_key = models.CharField(max_length=21, blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cc'


class Name(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    address1 = models.CharField(max_length=34, blank=True, null=True)
    address2 = models.CharField(max_length=30, blank=True, null=True)
    address3 = models.CharField(max_length=30, blank=True, null=True)
    alt_lookup = models.CharField(max_length=111, blank=True, null=True)
    appr = models.CharField(max_length=4, blank=True, null=True)
    appr_date = models.DateTimeField(blank=True, null=True)
    base_id = models.CharField(max_length=7, blank=True, null=True)
    city = models.CharField(max_length=33, blank=True, null=True)
    country = models.CharField(max_length=6, blank=True, null=True)
    delivery_code = models.CharField(max_length=2, blank=True, null=True)
    entity_type = models.CharField(max_length=6, blank=True, null=True)
    land_ten99_exempt = models.CharField(max_length=6, blank=True, null=True)
    name1 = models.CharField(max_length=35, blank=True, null=True)
    name2 = models.CharField(max_length=35, blank=True, null=True)
    name3 = models.CharField(max_length=33, blank=True, null=True)
    name_control_1099 = models.CharField(max_length=7, blank=True, null=True)
    residence_state = models.CharField(max_length=3, blank=True, null=True)
    site = models.CharField(max_length=3, blank=True, null=True)
    sort_key = models.CharField(max_length=87, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    tax_entity_type = models.CharField(max_length=6, blank=True, null=True)
    tax_id = models.CharField(max_length=12, blank=True, null=True)
    ten99_address = models.CharField(max_length=40, blank=True, null=True)
    ten99_city = models.CharField(max_length=27, blank=True, null=True)
    ten99_state = models.CharField(max_length=5, blank=True, null=True)
    ten99_tin_type = models.CharField(max_length=4, blank=True, null=True)
    ten99_zip = models.CharField(max_length=10, blank=True, null=True)
    tin_2nd_notice = models.CharField(max_length=6, blank=True, null=True)
    w8 = models.CharField(max_length=2, blank=True, null=True)
    w8_eff_date = models.DateTimeField(blank=True, null=True)
    w9 = models.CharField(max_length=2, blank=True, null=True)
    w9_eff_date = models.DateTimeField(blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'name'

class Voucher(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    appr = models.CharField(max_length=4, blank=True, null=True)
    appr_date = models.DateTimeField(blank=True, null=True)
    at_status = models.CharField(max_length=11, blank=True, null=True)
    company = models.CharField(max_length=4, blank=True, null=True)
    control_voucher = models.CharField(max_length=7, blank=True, null=True)
    description = models.CharField(max_length=109, blank=True, null=True)
    post_begin = models.CharField(max_length=10, blank=True, null=True)
    post_end = models.CharField(max_length=10, blank=True, null=True)
    source_table = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    system_date = models.DateTimeField(blank=True, null=True)
    system_time = models.CharField(max_length=8, blank=True, null=True)
    system_user_id = models.CharField(max_length=6, blank=True, null=True)
    voucher = models.CharField(max_length=18, blank=True, null=True)
    voucher_ref = models.CharField(max_length=18, blank=True, null=True)
    vou_no = models.CharField(max_length=10, blank=True, null=True)
    vou_src = models.CharField(max_length=3, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'voucher'

class Trans(models.Model):
    u2_id = models.TextField(primary_key=True)
    acct = models.ForeignKey(Coa,db_column='ACCT', on_delete=models.CASCADE, blank=True, null=True)                                            # TextField(db_column='ACCT', blank=True, null=True)  # Field name made lowercase.
    acctg_period = models.DateTimeField(db_column='ACCTG_PERIOD', db_index=True,blank=True, null=True)  # Field name made lowercase.
    activity_date = models.DateTimeField(db_column='ACTIVITY_DATE', blank=True, null=True)  # Field name made lowercase.
    alloc_enabled = models.TextField(db_column='ALLOC_ENABLED', blank=True, null=True)  # Field name made lowercase.
    alloc_pct = models.FloatField(db_column='ALLOC_PCT', blank=True, null=True)  # Field name made lowercase.
    alloc_tract_id = models.TextField(db_column='ALLOC_TRACT_ID', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='AMT', blank=True, null=True)  # Field name made lowercase.
    app = models.TextField(db_column='APP', blank=True, null=True)  # Field name made lowercase.
    apply_wht = models.TextField(db_column='APPLY_WHT', blank=True, null=True)  # Field name made lowercase.
    at_alloc_date = models.TextField(db_column='AT_ALLOC_DATE', blank=True, null=True)  # Field name made lowercase.
    at_asset_id = models.TextField(db_column='AT_ASSET_ID', blank=True, null=True)  # Field name made lowercase.
    at_basis_acct = models.TextField(db_column='AT_BASIS_ACCT', blank=True, null=True)  # Field name made lowercase.
    at_cc_alloc_id = models.TextField(db_column='AT_CC_ALLOC_ID', blank=True, null=True)  # Field name made lowercase.
    at_type = models.TextField(db_column='AT_TYPE', blank=True, null=True)  # Field name made lowercase.
    balancing_amt = models.TextField(db_column='BALANCING_AMT', blank=True, null=True)  # Field name made lowercase.
    bal_source_trans_id = models.TextField(db_column='BAL_SOURCE_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    cc_alloc_date = models.DateTimeField(db_column='CC_ALLOC_DATE', blank=True, null=True)  # Field name made lowercase.
    cc_alloc_date_enabled = models.TextField(db_column='CC_ALLOC_DATE_ENABLED', blank=True, null=True)  # Field name made lowercase.
    cc_alloc_id = models.TextField(db_column='CC_ALLOC_ID', blank=True, null=True)  # Field name made lowercase.
    cnv_id = models.TextField(db_column='CNV_ID', blank=True, null=True)  # Field name made lowercase.
    cn_grp_id = models.TextField(db_column='CN_GRP_ID', blank=True, null=True)  # Field name made lowercase.
    cn_pct = models.TextField(db_column='CN_PCT', blank=True, null=True)  # Field name made lowercase.
    company = models.TextField(db_column='COMPANY', blank=True, null=True)  # Field name made lowercase.
    cost_center = models.ForeignKey(Cc,db_column='COST_CENTER', on_delete=models.CASCADE, blank=True, null=True)  # models.TextField(db_column='COST_CENTER', blank=True, null=True)  # Field name made lowercase.
    cpt = models.TextField(db_column='CPT', blank=True, null=True)  # Field name made lowercase.
    curr_status = models.TextField(db_column='CURR_STATUS', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    desc_txt = models.TextField(db_column='DESC_TXT', blank=True, null=True)  # Field name made lowercase.
    direct_bill = models.TextField(db_column='DIRECT_BILL', blank=True, null=True)  # Field name made lowercase.
    dist_company = models.TextField(db_column='DIST_COMPANY', blank=True, null=True)  # Field name made lowercase.
    doi = models.TextField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    doi_session = models.TextField(db_column='DOI_SESSION', blank=True, null=True)  # Field name made lowercase.
    foreign_system_date = models.TextField(db_column='FOREIGN_SYSTEM_DATE', blank=True, null=True)  # Field name made lowercase.
    gen_acct = models.TextField(db_column='GEN_ACCT', blank=True, null=True)  # Field name made lowercase.
    gl_date = models.TextField(db_column='GL_DATE', blank=True, null=True)  # Field name made lowercase.
    ideas_export_date = models.TextField(db_column='IDEAS_EXPORT_DATE', blank=True, null=True)  # Field name made lowercase.
    ideas_export_fn = models.TextField(db_column='IDEAS_EXPORT_FN', blank=True, null=True)  # Field name made lowercase.
    ideas_fqa = models.TextField(db_column='IDEAS_FQA', blank=True, null=True)  # Field name made lowercase.
    interco_from_trans_id = models.TextField(db_column='INTERCO_FROM_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    interco_to_trans_id = models.TextField(db_column='INTERCO_TO_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    int_amt = models.FloatField(db_column='INT_AMT', blank=True, null=True)  # Field name made lowercase.
    int_balancing_amt = models.TextField(db_column='INT_BALANCING_AMT', blank=True, null=True)  # Field name made lowercase.
    int_pmt_amt = models.TextField(db_column='INT_PMT_AMT', blank=True, null=True)  # Field name made lowercase.
    int_stat1_amt = models.FloatField(db_column='INT_STAT1_AMT', blank=True, null=True)  # Field name made lowercase.
    int_wht_amt = models.TextField(db_column='INT_WHT_AMT', blank=True, null=True)  # Field name made lowercase.
    in_service_period = models.TextField(db_column='IN_SERVICE_PERIOD', blank=True, null=True)  # Field name made lowercase.
    ir_date = models.TextField(db_column='IR_DATE', blank=True, null=True)  # Field name made lowercase.
    ir_deck = models.TextField(db_column='IR_DECK', blank=True, null=True)  # Field name made lowercase.
    ir_deck_session = models.TextField(db_column='IR_DECK_SESSION', blank=True, null=True)  # Field name made lowercase.
    ir_enabled = models.TextField(db_column='IR_ENABLED', blank=True, null=True)  # Field name made lowercase.
    ir_pgm_id = models.TextField(db_column='IR_PGM_ID', blank=True, null=True)  # Field name made lowercase.
    jib_alloc_date = models.DateTimeField(db_column='JIB_ALLOC_DATE', blank=True, null=True)  # Field name made lowercase.
    jib_alloc_date_enabled = models.TextField(db_column='JIB_ALLOC_DATE_ENABLED', blank=True, null=True)  # Field name made lowercase.
    jib_deck = models.TextField(db_column='JIB_DECK', blank=True, null=True)  # Field name made lowercase.
    jib_deck_session = models.TextField(db_column='JIB_DECK_SESSION', blank=True, null=True)  # Field name made lowercase.
    jur_tax_table_id = models.TextField(db_column='JUR_TAX_TABLE_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.ForeignKey(Name,db_column='NAME', on_delete=models.CASCADE, blank=True, null=True)    # models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    original_vou_type = models.TextField(db_column='ORIGINAL_VOU_TYPE', blank=True, null=True)  # Field name made lowercase.
    pmt_amt = models.TextField(db_column='PMT_AMT', blank=True, null=True)  # Field name made lowercase.
    post_date = models.DateTimeField(db_column='POST_DATE', blank=True, null=True)  # Field name made lowercase.
    post_time = models.TextField(db_column='POST_TIME', blank=True, null=True)  # Field name made lowercase.
    po_no = models.TextField(db_column='PO_NO', blank=True, null=True)  # Field name made lowercase.
    product = models.TextField(db_column='PRODUCT', blank=True, null=True)  # Field name made lowercase.
    project = models.TextField(db_column='PROJECT', blank=True, null=True)  # Field name made lowercase.
    qty1 = models.FloatField(db_column='QTY1', blank=True, null=True)  # Field name made lowercase.
    qty2 = models.FloatField(db_column='QTY2', blank=True, null=True)  # Field name made lowercase.
    receipt_id = models.TextField(db_column='RECEIPT_ID', blank=True, null=True)  # Field name made lowercase.
    reconciled = models.TextField(db_column='RECONCILED', blank=True, null=True)  # Field name made lowercase.
    retirement_amt = models.TextField(db_column='RETIREMENT_AMT', blank=True, null=True)  # Field name made lowercase.
    retirement_period = models.TextField(db_column='RETIREMENT_PERIOD', blank=True, null=True)  # Field name made lowercase.
    reval_curr = models.TextField(db_column='REVAL_CURR', blank=True, null=True)  # Field name made lowercase.
    sales_tax_rate_id = models.TextField(db_column='SALES_TAX_RATE_ID', blank=True, null=True)  # Field name made lowercase.
    sale_tax_trans_index = models.TextField(db_column='SALE_TAX_TRANS_INDEX', blank=True, null=True)  # Field name made lowercase.
    source_currency = models.TextField(db_column='SOURCE_CURRENCY', blank=True, null=True)  # Field name made lowercase.
    source_gross_trans_id = models.TextField(db_column='SOURCE_GROSS_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    source_port = models.TextField(db_column='SOURCE_PORT', blank=True, null=True)  # Field name made lowercase.
    source_sales_tax_trans_id = models.TextField(db_column='SOURCE_SALES_TAX_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    source_table = models.TextField(db_column='SOURCE_TABLE', blank=True, null=True)  # Field name made lowercase.
    src_alloc_trans_id = models.TextField(db_column='SRC_ALLOC_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    src_cn_trans_id = models.TextField(db_column='SRC_CN_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    src_trans_id_at = models.TextField(db_column='SRC_TRANS_ID_AT', blank=True, null=True)  # Field name made lowercase.
    src_vir_trans_id = models.TextField(db_column='SRC_VIR_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    stat1_amt = models.FloatField(db_column='STAT1_AMT', blank=True, null=True)  # Field name made lowercase.
    stat1_qty1 = models.FloatField(db_column='STAT1_QTY1', blank=True, null=True)  # Field name made lowercase.
    stat1_qty2 = models.FloatField(db_column='STAT1_QTY2', blank=True, null=True)  # Field name made lowercase.
    stat2_amt = models.FloatField(db_column='STAT2_AMT', blank=True, null=True)  # Field name made lowercase.
    stat2_qty1 = models.TextField(db_column='STAT2_QTY1', blank=True, null=True)  # Field name made lowercase.
    stat2_qty2 = models.TextField(db_column='STAT2_QTY2', blank=True, null=True)  # Field name made lowercase.
    sub_acct = models.TextField(db_column='SUB_ACCT', blank=True, null=True)  # Field name made lowercase.
    summary_trans_id = models.TextField(db_column='SUMMARY_TRANS_ID', blank=True, null=True)  # Field name made lowercase.
    summary_trans_pct = models.TextField(db_column='SUMMARY_TRANS_PCT', blank=True, null=True)  # Field name made lowercase.
    system_date = models.DateTimeField(db_column='SYSTEM_DATE', blank=True, null=True)  # Field name made lowercase.
    system_time = models.TextField(db_column='SYSTEM_TIME', blank=True, null=True)  # Field name made lowercase.
    system_user_id = models.TextField(db_column='SYSTEM_USER_ID', blank=True, null=True)  # Field name made lowercase.
    target_document = models.TextField(db_column='TARGET_DOCUMENT', blank=True, null=True)  # Field name made lowercase.
    target_name = models.TextField(db_column='TARGET_NAME', blank=True, null=True)  # Field name made lowercase.
    target_table = models.TextField(db_column='TARGET_TABLE', blank=True, null=True)  # Field name made lowercase.
    ten99_code = models.TextField(db_column='TEN99_CODE', blank=True, null=True)  # Field name made lowercase.
    tract_id = models.TextField(db_column='TRACT_ID', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    virtual_flag = models.TextField(db_column='VIRTUAL_FLAG', blank=True, null=True)  # Field name made lowercase.
    voucher = models.ForeignKey(Voucher,db_column='VOUCHER', on_delete=models.CASCADE, blank=True, null=True)               # models.TextField(db_column='VOUCHER', blank=True, null=True)  # Field name made lowercase.
    wht_amt = models.TextField(db_column='WHT_AMT', blank=True, null=True)  # Field name made lowercase.
    wht_rate = models.TextField(db_column='WHT_RATE', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.TextField(blank=True, null=True)
    gen_acc = models.ForeignKey(CoaGen,db_column='gen_acc', on_delete=models.CASCADE, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'TRANS'
        indexes = [
            models.Index(fields=['acct','acctg_period', 'gen_acc']),
        ]


class ApInv(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    acct = models.CharField(max_length=12, blank=True, null=True)
    acctg_period = models.DateTimeField(blank=True, null=True)
    advice_remarks = models.CharField(max_length=668, blank=True, null=True)
    amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    appr_inits = models.CharField(max_length=5, blank=True, null=True)
    appr_profile = models.CharField(max_length=7, blank=True, null=True)
    bal = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    bank_acct = models.CharField(max_length=10, blank=True, null=True)
    company = models.CharField(max_length=4, blank=True, null=True)
    credit_terms = models.CharField(max_length=5, blank=True, null=True)
    disb_select_flag = models.CharField(max_length=12, blank=True, null=True)
    document_ref = models.CharField(max_length=3, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    existing_invoice = models.CharField(max_length=5, blank=True, null=True)
    hold_tax_acct = models.CharField(max_length=10, blank=True, null=True)
    image_ref = models.CharField(max_length=122, blank=True, null=True)
    int_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    int_bal = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    int_override_amt_to_pay = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    int_pmt_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    int_prov_disc_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    int_undist_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    int_vat_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    invoice_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_no_r = models.CharField(max_length=30, blank=True, null=True)
    jur_tax_table_id = models.CharField(max_length=8, blank=True, null=True)
    occur_date = models.DateTimeField(blank=True, null=True)
    override_amt_to_pay = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    paid_in_full_period = models.DateTimeField(blank=True, null=True)
    pay_disp = models.CharField(max_length=4, blank=True, null=True)
    pmt_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    prov_disc_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    recd_date = models.DateTimeField(blank=True, null=True)
    revalue_flag = models.CharField(max_length=7, blank=True, null=True)
    sep_chk = models.CharField(max_length=3, blank=True, null=True)
    source_currency = models.CharField(max_length=4, blank=True, null=True)
    std_ap_inv_id = models.CharField(max_length=26, blank=True, null=True)
    system_date = models.DateTimeField(blank=True, null=True)
    system_time = models.CharField(max_length=8, blank=True, null=True)
    system_user_id = models.CharField(max_length=8, blank=True, null=True)
    tax_acct = models.CharField(max_length=10, blank=True, null=True)
    tax_code = models.CharField(max_length=8, blank=True, null=True)
    tax_hold = models.CharField(max_length=4, blank=True, null=True)
    ten99_code = models.CharField(max_length=5, blank=True, null=True)
    tracking_flag = models.CharField(max_length=5, blank=True, null=True)
    undist_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    vat_amt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=19, decimal_places=8, blank=True, null=True)
    vendor = models.CharField(max_length=7, blank=True, null=True)
    vendor_id = models.CharField(max_length=8, blank=True, null=True)
    voucher = models.CharField(max_length=16, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ap_inv'



class CcType(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    alloc_enabled = models.CharField(max_length=10, blank=True, null=True)
    at_enabled = models.CharField(max_length=7, blank=True, null=True)
    category = models.CharField(max_length=4, blank=True, null=True)
    cc_type_code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=42, blank=True, null=True)
    eng_well_count_flag = models.CharField(max_length=5, blank=True, null=True)
    pui_usage = models.CharField(max_length=10, blank=True, null=True)
    report_heading = models.CharField(max_length=24, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cc_type'





class DataDictionaryTables(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    base_table_name = models.CharField(max_length=20, blank=True, null=True)
    dd_field_alias = models.CharField(max_length=20, blank=True, null=True)
    desc_field = models.CharField(db_column='desc_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    hidden = models.CharField(max_length=20, blank=True, null=True)
    nexus_table_pk = models.CharField(max_length=30, blank=True, null=True)
    nexus_table_description = models.CharField(max_length=122, blank=True, null=True)
    nexus_table_name = models.CharField(max_length=44, blank=True, null=True)
    prefix = models.CharField(max_length=38, blank=True, null=True)
    subtype_field = models.CharField(max_length=20, blank=True, null=True)
    subtype_match_type = models.CharField(max_length=20, blank=True, null=True)
    subtype_value = models.CharField(max_length=20, blank=True, null=True)
    unidata_file_name = models.CharField(max_length=30, blank=True, null=True)
    unidata_orig_file_name = models.CharField(max_length=30, blank=True, null=True)
    xref_i_types = models.CharField(max_length=20, blank=True, null=True)
    xref_tables = models.CharField(max_length=20, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_dictionary_tables'





class Proj(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    accrual_flag = models.CharField(max_length=7, blank=True, null=True)
    afe_category = models.CharField(max_length=3, blank=True, null=True)
    afe_date = models.DateTimeField(blank=True, null=True)
    afe_type = models.CharField(max_length=4, blank=True, null=True)
    alloc_enabled = models.CharField(max_length=7, blank=True, null=True)
    appr = models.CharField(max_length=8, blank=True, null=True)
    appr_date = models.DateTimeField(blank=True, null=True)
    begin_cost_date = models.DateTimeField(blank=True, null=True)
    billing_project = models.CharField(max_length=10, blank=True, null=True)
    budgeted = models.CharField(max_length=4, blank=True, null=True)
    budget_total = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    budget_year = models.CharField(max_length=4, blank=True, null=True)
    coding_flag = models.CharField(max_length=2, blank=True, null=True)
    company = models.CharField(max_length=4, blank=True, null=True)
    complete_flag = models.CharField(max_length=8, blank=True, null=True)
    cost_approval_date = models.DateTimeField(blank=True, null=True)
    cost_center = models.CharField(max_length=8, blank=True, null=True)
    description = models.CharField(max_length=812, blank=True, null=True)
    dflt_company_access = models.CharField(max_length=7, blank=True, null=True)
    discrete_bill_flag = models.CharField(max_length=8, blank=True, null=True)
    end_cost_date = models.DateTimeField(blank=True, null=True)
    expense_category = models.CharField(max_length=4, blank=True, null=True)
    exp_date = models.DateTimeField(blank=True, null=True)
    formation = models.CharField(max_length=9, blank=True, null=True)
    manager = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=383, blank=True, null=True)
    operator_afe = models.CharField(max_length=16, blank=True, null=True)
    priority = models.CharField(max_length=5, blank=True, null=True)
    project = models.CharField(max_length=33, blank=True, null=True)
    proj_no = models.CharField(max_length=33, blank=True, null=True)
    recalc_flag = models.CharField(max_length=2, blank=True, null=True)
    reclass_code = models.CharField(max_length=7, blank=True, null=True)
    results = models.CharField(max_length=4, blank=True, null=True)
    results_date = models.DateTimeField(blank=True, null=True)
    rollup_project = models.CharField(max_length=19, blank=True, null=True)
    sponsor_company = models.CharField(max_length=4, blank=True, null=True)
    status = models.CharField(max_length=4, blank=True, null=True)
    supplement_no = models.CharField(max_length=3, blank=True, null=True)
    supp_ref = models.CharField(max_length=7, blank=True, null=True)
    temp_acctg_period = models.DateTimeField(blank=True, null=True)
    tmp = models.CharField(max_length=4, blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proj'



class WellInfo(models.Model):
    u2_id = models.CharField(primary_key=True, max_length=255)
    api_well_no = models.CharField(max_length=18, blank=True, null=True)
    area = models.CharField(max_length=6, blank=True, null=True)
    basin = models.CharField(max_length=9, blank=True, null=True)
    cc_type = models.CharField(max_length=5, blank=True, null=True)
    company = models.CharField(max_length=3, blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)
    county = models.CharField(max_length=6, blank=True, null=True)
    date_of_first_sale = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=3904, blank=True, null=True)
    district = models.CharField(max_length=7, blank=True, null=True)
    field_id = models.CharField(max_length=6, blank=True, null=True)
    first_gas_prod_date = models.DateTimeField(blank=True, null=True)
    first_oil_prod_date = models.DateTimeField(blank=True, null=True)
    first_water_prod_date = models.DateTimeField(blank=True, null=True)
    gas_profile = models.CharField(max_length=6, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    input_user = models.CharField(max_length=5, blank=True, null=True)
    in_service_period = models.DateTimeField(blank=True, null=True)
    jib_property = models.CharField(max_length=8, blank=True, null=True)
    joa = models.CharField(max_length=185, blank=True, null=True)
    last_status = models.CharField(max_length=5, blank=True, null=True)
    legal_desc_id = models.CharField(max_length=7, blank=True, null=True)
    master_rptg_deck = models.CharField(max_length=6, blank=True, null=True)
    meridian = models.CharField(max_length=9, blank=True, null=True)
    mms_sale_month_lagx = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=89, blank=True, null=True)
    nri_rptg_doi = models.CharField(max_length=4, blank=True, null=True)
    ocs_no = models.CharField(max_length=6, blank=True, null=True)
    office = models.CharField(max_length=6, blank=True, null=True)
    operator = models.CharField(max_length=9, blank=True, null=True)
    other_legal_desc = models.CharField(max_length=3904, blank=True, null=True)
    pool = models.CharField(max_length=5, blank=True, null=True)
    price_method = models.CharField(max_length=8, blank=True, null=True)
    prod_fac_id = models.CharField(max_length=8, blank=True, null=True)
    prospect = models.CharField(max_length=6, blank=True, null=True)
    pumper = models.CharField(max_length=9, blank=True, null=True)
    rollup_prop = models.CharField(max_length=8, blank=True, null=True)
    rrc_district = models.CharField(max_length=4, blank=True, null=True)
    shadow_key = models.CharField(max_length=14, blank=True, null=True)
    spacing_acres = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    spud_date = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    state_lease_no = models.CharField(max_length=10, blank=True, null=True)
    supervisor = models.CharField(max_length=9, blank=True, null=True)
    survey_method = models.CharField(max_length=6, blank=True, null=True)
    termination_date = models.DateTimeField(blank=True, null=True)
    termination_remarks = models.CharField(max_length=221, blank=True, null=True)
    termination_type = models.CharField(max_length=4, blank=True, null=True)
    total_depth = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    unit_rptg_deck = models.CharField(max_length=9, blank=True, null=True)
    user_code1 = models.CharField(max_length=30, blank=True, null=True)
    wi_rptg_deck = models.CharField(max_length=5, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    u2_checksum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'well_info'


