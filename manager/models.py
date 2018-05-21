from django.db import models




class Dreyemainen(models.Model):
    entryno = models.IntegerField(primary_key=True, db_column='EntryNo')  # Field name made lowercase.
    entryword = models.TextField(db_column='EntryWord', blank=True, null=True)  # Field name made lowercase.
    kksymbol = models.TextField(db_column='KKsymbol', blank=True, null=True)  # Field name made lowercase.
    djsymbol = models.TextField(db_column='DJsymbol', blank=True, null=True)  # Field name made lowercase.
    online = models.TextField(db_column='Online', blank=True, null=True)  # Field name made lowercase.
    #modifydatetime = models.TextField(db_column='ModifyDateTime', blank=True, null=True)  # Field name made lowercase.
    modifydatetime = models.DateTimeField(db_column='ModifyDateTime')  # Field name made lowercase.    This field type is a guess.

    class Meta:
        db_table = 'DreyeMainEN'
        

class Dreyeendetail(models.Model):
    seqid = models.IntegerField(primary_key=True, db_column='SeqID')  # Field name made lowercase.
    #entryno = models.ForeignKey(Dreyemainen,db_column='EntryNo',on_delete=models.DO_NOTHING)
    entryno = models.IntegerField(db_column='EntryNo', blank=True, null=True)  # Field name made lowercase.
    entryword = models.TextField(db_column='EntryWord', blank=True, null=True)  # Field name made lowercase.
    orgcode = models.TextField(db_column='OrgCode', blank=True, null=True)  # Field name made lowercase.
    item = models.TextField(db_column='Item', blank=True, null=True)  # Field name made lowercase.
    groupno = models.TextField(db_column='GroupNo', blank=True, null=True)  # Field name made lowercase.
    itemcontent = models.TextField(db_column='ItemContent', blank=True, null=True)  # Field name made lowercase.
    enitem = models.TextField(db_column='EnItem', blank=True, null=True)  # Field name made lowercase.
    chitem = models.TextField(db_column='ChItem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'DreyeENDetail'