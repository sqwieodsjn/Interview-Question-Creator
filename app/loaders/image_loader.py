import easyocr
from langchain_core.documents import Document

reader = None

def load_image(file_path):

    global reader

    if reader is None:
        reader = easyocr.Reader(["en"])

    result = reader.readtext(file_path)

    text = " ".join(
        item[1]
        for item in result
    )

    return [
        Document(
            page_content=text,
            metadata={"source": file_path}
        )
    ]