import numpy as np
reference=np.array([74, 73, 74, 62, 61, 69, 64, 66, 62, 74, 73, 71, 73, 78, 81, 83, 79, 78, 76, 79, 78, 76, 74, 73, 71, 69, 67, 66, 64, 67, 66, 64])  #需要取定一个参考乐曲

initial_parameter= [-0.1,-0.1,1,200,10] #这些都是fitness function参数，之后可以人工修改

def evaluate_chord(chord):
    # chord是一个音符序列，假设为一个整数列表，表示和弦的音高
    
    # 在这里进行和弦的评估，根据具体需求和评估标准来编写评估逻辑
    
    # 示例评估逻辑：判断和弦是否符合某种特定的音程规则
    intervals = np.array([chord[i+1] - chord[i] for i in range(len(chord)-1)])  # 计算音程
    intervals[intervals>20] = 4
    # 定义一个目标音程列表，例如：大三度、纯四度、纯五度
    target_intervals = [4, 5, 7]
    
    # 计算和弦中与目标音程不符合的音程数量
    incorrect_intervals = sum([1 for interval in intervals if interval not in target_intervals])
    
    # 根据不符合音程的数量计算和弦的质量得分
    chord_quality = 1 - (incorrect_intervals / len(intervals))
    
    return chord_quality


def evaluate_leap_transitions(melody):
    leap_transitions = 0  # 记录跳跃音过渡的数量

    for i in range(len(melody) - 2):
        # 计算相邻音符之间的音高差
        interval1 = abs(melody[i+1] - melody[i])
        interval2 = abs(melody[i+2] - melody[i+1])
        
        # 判断是否存在跳跃音过渡，例如大于一个预设的音程阈值
        leap_threshold = 4  # 音程阈值，例如4表示大三度
        if interval1 > leap_threshold and interval2 > leap_threshold:
            leap_transitions += 1
    
    leap_transition_fitness = 1 - (leap_transitions / (len(melody) - 2))  # 计算跳跃音过渡的质量得分
    
    return leap_transition_fitness


def fitness_function(x,parameter):  #x是自变量，其余是参数 
    x=np.array(x)
    part_1 = abs(np.mean(reference)-np.mean(x[x>=21]))  #part_1表示与参考数组的均值差距
    part_2 = abs(np.var(reference)-np.var(x[x>=21]))   #part_2表示与参考数组的方差差距
    part_3 = 0    #part_3表示超出一个范围的音符个数，这里取【65，75】
    n=1
    m=0
    for i in range(len(x)):
        if (x[i]>=21) and not (65< x[i] <75) :
            n += 1
        if (x[i]==0) or (x[i]==20):
            m += 1
    if m < 4:
        n+=(4-m)*2
    if m > 12:
        n+=(m-12)*2


    part_3 = 1./n
    x_filter = x[x>=21]
    #print(x,x_filter)
    part_4 = evaluate_chord(x) #part_4表示好听的和弦的比例
    part_5 = evaluate_leap_transitions(x_filter)
    return parameter[0]*part_1 + parameter[1]*part_2 + parameter[2]*part_3 + parameter[3]*part_4 + parameter[4]*part_5

y=[64, 20, 20, 67, 67, 20, 20, 20, 64, 20, 20, 62, 60, 20, 20, 20, 62, 20, 20, 64, 67, 20, 20, 64, 62, 20, 20, 20, 20, 20, 20, 20]
#x = [64, 64, 64,64,64, 64, 64,64,64, 64, 64,64,64, 64, 62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62]
#random_y = np.random()
print(fitness_function(y,initial_parameter))
