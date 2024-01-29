import flet as ft
import heading as head

def main(page: ft.Page):
    page.title = "Personal website"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50

    head.heading(page)
    page.update()

ft.app(target=main)