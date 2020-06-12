distance = int(input('Type some distance in meters: '))

print('The distance of {} meters is equal to: \n'
      '{}km \n'
      '{}hm \n'
      '{}dam \n'
      '{}dm \n'
      '{}cm \n'
      '{}mm \n'.format(distance, distance/1000, distance/100, distance/10, distance*10, distance*100, distance*1000))