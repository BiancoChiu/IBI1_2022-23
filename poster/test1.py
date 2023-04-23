from tkinter import *
from tkinter.filedialog import askopenfilename
from pyjaspar import jaspardb
from math import log2
import pandas as pd
import re

jdb_obj = jaspardb(release='JASPAR2022')
factors = dict()
regular = dict()
PWM = dict()
check_box = {}


def get_score(seq, factor_name):
    score = 0
    for i in range(len(seq)):
        # 从 PWM 矩阵中查找当前位置对应的碱基得分
        site_score = PWM[factor_name].loc[seq[i], i]
        score += site_score
    return score


def create_check():
    global check_box
    for i in range(len(factors)):
        check_box[i] = BooleanVar()
        Checkbutton(main, text=factors[i], variable=check_box[i]).grid(row=i + 11, column=0, sticky=W)


def delete_checkbox():
    # 获取所有放置在主窗口上的小部件
    widgets = main.grid_slaves()
    for widget in widgets:
        # 如果这个小部件是一个复选框
        if isinstance(widget, Checkbutton):
            # 将其从窗口中移除
            widget.grid_remove()


def identify():
    # delete returns and spaces in input
    sequence = text1.get('1.0', 'end')
    seq_list = sequence.split()
    sequence = ''.join(seq_list)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, sequence)
    for i in sequence:
        if i not in ['A', 'T', 'C', 'G']:
            text6.delete('1.0', 'end')
            text6.insert('1.0', 'This is not a general DNA sequence.\n', 'tag')
            return
    boolean_list = list()
    selected_factors = list()
    for j in check_box:
        boolean_list.append(check_box[j].get())
        if check_box[j].get():
            selected_factors.append(factors[j])
    if boolean_list.count(True) == 2:
        label1.config(text='Output result')
        label_factor1.config(text='Factor1: ' + selected_factors[0])
        label_factor2.config(text='Factor2: ' + selected_factors[1])
        label3.config(text='Location and Scores of ' + selected_factors[0])
        label4.config(text='Location and Scores of ' + selected_factors[1])
        factor1 = [[m.start(), m.end()] for m in re.finditer(regular[selected_factors[0]], sequence)]
        factor2 = [[m.start(), m.end()] for m in re.finditer(regular[selected_factors[1]], sequence)]
        text1.delete('1.0', 'end')
        text2.delete('1.0', 'end')
        text3.delete('1.0', 'end')
        text1.insert(INSERT, 'There are %s sites for %s\n' % (len(factor1), selected_factors[0]))
        text1.insert(INSERT, 'There are %s sites for %s\n' % (len(factor2), selected_factors[1]))
        text2.insert(INSERT, sequence)
        text3.insert(INSERT, sequence)
        for L in factor1:
            sub_seq = sequence[L[0]: L[1]]
            sub_seq_score = get_score(sub_seq, selected_factors[0])
            if sub_seq_score > 0:
                text2.tag_add('tag', '1.' + str(L[0]), '1.' + str(L[1]))
                text4.insert(INSERT, sequence[L[0]: L[1]] + ' ' + str(L[0]) + ':' + str(L[1]) + ' '
                             + '%.2f' % sub_seq_score + '\n')
        for L in factor2:
            sub_seq = sequence[L[0]: L[1]]
            sub_seq_score = get_score(sub_seq, selected_factors[1])
            if sub_seq_score > 0:
                text3.tag_add('tag', '1.' + str(L[0]), '1.' + str(L[1]))
                text5.insert(INSERT, sequence[L[0]: L[1]] + ' ' + str(L[0]) + ':' + str(L[1]) + ' '
                             + '%.2f' % sub_seq_score + '\n')
        for i in factor1:
            for j in factor2:
                if i[0] > j[1] or i[1] < j[0]:
                    text1.insert(INSERT, 'These factors are possible to bind simultaneously')
                    return
                else:
                    text1.insert(INSERT, 'These factors are impossible to bind simultaneously')
                    return
    elif boolean_list.count(True) == 1:
        label1.config(text='Output result')
        label_factor1.config(text='Factor1: ' + selected_factors[0])
        label3.config(text='Location and Scores of ' + selected_factors[0])
        factor = [[m.start(), m.end()] for m in re.finditer(regular[selected_factors[0]], sequence)]
        text1.delete('1.0', 'end')
        text1.insert(INSERT, 'There are %s sites for %s\n' % (len(factor), selected_factors[0]))
        text2.insert(INSERT, sequence)
        for L in factor:
            sub_seq = sequence[L[0]: L[1]]
            sub_seq_score = get_score(sub_seq, selected_factors[0])
            if sub_seq_score > 0:
                text2.tag_add('tag', '1.' + str(L[0]), '1.' + str(L[1]))
                text4.delete('1.0', 'end')
                text4.insert(INSERT, sequence[L[0]: L[1]] + ' ' + str(L[0]) + ':' + str(L[1]) + ' '
                             + '%.2f' % sub_seq_score + '\n')
    else:
        text6.delete('1.0', 'end')
        text6.insert('1.0', 'Please select 1 or 2 factor(s)\n', 'tag')


