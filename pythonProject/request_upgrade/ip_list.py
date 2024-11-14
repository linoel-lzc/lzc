import re


def list_ip(text_name):
    read_txt = open(f'./{text_name}', 'r', encoding='utf-8')
    temp = []
    for line in read_txt:
        lines = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        string_lines = ' '.join(lines)
        temp.append(string_lines)
    return temp


if __name__ == '__main__':
    a = list_ip('ip_list1')
    print(a)
