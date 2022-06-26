import PySimpleGUI as sg

import os
import logging

sg.theme("Reddit")

status = True

layout = [
    [sg.Text("Program do pobierania muzyki :) ")],
    [sg.Text("Link do muzyki "), sg.InputText()],
    [sg.Text("Miejsce do zapisu pliku (jesli nie podasz nic, piosenka powinna sie pobrac do folderu 'pobrane-piosenki')"), sg.InputText(key='-USER FOLDER-')],
    [sg.FolderBrowse("Wybierz folder", target='-USER FOLDER-')],
    [sg.Button("Kliknij aby pobrać muzykę", button_color="red2")],
    [sg.Button("Wyjdz z programu", key="-WYJSCIE-")],
    [sg.Text(text="Plik pobrany", visible=False, key="udane")],
    [sg.Text(text="Plik nie zostal pobrany", visible=False, key="nieudane")]]

window = sg.Window("Program Jakub Bednarek", layout, icon="res\\default.png")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-WYJSCIE-":
        break
    if event == "Kliknij aby pobrać muzykę":
        window["udane"].update(visible=False)
        window["nieudane"].update(visible=False)
        status = True
        try:
            from yt_dlp import YoutubeDL

            listaUrl = []
            ydl_opts = {
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],
                'outtmpl': 'pobrane-piosenki/%(title)s.%(ext)s',
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(values[0])
            status = True
        except:
            logging.exception("Blad przy wyszukiwaniu linku")
            status = False
        if status == True:
            window["udane"].update(visible=True)
        else:
            window["nieudane"].update(visible=True)

window.close()
