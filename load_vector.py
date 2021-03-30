from gensim.models.keyedvectors import KeyedVectors
import numpy as np

file_vector='sgns.weibo.word'

# model = KeyedVectors.load_word2vec_format('sgns.zhihu.word', limit=100)
# model = gensim.models.Word2Vec.load('sgns.zhihu.word')
# print(type(model), dir(model))

works_set = set(['一对一', '现在', '主要', '那个', '面试', '销售', '这个', '场景', '对', '内容', '进行', '分析', '绘画', '会话'])
works_set = set(['会话', '绘画', '我们', '公司', '正在', '做', '的', '事情', '，', '其实', '要', '做', '人工智能', '的', '人工智能', '领域', '的', '会', '话', '分析', '。', '然后', '目前', '想要', '去', '在', '三个', '场景', '。'])
works_set = set(['对接', '就是', '我们', '现在', '不仅仅', '跟', '你', '一家', '在', '堆积', '，', '我们', '在', '了解', '到', '其他', '家', '的', '这个', '价格', '。'])

print(works_set)
weights_dict = {}
with open(file_vector, 'r') as f:
    for rl in f.readlines():
        items = rl.strip('\n').split(' ')
        _word=items[0]
        if _word in works_set:
            _vector = [float(_) for _ in items[1:-1]]
            print(rl, np.array(_vector))
            weights_dict[_word] = np.array(_vector)

# print(weights_dict)

def _calculate_distance(word:str):
    dist = 0
    for k, v in weights_dict.items():
        if k != word:
            print(type(v), type(weights_dict[word]))
            dist += np.linalg.norm(v - weights_dict[word])
    return dist

print(_calculate_distance('堆积'))
print(_calculate_distance('对接'))
