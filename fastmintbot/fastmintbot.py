from platform import platform
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from multiprocessing import Event
import PySimpleGUI as pg
import PySimpleGUI as sg
import schedule
from datetime import *
from datetime import datetime
import time
from time import sleep

def launchmynft():

    #Start WebBrowser
    chrome_options = ChromeOptions()
    chrome_options.add_extension('slope.crx')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    time.sleep(1)
    
    # LaunchMyNft Link
    driver.get(link)
    time.sleep(1)

    # Accept Cookies
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '//*[@id="rcc-confirm-button"]')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True

    # Connect Solana Wallet
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/button')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True

    # Select Slope
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/ul/li/button')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True

    driver.switch_to.window(driver.window_handles[1])

    # Agree Therms
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/span')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True
    
    # Import Wallet
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/button[2]')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True

    # Seed Input
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/textarea')
            find.send_keys(seed)
        except: time.sleep(0.01)
        finally: trigger = True
    
    # Next
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[4]/button')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True
    
    # Password1 Input
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/form/div[1]/div/div/div/div[2]/input')
            find.send_keys("FastMintBot2022")
        except: time.sleep(0.01)
        finally: trigger = True

    # Password2 Input
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/form/div[2]/div/div/div/div[2]/input')
            find.send_keys("FastMintBot2022")
        except: time.sleep(0.01)
        finally: trigger = True
    
    # Save
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/form/div[3]/button')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True
    
    # Finish
    time.sleep(5)
    find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/button')
    find.click()

    driver.switch_to.window(driver.window_handles[0])

    # Connect Solana Wallet
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/button')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True

    # Select Slope
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/ul/li/button')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True

    driver.switch_to.window(driver.window_handles[1])

    # Auto Approve
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True
    
    # Connect
    trigger = False
    while not trigger:
        try:
            find = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/button[2]')
            find.click()
        except: time.sleep(0.01)
        finally: trigger = True
    
    driver.switch_to.window(driver.window_handles[0])

    # Verify Time
    today = datetime.now()
    start_time = datetime.fromisoformat(f"{today.year}-{today.month:02}-{today.day:02} {i_hour:02}:{i_min:02}:{i_sec:02}").timestamp()
    while datetime.now().timestamp() < start_time:
        sleep

    # Mint
    while True:
        try: 
            find = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/button')
            find.click()
        except: time.sleep(0.01)

def confirm_w():

    # Confirm Windows
    layout = [
        [pg.Text("Pour tout problème ou bug contactez moi sur discord !", font="Roboto")],
        [pg.Text("Mon discord : dogevr#9999", font="Roboto")],
        [pg.Text("")],
        [pg.Text("Le lien du Mint est >", font="Roboto"),pg.Text(link)],
        [pg.Text("Votre Seed Slope est >", font="Roboto"),pg.Text(seed)],
        [pg.Text("L'Heure du Mint (-2 secondes) est >", font="Roboto"),pg.Text(total)],
        [pg.Text("")],
        [pg.Text("Veuillez verifier toutes les Informations avant de lancer le Bot", font="Roboto")],
        [pg.Text("Si vous avez le moindre doute allez sur le GitHub du Bot", font="Roboto")],
        [pg.Text("")],
        [pg.Button("Lancer", font="Roboto", key="launch"),]
    ]
    window = sg.Window("FastMintBot v.1 - Confirmation", layout, icon='fast.ico')
    while True:

        # Launch or Quit
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "launch":
            window.close()
            launchmynft()

def start_w():

    # Start Windows
    pg.theme("Dark Grey 13")
    layout = [
        [pg.Text("Pour tout problème ou bug contactez moi sur discord !", font="Roboto")],
        [pg.Text("Mon discord : dogevr#9999", font="Roboto")],
        [pg.Text("")],
        [pg.Text("Lien du Mint", size=(12, 1), font="Roboto"),pg.InputText(font="Roboto")],
        [pg.Text("Seed du Wallet", size=(12, 1), font="Roboto"),pg.InputText(font="Roboto")],
        [pg.Text("Heure du mint -2 secondes (HH:MM:SS)", size=(32, 1), font="Roboto"),pg.InputText(font="Roboto", size=(2, 1)),pg.Text(":", size=(1, 1), font="Roboto"),pg.InputText(font="Roboto", size=(2, 1)),pg.Text(":", size=(1, 1), font="Roboto"),pg.InputText(font="Roboto", size=(2, 1))],
        [[pg.Text("")]],
        [pg.Button("Confirmer", font="Roboto", key="confirm"),]
    ]
    window = pg.Window("FastMintBot v.1 - Sélection", layout, icon='fast.ico')
    while True:
        event, values = window.read()

        # Var Link
        global link
        link = values[0]
        link_len = int(len(link))
        if link == "":
            sg.popup("Pas de Lien")
            break
        if link_len < 30:
            sg.popup("Lien Invalide")
            break

        # Var Seed
        global seed
        seed = values[1]
        seed_len = int(len(seed))
        if seed == "":
            sg.popup("Pas de Seed")
            break
        if seed_len < 30:
            sg.popup("Seed Invalide")
            break

        # Var Time
        global i_hour
        i_hour = int(values[2])
        if i_hour > 23:
            sg.popup("Heure Invalide")
            break
        global i_min
        i_min = int(values[3])
        if i_min > 59:
            sg.popup("Minute Invalide")
            break
        global i_sec
        i_sec = int(values[4])
        if i_sec > 59:
            sg.popup("Seconde Invalide")
            break
        global total
        total = str(i_hour)+':'+str(i_min)+':'+str(i_sec)

        # Confirm or Quit
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "confirm":
            window.close()
            confirm_w()

# Start the Bot
start_w()