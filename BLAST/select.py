# -*- coding: UTF-8 -*-
import random

list = ["赵婵","秦国洋","柳皓宇","范达熠","雷昊晨","管子义","雷巧"]
list_num = [0,1,2,3,4,5,6,]
select = random.sample(list_num,2)
print list[select[0]],list[select[1]]