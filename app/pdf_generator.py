from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    content,
    output_path
):

    doc = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Interview Questions and Answers",
            styles["Title"]
        )
    )

    story.append(
        Spacer(
            1,
            20
        )
    )

    for line in content.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

    doc.build(story)

    return output_path