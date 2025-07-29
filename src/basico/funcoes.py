# -*- coding: utf-8 -*-
import base64
import io

from PIL import Image, ImageOps
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import reverse
from django.forms import forms
from django.conf import settings

from django.template.loader import render_to_string


from decimal import Decimal


import os
import re
import locale
import datetime
import glob
import hashlib
import shutil
import json
import time


# ApenasNumeros
def apenas_numeros(pValor):
    if (pValor is None) or (pValor == ''):
        return ''

    texto = pValor
    numeros = re.sub('[^0-9]', '', texto)
    return numeros


# ApenasNumeros
def apenas_numeros_conj(pValor):
    texto = pValor
    filtro = re.compile('([0-9]+)')
    numeros = filtro.findall(texto)

    return numeros


# Apenas Letras
def apenas_letras(pValor):
    texto = pValor
    filtro = re.compile('([A-Z]+)')
    letras = filtro.findall(texto)
    if len(letras) == 0:
        letras = ''

    else:
        letras = letras[0]

    return letras


def formatar_nome(name):
    vReturn = []

    vname = name
    vnames = vname.split() # Separando Nome e sobrenomes
    last = len(vnames)     # Quantidade de nomes

    vname = vnames[0]
    vname = vname.capitalize()

    if last >= 2:
        vlast_name = vnames[last - 1] # Pegando o último nome
        vlast_name = vlast_name.capitalize()
    else:
        vlast_name = ''

    vReturn.append(vname)
    vReturn.append(vlast_name)

    return vReturn


def formatar_telefone(telefone):
    # Formata de acordo com o número de dígitos
    vTelefone = apenas_numeros(telefone)

    if len(vTelefone) == 14:
        fone = '%s (%s) %s.%s-%s' % (vTelefone[:3], vTelefone[3:5], vTelefone[6:6], vTelefone[6:10], vTelefone[10:14])

    elif len(vTelefone) == 13:
        fone = '%s (%s) %s.%s-%s' % (vTelefone[:2], vTelefone[2:4], vTelefone[4:5], vTelefone[5:9], vTelefone[9:13])

    elif len(vTelefone) == 11:
        fone = '(%s) %s.%s-%s' % (vTelefone[:2], vTelefone[2:3], vTelefone[3:7], vTelefone[7:11])

    elif len(vTelefone) == 9:
        fone = '%s.%s-%s' % (vTelefone[:1], vTelefone[1:5], vTelefone[5:9])

    elif len(vTelefone) == 8:
        fone = '%s-%s' % (vTelefone[:4], vTelefone[4:8])

    else:
        fone = ''

    return fone


def dateToString(pData):
    """
    :return: Retorna uma data formatada como string no formato pt-br
    """
    if not pData:
        return None

    vData = None
    if type(pData) == type(datetime.date.today()):
        vData = datetime.datetime.strftime(pData, '%d/%m/%Y')

    return vData


def stringToDate(pData):
    """
    :return: Retorna uma data formatada como string no formato pt-br
    """
    if not pData:
        return None

    vData = pData
    if type(pData) == type('string'):
        vlData = pData[0:10]

        if '/' in vlData:

            try:
                vData = datetime.datetime.strptime(vlData, '%d/%m/%Y')
            except Exception as err:
                try:
                    vData = datetime.datetime.strptime(vlData, '%Y/%m/%d')
                except Exception as err:
                    pass

        elif '-' in vlData:

            try:
                vData = datetime.datetime.strptime(vlData, '%d-%m-%Y')
            except Exception as err:
                try:
                    vData = datetime.datetime.strptime(vlData, '%Y-%m-%d')
                except Exception as err:
                    pass

    return vData


def formatar_data(pData, pSaida=None):
    """
        CORRIGIR
    :param pData:
    :param pSaida:
    :return:
    """
    if not pData:
        return None

    # Se a entrada for do tipo data, converter em string
    if type(pData) == type(datetime.date.today()):
        vData = dateToString(pData)

    else:
        vData = stringToDate(pData)

    if '/' in vData:
        pass

    else:
        vDia = pData[:2]
        vMes = pData[2:4]
        vAno = pData[4:9]

        vData= '{}/{}/{}'.format(vDia.zfill(2), vMes.zfill(2), vAno)

    try:
        vTeste = datetime.datetime.strptime(vData, '%d/%m/%Y')

    except:
        vData = None

    return vData


