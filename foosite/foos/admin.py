from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Location
from .models import Player
from .models import Singles
from .models import Doubles

admin.site.register(Question)
admin.site.register(Location)
admin.site.register(Player)
admin.site.register(Singles)
admin.site.register(Doubles)

