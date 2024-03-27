import reflex as rx

from Portfolio_Python.components.heading import heading
from Portfolio_Python.components.info_detail import info_detail
from Portfolio_Python.data import Info
from Portfolio_Python.styles.styles import Size


def info(title: str, info: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(item)
                for item in info
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
