# 我们国家BMI正常范围标准波动在18.5-23.9kg/m^2。如果BMI≥24kg/m^2诊断超重；如果BMI≥28kg/m^2诊断肥胖；如果BMI＞35kg/m^2，甚至40kg/m^2以上，考虑重度危险性肥胖；如果BMI＜18.5kg/m^2，考虑体重过轻。

def count_bmi(h, w):
    bmi = w / h ** 2
    return bmi


def bmi_range(bmi):
    if bmi > 35:
        return '你属于危险性肥胖'
    elif bmi > 28:
        return '你属于肥胖'
    elif bmi > 24:
        return '你属于超重'
    elif bmi > 18.5:
        return '你属于正常体重'
    else:
        return '你属于体重过轻'


while True:
    try:
        height = float(input('请输入你的身高(cm):')) / 100
        weight = float(input('请输入你的体重(kg):'))
    except ValueError:
        print('你输入的数据有问题,请重新输入')
    else:
        break

print(bmi_range(count_bmi(height, weight)))
