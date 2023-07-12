valueTable = {
    'standard': {
        'A4Paper': 0.3,
        'BKPrinting': 0.3,
        'CMYKPrinting': 0.4,
        'FullPageAddition': 0.1,
        'DoublePageAddition': -0.02,
        'PaperProcessAddition': 0.1,
    },
    'special': {
        'A4Paper': 0.2,
        'BKPrinting': 0.2,
        'CMYKPrinting': 0.3,
        'FullPageAddition': 0.1,
        'DoublePageAddition': -0.05,
        'PaperProcessAddition': 0.1,
    },
    'custom': {
        'A4Paper': 0,
        'BKPrinting': 0,
        'CMYKPrinting': 0,
        'FullPageAddition': 0,
        'DoublePageAddition': 0,
        'PaperProcessAddition': 0,
    },
}

print('---------- 欢迎使用打印计价器 ----------')
print('请选择计价方式：')
print('1. 标准计价')
print('2. 优惠计价')
print('3. 自定义计价')
print('--------------------------------------')

mode = input('请输入计价方式：')
if mode == '1':
    mode = 'standard'
elif mode == '2':
    mode = 'special'
elif mode == '3':
    mode = 'custom'
else:
    print('输入错误！')
    exit()

usingValue = valueTable[mode]
if mode == 'custom':
    usingValue['A4Paper'] = float(input('请输入A4纸张价格：'))
    usingValue['BKPrinting'] = float(input('请输入黑白打印价格：'))
    usingValue['CMYKPrinting'] = float(input('请输入彩色打印价格：'))
    usingValue['FullPageAddition'] = float(input('请输入高墨水覆盖率加价：'))
    usingValue['DoublePageAddition'] = float(input('请输入双面打印优惠（须带负号）：'))
    usingValue['PaperProcessAddition'] = float(input('请输入纸张处理加价：'))

print('--------------------------------------')
print('您选择的计价方式为：' + mode)
print('A4纸张价格：' + str(usingValue['A4Paper']))
print('黑白打印价格：' + str(usingValue['BKPrinting']))
print('彩色打印价格：' + str(usingValue['CMYKPrinting']))
print('高墨水覆盖率加价：' + str(usingValue['FullPageAddition']))
print('双面打印优惠：' + str(usingValue['DoublePageAddition']))
print('纸张处理加价：' + str(usingValue['PaperProcessAddition']))
print('--------------------------------------')


printingInfo = {}

print('请输入打印信息：')
printingInfo['A4Paper'] = int(input('A4纸张数量：'))
printingInfo['BKPrinting'] = int(input('黑白打印面数：'))
printingInfo['CMYKPrinting'] = int(input('彩色打印面数：'))
printingInfo['FullPageAddition'] = int(input('高墨水覆盖率面数：'))
printingInfo['DoublePageAddition'] = int(input('双面打印张数：'))
printingInfo['PaperProcessAddition'] = int(input('纸张处理张数：'))

print('--------------------------------------')
print('您输入的打印信息为：')
print('A4纸张数量：' + str(printingInfo['A4Paper']))
print('黑白打印面数：' + str(printingInfo['BKPrinting']))
print('彩色打印面数：' + str(printingInfo['CMYKPrinting']))
print('高墨水覆盖率面数：' + str(printingInfo['FullPageAddition']))
print('双面打印张数：' + str(printingInfo['DoublePageAddition']))
print('纸张处理张数：' + str(printingInfo['PaperProcessAddition']))
print('--------------------------------------')
print('价格表：')
print('A4纸张价格：' + str(usingValue['A4Paper'] * printingInfo['A4Paper']))
print('黑白打印价格：' + str(usingValue['BKPrinting'] * printingInfo['BKPrinting']))
print('彩色打印价格：' + str(usingValue['CMYKPrinting'] * printingInfo['CMYKPrinting']))
print('高墨水覆盖率加价：' + str(usingValue['FullPageAddition'] * printingInfo['FullPageAddition']))
print('双面打印优惠：' + str(usingValue['DoublePageAddition'] * printingInfo['DoublePageAddition']))
print('纸张处理加价：' + str(usingValue['PaperProcessAddition'] * printingInfo['PaperProcessAddition']))
print('--------------------------------------')
print('总价：' + str(
    usingValue['A4Paper'] * printingInfo['A4Paper'] +
    usingValue['BKPrinting'] * printingInfo['BKPrinting'] +
    usingValue['CMYKPrinting'] * printingInfo['CMYKPrinting'] +
    usingValue['FullPageAddition'] * printingInfo['FullPageAddition'] +
    usingValue['DoublePageAddition'] * printingInfo['DoublePageAddition'] +
    usingValue['PaperProcessAddition'] * printingInfo['PaperProcessAddition']
))
print('--------------------------------------')
