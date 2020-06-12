import math

angle = float(input('Type the angle u want: '))
print('SINE: {:.2f}\n'
      'COSINE: {:.2f}\n'
      'TANGENT: {:.2f}\n'.format(math.sin(math.radians(angle)), math.cos(math.radians(angle)), math.tan(math.radians(angle))))