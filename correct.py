import pycorrector

pycorrector.set_custom_confusion_dict(path='./confusion.txt')
sentence = '分支下面的一个分支绘画智能。那在这绘画智能，我们把绘画智能运用到销售这个领域里面。那在国内整个行业里面应该算是就是。'
sentence = '我的爱好也就是绘画跟音乐而已，无他。'
corrected_sent, detail = pycorrector.correct(sentence)
print(corrected_sent, detail)
