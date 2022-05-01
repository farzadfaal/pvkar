from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from multiselectfield import MultiSelectField

from apps.utils.models import JalaliTimeStampedModel


class Category(models.TextChoices):
    # Contracting Service
    contracting_concrete = "contracting_concrete", "اجرای ساختمان بتنی"
    contracting_excavation = "contracting_excavation", "حفاری و گودبرداری"
    contracting_facing = "contracting_facing", "نما و سیمان‌کاری"
    contracting_gas = "contracting_gas", "لوله‌کشی گاز"
    contracting_nailing = "contracting_nailing", "نیلینگ"
    contracting_painting = "contracting_painting", "نقاشی"
    contracting_piling = "contracting_piling", "حفاری شمع"
    contracting_plastering = "contracting_plastering", "گچ‌کاری"
    contracting_plumbing = "contracting_plumbing", "لوله‌کشی"
    contracting_scaffolding = "contracting_scaffolding", "داربست"
    contracting_steel = "contracting_steel", "اجرای ساختمان فولادی"
    contracting_tiling = "contracting_tiling", "کاشی‌کاری"
    contracting_truss = "contracting_truss", "سازه نگهبان خرپایی"
    contracting_wall = "contracting_wall", "بنایی دیوارچینی"
    contracting_waterproofing = "contracting_waterproofing", "ایزوگام"
    contracting_wiring = "contracting_wiring", "سیم‌کشی"
    # Material Sales Service
    material_aac = "material_aac", "بلوک سبک AAC"
    material_beam = "material_beam", "تیرچه‌ی سقف"
    material_clay = "material_clay", "بلوک سفالی دیوار"
    material_concrete = "material_concrete", "بتن آماده"
    material_concrete_block = (
        "material_concrete_block",
        "بلوک سیمانی یا پوکه‌ای توخالی",
    )
    material_frame = "material_frame", "درب و پنجره"
    material_grains = "material_grains", "شن و ماسه"
    material_polystyrene = "material_polystyrene", "یونولیت"
    # Engineering Service
    engineering = "engineering", "مهندسی"
    # Insurance Service
    insurance_employee = "insurance_employee", "بیمه‌ی مسئولیت کارکنان"
    insurance_third_party = "insurance_third_party", "بیمه‌ی مسئولیت شخص ثالث"
    insurance_quality = "insurance_quality", "بیمه تضمین کیفیت"


def choices(start, end):
    choice_list = []
    for choice in range(start, end):
        choice_list.append((choice, f"{choice}"))
    return choice_list


class Service(JalaliTimeStampedModel):
    category = models.CharField(
        "نوع سرویس", max_length=25, choices=Category.choices, null=True
    )
    extra_info = models.TextField(
        "توضیحات اضافی",
        null=True,
        blank=True,
        help_text="توضیحات اضافی برای مواردی که ضروریست یا در گزینه‌های فوق وجود ندارد",
    )

    class Meta:
        abstract = True


class MaterialAACService(Service):
    required_quantity = models.PositiveIntegerField("تعداد مورد نیاز‌", help_text="عدد")
    required_dimensions = models.CharField(
        "ابعاد مورد نیاز",
        max_length=6,
        choices=(("normal", "متعارف"), ("custom", "سفارشی")),
    )
    thickness = models.PositiveSmallIntegerField(
        "ضخامت",
        choices=(
            (8, "۸"),
            (10, "۱۰"),
            (12, "۱۲"),
            (15, "۱۵"),
            (20, "۲۰"),
        ),
        blank=True,
        null=True,
        help_text="سانتی‌متر",
    )
    height = models.PositiveSmallIntegerField(
        "ارتفاع",
        choices=((20, "۲۰"), (25, "۲۵")),
        blank=True,
        null=True,
        help_text="سانتی‌متر",
    )
    length = models.PositiveSmallIntegerField(
        "طول",
        choices=((60, "۶۰"),),
        blank=True,
        null=True,
        help_text="سانتی‌متر",
    )
    custom_thickness = models.PositiveSmallIntegerField(
        "ضخامت سفارشی", blank=True, null=True, help_text="سانتی‌متر"
    )
    custom_height = models.PositiveSmallIntegerField(
        "ارتفاع سفارشی", blank=True, null=True, help_text="سانتی‌متر"
    )
    custom_length = models.PositiveSmallIntegerField(
        "طول سفارشی", blank=True, null=True, help_text="سانتی‌متر"
    )
    transport = models.BooleanField("هزینه‌ی حمل", default=False)
    palette = models.BooleanField("پالت", default=False)
    glue = models.BooleanField("هزینه‌ی چسب", default=False)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - بلوک سبک AAC"
        verbose_name_plural = "خدمات فروش مصالح - بلوک سبک AAC"


