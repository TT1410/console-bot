from re import search


def sanitize_phone_number(phone: str) -> str:
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    return new_phone


def check_phone(phone: str) -> int | ValueError:
    clean_phone = sanitize_phone_number(phone)

    phone = search(r"(?:380|0)\d{9}", clean_phone)

    if not phone:
        raise ValueError(f"Phone number {clean_phone} is not valid")

    phone = phone.group()

    phone = '38' + phone if phone.startswith('0') else phone

    return int(phone)
