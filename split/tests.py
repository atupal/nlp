#-*- coding: utf-8 -*-

from mmseg import Algorithm, dict_load_defaults

def cuttest(text):
    wlist = [word for word in Algorithm(text)]
    tmp = "/".join(wlist)
    print tmp
    print "================================"

def benchmark(text):
    import time
    dict_load_defaults()
    print ">>>> load dict done!"

    for i in range(100):
        begin = time.time()
        wlist = [word for word in Algorithm(text)]
        end = time.time()
        print ">>>> times: %f" % float(end-begin)

if __name__=="__main__":
    cuttest(u"请把手抬高一点儿")
    cuttest(u"长春市长春节致词。")
    cuttest(u"长春市长春药店。")
    cuttest(u"我的和服务必在明天做好。")
    cuttest(u"一次性交一百元。")
    cuttest(u"我发现有很多人喜欢他。")
    cuttest(u"我喜欢看电视剧大长今。")
    cuttest(u"半夜给拎起来陪看欧洲杯糊着两眼半晌没搞明白谁和谁踢。")
    cuttest(u"李智伟高兴兴以及王晓薇出去玩，后来智伟和晓薇又单独去玩了。")
    cuttest(u"一次性交出去很多钱。 ")
    cuttest(u"这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。")
    cuttest(u"我不喜欢日本和服。")
    cuttest(u"雷猴回归人间。")
    cuttest(u"工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
    cuttest(u"我需要廉租房")
    cuttest(u"永和服装饰品有限公司")
    cuttest(u"我爱北京天安门")
    cuttest(u"abc")
    cuttest(u"隐马尔可夫")
    cuttest(u"雷猴是个好网站")
    cuttest(u"“Microsoft”一词由“MICROcomputer（微型计算机）”和“SOFTware（软件）”两部分组成")
    cuttest(u"草泥马和欺实马是今年的流行词汇")
    cuttest(u"伊藤洋华堂总府店")
    cuttest(u"中国科学院计算技术研究所")
    cuttest(u"罗密欧与朱丽叶")
    cuttest(u"我购买了道具和服装")
    cuttest(u"PS: 我觉得开源有一个好处，就是能够敦促自己不断改进，避免敞帚自珍")
    cuttest(u"湖北省石首市")
    cuttest(u"总经理完成了这件事情")
    cuttest(u"电脑修好了")
    cuttest(u"做好了这件事情就一了百了了")
    cuttest(u"人们审美的观点是不同的")
    cuttest(u"我们买了一个美的空调")
    cuttest(u"线程初始化时我们要注意")
    cuttest(u"一个分子是由好多原子组织成的")
    cuttest(u"祝你马到功成")
    cuttest(u"他掉进了无底洞里")
    cuttest(u"中国的首都是北京")
    cuttest(u"孙君意")
    cuttest(u"外交部发言人马朝旭")
    cuttest(u"领导人会议和第四届东亚峰会")
    cuttest(u"在过去的这五年")
    cuttest(u"还需要很长的路要走")
    cuttest(u"60周年首都阅兵")
    cuttest(u"你好人们审美的观点是不同的")
    cuttest(u"买水果然后来世博园")
    cuttest(u"买水果然后去世博园")
    cuttest(u"但是后来我才知道你是对的")
    cuttest(u"存在即合理")
    cuttest(u"的的的的的在的的的的就以和和和")
    cuttest(u"I love你，不以为耻，反以为rong")
    cuttest(u" ")
    cuttest(u"")
    cuttest(u"hello你好人们审美的观点是不同的")
    cuttest(u"很好但主要是基于网页形式")
    cuttest(u"hello你好人们审美的观点是不同的")
    cuttest(u"为什么我不能拥有想要的生活")
    cuttest(u"后来我才")
    cuttest(u"此次来中国是为了")
    cuttest(u"使用了它就可以解决一些问题")
    cuttest(u",使用了它就可以解决一些问题")
    cuttest(u"其实使用了它就可以解决一些问题")
    cuttest(u"好人使用了它就可以解决一些问题")
    cuttest(u"是因为和国家")
    cuttest(u"老年搜索还支持")
    cuttest(u"干脆就把那部蒙人的闲法给废了拉倒！RT @laoshipukong : 27日，全国人大常委会第三次审议侵权责任法草案，删除了有关医疗损害责任“举证倒置”的规定。在医患纠纷中本已处于弱势地位的消费者由此将陷入万劫不复的境地。 ")
