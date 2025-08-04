import requests
import csv
import os
from datetime import datetime

def fetch_dog_image_by_breed(breed):
    breed = breed.lower().strip()
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    res = requests.get(url).json()

    if res["status"] == "success":
        return res["message"], breed, True
    else:
        return None, breed, False

def save_favorite(image_url, breed):
    csv_path = os.path.join("data", "favorites.csv")
    os.makedirs("data", exist_ok=True)

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), breed, image_url])

def save_search_history(breed, success):
    csv_path = os.path.join("data", "search_history.csv")
    os.makedirs("data", exist_ok=True)

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), breed, "成功" if success else "失敗"])

