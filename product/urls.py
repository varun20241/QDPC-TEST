from django.contrib import admin
from .views.raw_material import RawMaterialAdd
from.views.raw_material import RawMatrialListFetchView
from .views.raw_material_batch import RawMatrialBatchFetchView,RawMatrialBatchAddView
from .views.raw_matrial_accepatance import RawMaterialAcceptanceTestAdd,RawMaterialAcceptanceTestList
from django.urls import path,include


urlpatterns = [

path('raw-material/', RawMatrialListFetchView.as_view(), name='raw-material'),
path('raw-material-add/', RawMaterialAdd.as_view(), name='raw-material-add'),
path('raw-material/<int:batch_id>/', RawMatrialListFetchView.as_view(), name='raw-material-update'),

path('rawmaterial-batch-fetch/', RawMatrialBatchFetchView.as_view(), name='raw-material-batch-fetch'),
path('rawmaterial-batch-fetch/<int:pk>/', RawMatrialBatchFetchView.as_view(), name='raw-material-batch-fetch-detail'),
path('rawmaterial-add-batch/', RawMatrialBatchAddView.as_view(), name='raw-material-batch-add'),

path('rawmaterial-acceptance-add/',RawMaterialAcceptanceTestAdd.as_view(),name='raw-material-acceptance-add'),
path('rawmaterial-acceptance-list/',RawMaterialAcceptanceTestList.as_view(),name='raw-material-acceptance-list'),




]


