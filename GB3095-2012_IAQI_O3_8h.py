def calculate_aqi(Cp, Ih, Il, BPh, BPl):
    """ 通用计算AQI公式 """
    return round((Ih - Il) / (BPh - BPl) * (Cp - BPl) + Il, 2)


def aqi_pm25(concentration):
    """ 根据PM2.5浓度计算AQI值 """
    breakpoints = [
        (0, 35, 0, 50),  # (BPl, BPh, Il, Ih)
        (35, 75, 50, 100),
        (75, 115, 100, 150),
        (115, 150, 150, 200),
        (150, 250, 200, 300),
        (250, 350, 300, 400),
        (350, 500, 400, 500)
    ]
    for (BPl, BPh, Il, Ih) in breakpoints:
        if BPl <= concentration < BPh:
            return calculate_aqi(concentration, Ih, Il, BPh, BPl)
    return "超出规定计算范围"


def aqi_pm10(concentration):
    """ 根据PM10浓度计算AQI值 """
    breakpoints = [
        (0, 50, 0, 50),
        (50, 150, 50, 100),
        (150, 250, 100, 150),
        (250, 350, 150, 200),
        (350, 420, 200, 300),
        (420, 500, 300, 400),
        (500, 600, 400, 500)
    ]
    for (BPl, BPh, Il, Ih) in breakpoints:

        if BPl <= concentration < BPh:
            return calculate_aqi(concentration, Ih, Il, BPh, BPl)
    return "超出规定计算范围"


def aqi_co(concentration):
    breakpoints = [
        (0, 2, 0, 50),
        (2, 4, 50, 100),
        (4, 14, 100, 150),
        (14, 24, 150, 200),
        (24, 36, 200, 300),
        (36, 48, 300, 400),
        (48, 60, 400, 500)
    ]
    for (BPl, BPh, Il, Ih) in breakpoints:

        if BPl <= concentration < BPh:
            return calculate_aqi(concentration, Ih, Il, BPh, BPl)
    return "超出规定计算范围"


def aqi_so2(concentration):
    breakpoints = [
        (0, 50, 0, 50),
        (50, 150, 50, 100),
        (150, 475, 100, 150),
        (475, 800, 150, 200),
        (800, 1600, 200, 300),
        (1600, 2100, 300, 400),
        (2100, 2620, 400, 500)
    ]
    for (BPl, BPh, Il, Ih) in breakpoints:

        if BPl <= concentration < BPh:
            return calculate_aqi(concentration, Ih, Il, BPh, BPl)
    return "超出规定计算范围"


def aqi_no2(concentration):
    breakpoints = [
        (0, 40, 0, 50),
        (40, 80, 50, 100),
        (80, 180, 100, 150),
        (180, 280, 150, 200),
        (280, 565, 200, 300),
        (565, 750, 300, 400),
        (750, 940, 400, 500)
    ]
    for (BPl, BPh, Il, Ih) in breakpoints:

        if BPl <= concentration < BPh:
            return calculate_aqi(concentration, Ih, Il, BPh, BPl)
    return "超出规定计算范围"


def aqi_o3(concentration):
    breakpoints = [
        (0, 100, 0, 50),
        (100, 160, 50, 100),
        (160, 215, 100, 150),
        (215, 265, 150, 200),
        (265, 800, 200, 300),
    ]
    for (BPl, BPh, Il, Ih) in breakpoints:

        if BPl <= concentration < BPh:
            return calculate_aqi(concentration, Ih, Il, BPh, BPl)
    return "超出规定计算范围"


concentration_pm25 = float(input("请输入24小时的PM2.5平均浓度(单位：μg/m³)："))
concentration_pm10 = float(input("请输入24小时的PM10平均浓度(单位：μg/m³)："))
concentration_so2 = float(input("请输入24小时的二氧化硫平均浓度(单位：μg/m³)："))
concentration_no2 = float(input("请输入24小时的二氧化氮平均浓度(单位：μg/m³)："))
concentration_co = float(input("请输入24小时的一氧化碳平均浓度(单位：μg/m³)："))
concentration_o3 = float(input("请输入8小时的臭氧平均浓度(单位：μg/m³)："))


aqi_pm25_value = aqi_pm25(concentration_pm25)
aqi_pm10_value = aqi_pm10(concentration_pm10)
aqi_so2_value = aqi_so2(concentration_so2)
aqi_no2_value = aqi_no2(concentration_no2)
aqi_co_value = aqi_co(concentration_co)
aqi_o3_value = aqi_o3(concentration_o3)

print(f'24小时平均浓度为{concentration_pm25}μg/m³的PM2.5, IAQI值{aqi_pm25_value}')
print(f'24小时平均浓度为{concentration_pm10}μg/m³的PM10, IAQI值{aqi_pm10_value}')
print(f'24小时平均浓度为{concentration_so2}μg/m³的二氧化硫, IAQI值{aqi_so2_value}')
print(f'24小时平均浓度为{concentration_no2}μg/m³的二氧化氮, IAQI值{aqi_no2_value}')
print(f'24小时平均浓度为{concentration_co}μg/m³的一氧化碳, IAQI值{aqi_co_value}')
print(f'8小时平均浓度为{concentration_o3}μg/m³的臭氧, IAQI值{aqi_o3_value}')
