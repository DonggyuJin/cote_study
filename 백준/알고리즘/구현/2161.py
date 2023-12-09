card = int(input())

card_list = [card+1 for card in range(card)]
card_type = 0

result = []

while(len(card_list) > 1):
    if card_type == 0:
        result.append(card_list[0])
        card_type = 1
    elif card_type == 1:
        card_list.append(card_list[0])
        card_type = 0
    card_list.pop(0)

card_list = result + card_list
print(' '.join(list(map(str, card_list))))