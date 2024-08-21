from django.contrib import admin

# Register your models here.

from .models.user import User
from .models.role import Role
from .models.division import Division
from .models.center import Center
from .models.industry import Industry
from .models.user_type import UserType
from .models.reset_password import ResetPassword
from .models.raw_material import RawMaterial
from .models.raw_materialbach import RawMaterialBatch
from .models.source import Sources
from .models.supplier import Suppliers
from .models.acceptance_test_result import AcceptanceTestResult
from .models.acceptance_test import AcceptanceTest
from .models.unit import Unit
from.models.test_result import TestResult
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Division)
admin.site.register(Center)
admin.site.register(Industry)
admin.site.register(UserType)
admin.site.register(AcceptanceTest)
admin.site.register(RawMaterial)
admin.site.register(ResetPassword)
admin.site.register(RawMaterialBatch)
admin.site.register(Sources)
admin.site.register(Suppliers)
admin.site.register(AcceptanceTestResult)
admin.site.register(Unit)
admin.site.register(TestResult)