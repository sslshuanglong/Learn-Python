#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse

'''
批量修改指定目录下文件的后缀
'''

def barch_rename(work_dir,old_ext,new_ext):
    # 列出工作目录下的所有的文件及文件夹
    for filename in os.listdir(work_dir):
        # 分离文件名与扩展名
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]

        if old_ext == file_ext:
            newfile = split_file[0] + new_ext
        
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )

def get_parser():
    # 程序使用帮助，可以使用 -h 查看
    parser = argparse.ArgumentParser(description='charge extension of files in working directory')
    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1,help='the directory where to charge extension')
    parser.add_argument('old_ext',metavar='old_ext',type=str,nargs=1,help='old extension')
    parser.add_argument('new_ext',metavar='new_ext',type=str,nargs=1,help='new extension')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    print(args)
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext

    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    barch_rename(work_dir,old_ext,new_ext)

if __name__ == '__main__':
    main()
