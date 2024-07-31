from django.contrib import admin

# Register your models here.

from .models.user import User
from .models.role import Role
from .models.division import Division
from .models.center import Center
from .models.industry import Industry
from .models.user_type import UserType

admin.site.register(Role)

admin.site.register(User)

admin.site.register(Division)
admin.site.register(Center)
admin.site.register(Industry)
admin.site.register(UserType)
