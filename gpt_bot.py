# -*- coding:utf-8 -*-
# @project: 闲聊机器人
# @filename: gpt_bot.py
# @author: ShuleHao
# @contact: 2571540718@qq.com
# @time: 2022/8/25 7:16
# @Blog:https://blog.csdn.net/hubuhgyf?type=blog
from my_rouge import Rouge
import os
from collections import deque

# from dialogbot import config
from interact import Inference



class GPTBot:
    def __init__(self, model_dir="model_dir", device="cpu",
                 max_history_len=3, max_len=25, repetition_penalty=1.0, temperature=1.0,
                 topk=8, topp=0.0, last_txt_len=100):
        self.last_txt = deque([], last_txt_len)
        self.model = None
        self.model_dir = model_dir
        self.device = device
        self.max_history_len = max_history_len
        self.max_len = max_len
        self.repetition_penalty = repetition_penalty
        self.temperature = temperature
        self.topk = topk
        self.topp = topp
        self.sql=self.load_sql()
    def load_sql(self):
        sql=[]
        path = r"sql.txt"
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('\t')
                sql.append((line[0],line[1]))

        return sql

    def myscore(self,a, b):  # b为标准
        rouge = Rouge()
        a = ' '.join(a)
        b = ' '.join(b)
        rouge_score = rouge.my_scores(a, b)  # a和b里面包含多个句子的时候用

        return rouge_score  # 使用f得分
    def init(self):
        if not self.model:
            if os.path.exists(self.model_dir):
                self.model = Inference(self.model_dir, self.device, max_history_len=self.max_history_len,
                                       max_len=self.max_len, repetition_penalty=self.repetition_penalty,
                                       temperature=self.temperature,
                                       topk=self.topk, topp=self.topp)
            else:
                # logger.warning("GPT model not found. model: {}".format(self.model_dir))
                print("没有找到模型")
    def answer(self, query):
        self.init()
        for i in self.sql:
            score=self.myscore(i[1],i[0])
            # print(score)
            if score>=0.5:
                self.last_txt.append(query)
                response = i[0]
            else:
                self.last_txt.append(query)
                response = self.model.predict(query)
        self.last_txt.append(response)
        return response
