from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_bal = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.account_bal} - {self.user.username}"


class Package(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    charge = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class WingManager(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name


class Wing(models.Model):
    wing_manager = models.ForeignKey(WingManager, on_delete = models.CASCADE)
    wing_name = models.CharField(max_length = 50)
    wing_number = models.BigIntegerField(null = True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.wing_name


class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    wing = models.ForeignKey(Wing, on_delete = models.CASCADE)
    package = models.ForeignKey(Package, on_delete = models.CASCADE)
    room_number = models.IntegerField(unique=True)
    room_tag = models.CharField(max_length = 10, default="NEW")
    condition = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    image1 = models.FileField(default="default.png")
    image2 = models.FileField(default="default.png")
    image3 = models.FileField(default="default.png")
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.package.name} - {self.room_number}"


class RoomService(models.Model):
    wing = models.ForeignKey(Wing, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name


class SuiteRequest(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    nights = models.IntegerField(default=1)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.room.room_number}"


class HelpRequest(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.CharField(max_length = 40)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.first_name} - {self.subject}"


class RoomServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    subject = models.CharField(max_length = 40)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.room.room_number}"


class SuiteChange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_from = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name="room_from")
    room_to = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name="room_to")
    reason = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Transfer {self.user.first_name} From Suite {self.room_from.room_number} To Suite {self.room_to.room_number}"


class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 200)
    card_number = models.CharField(max_length=20)
    cvv = models.CharField(max_length = 6)
    expire = models.CharField(max_length = 6)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username


class Guideline(models.Model):
    rule = models.TextField()
    guideline1 = models.CharField(max_length = 250)
    guideline2 = models.CharField(max_length = 250)
    guideline3 = models.CharField(max_length = 250)
    guideline4 = models.CharField(max_length = 250)
    guideline5 = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.rule[:20]}"


class FAQ(models.Model):
    fullname = models.CharField(max_length=100)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question