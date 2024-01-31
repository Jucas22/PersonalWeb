import flet as ft

def heading(page: ft.page):

    heading_name = ft.Text(
        "Juan Castelló",
        size=70,
        weight=ft.FontWeight.W_700,
        selectable=True
    )
    hedaing_descr = ft.Text(
        "Estudiante de Ingeniería informática en la Universidad Politécnica de Valéncia",
        selectable=True
    )

    img = ft.Image(
        src=f"./paginaWeb/profile.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        border_radius = ft.border_radius.all(99999)
    )

    heading_text = ft.Column(
        [heading_name, hedaing_descr]
    )
    heading_imgText = ft.Row(
        [img, heading_text],
        alignment = ft.MainAxisAlignment.CENTER,
    )
    

    heading = ft.Container(
        heading_imgText,
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.top_center,
        #     end=ft.alignment.bottom_center,
        #     colors=[ft.colors.BLUE, ft.colors.GREY]
        # ),
        height=250,
        border = ft.border.all(5, ft.colors.BLACK)
    )
    
    page.add(heading)
    page.update()