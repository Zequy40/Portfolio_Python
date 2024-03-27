import reflex as rx
from Portfolio_Python.components.media import media
from Portfolio_Python.data import Media
from Portfolio_Python.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(data),
        spacing=Size.SMALL.value
    )
