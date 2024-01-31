import flet as ft
import heading as head
import body as body

def main(page: ft.Page):
    page.title = "Personal website"
    page.theme_mode = ft.ThemeMode.LIGHT    
    head.heading(page),
    body.body(page),
    page.update(),

ft.app(target=main)