import json,os


def analyze_log(filepath: str) -> dict:
    dic_count = {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
    dic_cmp = {"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "用户登录成功", "user": "张三"}
    with open(filepath,'r',encoding='utf-8') as f:
        for line in f.readlines():
            data = json.loads(line)

            dic_count['total'] += 1

            for key in data:
                if key not in dic_cmp:
                    data[key] = ""
            print(dic_count['total'])




    return data

path0 = os.path.dirname(os.path.abspath(__file__))
print(path0)
path1 = os.path.join(path0, input('请输入同一目录下的有效jsonl文件名：'))
while not os.path.exists(path1):
    path1 = os.path.join(path0, input('请重新输入同一目录下的有效jsonl文件名：'))


# dir_1 = os.getcwd11()
# print(dir_1)
print(analyze_log(path1))