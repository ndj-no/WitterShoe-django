from django.contrib import admin
from .models import *

admin.site.site_header = 'Bảng điều khiển - Witter'

admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Shoe)
admin.site.register(Image)
admin.site.register(DetailShoe)
