import jieba
from jieba import posseg
jieba.case_sensitive = True
my_load_file = 'angry.txt'
my_save_file = my_load_file[:-3]+'_myposseg.txt'

my_file_temp = []
with open(my_load_file, 'r', encoding='utf-8') as f:
    my_lines = f.readlines()
    for my_setense in my_lines:
        print(my_setense.split('\n')[0])

        documents = [my_setense.split('\n')[0]]
        # seg_list = jieba.cut("早安，我的女神，希望你有美好的一天。")

        for sentence in documents:
            seg_list = jieba.lcut(sentence)
            print(seg_list)

        words = posseg.cut(my_setense.split('\n')[0])
        for word, flag in words:
            if flag != 'x':
                print(f'{word} {flag}')
                my_flags = f'{word} /{flag} '
                my_file_temp.append(my_flags)
        my_file_temp.append('\n')

print(my_file_temp)
with open(my_save_file, 'w', encoding='utf-8') as f:
    for data in my_file_temp:
        f.write(data)

