from import_export import resources
from .models import Name

class PersonResource(resources.ModelResource):
    class Meta:
        model = Name