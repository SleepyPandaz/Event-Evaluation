
from django.db import migrations, models


class Migration(migrations.Migration):
    
    initial = True
    
    dependencies = [
        ]
    
    operations = [
        migrations.CreateModel(
            name = 'Groups',
            fields=[
                ('groupName', models.CharField(max_length=200)),
                ],
            ),
            
            
            
            
            ]