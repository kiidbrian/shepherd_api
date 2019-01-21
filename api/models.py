from django.db import models

class Abstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class User(Abstract):
    name = models.TextField()
    phone = models.TextField()
    email = models.EmailField(max_length=75)
    role = models.TextField()
    active = models.BooleanField(default=False)
    password = models.TextField()

    class Meta:
        pass

class Member(Abstract):
    name = models.TextField()
    phone = models.TextField()
    email = models.EmailField(max_length=75)
    address = models.TextField()

    class Meta:
        pass
    
class Attendance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    member_id = models.ForeignKey(Member, related_name="attendance", on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

