# Generated by Django 4.0.2 on 2022-03-16 09:29

import apps.utils.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', apps.utils.fields.JalaliAutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='تاریخ عضویت')),
                ('modified', apps.utils.fields.JalaliAutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='آخرین ویرایش')),
                ('status', models.CharField(choices=[('published', 'منتشر شده'), ('draft', 'چرک\u200cنویس')], default='draft', max_length=9, verbose_name='وضعیت')),
                ('title', models.CharField(help_text='لطفا برای شناسایی بهتر ساختمان یک عنوان برای ساختمان انتخاب کنید. مثلا: پروژه\u200cی ساختمانی ایپک', max_length=255, verbose_name='عنوان ساختمان')),
                ('province', models.CharField(choices=[('alborz', 'البرز'), ('ardabil', 'اردبیل'), ('east_azerbaijan', 'آذربایجان شرقی'), ('west_azerbaijan', 'آذربایجان غربی'), ('bushehr', 'بوشهر'), ('chahar_mahaal_and_bakhtiari', 'چهار محال و بختیاری'), ('fars', 'فارس'), ('gilan', 'گیلان'), ('golestan', 'گلستان'), ('hamadan', 'همدان'), ('hormozgan', 'هرمزگان'), ('ilam', 'ایلام'), ('isfahan', 'اصفحان'), ('kerman', 'کرمان'), ('kermanshah', 'کرمانشاه'), ('north_khorasan', 'خراسان شمالی'), ('razavi_khorasan', 'خراسان رضوی'), ('south_khorasan', 'خراسان جنوبی'), ('khuzestan', 'خوزستان'), ('kohgiluyeh_and_boyer_ahmad', 'کهکیلویه و بویر احمد'), ('kurdistan', 'کردستان'), ('lorestan', 'لرستان'), ('markazi', 'مرکزی'), ('mazandaran', 'مازندران'), ('qazvin', 'قزوین'), ('qom', 'قم'), ('semnan', 'سمنان'), ('sistan_and_baluchestan', 'سیستان و بلوچستان'), ('tehran', 'تهران'), ('yazd', 'یزد'), ('zanjan', 'زنجان')], help_text='استان محل ساختمان', max_length=27, verbose_name='استان')),
                ('city', models.CharField(help_text='شهر محل ساختمان', max_length=50, verbose_name='شهر')),
                ('district', models.CharField(help_text='محله یا ناحیه ساختمان. مثلا: منطقه ۸، هفت حوض', max_length=100, verbose_name='محله')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employer', verbose_name='کارفرما')),
            ],
            options={
                'verbose_name': 'ساختمان',
                'verbose_name_plural': 'ساختمان\u200cها',
            },
        ),
    ]