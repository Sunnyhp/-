
#!/usr/bin/python
# coding: utf-8

"""
pypinyin 模块 https://github.com/mozillazg/python-pinyin
"""
from pypinyin import lazy_pinyin # 加载汉语转拼音模块

with open('city_names.txt', 'r')as f:
    data = f.readlines()
    
    print '请输入一个城市名'
    input_name = raw_input('').strip()
    
    def is_city_name(name):
        '''
        1. 判断输入的城市名是否为中文，若不是中文，提示重新输入。
        2. 若输入的城市名为中文，则判断输入的城市名是否存在，若不存在，提示重新输入。
        3. 若输入的城市名存在，则返回 True。
        '''
        if u'\u4e00' <= name.decode('utf-8') <= u'\u9fff':
            for city_names in data:
                if city_names.strip() == name:
                    return True
            print '\n输入的城市名不存在，请重新输入！'
        else:
            print '\n请输入中文城市名'
    
    def get_city_name(input_name):
        '''
        两种匹配模式
        1. 匹配输入的城市名最后一个字和已知的城市名第一个字相同的情况。
        2. 谐音模式匹配
        '''
        if is_city_name(input_name):
            result = set() # 存储匹配的城市名
            for names in data:
                if input_name.decode('utf-8')[-1] == names.decode('utf-8')[0]:
                    result.add(names.strip())
                elif lazy_pinyin(input_name.decode('utf-8'))[-1] == lazy_pinyin(names.decode('utf-8'))[0]:
                    result.add(names.strip())
            
            if len(result) > 0:
                print '\n已找到对应的城市，它们是\n' ,repr(result).decode('string-escape')
            else:
                print '\n找不到，试试其它的城市吧'
    
    if __name__ == '__main__':
        get_city_name(input_name)

