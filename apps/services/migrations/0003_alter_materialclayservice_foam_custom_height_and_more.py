# Generated by Django 4.0.2 on 2022-04-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_contractingconcreteservice_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialclayservice',
            name='foam_custom_height',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='foam_custom_length',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='foam_custom_thickness',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='foam_height',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(20, '۲۰')], help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='foam_length',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(20, '۲۰'), (25, '۲۵')], help_text='سانتی\u200cمتر', null=True, verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='foam_thickness',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(15, '۱۵')], help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='simple_custom_height',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='simple_custom_length',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='simple_custom_thickness',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='simple_dimensions',
            field=models.CharField(blank=True, choices=[('normal', 'ابعاد متعارف'), ('custom', 'سفارشی')], help_text='سانتی\u200cمتر', max_length=255, null=True, verbose_name='ابعاد مورد نیاز'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='simple_height',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(20, '۲۰')], help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='simple_length',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(20, '۲۰'), (25, '۲۵')], help_text='سانتی\u200cمتر', null=True, verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='materialclayservice',
            name='simple_thickness',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(7, '۷'), (10, '۱۰'), (15, '۱۵')], help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='concrete_custom_height',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='concrete_custom_length',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='concrete_custom_thickness',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='concrete_height',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(20, '۲۰')], help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='concrete_length',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(40, '۴۰')], help_text='سانتی\u200cمتر', null=True, verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='concrete_thickness',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(7, '۷'), (10, '۱۰'), (15, '۱۵'), (20, '۲۰')], help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='required_amount',
            field=models.PositiveSmallIntegerField(help_text='عدد', verbose_name='تعداد مورد نیاز'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='tuff_custom_height',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='tuff_custom_length',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='tuff_custom_thickness',
            field=models.PositiveSmallIntegerField(blank=True, help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='tuff_height',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(20, '۲۰')], help_text='سانتی\u200cمتر', null=True, verbose_name='ارتفاع'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='tuff_length',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(40, '۴۰')], help_text='سانتی\u200cمتر', null=True, verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='materialconcreteblockservice',
            name='tuff_thickness',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(7, '۷'), (10, '۱۰'), (15, '۱۵')], help_text='سانتی\u200cمتر', null=True, verbose_name='ضخامت'),
        ),
        migrations.AlterField(
            model_name='materialconcreteservice',
            name='resistance',
            field=models.PositiveSmallIntegerField(help_text='کیلوگرم بر سانتی\u200cمتر مربع', verbose_name='مقاومت مشخصه ۲۸ روزه'),
        ),
    ]
