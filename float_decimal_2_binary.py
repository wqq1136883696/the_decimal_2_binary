#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Author: wyatt wang
Data : 2019.02.26
E-mail : 1136883696@qq.com
The purpose of this script is convert decimal float point number into binary display.

"""

from decimal import Decimal


def divide_float(f_number):
    """
        分离整数和小数，返回符号位，整数部分，和小数部分
    """
    # 转换成正数
    sign = 0
    if f_number < 0:
        sign = 1
        f_number = -1 * f_number

    # 整数部分
    integer = int(f_number)

    # 小数部分
    decimal_part = Decimal(str(f_number)) - integer

    return sign, integer, decimal_part


def int2bin(integer):
    """
        把整数部分转化成二进制，整数部分不为O
        返回转换后的整数部分
    """
    integer_covert = str(bin(integer))
    return integer_covert[2:]


def decimal_part2bin(decimal_part):
    """把小数部分转化成二进制,小数部分不为O"""
    decimal_convert = ""

    for i in range(23):
        result = decimal_part * 2
        # print(result)
        decimal_convert += str(int(result))
        decimal_part = result - int(result)

        if result == 1:
            break

    return decimal_convert


def get_bin(f_number):
    """得到完整的二进制表示"""
    sign, integer, decimal = divide_float(f_number)
    # 判断如果整数部分和小数部分都为0，则全为0
    if integer == 0 and decimal == 0:
        f_number_bin = "0" * 32
    else:
        # 如果整数部分为零，则显示为0
        if integer != 0:
            integer_bin = int2bin(integer)
        else:
            integer_bin = "0"

        # 如果小数部分为零，则不显示
        if decimal != 0:
            decimal_bin = decimal_part2bin(decimal)
            f_number_bin = integer_bin + "." + decimal_bin
        else:
            f_number_bin = integer_bin

    return f_number_bin


# noinspection PyBroadException
def main():
    """主程序的执行"""
    while True:
        print("输入q退出程序")
        input_str = input("请输入一个十进制数：")
        if input_str == "q":
            break
        try:
            f_number = Decimal(input_str)
            bin_number = get_bin(f_number)
            print(bin_number)
        except Exception:
            print("您的输入有误，请输入一个数字！")


if __name__ == '__main__':
    main()
