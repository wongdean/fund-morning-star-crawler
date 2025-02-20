'''
Desc:
File: /main.py
Project: fund-morning-star-crawler
File Created: Thursday, 28th October 2021 10:51:07 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2021 Camel Lu
'''

import logging
import sys

sys.path.append('./src')

from src.acquire_fund_base import acquire_fund_base
from src.acquire_fund_quarter import acquire_fund_quarter
from src.acquire_fund_snapshot import get_fund_list
from src.fund_info_supplement import update_fund_archive_status
from src.fund_statistic import (all_stock_holder_detail, all_stocks_rank,
                                calculate_quarter_fund_total,
                                get_combination_holder_stock_detail,
                                t100_stocks_rank)
from src.fund_strategy import output_high_score_funds
from src.sync_fund_base import further_complete_base_info, sync_fund_base


def main():
    input_value = input("请输入下列序号执行操作:\n \
        1.“快照” \n \
        2.“新基入库”\n \
        3.“快照同步新基”\n \
        4.“补充基金基础数据”\n \
        5.“基金状态归档”\n \
        6.“季度信息”\n \
        7.“基金持仓股排名”\n \
        8.“基金重仓股Top100”\n \
        9.“股票持仓基金明细”\n \
        10.“股票持仓基金汇总”\n \
        11.“高分基金”\n \
        12.“组合持仓明细”\n \
    输入：")
    if input_value == '1':
        page_index = 1
        get_fund_list(page_index)  # 执行申万行业信息入库
    elif input_value == '2':
        acquire_fund_base()  # 执行行业股票信息入库
    elif input_value == '3':
        page_index = 1
        sync_fund_base(page_index)
    elif input_value == '4':
        further_complete_base_info()
    elif input_value == '5':
        update_fund_archive_status()
    elif input_value == '6':
        acquire_fund_quarter()
    elif input_value == '7':
        all_stocks_rank()
    elif input_value == '8':
        t100_stocks_rank()
    elif input_value == '9':
        all_stock_holder_detail()
    elif input_value == '10':
        calculate_quarter_fund_total()
    elif input_value == '11':
        output_high_score_funds()
    elif input_value == '12':
        get_combination_holder_stock_detail()
    else:
        print('输入有误')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                        filename='log/crawler.log',  filemode='a', level=logging.INFO)
    main()
