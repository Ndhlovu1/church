from django.contrib import admin
from .models import blogDatabase

#Adding our Database file into the admin panel
#admin.site.register(blogDatabase)

#Used for Styling the Admin appearance of the Database
@admin.register(blogDatabase)
#The class is essential for telling Django how our admin interface should look like
class ChurchAdmin(admin.ModelAdmin):   


    #How to display our information
    list_display = ('title','author','status')

    #Filter
    list_filter = ('status','author','publish','created',)

    #Search in these field
    search_fields = ('title','body')

    #Auto Fill the Comments
    prepopulated_fields = {'slug':('title',)}

    #Auto add the author id fields
    raw_id_fields = ('author',)

    date_hierarchy = ('publish')

    ordering = ('status','publish',)






