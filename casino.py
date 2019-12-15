# coding=UTF-8
#[oppose_odds, uven_odds]

def manbet_uven(odd_platform, odd_manbet, money_platform, platform):
    '''
    万博尤文活动。
    :param odd_platform: 平台赔率
    :param odd_manbet: 万博赔率
    :param money_platform: 平台下注额
    :param platform: 平台
    :return: 万博下注额
    '''
    re_insurance_percent = 0.03 if platform == 'lovebet' else 0
    reward_percent_manbet = 0.004
    reward_percent_platform = 0.007 if platform == 'crown' else 0.004
    money_manbet_max = 152 / (odd_manbet - 1) / 0.05 #max_bet is for Uven, 0.05 is reward for uven
    money_platform_max = (money_manbet_max * odd_manbet + money_manbet_max * (odd_manbet - 1) * 0.05) / ( odd_platform - re_insurance_percent)
    money_manbet = money_platform / money_platform_max * money_manbet_max
    print('money_manbet_max: {money_manbet_max}, money_manbet: {money_manbet}\n'
          'money_platform_max: {money_platform_max}, money_platform: {money_platform}'.format(
        money_manbet_max=money_manbet_max, money_manbet=money_manbet, money_platform_max=money_platform_max, money_platform=money_platform))

    print('profit: {}'.format(
        money_platform * odd_platform - money_platform - money_manbet +
        money_platform * reward_percent_platform + money_manbet * reward_percent_manbet
    ))
    return money_manbet


def platform_vs_manbet(odd_platform, odd_manbet, money_platform, platform):
    '''
    平台与万博打对水。
    爱博负盈利>1000, 返水3%，爱博/万博 日返水 0.4%，爱博存款送10%彩金。

    :param odd_platform: 爱博赔率
    :param odd_manbetx: 万博赔率
    :param money_platform: 爱博下注额
    :param platform: 平台（爱博，贝博，吉祥坊等）
    :return: 万博下注额
    '''
    re_insurance_percent = 0.03 if platform == 'lovebet' else 0
    money_reward = int(money_platform/1000) * 10 if platform == 'lovebet' else 0
    reward_percent = 0.004
    money_manbet = money_platform * (odd_platform - re_insurance_percent)/odd_manbet
    print('money_manbet: {}'.format(money_manbet))
    print('profit: {}'.format(
        money_platform * odd_platform - money_platform - money_manbet + money_manbet * reward_percent +
        money_platform * reward_percent + money_reward
    ))
    return money_manbet


def lovebet_vs_manbetx_insurance(odd_lovebet, odd_wellbet, money_lovebet):
    '''
    爱博保险投注活动。
    爱博负盈利>1000, 返水3%，爱博/万博 日返水 0.4%，爱博存款送10%彩金，爱博指定赛事负盈利>1000赠送彩金。

    :param odd_lovebet: 爱博赔率
    :param odd_wellbet: 万博赔率
    :param money_lovebet: 爱博投注额
    :return:吉祥坊投注额
    '''
    if money_lovebet >= 1000 and money_lovebet <= 1999:
        money_rebonus = 59
    elif money_lovebet >= 2000 and money_lovebet <= 4999:
        money_rebonus = 99
    elif money_lovebet >= 5000 and money_lovebet <= 9999:
        money_rebonus = 199
    elif money_lovebet >= 10000 and money_lovebet <= 29999:
        money_rebonus = 299
    elif money_lovebet >= 30000 and money_lovebet <= 49999:
        money_rebonus = 399
    elif money_lovebet >= 50000 and money_lovebet <= 99999:
        money_rebonus = 699
    elif money_lovebet >= 100000:
        money_rebonus = 999

    money_wellbet = (odd_lovebet * money_lovebet - money_lovebet * 0.03 - money_rebonus)/odd_wellbet

    print("money_wellbet: {}".format(money_wellbet))
    print("profit: {}".format(
        odd_lovebet * money_lovebet - money_wellbet - money_lovebet + 0.004 * (money_wellbet + money_lovebet) + int(money_lovebet/1000) * 10
    ))
    return money_wellbet


def mycat_vs_manbetx(odd_mycat, odd_manbetx, money_mycat):
    '''

    :param odd_mycat: mycat赔率
    :param : 万博赔率
    :param money_mycat: mycat下注额
    :return:
    '''

    money_mycat_best = 2000/(odd_mycat - 1)  #money_mycat下注最佳额
    money_mycat_prof = money_mycat * (odd_mycat - 1)    #money_mycat盈利金额

    if money_mycat_prof >= 300 and money_mycat_prof < 500:
        bonus = 58
    elif money_mycat_prof >= 500 and money_mycat_prof < 2000:
        bonus = 88
    elif money_mycat_prof >= 2000:
        bonus = 388
    else:
        bonus = 0

    money_manbetx = (odd_mycat * money_mycat + bonus) / odd_manbetx

    profit = (odd_manbetx-1) * money_manbetx - money_mycat

    print("mycat最佳投注额: ", money_mycat_best)
    print("manbet下注额: ", money_manbetx)
    print("profit盈利: ", profit)


