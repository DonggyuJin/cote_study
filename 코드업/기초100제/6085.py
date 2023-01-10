w, h, b = map(int, input().split())
storage = (w*h*b)/8
mb = (storage) / (1024**2)

print('%.2f'%mb, 'MB')
