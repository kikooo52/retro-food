from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm


class NewsAppConfig(AppHookConfig):
    pass


class NewsAppConfigForm(AppDataForm):
    pass


setup_config(NewsAppConfigForm, NewsAppConfig)
