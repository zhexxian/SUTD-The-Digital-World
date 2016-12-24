weight = input('Weight in pound:')
height = input('Height in inches:')

def bmi(weight, height):
    weight_in_kg = 0.45359237 * weight
    height_in_m = 0.0254 * height
    BMI = (weight_in_kg) / ( height_in_m ** 2)
    return BMI

print 'BMI: %s' %(bmi(weight, height))