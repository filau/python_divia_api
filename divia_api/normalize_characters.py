# coding=utf-8

"""
normalize_characters.py

divia_api is a Python library that allows to retrieve the timetable
of Divia’s bus and tramways straight from a Python script.
Copyright (C) 2021  Firmin Launay

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

A_CHARACTERS = ['á', 'à', 'â', 'ä']
AE_CHARACTER = 'æ'
C_CHARACTER = 'ç'
E_CHARACTERS = ['é', 'è', 'ê', 'ë']
I_CHARACTERS = ['í', 'ì', 'î', 'ï']
N_CHARACTER = 'ñ'
O_CHARACTERS = ['ó', 'ò', 'ô', 'ö']
OE_CHARACTER = 'œ'
U_CHARACTERS = ['ú', 'ù', 'û', 'ü']
Y_CHARACTERS = ['ý', 'ỳ', 'ŷ', 'ÿ']
APP_CHARACTER = '’'


def normalize(expression: str) -> str:
    for char in A_CHARACTERS: expression = expression.replace(char, 'a')
    for char in E_CHARACTERS: expression = expression.replace(char, 'e')
    for char in I_CHARACTERS: expression = expression.replace(char, 'i')
    for char in O_CHARACTERS: expression = expression.replace(char, 'o')
    for char in U_CHARACTERS: expression = expression.replace(char, 'u')
    for char in Y_CHARACTERS: expression = expression.replace(char, 'y')
    expression = expression.replace(AE_CHARACTER, 'ae').replace(C_CHARACTER, 'c')
    expression = expression.replace(N_CHARACTER, 'n').replace(OE_CHARACTER, 'oe')
    expression = expression.replace(APP_CHARACTER, "'")
    
    return expression
