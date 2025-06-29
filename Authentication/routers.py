from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register("quardinators",QuardinatorsViews, basename="quardinators")
router.register("secretry",SecretryViews,basename="secretry")
router.register("trusherer",TrushererViews,basename="trusherer")
router.register("swifters",SwiftersViews,basename="swifters")
router.register("student",StudentViews,basename='studdnt')