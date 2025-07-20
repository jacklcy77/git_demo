# -*- coding: utf-8 -*-
# @FileName : 01-bleu.py
# @Author   : CY
# @Time     : 2025/4/14 星期一 15:00


from nltk.translate.bleu_score import sentence_bleu
import torch
import math

def sentence_bleu_1(reference,candidate):
    bleu_1 = sentence_bleu(reference,candidate,weights=(1,0,0,0))
    bleu_2 = sentence_bleu(reference,candidate,weights=(0.5,0.5,0,0))
    bleu_3 = sentence_bleu(reference,candidate,weights=(0.33,0.33,0.33,0))
    bleu_4 = sentence_bleu(reference,candidate)
    return bleu_1,bleu_2,bleu_3,bleu_4
# 生成的文本
candidate_text = ["This", "is",  "some",  "generated", "text"]

# 参考文本
reference_text = [["This", "is",  "a",  "reference", "text"]]  #todo:这里是列表套列表!!!!!!!!!!!!!!!!

c_bleu= sentence_bleu_1(reference_text,candidate_text)
print(c_bleu)
# print(bleu_1)
# print(bleu_2)
# print(bleu_3)
# print(bleu_4)
print()

