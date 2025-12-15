import random

import qrcode
import os


def generate_custom_qr(text, filename="QR/custom_qr.png",
                       box_size=10, border=4,
                       fill_color="black", back_color="white",
                       version=None):
    """
    Генератор QR-кода с расширенными настройками.
    """
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # Средняя коррекция
        box_size=box_size,
        border=border,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Создаём директорию если её нет
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)

    img.save(filename)
    return img


def name_generation(base: list[str], adjective: list[str], dop: list[str])-> list[str]:  # adective + base + dop
    random.shuffle(base)
    random.shuffle(adjective)
    random.shuffle(dop)
    names = []
    for i in range(min(len(base), len(dop), len(adjective))):
        names.append(f"{adjective} {base} {dop}")
    return names


# Примеры использования
if __name__ == "__main__":
    base = [
        "Машинка",
        "",
        "",
        "",
        "",
        "",
    ]
    dop = [
        "p",
    ]
    adjective = [
        "d",
    ]
    texts = name_generation(base=base, adjective=adjective, dop=dop)
    for i, text in enumerate(texts):
        generate_custom_qr(
            text,
            filename=f"QR/{text}.png",
            box_size=12,
            fill_color="#2E7D32",  # Зелёный
            back_color="#FFFFFF"
        )
