from django.apps import AppConfig


class PypConfig(AppConfig):
    name = 'pyp'
    
    def ready(self):
        import pyp.signals