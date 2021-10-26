from django.contrib import admin
from . models import Product,contact,Orders,OrderUpdate,ProductComment
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Product)
class pro(ImportExportActionModelAdmin):
    pass


admin.site.register(contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(ProductComment)
