#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
==================
crash率曲线绘制
==================

根据crash数据文件，绘制多版本crash率曲线
"""

import matplotlib.pyplot as plt
import pandas as pd

crash_data = pd.read_table('data.txt', sep='\s+', header=None, names=['date', 'ver', 'startup', 'crash'])
crash_data = crash_data.sort_values(['date'], ascending=True)

fig, ax = plt.subplots()

group_ver = crash_data.groupby('ver')
for name, group in group_ver:
    print name, group

    crash = group['crash']
    startup = group['startup']
    crash_rate = 100 * crash / startup

    print crash_rate
    date = group['date']
    x_index = range(0, len(crash))

    line = ax.plot(x_index, crash_rate, label=name)
    # line = ax.plot(x_index, crash, 'o', label=name)
    ax.legend(loc='upper center')
    plt.xticks(x_index, date, rotation='vertical')
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)

plt.show()
