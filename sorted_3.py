def bubble_sorted(seq):#冒泡排序
    length = len(seq)
    for i in range(length-1):
        print(seq)
        for j in range(length-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                
#选择排序
                
def select1_sorted(seq): #空间复杂度太大，容易理解
    length = len(seq)
    for i in range(length-1):
        print(seq)
        for j in range(i+1,length):
            if seq[j] < seq[i]:
                seq[j], seq[i] = seq[i], seq[j]
                
def select2_sorted(seq): #操作index，效率高
    length = len(seq)
    for i in range(length-1):
        min_idx = i #最小值索引
        for j in range(i+1,length):
            if seq[j] < seq[min_idx]:
                min_idx = j

        if min_idx != i: # 判断最小索引是否改变
            seq[min_idx], seq[i] = seq[i], seq[min_idx]

# 插入排序

def insertion_sorted(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        idx = i
        while idx > 0 and value <= seq[idx-1]:
            seq[idx] = seq[idx-1]
            idx -= 1
        seq[idx] = value

    
        
                
            
            
            
            
            
        
def test():
    import random
    l = list(range(10))
    random.shuffle(l)
    insertion_sorted(l)
    print(l)
    assert l == sorted(l)
if __name__ == '__main__':
    
    test()
