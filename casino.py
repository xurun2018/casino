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
    reward_percent = 0.004
    money_manbet_max = 152 / (odd_manbet - 1) / 0.05 #max_bet is for Uven, 0.05 is reward for uven
    money_platform_max = (money_manbet_max * odd_manbet + money_manbet_max * (odd_manbet - 1) * 0.05) / ( odd_platform - re_insurance_percent)
    money_manbet = money_platform / money_platform_max * money_manbet_max
    print('money_manbet_max: {money_manbet_max}, money_manbet: {money_manbet}\n'
          'money_platform_max: {money_platform_max}, money_platform: {money_platform}'.format(
        money_manbet_max=money_manbet_max, money_manbet=money_manbet, money_platform_max=money_platform_max, money_platform=money_platform))

    print('profit: {}'.format(
        money_platform * odd_platform - money_platform - money_manbet + money_platform * reward_percent + money_manbet * reward_percent
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
    if money_lovebet > 1000 and money_lovebet < 1999:
        money_rebonus = 59
    elif money_lovebet > 2000 and money_lovebet < 4999:
        money_rebonus = 99
    elif money_lovebet > 5000 and money_lovebet < 9999:
        money_rebonus = 199
    elif money_lovebet > 10000 and money_lovebet < 29999:
        money_rebonus = 299
    elif money_lovebet > 30000 and money_lovebet < 49999:
        money_rebonus = 399
    elif money_lovebet > 50000 and money_lovebet < 99999:
        money_rebonus = 699
    elif money_lovebet > 100000:
        money_rebonus = 999

    money_wellbet = (odd_lovebet * money_lovebet - money_lovebet * 0.03 - money_rebonus)/odd_wellbet

    print("money_wellbet: {}".format(money_wellbet))
    print("profit: {}".format(
        odd_lovebet * money_lovebet - money_wellbet - money_lovebet + 0.004 * (money_wellbet + money_lovebet) + int(money_lovebet/1000) * 10
    ))
    return money_wellbet

if __name__ == '__main__':

    # manbet_uven(1.92, 2.00, 2000, 'wellbet')
    platform_vs_manbet(odd_platform=2.11, odd_manbet=1.85, money_platform=2277,platform='lovebet')
    # lovebet_vs_manbetx_insurance(odd_lovebet=1.87, odd_wellbet=2.05, money_lovebet=3053)