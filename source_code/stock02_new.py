#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tushare as ts
import talib as ta
import numpy as np
import pandas as pd
import os,time,sys,re,datetime
import csv
import scipy
import smtplib
import email
from email.mime.text import MIMEText
#from email.MIMEMultipart import MIMEMultipart
#
import importlib

 

#首先是获取沪深两市的股票列表
#这里得到是对应的dataframe数据结构，它是类似于excel中一片数据的数据结构，有这些列：code,代码 name,名称 industry,所属行业 area,地区 pe,市盈率 outstanding,流通股本 totals,总股本(万) totalAssets,总资产(万)liquidAssets,流动资产 fixedAssets,固定资产 reserved,公积金 reservedPerShare,每股公积金 eps,每股收益 bvps,每股净资 pb,市净率 timeToMarket,上市日期
def Get_Stock_List():
    df = ts.get_stock_basics()
    #df = ts.get_k_data('399300', index=True,start='2017-01-01', end='2017-03-07')
    return df

 

#然后定义通过MACD判断买入卖出
def Get_MACD_New(df_Code):
    operate_array=[]
    for code in df_Code.index:
# 获取每只股票的历史价格和成交量 对应的列有index列,0 - 6列是 date：日期 open：开盘价 high：最高价 close：收盘价 low：最低价 volume：成交量 price_change：价格变动 p_change：涨跌幅
# 7-12列是 ma5：5日均价 ma10：10日均价 ma20:20日均价 v_ma5:5日均量v_ma10:10日均量 v_ma20:20日均量
        #print (code)
        df = ts.get_hist_data(code,start='2017-03-01')
        print (df)
        df.to_excel('/Users/FreySong/Python/code_group/stock.xlsx',encoding='utf-8')

    return df_Code

 

#输出CSV文件，其中要进行转码，不然会乱码
def Output_Csv(df,Dist):
    TODAY = datetime.date.today()
    CURRENTDAY=TODAY.strftime('%Y-%m-%d')
    importlib.reload(sys)
    df.to_csv(Dist+CURRENTDAY+'stock.csv',encoding='utf-8')#选择保存   

#输出CSV文件，其中要进行转码，不然会乱码
def Output_Excel(df,Dist):
    TODAY = datetime.date.today()
    CURRENTDAY=TODAY.strftime('%Y-%m-%d')
    importlib.reload(sys)
    df.to_excel(Dist+CURRENTDAY+'stock.xlsx',encoding='utf-8')#选择保存   
 

#def Close_machine():

   
#发送邮件
       
df = Get_Stock_List()
df = Get_MACD_New(df)
Dist = '/Users/FreySong/Python/code_group/'
#Output_Csv(df,Dist)
#Output_Excel(df,Dist)
#生成的csv文件中，macd列大于0的就是可以买入的，小于0的就是卖出的
#Send_Mail ('Finish TA',Dist)
#Close_machine()
