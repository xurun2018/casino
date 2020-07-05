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
    针对grace账户（v1）进行的投注策略判断。
    :param odd_mycat: mycat赔率
    :param odd_manbetx: 万博赔率
    :param money_mycat: mycat下注额
    :return:
    '''

    rebonus_manbetx = 0.02
    rebonus_cat = 0.04
    manbet_bonus = 152
    money_manbetx = (odd_mycat * money_mycat + manbet_bonus - money_mycat * rebonus_cat)/ (odd_manbetx + rebonus_manbetx)
    print(money_manbetx)
    print("总盈利:", (money_mycat * (odd_mycat - 1) - money_manbetx + manbet_bonus))
    print("总盈利:", (money_manbetx * (odd_manbetx - 1) + money_mycat * rebonus_cat + money_manbetx * rebonus_manbetx - money_mycat))

    # print("总盈利:", money_manebet_original * (odd_manbetx -1) + num_manbetx * 152 - money_mycat_add - money_mycat )


def platform_vs_manbetx(odd_plat, odd_manbetx, money_manbetx):
    '''
    父亲节万博活动
    :param odd_plat: 对打平台赔率
    :param odd_manbetx: 万博赔率
    :param money_manbetx: 万博平台下注额
    :return:
    '''

    #rebonus: 万博奖励彩金

    win_manbetx = money_manbetx * (odd_manbetx - 1)

    rebonus = 0
    if win_manbetx >= 352 and win_manbetx < 520:
        rebonus = 8

    elif win_manbetx >= 520 and win_manbetx < 888:
        rebonus = 18
    elif win_manbetx >= 888 and win_manbetx < 1520:
        rebonus = 28
    elif win_manbetx >= 1520 and win_manbetx < 5520:
        rebonus = 52
    elif win_manbetx >= 5520:
        rebonus = 188



    rebonus_water = 0.004
    money_plat = (money_manbetx * odd_manbetx + rebonus)/odd_plat
    print("money_plat:", money_plat)
    print("总盈利:", (money_manbetx * (odd_manbetx - 1) - money_plat + rebonus + money_manbetx * rebonus_water))
    print("总盈利:", money_plat * (odd_plat - 1)  - money_manbetx + money_manbetx * rebonus_water)

    # print("总盈利:", money_manebet_original * (odd_manbetx -1) + num_manbetx * 152 - money_mycat_add - money_mycat )



def  pb_vs_manbetx(odd_pb, odd_manbetx, money_pb):
    '''
    有效投注    最高返还    流水倍数
    >=300       28          3
    >=500       38          3
    >=1000      88          3
    >=5000      508         3
    >=10000     1088        3

    :param odd_pb: 拼搏赔率
    :param odd_manbetx: 万博赔率
    :param money_pb： pb下注额
    :return:
    '''

    rebonus_water = 0.004
    if money_pb >= 300 and money_pb < 500:
        rebonus = 28
    elif money_pb >= 500 and money_pb < 1000:
        rebonus = 38
    elif money_pb >= 1000 and money_pb < 5000:
        rebonus = 88
    elif money_pb >= 5000 and money_pb < 10000:
        rebonus = 588
    elif money_pb >= 10000:
        rebonus = 1088
    else:
        rebonus = 0

    money_manbetx = (money_pb * odd_pb - rebonus) / odd_manbetx
    print("manbet下注额: ", money_manbetx)
    print("profit:", money_manbetx * (odd_manbetx - 1) + rebonus - money_pb + ( money_pb + money_manbetx ) * rebonus_water )
    print("profit:", money_pb * (odd_pb - 1) - money_manbetx + ( money_pb + money_manbetx ) * rebonus_water )


def  pb_vs_manbetx_barcelona_madrid(odd_pb, odd_manbetx, money_pb):
    '''
    针对巴萨皇马pb比赛
    :param odd_pb: 拼搏赔率
    :param odd_manbetx: 万博赔率
    :param money_pb： pb下注额
    :return:
    '''

    if money_pb >= 100 and money_pb < 500:
        rebonus = 8
    elif money_pb >= 500 and money_pb < 1000:
        rebonus = 58
    elif money_pb >= 1000 and money_pb < 5000:
        rebonus = 118
    elif money_pb >= 5000:
        rebonus = 588

    money_manbetx = (money_pb * odd_pb + rebonus) / odd_manbetx
    print("manbet下注额: ", money_manbetx)
    print("profit:", money_manbetx * (odd_manbetx - 1) - money_pb )
    print("profit:", money_pb * (odd_pb - 1) - money_manbetx + rebonus )


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


    mycat_vs_manbetx(odd_mycat=2.03, odd_manbetx=1.91, money_mycat=9776)
    # platform_vs_manbetx(odd_plat=1.97, odd_manbetx=2.02, money_manbetx=5520)