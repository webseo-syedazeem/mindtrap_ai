# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Basic Urdu to Devanagari transliteration test
CHAR_MAP = {
    'آ': 'आ', 'ا': 'अ', 'ب': 'ब', 'پ': 'प', 'ت': 'त', 'ٹ': 'ट', 'ث': 'स',
    'ج': 'ज', 'چ': 'च', 'ح': 'ह', 'خ': 'ख', 'د': 'द', 'ڈ': 'ड', 'ذ': 'ज़',
    'ر': 'र', 'ڑ': 'ड़', 'ز': 'ज़', 'ژ': 'झ', 'س': 'स', 'ش': 'श', 'ص': 'स',
    'ض': 'ज़', 'ط': 'त', 'ظ': 'ज़', 'ع': 'अ', 'غ': 'ग़', 'ف': 'फ़', 'ق': 'क़',
    'ک': 'क', 'گ': 'ग', 'ل': 'ल', 'م': 'म', 'ن': 'न', 'ں': 'ँ', 'و': 'व',
    'ہ': 'ह', 'ھ': 'ह', 'ء': '', 'ی': 'य', 'ے': 'े', 'ئ': '', '؟': '?'
}

def transliterate(urdu_text):
    res = []
    for ch in urdu_text:
        res.append(CHAR_MAP.get(ch, ch))
    return ''.join(res)

test_q = "وہ کیا ہے جس کے ہاتھ ہیں مگر وہ تالی نہیں بجا سکتی؟"
print("Original:", test_q)
print("Transliterated:", transliterate(test_q))
