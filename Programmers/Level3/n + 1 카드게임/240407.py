def solution(coin, cards):
    n = len(cards)
    target = n + 1
    my_card = set(cards[:n//3])
    passed_card = set()
    for round, i in enumerate(range(n//3, n, 2)):
        passed_card.add(cards[i])
        passed_card.add(cards[i+1])
        # 내 카드만으로 제출할 수 있다면?
        pair = []
        for card in my_card:
            if target - card in my_card:                
                pair = [card, target - card]
                break
        if pair:
            for card in pair:
                my_card.remove(card)
            continue
        # 내 카드만으로는 제출할 수 없었음, 코인 1개 지출
        coin -= 1
        if coin < 0:
            return round + 1
        for card in my_card:
            if target - card in passed_card:
                pair = [card, target - card]
                break
        if pair:
            my_card.remove(pair[0])
            passed_card.remove(pair[1])
            continue
        # 내 카드를 섞을 수 없음, 코인 2개 지출
        coin -= 1
        if coin < 0:
            return round + 1
        for card in passed_card:
            if target - card in passed_card:
                pair = [card, target - card]
                break
        if pair:
            for card in pair:
                passed_card.remove(card)
            continue
        return round + 1
    return round + 2