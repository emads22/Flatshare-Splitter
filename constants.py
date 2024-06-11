import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


ASSETS = Path(__file__).parent / "assets"  # dynamic path
BILLS = ASSETS / "pdf_bills"
IMAGES = ASSETS / "images"
BILL_LOGO = IMAGES / "house.png"

FILESTACK_API_KEY = os.getenv('FILESTACK_API_KEY')

ASCII_ART = """

  ______  _         _         _                             _____         _  _  _    _              
 |  ____|| |       | |       | |                           / ____|       | |(_)| |  | |             
 | |__   | |  __ _ | |_  ___ | |__    __ _  _ __  ___     | (___   _ __  | | _ | |_ | |_  ___  _ __ 
 |  __|  | | / _` || __|/ __|| '_ \  / _` || '__|/ _ \     \___ \ | '_ \ | || || __|| __|/ _ \| '__|
 | |     | || (_| || |_ \__ \| | | || (_| || |  |  __/     ____) || |_) || || || |_ | |_|  __/| |   
 |_|     |_| \__,_| \__||___/|_| |_| \__,_||_|   \___|    |_____/ | .__/ |_||_| \__| \__|\___||_|   
                                                               | |                               
                                                               |_|                               

"""