class MaterialBeamService(Service):
    type = models.CharField(
        "جنس",
        max_length=255,
        default="concrete",
        choices=(("concrete", "بتنی"), ("steel", "فلزی")),
    )
    implementation_area = models.CharField(
        "محل استفاده",
        max_length=255,
        default="residential",
        choices=(
            ("parking", "پارکینگ"),
            ("residential", "مسکونی"),
            ("commercial", "تجاری"),
            ("other", "سایر"),
        ),
    )
    required_length = models.PositiveSmallIntegerField("طول مورد نیاز", help_text="متر")
    required_quantity = models.PositiveSmallIntegerField(
        "تعداد مورد نیاز", help_text="عدد"
    )
    transport = models.BooleanField("هزینه‌ی حمل", default=False)
    plan = models.FileField("نقشه مقطع تیرچه‌ها", max_length=255, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - تیرچه سقف"
        verbose_name_plural = "خدمات فروش مصالح - تیرچه‌ی سقف"


class MaterialClayService(Service):
    required_quantity = models.PositiveIntegerField("مقدار مورد نیاز", help_text="عدد")
    type = models.CharField(
        "نوع",
        max_length=255,
        choices=(("simple", "ساده"), ("foam", "فوم‌دار")),
        null=True,
        blank=True,
    )
    simple_dimensions = models.CharField(
        "ابعاد مورد نیاز",
        max_length=255,
        choices=(("normal", "ابعاد متعارف"), ("custom", "سفارشی")),
        blank=True,
        null=True,
        help_text="سانتی‌متر",
    )
    simple_thickness = models.PositiveSmallIntegerField(
        "ضخامت", choices=((7, "۷"), (10, "۱۰"), (15, "۱۵")), blank=True, null=True, help_text="سانتی‌متر",
    )
    simple_height = models.PositiveSmallIntegerField(
        "ارتفاع", choices=((20, "۲۰"),), blank=True, null=True, help_text="سانتی‌متر",
    )
    simple_length = models.PositiveSmallIntegerField(
        "طول", choices=((20, "۲۰"), (25, "۲۵")), blank=True, null=True, help_text="سانتی‌متر",
    )
    simple_custom_thickness = models.PositiveSmallIntegerField(
        "ضخامت", blank=True, null=True, help_text="سانتی‌متر",
    )
    simple_custom_height = models.PositiveSmallIntegerField(
        "ارتفاع", blank=True, null=True, help_text="سانتی‌متر",
    )
    simple_custom_length = models.PositiveSmallIntegerField(
        "طول", blank=True, null=True, help_text="سانتی‌متر",
    )
    foam_dimensions = models.CharField(
        "ابعاد مورد نیاز",
        max_length=255,
        choices=(("normal", "ابعاد متعارف"), ("custom", "سفارشی")),
        blank=True,
        null=True,
    )
    foam_thickness = models.PositiveSmallIntegerField(
        "ضخامت", choices=((15, "۱۵"),), blank=True, null=True, help_text="سانتی‌متر",
    )
    foam_height = models.PositiveSmallIntegerField(
        "ارتفاع", choices=((20, "۲۰"),), blank=True, null=True, help_text="سانتی‌متر",
    )
    foam_length = models.PositiveSmallIntegerField(
        "طول", choices=((20, "۲۰"), (25, "۲۵")), blank=True, null=True, help_text="سانتی‌متر",
    )
    foam_custom_thickness = models.PositiveSmallIntegerField(
        "ضخامت", blank=True, null=True, help_text="سانتی‌متر",
    )
    foam_custom_height = models.PositiveSmallIntegerField(
        "ارتفاع", blank=True, null=True, help_text="سانتی‌متر",
    )
    foam_custom_length = models.PositiveSmallIntegerField(
        "ضخامت", blank=True, null=True, help_text="سانتی‌متر",
    )
    transport = models.BooleanField("به همراه هزینه‌ی حمل", default=False)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - بلوک سفالی دیوار"
        verbose_name_plural = "خدمات فروش مصالح - بلوک سفالی دیوار"


class MaterialConcreteService(Service):
    required_amount = models.IntegerField(
        "مقدار تقریبی مورد نیاز", null=True, help_text="متر مکعب"
    )
    concreting_area = models.CharField(
        "محل بتن‌ریزی",
        max_length=250,
        choices=(
            ("column", "ستون"),
            ("ceiling", "سقف"),
            ("foundation", "فونداسیون"),
        ),
        default="column",
    )
    story = models.SmallIntegerField(
        "طبقه",
        validators=[MaxValueValidator(40), MinValueValidator(-10)],
        choices=choices(-10, 41),
        default=1,
    )
    pump_type = models.CharField(
        "نوع پمپ درخواستی",
        max_length=250,
        choices=(
            ("ground_pump", "زمینی"),
            ("air_pump", "هوایی"),
            ("custom", "به انتخاب فروشنده"),
        ),
        default="ground_pump",
    )
    resistance = models.PositiveSmallIntegerField(
        "مقاومت مشخصه ۲۸ روزه",
        help_text="کیلوگرم بر سانتی‌متر مربع"
    )
    required_slump = models.PositiveSmallIntegerField(
        "اسلامپ مورد نیاز", choices=choices(0, 31), default=0
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - بتن آماده"
        verbose_name_plural = "خدمات فروش مصالح - بتن آماده"


class MaterialConcreteBlockService(Service):
    required_amount = models.PositiveSmallIntegerField("تعداد مورد نیاز", help_text="عدد", )
    type = models.CharField(
        "جنس",
        max_length=255,
        choices=(("concrete", "سیمانی"), ("tuff", "پوکه")),
        blank=True,
        null=True,
    )

    # Type: Concrete
    concrete_dimensions = models.CharField(
        "ابعاد مورد نیاز",
        max_length=255,
        choices=(("normal", "ابعاد متعارف"), ("custom", "سفارشی")),
        blank=True,
        null=True,
    )
    concrete_thickness = models.PositiveSmallIntegerField(
        "ضخامت",
        choices=((7, "۷"), (10, "۱۰"), (15, "۱۵"), (20, "۲۰")),
        blank=True,
        null=True,
        help_text="سانتی‌متر",
    )
    concrete_height = models.PositiveSmallIntegerField(
        "ارتفاع", choices=((20, "۲۰"),), blank=True, null=True, help_text="سانتی‌متر",
    )
    concrete_length = models.PositiveSmallIntegerField(
        "طول", choices=((40, "۴۰"),), blank=True, null=True, help_text="سانتی‌متر",
    )
    concrete_custom_thickness = models.PositiveSmallIntegerField(
        "ضخامت", blank=True, null=True, help_text="سانتی‌متر",
    )
    concrete_custom_height = models.PositiveSmallIntegerField(
        "ارتفاع", blank=True, null=True, help_text="سانتی‌متر",
    )
    concrete_custom_length = models.PositiveSmallIntegerField(
        "طول", blank=True, null=True, help_text="سانتی‌متر",
    )

    # Type: Tuff
    tuff_dimensions = models.CharField(
        "ابعاد مورد نیاز",
        max_length=255,
        choices=(("normal", "ابعاد متعارف"), ("custom", "سفارشی")),
        blank=True,
        null=True,
    )
    tuff_thickness = models.PositiveSmallIntegerField(
        "ضخامت", choices=((7, "۷"), (10, "۱۰"), (15, "۱۵")), blank=True, null=True, help_text="سانتی‌متر",
    )
    tuff_height = models.PositiveSmallIntegerField(
        "ارتفاع", choices=((20, "۲۰"),), blank=True, null=True, help_text="سانتی‌متر",
    )
    tuff_length = models.PositiveSmallIntegerField(
        "طول", choices=((40, "۴۰"),), blank=True, null=True, help_text="سانتی‌متر",
    )
    tuff_custom_thickness = models.PositiveSmallIntegerField(
        "ضخامت", blank=True, null=True, help_text="سانتی‌متر",
    )
    tuff_custom_height = models.PositiveSmallIntegerField(
        "ارتفاع", blank=True, null=True, help_text="سانتی‌متر",
    )
    tuff_custom_length = models.PositiveSmallIntegerField("طول", blank=True, null=True, help_text="سانتی‌متر", )

    transport = models.BooleanField("به همراه هزینه‌ی حمل", default=False)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - بلوک سیمانی یا پوکه‌ای توخالی"
        verbose_name_plural = "خدمات فروش مصالح - بلوک سیمانی یا پوکه‌ای توخالی"


class MaterialFrameService(Service):
    required_area = models.PositiveIntegerField(
        "سطح تقریبی مورد نیاز", default=0, help_text="متر مربع"
    )
    required_length = models.PositiveIntegerField(
        "طول پروفیل مورد نیاز", blank=True, help_text="متر"
    )
    glass_type = models.CharField(
        "نوع شیشه",
        max_length=255,
        choices=(
            ("double_glazed", "دو جداره"),
            ("triple_glazed", "سه جداره"),
            ("pleated_lace", "توری پلیسه"),
            ("sliding", "کشویی"),
            ("thermal_break", "ترمال بریک"),
            ("other", "سایر"),
        ),
        default="double_glazed",
    )
    profile_type = models.CharField("نوع پروفیل", max_length=255, blank=True)
    fitting_type = models.CharField("نوع یراق‌آلات", max_length=255, blank=True)
    plan = models.FileField(
        "نقشه ساختمان",
        max_length=255,
        upload_to="plans/",
        blank=True,
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - درب و پنجره UPVC"
        verbose_name_plural = "خدمات فروش مصالح - درب و پنجره UPVC"


class MaterialGrainsService(Service):
    material_type = models.TextField(
        "نوع مصالح",
        max_length=255,
        choices=(
            ("sand", "ماسه"),
            ("gravel", "شن"),
            ("stone", "لاشه‌سنگ"),
            ("tuff", "پوکه"),
        ),
        blank=True,
        null=True,
    )
    sand_type = models.CharField(
        "نوع ماسه",
        max_length=255,
        choices=(
            ("second_wash", "دوبارشور"),
            ("wind", "بادی"),
            ("soil", "خاک‌دار"),
            ("broken", "شکسته"),
        ),
        blank=True,
        null=True,
    )
    gravel_type = models.CharField(
        "نوع شن",
        max_length=255,
        choices=(("broken", "شکسته"), ("natural", "طبیعی")),
        blank=True,
        null=True,
    )
    gravel_size = models.CharField(
        "اندازه شن",
        max_length=255,
        choices=(("pea", "نخودی"), ("almond", "بادامی")),
        blank=True,
        null=True,
    )
    required_amount = models.PositiveSmallIntegerField(
        "مقدار تقریبی مورد نیاز", help_text="تن"
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - شن و ماسه"
        verbose_name_plural = "خدمات فروش مصالح - شن و ماسه"


class MaterialPolystyreneService(Service):
    required_amount = models.PositiveSmallIntegerField(
        "مقدار تقریبی مورد نیاز", help_text="متر مکعب"
    )
    type = models.CharField(
        "نوع",
        max_length=255,
        choices=(("sheet", "ورقه‌ای"), ("block", "بلوکی")),
        blank=True,
        null=True,
    )
    required_dimensions = models.CharField(
        "ابعاد مورد نیاز",
        max_length=255,
        choices=(("normal", "ابعاد متعارف"), ("custom", "سفارشی")),
        blank=True,
        null=True,
    )
    thickness = models.PositiveSmallIntegerField(
        "ضخامت",
        choices=((20, "۲۰"), (25, "۲۵")),
        blank=True,
        null=True,
        help_text="سانتی‌متر"
    )
    height = models.PositiveSmallIntegerField(
        "ارتفاع",
        choices=((50, "۵۰"), (60, "۶۵")),
        blank=True,
        null=True,
        help_text="سانتی‌متر"
    )
    length = models.PositiveSmallIntegerField(
        "طول",
        choices=((200, "۲۰۰"),),
        blank=True,
        null=True,
        help_text="سانتی‌متر"
    )
    custom_thickness = models.PositiveSmallIntegerField("ضخامت", blank=True, null=True, help_text="سانتی‌متر")
    custom_height = models.PositiveSmallIntegerField("ارتفاع", blank=True, null=True, help_text="سانتی‌متر")
    custom_length = models.PositiveSmallIntegerField("طول", blank=True, null=True, help_text="سانتی‌متر")
    weight = models.CharField(
        "وزن بلوک",
        max_length=255,
        choices=(
            ("0.8", "0.8 - 1.0"),
            ("1.0", "1.0 - 1.2"),
            ("1.2", "1.2 - 1.4"),
            ("1.4", "1.4 - 1.6"),
            ("1.6", "1.6 - 1.8"),
            ("1.8", "1.8 - 2.0"),
            ("2.0", "2.0 - 2.2"),
            ("2.2", "2.2 - 2.4"),
        ),
        blank=True,
        null=True,
        help_text="کیلوگرم"
    )
    sheet_type = models.CharField(
        "نوع ورق",
        max_length=255,
        choices=(("normal", "معمولی"), ("compressed", "فشرده")),
        blank=True,
        null=True,
    )
    particles_type = models.CharField(
        "نوع دانه",
        max_length=255,
        choices=(
            ("small", "ریز"),
            ("big", "درشت"),
            ("no_difference", "فرقی ندارد"),
        ),
        blank=True,
        null=True,
    )
    transport = models.BooleanField("به همراه هزینه‌ی حمل؟", default=False)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس فروش مصالح - یونولیت"
        verbose_name_plural = "خدمات فروش مصالح - یونولیت"


class EngineeringService(Service):
    engineering_type = models.CharField(
        "زمینه‌ی مهندسی",
        max_length=255,
        choices=(
            # labs
            ("lab_geotechnical", "آزمایشگاه خاک (ژئوتکنیک)"),
            ("lab_concrete", "آزمایشگاه بتن"),
            ("lab_weld", "آزمایشگاه جوش"),
            # design
            ("design_architectural", "طراحی معماری"),
            ("design_structure", "طراحی سازه"),
            ("design_mechanical", "طراحی مکانیک"),
            ("design_electrical", "طراحی برق"),
            (
                "design_complete",
                "طراحی رشته‌های چهارگانه به صورت یکجا (سازه، معماری، مکانیک، برق و در صورت نیاز شهرسازی و ترافیک)",
            ),
            ("design_retaining_wall", "طراحی سازه حائل"),
            ("design_civil", "طراحی شهرسازی"),
            ("design_traffic", "طراحی ترافیک"),
            # supervision
            ("supervision_architectural", "نظارت معماری"),
            ("supervision_structure", "نظارت سازه"),
            ("supervision_mechanical", "نظارت مکانیک"),
            ("supervision_electrical", "نظارت برق"),
            (
                "supervision_complete",
                "نظارت رشته‌های چهارگانه به صورت یکجا (سازه، معماری، مکانیک، برق و درصورت نیاز نقشه‌برداری)",
            ),
            # other
            ("other_constructor", "مجری (سازنده)"),
            ("other_surveying", "نقشه‌برداری"),
        ),
    )
    total_stories = models.PositiveSmallIntegerField(
        "تعداد کل طبقات سازه‌ای",
        default=1,
        validators=[MinValueValidator(1)],
    )
    building_type = models.CharField(
        "نوع سازه",
        max_length=255,
        choices=(("concrete", "بتنی"), ("steel", "فولادی")),
        default="concrete",
    )
    constructable_area = models.PositiveSmallIntegerField("مساحت زمین قابل ساخت", help_text="متر مربع")
    infrastructure_area = models.PositiveSmallIntegerField("متراژ کل زیربنا", help_text="متر مربع")

    total_basements = models.SmallIntegerField(
        "تعداد طبقات زیرزمین",
        choices=(
            (0, "۰"),
            (1, "۱"),
            (2, "۲"),
            (3, "۳"),
            (4, "۴"),
            (5, "۵"),
            (6, "۶"),
            (7, "۷"),
            (8, "۸"),
            (9, "۹"),
            (10, "۱۰"),
        ),
        default=0,
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس مهندسی"
        verbose_name_plural = "خدمات مهندسی"


class ContractingService(models.Model):
    start = models.CharField(
        "تاریخ تقریبی شروع پروژه",
        max_length=100,
        blank=True,
        null=True,
        help_text="مثلا: ۱۲ مهر ۱۴۰۱",
    )

    class Meta:
        abstract = True


class ContractingConcreteService(Service, ContractingService):
    foundation_type = models.CharField(
        "نوع فونداسیون",
        max_length=255,
        choices=(("expanded", "گسترده"), ("striped", "نواری")),
        default="expanded",
    )
    infrastructure_area = models.PositiveSmallIntegerField("زیربنای کل پروژه")
    ceiling_area = models.PositiveSmallIntegerField("متراژ هر سقف")
    ceiling_type = models.CharField(
        "نوع سقت",
        max_length=255,
        choices=(
            ("beam", "تیرچه"),
            ("waffle", "وافل"),
            ("concrete_wing", "بال بتنی"),
            ("other", "سایر"),
        ),
        default="beam",
    )
    total_ceilings = models.PositiveSmallIntegerField("تعداد کل سقف")
    total_basements = models.PositiveSmallIntegerField("تعداد کل زیرزمین", default=0)
    columns_concreting = models.CharField(
        "نوع بتن‌ریزی ستون‌ها",
        max_length=255,
        choices=(("manual", "دستی"), ("batching", "آماده")),
        default="manual",
    )
    plan = models.FileField("نقشه‌ی سازه‌ای", upload_to="plans/", blank=True)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - اجرای ساختمان بتنی"
        verbose_name_plural = "خدمات پیمانکاری - اجرای ساختمان بتنی"


class ContractingExcavationService(Service, ContractingService):
    excavation_volume = models.PositiveIntegerField("حجم خاک‌برداری", null=True)
    excavation_depth = models.PositiveIntegerField("عمق خاک‌برداری", null=True)
    area_image = models.ImageField(
        "تصویر محل خاک‌برداری", null=True, upload_to="area-images/"
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - حفاری و گودبرداری"
        verbose_name_plural = "خدمات پیمانکاری - حفاری و گودبرداری"


class ContractingFacingService(Service, ContractingService):
    total_area = models.PositiveSmallIntegerField("مساحت کل", null=True)
    opening_area = models.PositiveSmallIntegerField("مساحت بازشو", null=True)
    type = models.CharField(
        "نوع کار",
        max_length=255,
        null=True,
        choices=(("facing", "نماکاری"), ("concrete", "سیمان‌کاری ساده")),
        default="facing",
    )
    facing_type = models.CharField(
        "نوع نما",
        max_length=255,
        null=True,
        choices=(
            ("stone", "سنگی"),
            ("brick", "آجری"),
            ("composite", "کامپوزیت"),
            ("tile", "سرامیک"),
            ("other", "سایر"),
        ),
    )
    custom_facing = models.CharField(
        "توضیح دهید", max_length=255, null=True, blank=True
    )
    plan = models.FileField("نقشه‌ی معماری نما", null=True, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - نما و سیمان‌کاری"
        verbose_name_plural = "خدمات پیمانکاری - نما و سیمان‌کاری"


class ContractingGasService(Service, ContractingService):
    usecase = models.CharField(
        "کاربری ساختمان",
        max_length=255,
        null=True,
        choices=(
            ("residential", "مسکونی"),
            ("commercial", "تجاری"),
            ("warehouse", "انباری"),
            ("other", "سایر"),
        ),
    )
    total_suites = models.PositiveSmallIntegerField("تعداد کل واحد‌ها", null=True)
    average_area = models.PositiveSmallIntegerField("میانگین متراژ هر واحد", null=True)
    total_stories = models.PositiveSmallIntegerField("تعداد کل طبقات", null=True)
    total_parkings = models.PositiveSmallIntegerField(
        "تعداد کل طبقات پارکینگ", null=True
    )
    plan = models.FileField("نقشه‌ی تاسیسات", null=True, blank=True, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - لوله‌کشی گاز"
        verbose_name_plural = "خدمات پیمانکاری - لوله‌کشی گاز"


class ContractingNailingService(Service, ContractingService):
    total_area = models.PositiveSmallIntegerField("سطح کل دیواره‌ی گود", null=True)
    depth = models.PositiveSmallIntegerField("عمق گود", null=True)
    horizontal_distance = models.PositiveSmallIntegerField(
        "فواصل افقی نیل‌ها", null=True
    )
    vertical_distance = models.PositiveSmallIntegerField(
        "فواصل عمودی نیل‌ها", null=True
    )
    shotcret = models.CharField(
        "شاتکریت",
        max_length=255,
        null=True,
        choices=(("single", "تک‌لایه"), ("double", "دولایه")),
    )
    highest_length = models.PositiveSmallIntegerField("طول بلندترین نیل", null=True)
    lowest_length = models.PositiveSmallIntegerField("طول کوتاه‌ترین نیل", null=True)
    water_level = models.PositiveSmallIntegerField("سطح تقریبی آب", null=True)
    soil_type = models.CharField(
        "جنس خاک",
        max_length=255,
        null=True,
        choices=(
            ("soft_clay", "رس نرم"),
            ("hard_clay", "رس سخت"),
            ("loose_sand", "شن و ماسه سست"),
            ("dense_sand", "شن و ماسه متراکم"),
            ("hand_soil", "خاک دستی"),
            ("other", "سایر"),
        ),
    )
    area_image = models.ImageField(
        "تصویر محل", max_length=255, null=True, upload_to="area-images/"
    )
    log = models.FileField("لوگ گمانه", null=True, upload_to="logs/")
    plan = models.FileField("نقشه‌ی اجرایی", null=True, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - نیلینگ"
        verbose_name_plural = "خدمات پیمانکاری - نیلینگ"


class ContractingPaintingService(Service, ContractingService):
    color_type = models.CharField(
        "نوع رنگ",
        max_length=255,
        null=True,
        choices=(
            ("oil", "روغنی"),
            ("plastic", "پلاستیک"),
            ("acrylic", "اکریلیک"),
            ("other", "سایر"),
        ),
    )
    total_area = models.PositiveSmallIntegerField("متراژ کل", null=True)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - نقاشی"
        verbose_name_plural = "خدمات پیمانکاری - نقاشی"


class ContractingPilingService(Service, ContractingService):
    total_piles = models.PositiveSmallIntegerField("تعداد شمع", null=True)
    pile_diameter = models.PositiveSmallIntegerField("قطر شمع", null=True)
    pile_depth = models.PositiveSmallIntegerField("عمق شمع", null=True)
    bell_diameter = models.PositiveSmallIntegerField("قطر پافیلی", null=True)
    water_level = models.PositiveSmallIntegerField("سطح تقریبی آب", null=True)
    material_type = models.CharField(
        "مصالح",
        max_length=255,
        null=True,
        choices=(
            ("soft_clay", "رس نرم"),
            ("hard_clay", "رس سخت"),
            ("loose_sand", "شن و ماسه سست"),
            ("dense_sand", "شن و ماسه متراکم"),
            ("hand_soil", "خاک دستی"),
            ("other", "سایر"),
        ),
    )
    log = models.FileField("لوگ گمانه", null=True, upload_to="logs/")
    plan = models.FileField("نقشه‌ی شمع", null=True, upload_to="plans/")
    area_image = models.ImageField("تصویر محل", null=True, upload_to="area-images/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - حفاری شمع"
        verbose_name_plural = "خدمات پیمانکاری - حفاری شمع"


class ContractingPlasteringService(Service, ContractingService):
    plastering_type = models.CharField(
        "نوع گچ",
        max_length=255,
        null=True,
        choices=(("white", "سفید"), ("soil", "گچ و خاک")),
    )
    total_area = models.PositiveSmallIntegerField("متراژ کل", null=True)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - گچ‌کاری"
        verbose_name_plural = "خدمات پیمانکاری - گچ‌کاری"


class ContractingPlumbingService(Service, ContractingService):
    facility_type = models.CharField(
        "نوع تاسیسات",
        max_length=255,
        null=True,
        choices=(
            ("package", "پکیج"),
            ("water", "آب سرد و گرم"),
            ("wastewater", "فاضلاب"),
        ),
    )
    pipe_type = models.CharField(
        "نوع لوله",
        max_length=255,
        null=True,
        choices=(("white", "سفید"), ("other", "سایر")),
    )
    usecase = models.CharField(
        "کاربری ساختمان",
        max_length=255,
        null=True,
        choices=(
            ("residential", "مسکونی"),
            ("commercial", "تجاری"),
            ("warehouse", "انباری"),
            ("other", "سایر"),
        ),
    )
    total_suites = models.PositiveSmallIntegerField("تعداد کل واحد‌ها", null=True)
    total_stories = models.PositiveSmallIntegerField("تعداد کل طبقات", null=True)
    total_parkings = models.PositiveSmallIntegerField(
        "تعداد کل طبقات پارکینگ", null=True
    )
    suite_area = models.PositiveSmallIntegerField("متراژ هر واحد", null=True)
    total_wc = models.PositiveSmallIntegerField("تعداد کل سرویس‌های بهداشتی", null=True)
    total_baths = models.PositiveSmallIntegerField("تعداد کل حمام‌ها", null=True)
    plan = models.FileField("نقشه‌ی تاسیسات", null=True, blank=True, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - لوله‌کشی آب و فاضلاب"
        verbose_name_plural = "خدمات پیمانکاری - لوله‌کشی آب و فاضلاب"


class ContractingScaffoldingService(Service, ContractingService):
    usecase = models.CharField(
        "مورد استفاده",
        max_length=7,
        choices=(("facing", "نما"), ("ceiling", "چهارپایه زیرسقفی")),
    )
    required_duration = models.PositiveSmallIntegerField("مدت نیاز (به ماه)")

    # facing
    required_area = models.PositiveSmallIntegerField(
        "مساحت مورد نیاز", null=True, blank=True
    )
    # ceiling
    required_volume = models.PositiveSmallIntegerField(
        "حجم مورد نیاز", null=True, blank=True
    )

    required_height = models.PositiveSmallIntegerField("ارتفاع مورد نیاز")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - داربست"
        verbose_name_plural = "خدمات پیمانکاری - داربست"


class ContractingSteelService(Service, ContractingService):
    foundation_type = models.CharField(
        "نوع فونداسیون",
        max_length=255,
        null=True,
        choices=(("expanded", "گسترده"), ("striped", "نواری")),
    )
    infrastructure_area = models.PositiveSmallIntegerField(
        "زیربنای کل پروژه", null=True
    )
    ceiling_area = models.PositiveSmallIntegerField("متراژ هر سقف", null=True)
    total_ceilings = models.PositiveSmallIntegerField("تعداد کل سقف", null=True)
    total_basements = models.PositiveSmallIntegerField("تعداد کل زیرزمین", null=True)
    total_area = models.PositiveIntegerField("متراژ کل", null=True)
    plan = models.FileField("نقشه‌ی سازه‌ای", null=True, blank=True, upload_to="plans/")
    contractor_responsibilities = MultiSelectField(
        "آیا این موارد بر عهده پیمان‌کار باشد؟",
        choices=(
            ("ceiling", "اجرای سقف"),
            ("color", "رنگ‌کاری و سندبلاست"),
        ),
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - اجرای سازه فولادی"
        verbose_name_plural = "خدمات پیمانکاری - اجرای سازه فولادی"


class ContractingTilingService(Service, ContractingService):
    place = models.CharField(
        "محل",
        max_length=255,
        null=True,
        choices=(
            ("kitchen", "آشپزخانه"),
            ("living_room", "هال، پذیرایی و اتاق"),
            ("parking", "پارکینگ"),
            ("backyard", "حیاط"),
            ("other", "سایر"),
        ),
    )
    type = models.CharField(
        "نوع",
        max_length=255,
        null=True,
        choices=(("ceramic", "کاشی و سرامیک"), ("stone", "سنگ")),
    )
    size = models.CharField(
        "اندازه",
        max_length=255,
        null=True,
        choices=(("normal", "معمولی"), ("slab", "اسلب")),
    )
    total_area = models.PositiveSmallIntegerField("متراژ کل", null=True)
    plan = models.FileField("نقشه‌ی معماری", null=True, blank=True, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - کاشی‌کاری"
        verbose_name_plural = "خدمات پیمانکاری - کاشی‌کاری"


class ContractingTrussService(Service, ContractingService):
    total_area = models.PositiveSmallIntegerField("سطح کل دیواره‌ی گود", null=True)
    depth = models.PositiveSmallIntegerField("عمق گود", null=True)
    total_truss = models.PositiveSmallIntegerField("تعداد کل خرپاها", null=True)
    profile_tonnage = models.PositiveSmallIntegerField("تناژ تقریبی کل پروفیل‌ها")
    wall_type = models.CharField(
        "جنس دیوار",
        max_length=255,
        null=True,
        choices=(
            ("brick", "آجر"),
            ("timber", "الوار"),
            ("shotcret", "شاتکریت"),
            ("other", "سایر"),
        ),
    )
    water_level = models.PositiveSmallIntegerField("سطح تقریبی آب", null=True)
    plan = models.FileField("نقشه‌ی اجرایی", null=True, upload_to="plans/")
    area_image = models.ImageField(
        "تصویر محل", max_length=255, null=True, upload_to="area-images/"
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - سازه نگهبان خرپایی"
        verbose_name_plural = "خدمات پیمانکاری - سازه نگهبان خرپایی"


class ContractingWallService(Service, ContractingService):
    wall_area = models.PositiveSmallIntegerField("مساحت دیوار", null=True)
    wall_thickness = models.PositiveSmallIntegerField("ضخامت دیوار", null=True)
    wall_type = models.CharField(
        "نوع دیوار",
        max_length=255,
        null=True,
        choices=(
            ("brick", "آجر"),
            ("concrete_block", "بلوک سیمانی توخالی"),
            ("aac_block", "بلوک AAC"),
            ("prebuilt", "پیش‌ساخته"),
            ("other", "سایر"),
        ),
    )
    plan = models.FileField("نقشه‌ی معماری", null=True, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - بنایی دیوارچینی"
        verbose_name_plural = "خدمات پیمانکاری - بنایی دیوارچینی"


class ContractingWaterproofingService(Service, ContractingService):
    required_places = MultiSelectField(
        "محل مورد استفاده",
        max_length=255,
        null=True,
        choices=(
            ("kitchen", "سرویس و یا آشپزخانه"),
            ("roof", "پشت بام"),
            ("other", "سایر"),
        ),
    )
    total_area = models.PositiveSmallIntegerField("متراژ کل مورد نیاز")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - ایزوگام"
        verbose_name_plural = "خدمات پیمانکاری - ایزوگام"


class ContractingWiringService(Service, ContractingService):
    usecase = models.CharField(
        "کاربری ساختمان",
        max_length=255,
        null=True,
        choices=(
            ("residential", "مسکونی"),
            ("commercial", "تجاری"),
            ("warehouse", "انباری"),
            ("other", "سایر"),
        ),
    )
    total_suites = models.PositiveSmallIntegerField("تعداد کل واحد‌ها", null=True)
    average_area = models.PositiveSmallIntegerField("متراژ میانگین هر واحد", null=True)
    total_stories = models.PositiveSmallIntegerField("تعداد کل طبقات", null=True)
    total_parkings = models.PositiveSmallIntegerField(
        "تعداد کل طبقات پارکینگ", null=True
    )
    total_halogens = models.PositiveSmallIntegerField(
        "تعداد تقریبی هالوژن‌ها", null=True
    )
    contractor_responsibilities = MultiSelectField(
        "آیا این موارد شامل خدمات باشد؟",
        choices=(
            ("elevator", "نصب چراغ‌های تونلی آسانسور"),
            ("earth", "سیم‌کشی ارت"),
            ("detectors", "نصب دتکتورها و شستی‌ها و راه‌اندازی کامل اعلام حریق"),
        ),
    )
    plan = models.FileField("نقشه‌ی تاسیسات", null=True, upload_to="plans/")
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس پیمانکاری - سیم‌کشی"
        verbose_name_plural = "خدمات پیمانکاری - سیم‌کشی"


class InsuranceService(models.Model):
    usecase = models.CharField(
        "کاربری ساختمان",
        max_length=255,
        null=True,
        choices=(
            ("residential", "مسکونی"),
            ("commercial", "تجاری"),
            ("warehouse", "انباری"),
            ("other", "سایر"),
        ),
        default="residential",
    )
    infrastructure_area = models.PositiveSmallIntegerField(
        "متراژ کل زیربنا", null=True, help_text="متر مربع"
    )
    skeleton_type = models.CharField(
        "نوع اسکلت",
        max_length=255,
        null=True,
        choices=(
            ("steel", "فلزی"),
            ("concrete", "بتنی"),
            ("bolts", "پیچ و مهره سبک"),
        ),
    )
    total_stories = models.PositiveSmallIntegerField("تعداد کل طبقات", null=True)
    total_basements = models.CharField(
        "تعداد کل طبقات زیرزمین",
        max_length=255,
        null=True,
        choices=(
            ("0", "۰"),
            ("1", "۱"),
            ("2", "۲"),
            ("3", "۳"),
            ("4", "۴"),
            ("5", "۵"),
            ("6", "۶"),
            ("7", "۷"),
            ("8", "۸"),
            ("9", "۹"),
            ("10", "۱۰"),
        ),
        default="0",
    )
    current_status = models.CharField(
        "وضعیت فعلی",
        max_length=255,
        null=True,
        choices=(
            ("moor", "بایر"),
            ("being_destructed", "در حال تخریب"),
            ("before_excavating", "شروع گودبرداری"),
            ("being_excavated", "در حال گود برداری"),
        ),
    )
    requested_insurance_duration = models.PositiveSmallIntegerField(
        "مدت زمان درخواست بیمه", null=True
    )
    construction_area = models.PositiveSmallIntegerField(
        "مساحت زمین مورد ساخت", null=True, help_text="متر مربع"
    )
    structural_system = models.PositiveSmallIntegerField(
        "سیستم سازه",
        null=True,
        choices=(
            (1, "فلزی مهاربندی"),
            (2, "فلزی صلب"),
            (3, "بتنی بدون دیوار برشی"),
            (4, "بتنی با دیوار برشی"),
        ),
    )

    class Meta:
        abstract = True


class InsuranceEmployeesLiabilityService(Service, InsuranceService):
    # Required Fields
    singular_medical_expenses = models.PositiveSmallIntegerField(
        "هزینه‌ی پزشکی هر نفر در هر حادثه", help_text="ریال"
    )
    total_medical_expenses = models.PositiveSmallIntegerField(
        "هزینه‌ی پزشکی هر نفر در طول کل مدت بیمه", help_text="ریال"
    )
    maximum_employees = models.PositiveSmallIntegerField("حداکثر نفرات", null=True)
    total_defected = models.PositiveSmallIntegerField(
        "تعداد نفرات فوت و نقص عضو شده (پیشنهاد: ۲ الی ۳ نفر)", null=True
    )
    maximum_expenses_normal = models.PositiveIntegerField(
        "حداکثر مبلغ برای ماه‌های عادی", null=True, help_text="ریال"
    )
    maximum_expenses_haram = models.PositiveIntegerField(
        "حداکثر مبلغ برای ماه‌های حرام", null=True, help_text="ریال"
    )

    # Optional Fields
    liability_3rd_parties = models.BooleanField(
        "مسئولیت در قبال شخص ثالث؟", null=True, default=False, blank=True
    )
    diyats = models.PositiveSmallIntegerField("تعداد دیات", null=True, blank=True)
    tamin_ejtemaei_numbers = models.PositiveSmallIntegerField(
        "تعداد نفرات برای مطالبات تامین اجتماعی", null=True, blank=True
    )
    tamin_ejtemaei_demands = models.PositiveIntegerField(
        "مبلغ مطالبات تامین اجتماعی", null=True, blank=True, help_text="ریال"
    )
    increase_wergild = models.PositiveSmallIntegerField(
        "افزایش دیه", null=True, blank=True, choices=((2, "۲"), (3, "۳"))
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس بیمه - بیمه مسئولیت کارکنان"
        verbose_name_plural = "خدمات بیمه - بیمه مسئولیت کارکنان"


class InsuranceThirdPartyLiabilityService(Service, InsuranceService):
    width = models.PositiveSmallIntegerField("عرض قطعه", null=True, help_text="متر")
    depth = models.PositiveSmallIntegerField(
        "عمق خاک‌برداری", null=True, help_text="متر"
    )
    soil_type = models.CharField(
        "نوع خاک",
        max_length=255,
        null=True,
        choices=(
            ("hand", "دستی"),
            ("clay", "رسی"),
            ("sand", "ماسه"),
            ("gravel", "شن"),
            ("dj", "دج"),
        ),
    )
    excavation_method = models.CharField(
        "روش خاک‌برداری",
        max_length=255,
        null=True,
        choices=(("hand", "دستی"), ("machine", "ماشینی"), ("both", "توام")),
    )
    has_water_level = models.BooleanField(
        "در عمق گودبرداری نشست آب و عمق آب وجود دارد؟", null=True, default=False
    )
    water_level = models.PositiveSmallIntegerField(
        "عمق سطح آب", null=True, help_text="متر"
    )
    traffic = models.PositiveSmallIntegerField(
        "نوع تردد منطقه",
        null=True,
        choices=((1, "خلوت"), (2, "متوسط"), (3, "شلوغ")),
    )
    raining_season = models.BooleanField(
        "آیا عملیات همزمان با فصل بارندگی است؟", default=False
    )
    drainage = models.BooleanField(
        "در صورت بالا بودن سطح آب، آیا عملیات زهکشی انجام می‌شود؟", default=False
    )
    verified_plan = models.BooleanField(
        "آیا پروژه دارای نقشه سازه نگهبان مورد تایید سازمان نظام مهندسی است؟",
        default=False,
    )
    has_fence = models.BooleanField(
        "آیا اطراف محل پروژه حصار و توری فلزی جهت جلوگیری از سقوط اجسام انجام خواهد شد؟",
        default=False,
    )
    financial_commitment = models.PositiveBigIntegerField(
        "مبلغ تعهد مالی",
        help_text="ریال",
        null=True,
        blank=True,
    )
    medical_expenses_per_person = models.PositiveBigIntegerField(
        "هزینه‌ی پزشکی هر نفر در هر حادثه", null=True, blank=True, help_text="ریال"
    )
    medical_expenses_per_period = models.PositiveBigIntegerField(
        "هزینه‌ی پزشکی هر نفر در طول مدت بیمه", null=True, blank=True, help_text="ریال"
    )

    # check
    north_neighbours = models.TextField("شرایط مجاورهای شمالی", blank=True, null=True)
    east_neighbours = models.TextField("شرایط مجاورهای شرقی", blank=True, null=True)
    south_neighbours = models.TextField("شرایط مجاورهای جنوبی", blank=True, null=True)
    west_neighbours = models.TextField("شرایط مجاورهای غربی", blank=True, null=True)
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس بیمه - بیمه مسئولیت شخص ثالث"
        verbose_name_plural = "خدمات بیمه - بیمه مسئولیت شخص ثالث"


class InsuranceQualityService(Service, InsuranceService):
    total_suites = models.PositiveSmallIntegerField("تعداد کل واحدها")
    soil_type = models.CharField(
        "جنس خاک",
        max_length=255,
        null=True,
        choices=(
            ("soft_clay", "رس نرم"),
            ("hard_clay", "رس سخت"),
            ("loose_sand", "شن و ماسه سست"),
            ("dense_sand", "شن و ماسه متراکم"),
            ("hand_soil", "خاک دستی"),
            ("other", "سایر"),
        ),
    )
    foundation_type = models.CharField(
        "نوع فونداسیون",
        max_length=255,
        choices=(
            ("sigleton", "منفرد"),
            ("striped", "نواری"),
            ("expanded", "گسترده"),
            ("pile", "شمع"),
        ),
        default="expanded",
    )
    excavation_depth = models.SmallIntegerField("عمق گودبرداری")
    building_type = models.CharField(
        "نوع سازه",
        max_length=255,
        choices=(("concrete", "بتنی"), ("steel", "فولادی")),
        default="concrete",
    )
    ceiling_height = models.SmallIntegerField("ارتفاع هر سقف")
    # TODO: check ceiling types
    ceiling_type = models.CharField(
        "نوع سقت",
        max_length=255,
        choices=(
            ("beam", "تیرچه"),
            ("waffle", "وافل"),
            ("concrete_wing", "بال بتنی"),
            ("other", "سایر"),
        ),
        default="beam",
    )
    wall_material_type = models.CharField(
        "نوع مصالح دیوارچینی",
        max_length=14,
        choices=(
            ("brick", "آجر فشاری"),
            ("clay", "سفالی"),
            ("concrete_block", "بلوک سیمانی"),
            ("aac", "بلوک سبک AAC"),
            ("plaster", "قطعات گچی"),
            ("other", "سایر"),
        ),
    )
    facing_type = models.CharField(
        "نوع نما",
        max_length=255,
        null=True,
        choices=(
            ("brick", "آجری"),
            ("stone", "سنگی"),
            ("concrete", "سیمانی"),
            ("glass", "شیشه"),
            ("aluminum", "آلومینوم"),
            ("composite", "کامپوزیت"),
            ("other", "سایر"),
        ),
    )
    roofing = models.CharField(
        "پوشش بام",
        max_length=255,
        null=True,
        choices=(
            ("iso", "آجری"),
            ("mosaic", "موزاییک"),
            ("asphalt", "آسفالت"),
            ("other", "سایر"),
        ),
    )
    construction_place = models.CharField(
        "محل ساخت",
        max_length=255,
        null=True,
        choices=(
            ("waste", "بایر"),
            ("building", "ساختمان قدیمی"),
        ),
    )
    humidity = models.CharField(
        "شرایط رطوبت محیط",
        max_length=255,
        null=True,
        choices=(
            ("low", "ملایم"),
            ("medium", "متوسط"),
            ("high", "شدید"),
        ),
    )
    leak_possibility = models.PositiveSmallIntegerField(
        "احتمال نشت به ساختمان از طریق آب زیرزمینی یا سطحی وجود دارد؟",
        null=True,
        choices=(
            (1, "بله"),
            (0, "خیر"),
        ),
    )
    special_conditions = models.CharField(
        "شرایط خاص مانند ذوب، یخبندان متناوب یا مواد خوردنده در محیط را توضیح دهید.",
        max_length=500,
    )
    experiments = MultiSelectField(
        "کدامیک از آزمایش‌ها در حین عملیات انجام می‌شود؟",
        choices=(
            ("soil", "مکانیک خاک"),
            ("concrete", "بتن"),
            ("weld", "جوش"),
        ),
    )
    other_experiments = models.CharField("سایر آزمایش‌ها", max_length=255)
    excavation_time = models.PositiveSmallIntegerField(
        "زمان تقریبی شروع تخریب یا گودبرداری از امروز"
    )
    skeleton_time = models.PositiveSmallIntegerField("زمان تقریبی پایان اسکلت از امروز")
    finish_time = models.PositiveSmallIntegerField(
        "زمان تقریبی پایان عملیات (صدور پایان‌کار و شروع پوشش بیمه)"
    )
    construction_value = models.PositiveBigIntegerField(
        "ارزش اجرای سازه (گودبرداری، اجرای فونداسیون و اسکلت)", help_text="تومان"
    )
    walling_value = models.PositiveBigIntegerField(
        "ارزش عملیات بنایی (دیوارچینی)", help_text="تومان"
    )
    facilities_value = models.PositiveBigIntegerField(
        "ارزش عملیات تاسیساتی", help_text="تومان"
    )
    facing_value = models.PositiveBigIntegerField(
        "ارزش عملیات نازک‌کاری و نما", help_text="تومان"
    )
    other_value = models.PositiveBigIntegerField("ارزش سایر عملیات", help_text="تومان")
    area_value = models.PositiveBigIntegerField("ارزش هر متر مربع", help_text="تومان")
    required_annual_inflation = models.CharField(
        "میزان تورم سالانه مورد درخواست طی ده سال",
        max_length=4,
        choices=(
            ("5", "۵"),
            ("10", "۱۰"),
            ("12.5", "۱۲٫۵"),
            ("15", "۱۵"),
            ("20", "۲۰"),
        ),
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="درخواست",
    )

    class Meta:
        verbose_name = "سرویس بیمه - تضمین کیفیت"
        verbose_name_plural = "خدمات بیمه - تضمین کیفیت"
