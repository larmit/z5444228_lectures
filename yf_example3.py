# Created at 4/10/2023
# Name: Tianhao Wu
# Student ID: z5444228
# Course: FINS 5546
# Project: To download stock price data for Qantas for a given year and save the information in a CSV file.

import os
import yf_example2
import toolkit_config as cfg

def qan_prc_to_csv(year: int):
    s_date=f'{year}-01-01'
    e_date=f'{year}-12-31'
    tic='QAN.AX'
    outputDoc=f'qan_prc_{year}.csv'
    pth=os.path.join(cfg.DATADIR,outputDoc)

    yf_example2.yf_prc_to_csv(tic,pth,s_date,e_date)



if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)


