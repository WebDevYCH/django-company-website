from django.apps import AppConfig


class CommentConfig(AppConfig):
    name = 'apps.comment'
    verbose_name = 'Comment management'

    def ready(self):
        super(CommentConfig,self).ready()
        from . import signals
