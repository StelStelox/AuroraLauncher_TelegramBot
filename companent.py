from aiogram import Router
from dynaconf import Dynaconf
router = Router()
conf = Dynaconf(settings_files='conf/settings.yaml')