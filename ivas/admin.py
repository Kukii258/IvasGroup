import os

from django.contrib import admin, messages
from django.contrib.admin import helpers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms.models import modelform_factory
from django.utils.html import format_html

from .models import Slika
from .forms import FileFieldForm


@admin.action(description="Dodaj Mapu Slika")
def import_slike(modeladmin, request, queryset):
    form = None

    if "upload" in request.POST:
        form = FileFieldForm(request.POST, request.FILES)

        if form.is_valid():
            category = request.POST.get('kategorija')
            files = request.FILES.getlist("file_field")  # Get all uploaded files

            for uploaded_file in files:
                modeladmin.model.objects.create(slika=uploaded_file, kategorija=category)

            messages.success(request, f"Successfully uploaded {len(files)} files.")
            model_meta = modeladmin.model._meta
            return HttpResponseRedirect(reverse(f"admin:{model_meta.app_label}_{model_meta.model_name}_changelist"))

    if not form:
        form = FileFieldForm(initial={"_selected_action": request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)})
        form.fields['kategorija'].choices = Slika.CATEGORY_CHOICES  # Populate choices for category

    return render(request, "html/upload_slike.html", {"upload_form": form, "categories": Slika.CATEGORY_CHOICES})


@admin.register(Slika)
class SlikaAdmin(admin.ModelAdmin):
    list_display = ("get_naslov_or_filename", "media_display", "datum_uploada", "kategorija")
    actions = [import_slike]

    @admin.display(description="Naslov")
    def get_naslov_or_filename(self, obj):
        if obj.naslov:
            return obj.naslov
        elif obj.slika:
            return os.path.basename(obj.slika.name) if obj.slika else "-"
        return "-"

    @admin.display(description="Slika")
    def media_display(self, obj):
        if obj.slika:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.slika.url)
        return "-"

    def changelist_view(self, request, extra_context=None):
        if request.POST.get("action") == "import_slike":
            if not request.POST.getlist(helpers.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                post.setlist(helpers.ACTION_CHECKBOX_NAME, [str(p.id) for p in self.model.objects.all()])
                request.POST = post
        return super().changelist_view(request, extra_context)

    def run_make_slike(self, request):
        import_slike(self, request, None)
        messages.success(request, "Slike uspješno dodane")
        return HttpResponseRedirect(request.headers.get("referer", "/"))




