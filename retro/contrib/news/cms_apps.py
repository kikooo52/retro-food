from cms.apphook_pool import apphook_pool
from cms.app_base import CMSApp

from aldryn_apphooks_config.app_base import CMSConfigApp

from .cms_appconfig import NewsAppConfig
from .urls import urlpatterns


@apphook_pool.register
class NewsApphook(CMSApp):
    # app_config = NewsAppConfig
    app_name = "news"
    name = "News Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return urlpatterns
