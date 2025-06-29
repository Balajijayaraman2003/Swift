from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()

router.register("fund",FundViews,basename="fund")
router.register("expence",ExpenceViews,basename="expence")