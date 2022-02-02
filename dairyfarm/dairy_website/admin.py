from django.contrib import admin
from .models import  farmer_record
from .models import animal_record
from .models import vaccination
from .models import milk_record
from .models import deworming
from .models import questions
from .models import answer
admin.site.register(farmer_record)
admin.site.register(animal_record)
admin.site.register(milk_record)
admin.site.register(deworming)
admin.site.register(questions)
admin.site.register(answer)

admin.site.register(vaccination)

