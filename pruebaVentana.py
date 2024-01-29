import flet as ft

def header(page: ft.Page):
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False
                    ),
                ]
            ),
        ],
    )

def body(page: ft.Page):
    page.add(ft.Text("Body!"))

def main(page: ft.Page):
    # def check_item_clicked(e):
    #     e.control.checked = not e.control.checked
    #     page.update()

    header(page)
    body(page)

ft.app(target=main)