import reflex as rx
from Portfolio_Python.components.card_detail import card_detail
from Portfolio_Python.components.heading import heading
from Portfolio_Python.data import Extra
from Portfolio_Python.styles.styles import Size


def extra(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
