import os

from .pdf_loader import load_pdf
from .txt_loader import load_txt
from .docx_loader import load_docx
from .image_loader import load_image


def load_document(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return load_pdf(file_path)

    elif extension == ".txt":
        return load_txt(file_path)

    elif extension == ".docx":
        return load_docx(file_path)

    elif extension in [".png", ".jpg", ".jpeg"]:
        return load_image(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )