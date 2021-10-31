from django.db import models

class states(models.Model):
    statename = models.CharField(db_column='stateName', max_length=255, null=False)  # Field name made lowercase.
    stateabrv = models.CharField(db_column='stateabrv', max_length=2, primary_key=True)
    class Meta:
        managed = False
        db_table = 'states'

class results(models.Model):
    statename = models.CharField(db_column='stateName', max_length=255, null=False, primary_key=True)  # Field name made lowercase.
    result = models.CharField(db_column='result', max_length=1, null=False)  # Field name made lowercase.
    demvotes = models.IntegerField(db_column='demVotes', null=False)
    repvotes = models.IntegerField(db_column='repVotes', null=False)
    othervotes = models.IntegerField(db_column='otherVotes', null=False)
    dempercent = models.FloatField(db_column='demPercent', null=False)
    reppercent = models.FloatField(db_column='repPercent', null=False)
    otherpercent = models.FloatField(db_column='otherPercent', null=False)
    stateid = models.CharField(db_column='stateID', max_length=2)
    class Meta:
        managed = False
        db_table = 'results'
