# all_files = open('all_files.txt', 'r+', encoding='utf8')


def wf1():
    with open('all_files.txt','r+', encoding = 'utf8') as all_files:
        all_files.write(f'1.txt\n{len(quanity_1)}\n')
        for i in quanity_1:
            all_files.write(i)
        all_files.write('\n\n')
        all_files.readline()



def wf2():
    with open('all_files.txt','r+', encoding = 'utf8') as all_files:
        all_files.write(f'2.txt\n{len(quanity_2)}\n')
        for i in quanity_2:
            all_files.write(i)
        all_files.write('\n')
        all_files.readline()


def wf3():
    with open('all_files.txt','r+', encoding = 'utf8') as all_files:
        all_files.write(f'3.txt\n{len(quanity_3)}\n')
        for i in quanity_3:
            all_files.write(i)
        all_files.write('\n\n')
        all_files.readline()

with open('1.txt','r', encoding = 'utf8') as file_1, open('2.txt','r', encoding = 'utf8') as file_2, open('3.txt','r', encoding = 'utf8') as file_3:
    quanity_1 = []
    quanity_2 = []
    quanity_3 = []

    for line1 in file_1:
        quanity_1.append(line1)
    
    for line2 in file_2:
        quanity_2.append(line2)

    for line3 in file_3:
        quanity_3.append(line3)
    
max = max(len(quanity_1), len(quanity_2), len(quanity_3))
min = min(len(quanity_1), len(quanity_2), len(quanity_3))

if len(quanity_1) > len(quanity_2) > len(quanity_3):
    wf3()
    wf2()
    wf1()
elif len(quanity_1) < len(quanity_2) < len(quanity_3):
    wf1()
    wf2()
    wf3()
elif len(quanity_1) < len(quanity_2) > len(quanity_3) and len(quanity_1) > len(quanity_3):
    wf3()
    wf1()
    wf2()
elif len(quanity_1) < len(quanity_2) > len(quanity_3) and len(quanity_1) < len(quanity_3):
    wf1()
    wf3()
    wf2()
elif len(quanity_1) > len(quanity_2) < len(quanity_3) and len(quanity_1) > len(quanity_3):
    wf2()
    wf3()
    wf1()
elif len(quanity_1) > len(quanity_2) < len(quanity_3) and len(quanity_1) < len(quanity_3):
    wf2()
    wf1()
    wf3()
