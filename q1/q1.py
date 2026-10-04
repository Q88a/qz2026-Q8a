import json,os


def analyze_log(filepath: str) -> dict:
    dic_count = {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
    dic_cmp = {'timestamp': [], 'level': [], 'message': [], 'user': []}
    set1 = set()
    set2 = set()#空集合，去重，建键 这里连等会bug!!!!!!!print大法助我捉虫成功
    with open(filepath,'r',encoding='utf-8') as f:

        for line in f.readlines():
            try:
                data:dict = json.loads(line)

                for key in data:
                    if key not in dic_cmp:
                        data[key] = ''#在想如果jsonl里面有多余的项怎么办 先试一下

                set1.add(data.get('level'))
                set2.add(data.get('user'))

                for key in dic_cmp:
                    dic_cmp[key].append(data.get(key))#先放进列表 方便转成数值

                for a in set1:
                    dic_count['by_level'][a] = dic_cmp['level'].count(a)

                for a in set2:
                    dic_count['by_user'][a] = dic_cmp['user'].count(a)

                dic_count['total'] += 1
            except:
                pass
    f.close()
    if 'ERROR' in set1:
        dic_cmp['level'].reverse()
        dic_count['last_error'] = dic_cmp['message'][-dic_cmp['level'].index('ERROR')-1]#倒序实现反向切
    else:
        pass

    return dic_count

path0 = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(path0, input('请输入同一目录下的有效jsonl文件名：'))
while not os.path.exists(path1):
    path1 = os.path.join(path0, input('请重新输入同一目录下的有效jsonl文件名：'))

print(analyze_log(path1))