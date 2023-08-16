# -*- coding: utf-8 -*-
# @Time : 2023/8/16 11:54
# @Author : luke
# @Email : cuba3@163.com
# @File : main.py
# @Project : cramForSMP2023ChatGLM
from dataTools import pdf2Json

# from modelscope.msdatasets import MsDataset
# ds = MsDataset.load('chatglm_llm_fintech_raw_dataset', split='train', use_streaming=True, stream_batch_size=1)

for item in ds:
    print(item)
    break
path = item['pdf:FILE']
s = pdf2Json.pdf2Json(path[0]).encode('utf-8').decode('unicode_escape')
print(s)