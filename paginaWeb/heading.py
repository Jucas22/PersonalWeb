import flet as ft

def heading(page: ft.page):
    img = ft.Image(
        src=f"./paginaWeb/profile.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    name = ft.Text(
        "Juan Castelló",
        size=70,
        weight=ft.FontWeight.W_700,
        selectable=True
    )
    description = ft.Text(
        "Estudiante de Ingeniería informática en la Universidad Politécnica de Valéncia"
    )

    heading_text = ft.Column(
        [name, description]
    )

    encabezado = ft.Row(
        [img, heading_text],
        alignment = ft.MainAxisAlignment.CENTER
    )
    img.border_radius = ft.border_radius.all(99999)

    # page.add(name)
    # page.add(img)
    page.add(encabezado)
    page.update()


