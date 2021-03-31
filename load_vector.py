from gensim.models.keyedvectors import KeyedVectors
import numpy as np

file_vector = 'sgns.weibo.word'

# model = KeyedVectors.load_word2vec_format('sgns.zhihu.word', limit=100)
# model = gensim.models.Word2Vec.load('sgns.zhihu.word')
# print(type(model), dir(model))

works_set = set([
    '一对一', '现在', '主要', '那个', '面试', '销售', '这个', '场景', '对', '内容', '进行', '分析',
    '绘画', '会话'
])
works_set = set([
    '会话', '绘画', '我们', '公司', '正在', '做', '的', '事情', '，', '其实', '要', '做', '人工智能',
    '的', '人工智能', '领域', '的', '会', '话', '分析', '。', '然后', '目前', '想要', '去', '在',
    '三个', '场景', '。'
])
works_set = set([
    '会话', '针对', '这', '里面', '去', '做', '复盘', '，', '然后', '呢', '在', '这', '里面', '呢',
    '它', '有', '一个', '分析', '，', '就是', '这个', '核心', '这个', '公司', '的', '核心', '的',
    '提供', '的', '服务', '就', '叫做', '绘画', '智能', '。'
])

# print(works_set)
# weights_dict = {}
# with open(file_vector, 'r') as f:
#     for rl in f.readlines()[:10]:
#         items = rl.rstrip().split(' ')
#         print(items)
#         # _word = items[0]
# if _word in works_set:
#     _vector = [float(_) for _ in items[1:-1]]
#     # print(rl, np.array(_vector))
#     weights_dict[_word] = np.array(_vector)

# print(weights_dict)


def load_vectors(file_vector) -> dict:
    res = {}
    with open(file_vector, 'r') as f:
        for rl in f.readlines():
            items = rl.rstrip().split(' ')
            res[items[0]] = items[1:]
    print(f'{file_vector} completely loaded.')
    return res


def _calculate_distance(vec, vec_list):
    def str2float(vec):
        return np.array([float(e) for e in vec])

    float_vec = str2float(vec)
    return sum(np.linalg.norm(float_vec - str2float(e)) for e in vec_list)


vector_dict = load_vectors('sgns.weibo.word')


def pick_one(wa: str, wb: str, sentence: str):
    import jieba
    wordlist = jieba.lcut(sentence)
    filter_set = {'、', '，', '。', '！', '？', wa, wb}
    wordlist = [w for w in wordlist if w not in filter_set]
    wordlist += [wa, wb]
    
    print('set of words: ', wordlist)

    vector_list = [vector_dict.get(word, [0] * 300) for word in wordlist]

    res1 = _calculate_distance(vector_dict[wa], vector_list)
    res2 = _calculate_distance(vector_dict[wb], vector_list)
    print(wa, res1, wb, res2)


# print(_calculate_distance('会话'))
# print(_calculate_distance('绘画'))
sss = """"针对这里面去做复盘，然后呢在这里面呢它有一个分析，就是这个核心这个公司的核心的提供的服务就叫做绘画智能。"
 "它是把绘画智能这个技术应用到了那个销售领域销售团队上面，然后未销售整个团队这个赋能，对吧？是这样一个东西，那除了这个以外呢。"
 "就是他其实就不仅是说提供一个这样的软件类的东西，他更多的是想提供一个就我说的绘画智能这样一个服务。它可能这个服务可以应用于。"
 "它就是两个核心。第一个核心就是它提供的绘画智能分析这样一个功能是吧？这是这个公司的最大的一个核心技术支持。在此基础上呢，我们衍生出来的这个是对销售团队去赋能的这样。"
 "还是重点，不是抓c，rm就是重点是抓绘画智能。然后那个绘画智能它对于整个销售的各个方面的能力的提升。"
 "然后你包括你去搜绘画智能相关的东西的话，你可能在百度上现在都搜不到什么确定的内容。所以说其实就是我们在这个领域里面是做的。"
 "分支下面的一个分支绘画智能。那在这绘画智能，我们把绘画智能运用到销售这个领域里面。那在国内整个行业里面应该算是就是。"
 "平时呢，我也就喜欢绘画或者看书，也就这点爱好。"
 "摄影、绘画、读书、音乐
 绘画在技术层面上，是一个以表面作为支撑面，并在其之上加上颜色的动作。那些表面可以是纸张、油画布、木材、玻璃、漆器或混凝土等，上色的工具可以是画笔，也可以是刀、海绵，甚至是油漆喷雾器、牙刷、手指等等"""
# pick_one('绘画', '会话', sentence)

for s in sss.split('\n'):
    sentence = s.lstrip().strip("\"")
    print(sentence)
    pick_one('销售', '消瘦', sentence)
