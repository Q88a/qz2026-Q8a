'''理解了一下测试脚本是啥后，果断让deepseek生成了以下:
但保证main是手搓的！
'''
import json
import os

from main import analyze_log

print('——上方数据是将新输入数据作为文件名的返回结果——'
      '——下方是基于app.jsonl结果，ai生成的测试脚本检查结果——')

def test_file_not_exist():
    """测试 1：文件不存在，应返回固定的空结构"""
    result = analyze_log("not_exist.jsonl")
    expected = {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
    assert result == expected, f"文件不存在应返回 {expected}，实际得到 {result}"
    print("[通过] 文件不存在返回空结构")


def test_empty_file():
    """测试 2：空文件，应返回固定的空结构"""
    with open('_empty_test.jsonl', 'w', encoding='utf-8') as f:
        pass
    result = analyze_log('_empty_test.jsonl')
    expected = {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
    assert result == expected, f"空文件应返回 {expected}，实际得到 {result}"
    os.remove('_empty_test.jsonl')
    print("[通过] 空文件返回空结构")


def test_bad_line_skipped():
    """测试 3：坏行应被跳过，不中断"""
    with open('_bad_test.jsonl', 'w', encoding='utf-8') as f:
        f.write('{"timestamp": "t1", "level": "INFO", "message": "ok", "user": "u1"}\n')
        f.write('111\n')
        f.write('{"timestamp": "t2", "level": "ERROR", "message": "bad", "user": "u2"}\n')
    result = analyze_log('_bad_test.jsonl')
    assert result['total'] == 2, f"坏行应被跳过，total 应为 2，实际得到 {result['total']}"
    os.remove('_bad_test.jsonl')
    print("[通过] 坏行被跳过")


def test_normal_file():
    """测试 4：用 app.jsonl 验证真实数据"""
    result = analyze_log('app.jsonl')
    # app.jsonl 里正常行数：你自己数一下，把下面的 6 改成实际值
    print(f"[信息] app.jsonl 结果: {result}")
    assert result['total'] > 0, "正常文件 total 应大于 0"
    print("[通过] 正常文件能解析")


if __name__ == '__main__':
    test_file_not_exist()
    test_empty_file()
    test_bad_line_skipped()
    test_normal_file()
    print("\n全部测试通过！")