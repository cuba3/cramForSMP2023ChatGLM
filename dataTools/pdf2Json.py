# -*- coding: utf-8 -*-
# @Time : 2023/8/16 11:55
# @Author : luke
# @Email : cuba3@163.com
# @File : pdf2Json.py
# @Project : cramForSMP2023ChatGLM
import pdfminer
import pdfminer.high_level
import json
def pdf2Json(filePath):
    text = pdfminer.high_level.extract_text(filePath)
    # 将文本转换为JSON字符串
    jsonStr = json.dumps({'text': text})
    return jsonStr