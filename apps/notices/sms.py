import ippanel
from django.conf import settings

client = ippanel.Client(settings.HAMKARAN_API_KEY)

from django.conf import settings


def new_order_sms(
    pattern_code: str = "b9y4nakoa2",
    cell: str = "",
    name: str = "",
    price: int = 0,
) -> None:
    pattern_values = (
        {
            "name": str(name),
            "price": str(price),
        },
    )
    try:
        bulk_id = client.send_pattern(
            pattern_code,  # pattern code
            "+983000505",  # originator
            str(cell),  # recipient
            pattern_values,  # pattern values
        )
        print(bulk_id)
    except ippanel.Error as e:  # ippanel sms error
        print("Error handled => code: %s, message: %s" % (e.code, e.message))
        if e.code == ippanel.ResponseCode.ErrUnprocessableEntity.value:
            for field in e.message:
                print("Field: %s , Errors: %s" % (field, e.message[field]))
    except ippanel.HTTPError as e:  # http error like network error, not found, ...
        print("Error handled => code: %s" % (e))