def eura_champion(odd_mycat, odd_manbetx, mycat_flag=True):
    '''

    :param odd_mycat: mycat 赔率
    :param odd_manbetx: 万博赔率
    :param money_mycat: mycat下注额
    :param mycat_flag: mycat赔率是否是上盘
    :return:
    '''

    # 活动期间用户于平博体育、沙巴体育或猫先生体育投注欧洲冠军联赛（仅限早盘），用户投注队伍为该场赛事首先进球队伍，注单为结算为赢，即可获得58元红利。
    # 有效投注>=200，上盘打出，大概率盈利嘉奖58元

    money_mycat = 205
    bonus = 58

    if mycat_flag:
        money_manbetx = (odd_mycat * money_mycat + bonus) / odd_manbetx
        profit = money_manbetx * ( odd_manbetx - 1 ) - money_mycat
        max_lose = money_mycat * (odd_mycat - 1) - money_manbetx
    else:
        money_manbetx = (odd_mycat * money_mycat - bonus) / odd_manbetx
        profit = money_mycat * (odd_mycat - 1) - money_manbetx
        max_lose = money_manbetx * (odd_manbetx - 1) - money_mycat

    print("manbet下注额: ", money_manbetx)
    print("profit盈利: ", profit)
    print("max损失:", max_lose)


if __name__ == '__main__':

    # manbet_uven(1.92, 2.00, 2000, 'wellbet')
    # manbet_uven(odd_platform=1.86,odd_manbet=2.07,money_platform=1418,platform='crown')
    # platform_vs_manbet(odd_platform=1.96, odd_manbet=1.99, money_platform=3191,platform='lovebet')
    # lovebet_vs_manbetx_insurance(odd_lovebet=2.02, odd_wellbet=1.91, money_lovebet=2031)

    mycat_vs_manbetx(odd_mycat=1.94, odd_manbetx=2.00, money_mycat=2200)


    # mycat_grace 210
    # 萨格勒布戴纳魔 vs 曼城cat
    # eura_champion(odd_mycat=1.96, odd_manbetx=2.02, mycat_flag=True)
    # 勒沃库森cat vs 尤文图斯
    # eura_champion(odd_mycat=2.01, odd_manbetx=1.94, mycat_flag=True)
    # 旷工 vs 亚特兰大cat
    # eura_champion(odd_mycat=1.87, odd_manbetx=2.09, mycat_flag=False)
    # 布鲁日 vs 皇马cat
    # eura_champion(odd_mycat=1.94, odd_manbetx=2.01, mycat_flag=True)
    # 拜仁 vs 热刺cat
    # eura_champion(odd_mycat=2.04, odd_manbetx=1.93, mycat_flag=False)
    # 马竞 vs 火车头cat
    # eura_champion(odd_mycat=2.12, odd_manbetx=1.87, mycat_flag=False)
    # 巴黎cat vs 加拉塔萨雷
    # eura_champion(odd_mycat=1.98, odd_manbetx=1.96, mycat_flag=True)
    # 奥林匹亚 vs 贝尔格莱德cat
    # eura_champion(odd_mycat=1.9, odd_manbetx=2.07, mycat_flag=False)


    # mycat_badou 205
    # 萨格勒布戴纳魔 vs 曼城cat
    # eura_champion(odd_mycat=1.94, odd_manbetx=2.01, mycat_flag=True)
    # 勒沃库森cat vs 尤文图斯
    # eura_champion(odd_mycat=1.97, odd_manbetx=1.98, mycat_flag=True)
    # 旷工cat vs 亚特兰大
    # eura_champion(odd_mycat=2.03, odd_manbetx=1.92, mycat_flag=True)
    # 布鲁日 vs 皇马cat
    # eura_champion(odd_mycat=1.95, odd_manbetx=2.0, mycat_flag=True)
    # 拜仁cat vs 热刺
    # eura_champion(odd_mycat=1.98, odd_manbetx=1.97, mycat_flag=True)
    # 马竞cat vs 火车头
    # eura_champion(odd_mycat=1.85, odd_manbetx=2.11, mycat_flag=True)
    # 巴黎cat vs 加拉塔萨雷
    # eura_champion(odd_mycat=2, odd_manbetx=1.95, mycat_flag=True)
    # 奥林匹亚cat vs 贝尔格莱德
    # eura_champion(odd_mycat=2.05, odd_manbetx=1.86, mycat_flag=True)




    # mycat_badou
