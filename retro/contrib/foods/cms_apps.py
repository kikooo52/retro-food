from cms.apphook_pool import apphook_pool
from cms.app_base import CMSApp

from aldryn_apphooks_config.app_base import CMSConfigApp

from .cms_appconfig import FoodsAppConfig
from .urls import urlpatterns


@apphook_pool.register
class FoodsApphook(CMSConfigApp):
    name = u'Храни'
    app_name = 'foods'
    #app_config = FoodsAppConfig

    def get_urls(self, page=None, language=None, **kwargs):
        return urlpatterns