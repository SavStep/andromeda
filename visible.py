# color = 'blue'
# def f():
#     global color
#     color = 'red'
#     print(f'Внутри {color}')
# if __name__ ==  '__main__':
#     print(f'Снаружи {color}')
#     f()
#     print(f'Снаружи {color}')
def download():
    from progress.bar import Bar
    import time
    bar = Bar('Processing', max=100)
    for i in range(100):
        # Do some work
        bar.next()
        time.sleep(0.1)
    bar.finish()
# from playsound import playsound
# playsound('C:/Users/User/Desktop/андромеда/time.mp3')
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
