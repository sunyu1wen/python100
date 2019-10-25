from time import  time
def main():
    total = 0
    number_list = [x for x in range(1,10000001)]
    # result_queue  = Queue()
    # index = 0
    start = time()
    for number in number_list:
         total += number
    print(total)
    end = time()
    print('Excusion time: %.3fs' %(end -start))

if __name__ == '__main__':
    main()

# 具体的做法就是通过multiprocessing.managers模块中提供的管理器将Queue对象通过网络共享出来（注册到网络上让其他计算机可以访问），
# 这部分内容也留到爬虫的专题再进行讲解。