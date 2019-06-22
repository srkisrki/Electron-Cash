#!/usr/bin/env python3
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2012 thomasv@gitorious
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import gettext
import os
import re
import locale
from typing import Dict
from collections import namedtuple

LOCALE_DIR = os.path.join(os.path.dirname(__file__), 'locale')
language = gettext.translation('electron-cash', LOCALE_DIR, fallback=True)

def _(x):
    global language
    return language.gettext(x)

def set_language(x):
    global language

    if not x:
        # User hasn't selected a language so we default to the system language
        x = get_system_language_match()

    if x:
        language = gettext.translation('electron-cash', LOCALE_DIR, fallback=True, languages=[x])

def get_system_language_match() -> str:
    """
    Returns the language code best matching the systems default language or None if none match.
    """
    try:
        default_locale = locale.getdefaultlocale()[0]
    except Exception:
        return None
    return match_language(default_locale)

def match_language(language_code: str) -> str:
    """
    Returns the language code from the languages dictionary that most closely matches the given
    language code or None if none match.
    """

    if not language_code:
        return None

    for (code, ldef) in languages.items():
        if ldef.matches(language_code) and not ldef.excludes(language_code):
            return code

    return None

LanguageDef = namedtuple(
    'LanguageDef', ['name', 'matches', 'excludes'])

languages: Dict[str, LanguageDef] = {
    '':      LanguageDef(
        name=_('System'),
        matches=lambda c: False, excludes=lambda c: False
        ),
    'ar_SA': LanguageDef(
        name='العَرَبِيَّة‎',
        matches=lambda c: re.match('^ar.*', c), excludes=lambda c: False
        ),
    'bg_BG': LanguageDef(
        name='Български',
        matches=lambda c: re.match('^bg.*', c), excludes=lambda c: False
        ),
    'cs_CZ': LanguageDef(
        name='Čeština',
        matches=lambda c: re.match('^bg.*', c), excludes=lambda c: False
        ),
    'da_DK': LanguageDef(
        name='Dansk',
        matches=lambda c: re.match('^da.*', c), excludes=lambda c: False
        ),
    'de_DE': LanguageDef(
        name='Deutsch',
        matches=lambda c: re.match('^de.*', c), excludes=lambda c: False
        ),
    'el_GR': LanguageDef(
        name='Ελληνικά',
        matches=lambda c: re.match('^el.*', c), excludes=lambda c: False
        ),
    'eo_UY': LanguageDef(
        name='Esperanto',
        matches=lambda c: re.match('^eo.*', c), excludes=lambda c: False
        ),
    'en_US': LanguageDef(
        name='English',
        matches=lambda c: re.match('^en.*', c), excludes=lambda c: False
        ),
    'es_AR': LanguageDef(
        name='Español (S. América)',
        matches=lambda c: re.match('^es.*', c), excludes=lambda c: re.match('^es_(ES|MX)', c)
        ),
    'es_ES': LanguageDef(
        name='Español',
        matches=lambda c: re.match('^es_ES', c), excludes=lambda c: False
        ),
    'es_MX': LanguageDef(
        name='Español (México)',
        matches=lambda c: re.match('^es_MX', c), excludes=lambda c: False
        ),
    'fa_IR': LanguageDef(
        name='فارسی',
        matches=lambda c: re.match('^fa.*', c), excludes=lambda c: False
        ),
    'fr_FR': LanguageDef(
        name='Français',
        matches=lambda c: re.match('^fr.*', c), excludes=lambda c: False
        ),
    'hu_HU': LanguageDef(
        name='Magyar',
        matches=lambda c: re.match('^hu.*', c), excludes=lambda c: False
        ),
    'hy_AM': LanguageDef(
        name='Հայաստան',
        matches=lambda c: re.match('^hy.*', c), excludes=lambda c: False
        ),
    'id_ID': LanguageDef(
        name='Bahasa Indonesia',
        matches=lambda c: re.match('^id.*', c), excludes=lambda c: False
        ),
    'it_IT': LanguageDef(
        name='Italiano',
        matches=lambda c: re.match('^it.*', c), excludes=lambda c: False
        ),
    'ja_JP': LanguageDef(
        name='日本語',
        matches=lambda c: re.match('^ja.*', c), excludes=lambda c: False
        ),
    'ko_KR': LanguageDef(
        name='한국어',
        matches=lambda c: re.match('^ko.*', c), excludes=lambda c: False
        ),
    'ky_KG': LanguageDef(
        name='кыргызча',
        matches=lambda c: re.match('^ky.*', c), excludes=lambda c: False
        ),
    'lv_LV': LanguageDef(
        name='Latviešu',
        matches=lambda c: re.match('^lv.*', c), excludes=lambda c: False
        ),
    'nb_NO': LanguageDef(
        name='Norsk',
        matches=lambda c: re.match('^n[bno].*', c), excludes=lambda c: False
        ),
    'nl_NL': LanguageDef(
        name='Nederlands',
        matches=lambda c: re.match('^nl.*', c), excludes=lambda c: False
        ),
    'pl_PL': LanguageDef(
        name='Polski',
        matches=lambda c: re.match('^pl.*', c), excludes=lambda c: False
        ),
    'pt_BR': LanguageDef(
        name='Português brasileiro',
        matches=lambda c: re.match('^pt_BR', c), excludes=lambda c: False
        ),
    'pt_PT': LanguageDef(
        name='Português',
        matches=lambda c: re.match('^pt.*', c), excludes=lambda c: re.match('^pt_BR', c)
        ),
    'ro_RO': LanguageDef(
        name='Românește',
        matches=lambda c: re.match('^ro.*', c), excludes=lambda c: False
        ),
    'ru_RU': LanguageDef(
        name='Русский',
        matches=lambda c: re.match('^ru.*', c), excludes=lambda c: False
        ),
    'sk_SK': LanguageDef(
        name='Slovenčina',
        matches=lambda c: re.match('^sk.*', c), excludes=lambda c: False
        ),
    'sl_SI': LanguageDef(
        name='Slovenščina',
        matches=lambda c: re.match('^sl.*', c), excludes=lambda c: False
        ),
    'sv_SE': LanguageDef(
        name='Svenska',
        matches=lambda c: re.match('^sv.*', c), excludes=lambda c: False
        ),
    'ta_IN': LanguageDef(
        name='தமிழ்',
        matches=lambda c: re.match('^ta.*', c), excludes=lambda c: False
        ),
    'th_TH': LanguageDef(
        name='ภาษาไทย',
        matches=lambda c: re.match('^th.*', c), excludes=lambda c: False
        ),
    'tr_TR': LanguageDef(
        name='Türkçe',
        matches=lambda c: re.match('^tr.*', c), excludes=lambda c: False
        ),
    'uk_UA': LanguageDef(
        name='Українська',
        matches=lambda c: re.match('^uk.*', c), excludes=lambda c: False
        ),
    'vi_VN': LanguageDef(
        name='Tiếng việt',
        matches=lambda c: re.match('^vi.*', c), excludes=lambda c: False
        ),
    'zh_CN': LanguageDef(
        name='普通話',
        matches=lambda c: re.match('^zh.*', c), excludes=lambda c: re.match('^zh_TW', c)
        ),
    'zh_TW': LanguageDef(
        name='台灣話',
        matches=lambda c: re.match('^zh_TW', c), excludes=lambda c: False
        ),
}
