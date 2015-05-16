# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 12:01:50 2014

@author: Wouter
"""
import csv
import datetime
import argparse


def fix_date(rawdate):
    return datetime.datetime.strptime(rawdate, "%Y%m%d").strftime("%d/%m/%Y")

parser = argparse.ArgumentParser(description='Convert Rabo csv to YNAB csv')
parser.add_argument("filename", help='csv filename to convert')
args = parser.parse_args()

input_file = args.filename
output_file = input_file[:-4]+'_rabo.csv'
with open(input_file, 'rb') as csv_in, open(output_file, 'wb') as csv_out:
    csvreader = csv.reader(csv_in, delimiter=',')
    csvwriter = csv.writer(csv_out, delimiter=',')
    header_row = ['Date', 'Payee', 'Category', 'Memo', 'Outflow', 'Inflow']
    csvwriter.writerow(header_row)
    for row in csvreader:
        row_str = ['','','','','','']
        row_str[0] = fix_date(row[2]) # Date
        if row[6]:
            row_str[1] = row[6] # Payee
        elif not row[6]:
            row_str[1] = row[10] # Memo is payee
        row_str[2] = '' # Category, leave empty for now
        row_str[3] = row[10] # Memo
        if row[3] =='D':
            row_str[4] = row[4] 
            row_str[5] = ''
        elif row[3] == 'C':
            row_str[4] = ''
            row_str[5] = row[4]
        csvwriter.writerow(row_str)
    print 'file converted and saved to:\n%s' % output_file
    

