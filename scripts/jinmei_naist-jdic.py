# coding:utf-8
# 人名辞書をjson形式に変換
import sys
import csv
import json
import re
from tqdm import tqdm

args = sys.argv

path = args[1] # '../mecab-naist-jdic-0.6.3b-20111013/naist-jdic.csv'
seipath = './sei.json' if len(args) < 4 else args[2]
meipath = './mei.json' if len(args) < 4 else args[3]

def append_dict(row, jinmei_dict):
    yomi = row[11]
    kaki = row[0]
    if re.match(u'^[\u30a1-\u30fa\u30fcぁ-ん]+$', kaki) or re.match(u'^[a-zA-Z]+$', kaki):
        return
    if yomi in jinmei_dict:
        jinmei_dict[yomi].append(kaki)
    else:
        jinmei_dict[yomi] = [kaki]

sei_dict = dict()
mei_dict = dict()
with open(path, mode='r', encoding='euc_jp') as f:
    csv_file = csv.reader(f, delimiter=",")
    for row in tqdm(csv_file):
        if row[6] == '人名' and row[7] == '姓':
            append_dict(row, sei_dict)
        elif row[6] == '人名' and row[7] == '名':
            append_dict(row, mei_dict)

with open(seipath, mode='w', encoding='utf_8') as s:
    s.write(json.dumps(sei_dict, ensure_ascii=False))

with open(meipath, mode='w', encoding='utf_8') as m:
    m.write(json.dumps(mei_dict, ensure_ascii=False))
