#-*- coding: utf-8 -*-

###############################################################################
# 基本数据结构
###############################################################################

class Word:
    def __init__(self, text='', freq=0):
        self.text = text
        self.freq = freq
        self.length = len(text)

class Chunk:
    def __init__(self, w1, w2=None, w3=None):
        self.words = []
        self.words.append(w1)
        if w2:
            self.words.append(w2)
        if w3:
            self.words.append(w3)

    # 总长度
    def total_length(self):
        length = 0
        for w in self.words:
            length += len(w.text)
        return length

    # 平均长度
    def average_length(self):
        return float(self.total_length()) / float(len(self.words))

    # 标准平方差
    def variance(self):
        import math
        avg = self.average_length()
        sqr_sum = 0.0

        for w in self.words:
            tmp = len(w.text)
            tmp = tmp-avg
            sqr_sum += float(tmp)*float(tmp)
        return math.sqrt(sqr_sum)

    # 自由语素度
    def degree_of_morphemic_freedom(self):
        freqs = 0
        for w in self.words:
            freqs += w.freq
        return freqs

    # 调试输出
    def printx(self):
        print ('========================================')
        for w in self.words:
            print ('word: %s' % w.text)
        print ('total_length = %d' % self.total_length())
        print ('average_length = %f' % self.average_length())
        print ('variance = %f' % self.variance())
        print ('degree_of_morphemic_freedom = %f' % self.degree_of_morphemic_freedom())
        print ('========================================')

###############################################################################
# 字典的加载与解析
###############################################################################

words_dict = {}
max_word_length = 0

def dict_get_word(text):
    entry = words_dict.get(text)
    if entry:
        return Word(text, entry[1])
    return None

def dict_load_chars(filename):
    global max_word_length
    f = file(filename)
    for line in f.readlines():
        freq, word = line.split(' ')
        word = unicode(word.strip(), 'utf-8')
        words_dict[word] = (len(word), int(freq))
        max_word_length = max_word_length < len(word) and len(word) or max_word_length
    f.close()

def dict_load_words(filename):
    global max_word_length
    f = file(filename)
    for line in f.readlines():
        word = unicode(line.strip(), 'utf-8')
        words_dict[word] = (len(word), 0)
        max_word_length = max_word_length < len(word) and len(word) or max_word_length
    f.close()

def dict_load_defaults():
    from os.path import join, dirname
    dict_load_chars(join(dirname(__file__), 'data', 'chars.dic'))
    dict_load_words(join(dirname(__file__), 'data', 'words.dic'))

###############################################################################
# 过滤器
###############################################################################

def take_highest(chunks, comparator):
    i = 1
    for j in range(1, len(chunks)):
        rlt = comparator(chunks[j], chunks[0])
        if rlt > 0:
            i = 0
        if rlt >= 0:
            chunks[i], chunks[j] = chunks[j], chunks[i]
            i += 1
    return chunks[0:i]

def mm_filter(chunks):
    def comparator(a, b):
        return a.total_length() - b.total_length()
    return take_highest(chunks, comparator)

def lawl_filter(chunks):
    def comparator(a, b):
        return a.average_length() - b.average_length()
    return take_highest(chunks, comparator)

def svwl_filter(chunks):
    def comparator(a, b):
        return a.variance() - b.variance()
    return take_highest(chunks, comparator)

def lsdmfocw_filter(chunks):
    def comparator(a, b):
        return a.degree_of_morphemic_freedom() - b.degree_of_morphemic_freedom()
    return take_highest(chunks, comparator)

###############################################################################
# 以下为算法实现
###############################################################################

