width = float(input('Type ur wall width: '))
height = float(input('Type ur wall height: '))

print('Your wall size is {}x{} or {}m².\nYou will need {: .2f}L of ink to paint your wall'.format(width, height,(width*height), (width*height)/2))