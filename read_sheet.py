import pypinyin

def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s




with open(r'D:\sheets\member.txt','r', encoding='UTF-8') as f:
    datas = f.read()
    # print(datas)

new_datas = []
new_datas_pinyin = []
for data in datas.split(','):
    new_datas.append(data)

for new_data in new_datas:
    py = pinyin(new_data)
    new_datas_pinyin.append(py + ":" + new_data + ":" + py + "@hnzycfc.com")

print(new_datas_pinyin)

# new_datas_conf = []
# with open(r'D:\sheets\member_conf.txt','r', encoding='UTF-8') as f:
#     datas_conf = f.read()
#     # print(datas_conf)
# for data_conf in datas_conf.split(','):
#     new_datas_conf.append(data_conf)

# print(new_datas_conf)

# for new_data_conf in new_datas_conf:
#     for new_data_pinyin in new_datas_pinyin:
#         # print(1111)
#         # print(new_data_pinyin, new_data_conf)
#         # print(1111)
#         if new_data_conf in new_data_pinyin:
#             break
#         else:
#             print(new_data_pinyin)