class Algorithm(object):
    match_cache_size = 3

    def __init__(self, text):
        if isinstance(text, unicode):
            self.text = text
        else:
            self.text = unicode(text, 'utf-8')
        self.text_length = len(self.text)
        self.pos = 0
        self.match_cache_i = 0
        self.match_cache = []

        for i in range(self.match_cache_size):
            self.match_cache.append([-1, Word()])

        # 确保有字典
        if not words_dict:
            dict_load_defaults()

    def __iter__(self):
        while True:
            tk = self.next_token()
            if tk is None:
                raise StopIteration
            yield tk

    def next_token(self):
        while self.pos < self.text_length:
            if self.is_cjk_char(self.next_char()):
                tk = self.get_cjk_word()
            else:
                tk = self.get_basic_latin_word()
            if len(tk) > 0:
                return tk
        return None

    def next_char(self):
        return self.text[self.pos]

    def is_cjk_char(self, ch):
        return 0x4e00 <= ord(ch) < 0x9fa6

    def is_latin_char(self, ch):
        import string
        if ch in string.whitespace:
            return False
        if ch in string.punctuation:
            return False
        return ch in string.printable

    def get_basic_latin_word(self):
        # Skip pre-word whitespaces and punctuations
        while self.pos < self.text_length:
            ch = self.next_char()
            if self.is_latin_char(ch) or self.is_cjk_char(ch):
                break
            self.pos += 1

        start = self.pos
        while self.pos < self.text_length:
            if not self.is_latin_char(self.next_char()):
                break
            self.pos += 1
        end = self.pos

        # Skip post-word whitespaces and punctuations
        while self.pos < self.text_length:
            ch = self.next_char()
            if self.is_latin_char(ch) or self.is_cjk_char(ch):
                break
            self.pos += 1

        return self.text[start:end]

    def get_cjk_word(self):
        chunks = self.create_chunks()
        if len(chunks) > 1:
            chunks = mm_filter(chunks)
        if len(chunks) > 1:
            chunks = lawl_filter(chunks)
        if len(chunks) > 1:
            chunks = svwl_filter(chunks)
        if len(chunks) > 1:
            chunks = lsdmfocw_filter(chunks)

        if len(chunks) < 1:
            return ''

        length = len(chunks[0].words[0].text)
        token = self.text[self.pos:self.pos+length]
        self.pos += length
        return token

    def create_chunks(self):
        chunks = []
        orig_pos = self.pos

        words1 = self.find_match_words()
        for w1 in words1:
            self.pos += len(w1.text)
            if self.pos < self.text_length:
                words2 = self.find_match_words()
                for w2 in words2:
                    self.pos += len(w2.text)
                    if self.pos < self.text_length:
                        words3 = self.find_match_words()
                        for w3 in words3:
                            if w3.length == -1:
                                chunk = Chunk(w1, w2)
                            else:
                                chunk = Chunk(w1, w2, w3)
                            chunks.append(chunk)
                    elif self.pos == self.text_length:
                        chunk = Chunk(w1, w2)
                        chunks.append(chunk)
                    self.pos -= len(w2.text)
            elif self.pos == self.text_length:
                chunk = Chunk(w1)
                chunks.append(chunk)
            self.pos -= len(w1.text)

        self.pos = orig_pos
        return chunks

    def find_match_words(self):
        for i in range(self.match_cache_size):
            if self.match_cache[i][0] == self.pos:
                return self.match_cache[i][1]

        orig_pos = self.pos
        n = 0
        words = []

        while self.pos < self.text_length:
            if n >= self.max_word_length():
                break
            if not self.is_cjk_char(self.next_char()):
                break

            self.pos += 1
            n += 1

            text = self.text[orig_pos:self.pos]
            word = dict_get_word(text)
            if word:
                words.append(word)

        self.pos = orig_pos
        if not words:
            word = Word()
            word.length = -1
            word.text = 'X'
            words.append(word)

        self.match_cache[self.match_cache_i] = (self.pos, words)
        self.match_cache_i += 1
        if self.match_cache_i >= self.match_cache_size:
            self.match_cache_i = 0

        return words

    def max_word_length(self):
        return max_word_length