def formatar_cpf_cnpj(numero):
    # Formata de acordo com o número de dígitos
    vNumero = apenas_numeros(numero)

    if len(vNumero) == 14: # 99 999 999 9999 99
        doc = '%s.%s.%s/%s-%s' % (vNumero[:2], vNumero[2:5], vNumero[5:8], vNumero[8:12], vNumero[12:14])

    elif len(vNumero) == 11: # 99 9 9999 9999
        doc = '%s.%s.%s-%s' % (vNumero[:3], vNumero[3:6], vNumero[6:9], vNumero[9:11])

    elif len(vNumero) >= 1: # Qualquer outra coisa
        doc = ''

    else:
        doc = 'INVÁLIDO'

    return doc


def formatar_moeda(pValor, pSimbolo=None):
    vValor = pValor

    # Corrigindo conversões se houver
    if (type(vValor) == type('A')):
        if (vValor is None) or (vValor == ''):
            vValor = 0

        else:
            try:
                vValor = float(vValor)
            except:
                raise Exception('A string deve conter valores. (Sem caracteres alfanuméricos)')


    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    except Exception as e:
        raise Exception('Erro de "locale". Possivelmente locale não está instalado no servidor. (apt-get install locales-all)')

    valor_formatado = locale.currency(vValor, grouping=True, symbol=pSimbolo)

    return valor_formatado


def formatar_numero(pNumero):
    vNumero = pNumero

    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    except Exception as e:
        raise Exception('Erro de "locale". Possivelmente locale não está instalado no servidor.')

    if vNumero:
        # Se a entrada for do tipo string, converter para float
        if type(vNumero) == type('A'):
            try:
                vNumero = int(vNumero)
            except:
                raise Exception('A string deve conter valores. (Sem caracteres alfanuméricos)')


        numero_formatado = locale.format('%d', vNumero, grouping=True)

    else:
        numero_formatado = ''

    return numero_formatado


def formatar_cep(pString):
    if (pString == ''):
        return ''

    cep = '%s.%s-%s' % (pString[:2], pString[2:5], pString[5:8])

    return cep


def formatar_float_to_datetime(pFloat):
    try:
        return datetime.datetime.fromtimestamp(pFloat).strftime('%d/%m/%Y %H:%M:%S')
    except:
        return ''


def retornar_mes(month):
    arrayMes = []
    arrayMes.append('Janeiro')
    arrayMes.append('Fevereiro')
    arrayMes.append('Março')
    arrayMes.append('Abril')
    arrayMes.append('Maio')
    arrayMes.append('Junho')
    arrayMes.append('Julho')
    arrayMes.append('Agosto')
    arrayMes.append('Setembro')
    arrayMes.append('Outubro')
    arrayMes.append('Novembro')
    arrayMes.append('Dezembro')

    return arrayMes[ month - 1]


# Retorna o Item de uma tupla de tuplas
def retornar_choice(lista, opcao):

    for opc in lista:
        if opc[0] == opcao:
            return opc[1]

    return None


# Retorna o Item de uma tupla de tuplas ( Faz a mesma coisa da função acima - Precisa fazer mais testes )
def get_choice(lista, opcao):
    return dict(lista).get(opcao)


def destacar(value):
    if (value is None) or (value == ''):
        return ''

    palavra = value
    classe = ''
    style = ''

    if palavra in VERMELHO:
        classe = 'text-danger'

    elif palavra in AZUL:
        classe = 'text-success'

    elif palavra in AMARELO:
        classe = 'text-warning'

    elif palavra in VERDE:
        style += 'color: #19bd04'

    if palavra in NEGRITO:
        classe += ' font-bold'

    if classe != '':
        palavra = '<span class="%s"> %s </span>' % (classe, palavra)

    if style != '':
        palavra = '<span style="%s" class="%s"> %s </span>' % (style, classe, palavra)

    return palavra


def converter_strings_para_maiusculas(dados):
    novo_dicionario = {}

    for chave, valor in dados.items():
        if isinstance(valor, str):
            novo_dicionario[chave] = valor.upper()
        else:
            novo_dicionario[chave] = valor

    return novo_dicionario
