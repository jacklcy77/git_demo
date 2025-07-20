# -*- coding: utf-8 -*-
# @FileName : 02_rouge.py
# @Author   : CY
# @Time     : 2025/4/14 星期一 15:29
from rouge import Rouge

# 生成文本
generated_text = "This is some generated text."

# 参考文本列表
reference_texts = ["This is another generated reference text."]

#计算rouge值
rouge = Rouge()
scores =rouge.get_scores(generated_text,reference_texts[0])
print(f'score-->{scores}')
#结果score-->[{'rouge-1': {'r': 0.6666666666666666, 'p': 0.8, 'f': 0.7272727223140496},
# 'rouge-2': {'r': 0.2, 'p': 0.25, 'f': 0.22222221728395072},
# 'rouge-l': {'r': 0.6666666666666666, 'p': 0.8, 'f': 0.7272727223140496}}]

print("ROUGE-1 precision:", scores[0]["rouge-1"]["p"])
print("ROUGE-1 recall:", scores[0]["rouge-1"]["r"])
print("ROUGE-1 F1 score:", scores[0]["rouge-1"]["f"])