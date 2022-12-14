# Generated by Django 4.0.7 on 2022-08-12 00:41

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='your title', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='additional text', required=False))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
