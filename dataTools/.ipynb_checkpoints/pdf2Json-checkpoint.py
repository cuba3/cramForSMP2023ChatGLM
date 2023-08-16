# -*- coding: utf-8 -*-
# @Time : 2023/8/16 11:55
# @Author : luke
# @Email : cuba3@163.com
# @File : pdf2Json.py
# @Project : cramForSMP2023ChatGLM
from pypdf import PdfReader
def pdf2Json(filename):
    # Open and read PDF file
    outputJson = {}
    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)
    for num in range(0,number_of_pages):
        page = reader.pages[num]
        text = page.extract_text()
        outputJson[page]=text
    return outputJson
