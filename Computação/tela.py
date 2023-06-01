#A styled DataTable
import photogate
from photogate import *
import flet as ft
from flet import *

def main(page: ft.Page):
    distancia = int(input())
    voltas = leitura_arquivo("/home/ec2023/ra250094/Desktop/aqui/Photogate/Computação/tempos.CSV")
    voltas = calculo_acrescimos(voltas)
    voltas = calculo_velocidades(distancia, voltas)
    voltas_ordenadas = ordenacao_velocidades(voltas, False)
    voltas_ordenadas_reversa = ordenacao_velocidades(voltas, True)
    dados = [
        {"volta": x[0],"tempo":x[1], "acrescimo":x[2], "inst": x[3]} for x in voltas
    ]
    

    def carregartable(dados:list[dict[str,any]]):
        global tempos
        for x in dados:
            tempos.rows.append(
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(x["volta"])),
                    ft.DataCell(ft.Text(x["tempo"])),
                    ft.DataCell(ft.Text(x["acrescimo"])),
                    ft.DataCell(ft.Text(x["inst"]))

                ]
                )
            )

    '''
        if type(i) == int:
            tempos.rows += [
            for x in dados:
                tempos.rows.add(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(x["volta"])),
                            ft.DataCell(ft.Text(x["tempo"])),
                            ft.DataCell(ft.Text(x["acrescimo"])),
                            ft.DataCell(ft.Text(x["inst"]))
                        ]
                        )
                )
            ]

        else:
            data: list[dict[str,any]] = dados
            data: list[dict[str,any]] = data.sort(key= lambda x: x['tempo'], reverse= i)
            e.rows.clear()
            for x in data:
                e.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(x["volta"])),
                            ft.DataCell(ft.Text(x["tempo"])),
                            ft.DataCell(ft.Text(x["acrescimo"])),
                            ft.DataCell(ft.Text(x["inst"]))
                        ]
                        )
                )'''

    tempos = ft.DataTable(
        width=700,
        bgcolor="yellow",
        border=ft.border.all(2, "red"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "green"),
        sort_column_index=1,
        sort_ascending=True,
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        columns=[
            ft.DataColumn(
                ft.Text("volta"),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
            ft.DataColumn(
                ft.Text("Tempo"),
                tooltip="This is a second column",
                numeric=True,
                on_sort= lambda e: recarrega(e.ascending),
            ),
            ft.DataColumn(
                ft.Text("Acrescimo"),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
            ft.DataColumn(
                ft.Text("Vel. Instantanea"),
                tooltip="This is a second column",
                numeric=True,
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
            
            
        ],
        rows=[],
    )

    carregartable(dados)




    page.add(tempos)
        
ft.app(target=main)