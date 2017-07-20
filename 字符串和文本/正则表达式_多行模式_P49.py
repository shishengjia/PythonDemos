import re

comment_pat = re.compile(r'/\*(.*?)\*/')
text_1 = '/* this is a comment */'
text_2 = '''/* this is a
                multiline comment */
        '''
print(comment_pat.findall(text_1)) # [' this is a comment ']
# 句点不能和匹配换行符
print(comment_pat.findall(text_2)) # []

"""
两种方法添加对换行符的支持
"""

# 第一种，re.compile()接受一个标记，re.DOTALL
comment_pat_2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment_pat_2.findall(text_2)) # [' this is a\n                multiline comment ']

# 第二种，(?:.|\n)指定了一个非捕获组，这个组只做匹配但不捕获结果,Python核心编程正则表达式扩展表示法可以查到
comment_pat_2 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment_pat_2.findall(text_2)) # [' this is a\n                multiline comment ']
