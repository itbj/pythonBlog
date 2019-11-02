import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 定义基本的一个环境（问题简单，直接写在外面了）
# 假设这个世界有20个位置
N_LOCATION = 90
# 定义动作空间，假设只有两个动作，向左或者向右
ACTIONS = ('L', 'R')
# 定义强化学习公式中的GAMMA，奖励递减率
GAMMA = 0.9
# 定义强化学习中的ALPHA,其实就是学习率，学习现实值和估计值之间的差异
ALPHA = 0.2
# 随机动作的概率
EPSILON = 0.1
# 一共训练160回合
EPISODES = 160


def create_q_table(n_state, actions):
    '''
    这里每一个状态用位置的下标去表示
    :param n_state: 状态的个数
    :param actions: 动作空间
    :return: q表
    '''
    table = pd.DataFrame(np.zeros((n_state, len(actions))), columns=actions)
    return table


# 定义一个选择动作的函数
def choose_action(state, q_table):
    # 得到该状态下，所有动作的概率
    state_actions_prob = q_table.iloc[state, :]
    # 如果是处于随机的那一部分或者所有行动概率都是０，那就随机选取一个动作
    if np.random.uniform() <= EPSILON or state_actions_prob.all() == 0:
        action = np.random.choice(ACTIONS)
    else:
        # 否则就选取概率较大的一个
        action = state_actions_prob.argmax()
    return action


# 定义一个执行动作之后，得到环境反馈的函数
def get_feedback(state, action):
    if action == 'L':
        if state == N_LOCATION - 2:
            state_ = 'OVER'
            reward = 1
        else:
            state_ = state + 1
            reward = 0
    else:
        reward = 0
        if state == 0:
            state_ = 0
        else:
            state_ = state -1
    return state_, reward


# 可视化
def show(state):
    s = ['－']*(N_LOCATION-1) + ['T']
    s[state] = '&'
    print(''.join(s))


# 进行强化学习的主题
def learn():
    q_table = create_q_table(N_LOCATION, ACTIONS)
    steps = []
    for i in range(EPISODES):
        # 假设寻宝人的出发地是第1个点
        state = 0
        # 是否寻找到宝藏
        is_find = False
        step = 0
        while not is_find:
            show(state)
            action = choose_action(state, q_table)
            state_, reward = get_feedback(state, action)
            # 得到state到state_的估计值
            q_predict = q_table.loc[state, action]
            if state_ == 'OVER':
                # 得到现实值
                q_target = reward
                is_find = True
            else:
                q_target = reward + GAMMA*q_table.iloc[state_, :].max()
            q_table.loc[state, action] += ALPHA * (q_target - q_predict)
            state = state_
            step += 1
        print('第　', i+1, '次训练结束, 用了 ', step, ' 步.')
        steps.append(step)
    plt.plot(steps)
    plt.show()


learn()
