def main(today, reserve_day):
    """メインロジック"""
    if not dateCheck(today, reserve_day):
        return print(f'today: {today}, reserve_day: {reserve_day} '
                     f'当日より前に予約日は設定できません')
    print('予約処理に続きます')


def dateCheck(before, after):
    """ 日付チェック

    ex: 2022/06/04が依頼日で2022/11/11に予約する: True
        2022/06/04が依頼日で2022/05/04 を予約する: False
    :param before:
    :param after:
    :return: 日付チェックの結果
    """

    if before >= after:
        return False
    return True


if __name__ == '__main__':
    # 日付がYYYY/MM/DD 形式だとTrue
    main('2022/06/04', '2022/11/11')
    # 日付がYYYY/M/D 形式だとFalse
    main('2022/6/4', '2022/11/11')

    # なぜなのか？
    print(ord('2'))  # 50
    print(ord('0'))  # 48
    print(ord('2'))  # 50
    print(ord('2'))  # 50
    print(ord('/'))  # 47
    print(ord('0'))  # 48
    print(ord('6'))  # 54
    print(ord('/'))  # 47
    print(ord('0'))  # 48
    print(ord('4'))  # 52

    print(ord('1'))  # 49
    print(ord('1'))  # 49

    # なぜなのか？ 文字列を比較する場合、
    # > 文字列 (str のインスタンス) の比較は、文字の Unicode のコードポイントの数としての値 (組み込み関数 ord() の返り値) を使った辞書式順序で行われます。
    # なので。

    # 比較する場合、辞書順序となる。先頭から比較するため、2022/ までは同じ。その次が6と1の比較。6のordの結果が54に対して1のordが49なので
    # 6(54) > 1(49) 隣、6の方が大きい
    # 2022/6/4 の方が 2022/11/11 より大きいとされる

    # https: // docs.python.org / ja / 3 / tutorial / datastructures.html  # comparing-sequences-and-other-types
