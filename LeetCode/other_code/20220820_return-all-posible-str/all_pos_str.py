#!/usr/bin/python
#-*-encoding:utf-8 -*-

'''
以终为始，对这类通用性的方法，其实可以仅仅考虑最后一步和第一步的。考虑的方法如果这两步是通的，就说明这些步骤都是可以通用化完成了。
'''


tmp_dict = {
  '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
}

def recur_str(one_str):
    if len(one_str) == 1:
        return [one_letter for one_letter in tmp_dict[one_str]]
    else:
        list_before = recur_str(one_str[:-1])
        list_now = [one_letter for one_letter in tmp_dict[one_str[-1]]]
        list_result = []
        for one_before in list_before:
            for one_now in list_now:
                list_result.append(one_before + one_now)
        return list_result 

if __name__ == '__main__':
    print(recur_str('298'))
