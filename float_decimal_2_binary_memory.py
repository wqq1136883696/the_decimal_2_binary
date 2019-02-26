#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
Author: wyatt wang
Data : 2019.02.26
E-mail : 1136883696@qq.com
The purpose of this script is convert decimal float point number into binary display
and  display it as a decimal floating point number stored in the computer's memory.
此脚本的目的是将十进制浮点数(包括整数)转换为二进制显示，并显示在计算机内存中的十进制浮点数存储形式。

"""

from decimal import Decimal

BIAS = 127  # 指数位的偏移量


def divide_float(f_number):
    """分离整数和小数, 返回符号位，整数部分，和小数部分"""

    # 转换成正数
    sign = "0"
    if f_number < 0:
        sign = "1"
        f_number = -1 * f_number

    # 整数部分
    integer = int(f_number)

    # 小数部分
    decimal_part = Decimal(str(f_number)) - integer

    return sign, integer, decimal_part


def int2bin(integer):
    """把整数部分转化成二进制，整数部分不为O
    返回转换后的整数部分
    """
    integer_covert = str(bin(integer))
    return integer_covert[2:]


def decimal_part2bin(decimal_part):
    """把小数部分转化成二进制,小数部分不为O"""
    decimal_convert = ""

    for i in range(32):
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
        f_number_bin = "0"
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

    return f_number_bin, sign


def science_display(f_number_bin):
    """把二进制显示为科学计数表示,返回指数部分和小数部分的值
        例如： 1.01*2**3，默认整数位为1
    """
    str_part = f_number_bin.split('.')
    integer_bin = str_part[0]
    decimal_bin = ""
    if len(str_part) == 2:
        decimal_bin = str_part[1]

    if integer_bin != "0":
        # print(integer_bin)
        integer_length = len(integer_bin)
        exponent = integer_length - 1  # 科学计数法的指数部分
        # print(exponent)
        decimal_part1 = integer_bin[1:]  # 第一位为1，去剩下的作为小数部分的一部分
        decimal_part = decimal_part1 + decimal_bin  # 与原有的小数部分组合成一个新的小数部分
        # print(decimal_part)
    else:
        # print(decimal_bin)
        position = decimal_bin.find("1") + 1  # 小数部分第一个非0的位置
        exponent = -position  # 科学计数法的指数部分
        # print(exponent)
        decimal_part = decimal_bin[position:]
        # print(decimal_part)

    return exponent, decimal_part


def display_in_memory(f_number_bin, sign, exponent, decimal_part):
    """在计算机内存中的显示"""

    if f_number_bin == "0":
        f_number_memory = "0" * 32
    else:
        # 把指数位显示出来
        exponent = exponent + BIAS
        exponent_bin = bin(exponent)[2:]
        # print(exponent_bin)
        # 如果不足8位，在前面加0
        exponent_length = len(exponent_bin)
        add_number = 8 - exponent_length
        exponent_bin_memory = "0" * add_number + exponent_bin
        # print(exponent_bin_memory)

        # 把小数位显示出来，默认整数位为1,如果不足23位，在后面加0补足
        if len(decimal_part) >= 23:
            decimal_part_memory = decimal_part[:23]
        else:
            add_number_decimal = 23 - len(decimal_part)
            decimal_part_memory = decimal_part + "0" * add_number_decimal
        # print(decimal_part_memory)

        f_number_memory = sign + exponent_bin_memory + decimal_part_memory

    return f_number_memory


def main():
    """主程序的执行"""
    while True:
        print("输入q退出程序")
        input_str = input("请输入一个十进制数：")
        if input_str == "q":
            break
        try:
            f_number = Decimal(input_str)
            bin_number, sign = get_bin(f_number)
            # print(type(bin_number), bin_number)

            exponent, decimal_part = science_display(bin_number)
            f_number_memory = display_in_memory(bin_number, sign, exponent, decimal_part)
            print("你输入的数字为： %s\n转换为二进制为： %s \n在计算机中的表示为： %s\n\n"
                  % (input_str, bin_number, f_number_memory))
        except Exception:
            print("您的输入有误，请输入一个数字！\n")


if __name__ == '__main__':
    main()
