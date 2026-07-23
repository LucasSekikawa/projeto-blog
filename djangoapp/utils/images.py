from pathlib import Path
from django.conf import settings
from PIL import Image

def resize_image(image_django, new_width=800, optimize=True, quality=60):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    # 1. Se a imagem já for menor ou igual, apenas fecha e encerra a função
    if original_width <= new_width:
        image_pillow.close()
        return

    new_height = round(new_width * original_height / original_width)

    # 2. Atualizado para a sintaxe moderna do Pillow (Resampling)
    new_image = image_pillow.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # 3. Fechamos a imagem original ANTES de salvar a nova por cima
    # Isso evita erros de permissão de arquivo no Windows
    image_pillow.close()

    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    # 4. Fechamos a nova imagem para limpar a memória do servidor
    new_image.close()