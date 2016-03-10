# -*- coding:utf-8 -*-
"""
    
"""

__author__ = 'Jux.Liu'

lrc_list = list()


def analyseLRC(file_path):
    line_current = ''
    line_current_items = []
    flag = True
    with open(file_path, 'r') as fh:
        while flag:
            if len(line_current) == 0:
                line_current = fh.readline()
            if len(line_current_items) == 0:
                line_current_items = line_current.split()
                time_current = line_current_items[0][1:-2]

            line_next = fh.readline()

            if len(line_next):
                line_next_items = line_next.split()
                time_next = line_next_items[0][1:-2]
            else:
                flag = False

            item = {
                'time'       : None,
                'duration'   : None,
                'word'       : None,
                'definitions': list()
            }

            item['time'] = time_current
            item['duration'] = subtimestr(time_next, time_current)
            item['word'] = line_current_items[1]
            length = len(line_current_items) - 1
            for n in range(2, length, 2):
                item['definitions'].append('{0} {1}'.format(line_current_items[n], line_current_items[n + 1]))

            line_current = line_next
            line_current_items = line_next_items
            time_current = time_next

            lrc_list.append(item)

    return lrc_list


def subtimestr(time_1, time_2):
    time_1 = time_1.split(':')
    time_2 = time_2.split(':')
    minute = int(time_1[0]) - int(time_2[0])
    second = float(time_1[1]) - float(time_2[1])
    res = '%02d:%0.2f' % (minute, second) if minute > 0  else float("%0.2f" % (second))
    return res


if __name__ == '__main__':
    print(analyseLRC('/home/jux/Documents/bw/words.txt'))
