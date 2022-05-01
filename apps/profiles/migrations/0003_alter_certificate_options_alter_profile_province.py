# Generated by Django 4.0.2 on 2022-03-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_province'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': 'گواهی', 'verbose_name_plural': 'گواهی\u200cها'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='province',
            field=models.CharField(choices=[('alborz', 'البرز'), ('ardabil', 'اردبیل'), ('east_azerbaijan', 'آذربایجان شرقی'), ('west_azerbaijan', 'آذربایجان غربی'), ('bushehr', 'بوشهر'), ('chahar_mahaal_and_bakhtiari', 'چهار محال و بختیاری'), ('fars', 'فارس'), ('gilan', 'گیلان'), ('golestan', 'گلستان'), ('hamadan', 'همدان'), ('hormozgan', 'هرمزگان'), ('ilam', 'ایلام'), ('isfahan', 'اصفهان'), ('kerman', 'کرمان'), ('kermanshah', 'کرمانشاه'), ('north_khorasan', 'خراسان شمالی'), ('razavi_khorasan', 'خراسان رضوی'), ('south_khorasan', 'خراسان جنوبی'), ('khuzestan', 'خوزستان'), ('kohgiluyeh_and_boyer_ahmad', 'کهکیلویه و بویر احمد'), ('kurdistan', 'کردستان'), ('lorestan', 'لرستان'), ('markazi', 'مرکزی'), ('mazandaran', 'مازندران'), ('qazvin', 'قزوین'), ('qom', 'قم'), ('semnan', 'سمنان'), ('sistan_and_baluchestan', 'سیستان و بلوچستان'), ('tehran', 'تهران'), ('yazd', 'یزد'), ('zanjan', 'زنجان')], help_text='استان محل ساختمان', max_length=27, verbose_name='استان محل سکونت'),
        ),
    ]
