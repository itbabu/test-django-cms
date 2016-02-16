from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class BiologicoApphook(CMSApp):
    name = _("Demo Apphook")
    urls = ["demo_app.urls", ]


apphook_pool.register(BiologicoApphook)
