from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm


class FoodsAppConfig(AppHookConfig):

    class Meta(AppHookConfig.Meta):
        abstract = False
        verbose_name = u'Настройки на приложението'
        verbose_name_plural = u'Настройки на приложението'


class FoodsAppConfigForm(AppDataForm):
    pass


setup_config(FoodsAppConfigForm, FoodsAppConfig)