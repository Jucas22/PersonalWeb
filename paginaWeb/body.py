import flet as ft

def body(page: ft.page):
    body = ft.Container(
        ft.Row([
            ft.Column([aboutMe(), contact()]),
            trajectory()
            ],
        alignment = ft.MainAxisAlignment.CENTER,
        )
    )

    page.add(body)
    page.update()

def aboutMe():

    title = ft.Text(
        "Sobre mi:",
        size = 25,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.CENTER,
    )
    description = ft.Text(
        "una persona interesada en el mundo del software y de la inteligancia artificial",
        text_align = ft.TextAlign.CENTER,
    )

    return ft.Column(
        [title, description],
        alignment = ft.alignment.center
    )

def trajectory():

    title = ft.Text(
        "Mi trayectoria: ",
        size = 25,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.CENTER,
    )
    description = ft.Text(
        "adsfasdf",
        text_align = ft.TextAlign.CENTER,
    )

    return ft.Column(
        [title, description],     
    )

def contact():

    title = ft.Text(
        "Contacto:",
        size = 25,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.CENTER,
    )
    description = ft.Text(
        "Puedes contactar conmigo a traves de ...",
        text_align = ft.TextAlign.CENTER,
    )

    return ft.Column(
        [title, description],
        
    )
