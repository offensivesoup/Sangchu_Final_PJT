from django.db import models

class UserModel(models.Model):
    class Meta:
        db_table = "my_user_data"

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


# Create your models here.
class EmptyRoomData(models.Model):
    deposit = models.IntegerField(blank=True, null=True)
    month = models.SmallIntegerField(blank=True, null=True)
    criteria = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=20, decimal_places=6)
    lng = models.DecimalField(max_digits=20, decimal_places=6)
    address = models.CharField(max_length=10)
    when = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=10)
    my_area = models.CharField(max_length=10, blank=True, null=True)
    my_floor = models.CharField(max_length=10, blank=True, null=True)
    total_floor = models.CharField(max_length=10, blank=True, null=True)
    now = models.CharField(max_length=20, blank=True, null=True)
    recommend = models.CharField(max_length=50, blank=True, null=True)
    parking = models.CharField(max_length=10, blank=True, null=True)
    usage = models.CharField(max_length=20, blank=True, null=True)
    direction = models.CharField(max_length=20)
    index = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'empty_room_data'

class LikeModel(models.Model):
    class Meta:
        db_table = "like_data"
    # id
    user_id = models.ForeignKey(UserModel,
                                on_delete=models.CASCADE,
                                db_column= 'user_id',
                                null=False)
    maemul_id = models.ForeignKey(EmptyRoomData,
                                  on_delete=models.CASCADE,
                                  db_column='maemul_id',
                                  null=False)

