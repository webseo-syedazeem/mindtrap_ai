# -*- coding: utf-8 -*-
import json
import os
import sys

from build_en_bank import build_english_bank
from build_ur_bank import build_urdu_bank
from validate_banks import validate_bank

def main():
    os.makedirs("assets/questions", exist_ok=True)

    print("Building English bank...")
    en_bank = build_english_bank()
    validate_bank(en_bank, "English")
    with open("assets/questions/en.json", "w", encoding="utf-8") as f:
        json.dump(en_bank, f, ensure_ascii=False, indent=2)
    print("assets/questions/en.json saved successfully.")

    print("\nBuilding Urdu bank...")
    ur_bank = build_urdu_bank()
    validate_bank(ur_bank, "Urdu")
    with open("assets/questions/ur.json", "w", encoding="utf-8") as f:
        json.dump(ur_bank, f, ensure_ascii=False, indent=2)
    print("assets/questions/ur.json saved successfully.")

    print("\nAll master banks built and validated successfully!")

if __name__ == "__main__":
    main()
