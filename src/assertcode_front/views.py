from django.shortcuts import render

from .forms import QRCodeForm
from .services.qr_service import generate_qr_code


def home(request):
    qr_code_url = None

    if request.method == 'POST':
        form = QRCodeForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            fill_color = form.cleaned_data['fill_color']
            back_color = form.cleaned_data['back_color']

            qr_path = generate_qr_code(
                data=url,
                fill_color=fill_color,
                back_color=back_color
            )

            qr_code_url = f"/media/{qr_path}"

    else:
        form = QRCodeForm()

    return render(request, 'assertcode_front/home.html', {
        'form': form,
        'qr_code_url': qr_code_url
    })