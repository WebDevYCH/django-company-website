from django.dispatch import Signal


object_liked = Signal(providing_args=["like", "request"])
object_unliked = Signal(providing_args=["object", "request"])