def open_file():
    file_path = askopenfilename(title='Select the sequence file')
    if file_path is not None:
        with open(file=file_path) as f:
            input_sequence = f.read()
        text1.delete('1.0', 'end')
        text1.insert(INSERT, input_sequence)


def initialization():
    text1.delete('1.0', 'end')
    text2.delete('1.0', 'end')
    text3.delete('1.0', 'end')
    text4.delete('1.0', 'end')
    text5.delete('1.0', 'end')
    text6.delete('1.0', 'end')
    entry1.delete(0, END)
    label1.config(text='Input Sequence')
    label3.config(text='Location and Scores of ___')
    label4.config(text='Location and Scores of ___')
    label_factor1.config(text='Factor 1: ___')
    label_factor2.config(text='Factor 2: ___')


main = Tk()
main.title('bonding site')

menu = Menu(main, tearoff=1)
menu.add_command(label='Open File', command=open_file)
menu.add_command(label='Initialization', command=initialization)
menu.add_command(label='Exit', command=main.destroy)
main.config(menu=menu)

# text1: input and output box
# text2 and 3: visualize sites
# text4 and 5: show scores
# text6: show error info
text1 = Text(main, height=8)
text1.grid(rowspan=2, row=2, column=1)
text2 = Text(main, height=8)
text2.grid(rowspan=3, row=5, column=1)
text2.tag_configure('tag', foreground='indianred')
text3 = Text(main, height=8)
text3.grid(rowspan=3, row=9, column=1)
text3.tag_configure('tag', foreground='orange')

text4 = Text(main, height=20, width=30)
text4.grid(rowspan=6, row=2, column=3)
text5 = Text(main, height=20, width=30)
text5.grid(rowspan=6, row=2, column=4)
text6 = Text(main, height=6, width=30)
text6.grid(rowspan=2, row=8, column=0)
text6.tag_config('tag', foreground='red')

label1 = Label(text='Input Sequence', bg='lightyellow')
label1.grid(row=1, column=1)
label2 = Label(text='Type in the JASPAR ID of the new factor you are interested in')
label2.grid(row=2, column=0)
label3 = Label(main, text='Location and Scores of ___', bg='navajowhite')
label3.grid(row=1, column=3)
label4 = Label(main, text='Location and Scores of ___', bg='navajowhite')
label4.grid(row=1, column=4)
label_factor1 = Label(text='Factor 1: ___', bg='lightyellow')
label_factor1.grid(row=4, column=1)
label_factor2 = Label(text='Factor 2: ___', bg='lightyellow')
label_factor2.grid(row=8, column=1)
label_error = Label(text='Error Info', bg='red')
label_error.grid(row=7, column=0)


def fetch_motif(tf_id=None):
    if entry1.get():
        tf_id = entry1.get()
    # 从jaspar获取TF的信息
    motif = jdb_obj.fetch_motif_by_id(tf_id)
    # 数据处理，生成PWM矩阵用于打分
    df = pd.DataFrame(motif.counts).T
    df_sum = df.sum()
    df = df / df_sum
    df = df / 0.25
    df = df.applymap(lambda x: log2(x + 1e-20))
    # 将PWM存储在哈希
    PWM[str(motif).split()[2]] = df
    regular_motif = ''
    factors[len(factors)] = str(motif).split()[2]
    for i in range(len(df.columns)):
        temp_df = pd.DataFrame(df.iloc[:, i])
        temp_df.columns = ['0']
        temp_df = temp_df[temp_df['0'] > -2]
        regular_motif += '[' + ''.join(temp_df.index) + ']'
    regular[str(motif).split()[2]] = regular_motif
    entry1.delete(0, END)
    delete_checkbox()
    create_check()


entry1 = Entry(main)
entry1.grid(row=3, column=0)
add_button = Button(main, text='Add factor', command=fetch_motif)
add_button.grid(row=4, column=0)

button1 = Button(main, text='Try to find sites', command=identify)
button1.grid(row=10, column=0)

fetch_motif('MA0032.2')
fetch_motif('MA0033.2')
main.mainloop()
