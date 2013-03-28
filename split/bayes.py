#coding=utf-8
import re
import xml.dom.minidom
from mmseg import Algorithm, dict_load_defaults

class Bayes:
    def __init__(self):
        self.message_xml = open('message.xml', "r")
        self.message = self.message_xml.read()
        self.good = {}
        self.bad = {}
        import collections
        self.total = collections.defaultdict(lambda: 1)
        return

    def get_messages(self):
        pattern_message = re.compile('(<Body><\!\[CDATA\[)(.+?)(\]\]></Body>)')
        self.message.decode('utf-8')
        res = pattern_message.findall(self.message)
        message_flag = open('message_flag', 'w')
        for mes in res:
            tmp = unicode(mes[1], 'utf-8')
            print(tmp)
            flag = raw_input()
            message_flag.write(tmp.encode('utf-8') + ' ' + flag + '\n')
            for word in Algorithm(tmp):
                self.total[word] += 1
        message_xml.close()
        for i in self.total.keys():
            print i,self.total[i]

    def cuttest(self, text):
        wlist = [word for word in Algorithm(text)]
        tmp = "/".join(wlist)
        print (tmp)
        print ("================================")

if __name__ == '__main__':
    bayes = Bayes()
    bayes.get_messages()
