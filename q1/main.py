import json,os
from json import JSONDecodeError


def analyze_log(filepath: str) -> dict:
    dic_count = {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
    dic_cmp = {'timestamp': [], 'level': [], 'message': [], 'user': []}
    set1 = set()
    set2 = set()#空集合，去重，建键 这里连等会bug!!!!!!!print大法助我捉虫成功
    path0 = os.path.dirname(os.path.abspath(__file__))
    path1 = os.path.join(path0,filepath)#需要jsonl文件放在同一目录下

    if not os.path.exists(path1):
        return dic_count

    with open(path1,'r',encoding='utf-8') as f:

        for line in f.readlines():
            try:
                data:dict = json.loads(line)

                set1.add(data.get('level'))
                set2.add(data.get('user'))

                for key in dic_cmp:
                    dic_cmp[key].append(data.get(key))#先放进列表 方便转成数值

                for a in set1:
                    dic_count['by_level'][a] = dic_cmp['level'].count(a)

                for a in set2:
                    dic_count['by_user'][a] = dic_cmp['user'].count(a)

                dic_count['total'] += 1
            except(TypeError,JSONDecodeError,AttributeError):
                pass
    f.close()

    if 'ERROR' in set1:#搞last_error
        dic_cmp['level'].reverse()
        dic_count['last_error'] = dic_cmp['message'][-dic_cmp['level'].index('ERROR')-1]#倒序实现反向切。但这里有个问题：因为我追踪最后问题是通过追踪level状态来实现的，所以一旦level数据出错就会错。有何办法没有？
    else:
        pass

    return dic_count

result = analyze_log(input('请输入同一目录下的有效jsonl文件名：'))
print(result["total"])
print(result["by_level"])    #
print(result["last_error"])