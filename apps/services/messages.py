from django.contrib import messages


def service_success_message(request):
    messages.success(
        request,
        "آیتم مورد نظر با موفقیت برای درخواست ثبت شد.",
    )


def service_new_info(request):
    messages.info(
        request,
        "پس از اضافه کردن آیتم جدید می‌توانید با مراجعه به آیتم‌های ثبت شده (انتهای همین صفحه) درخواست خود را بازبینی "
        "و ثبت نهایی کنید.",
    )
