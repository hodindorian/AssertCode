from django.conf import settings
import qrcode
import uuid
from pathlib import Path


def generate_qr_code(data, fill_color, back_color):
    qr = qrcode.QRCode(
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    )

    filename = f"{uuid.uuid4()}.png"

    output_dir = Path(settings.MEDIA_ROOT) / "qrcodes"
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / filename

    image.save(file_path)

    return f"qrcodes/{filename}"
