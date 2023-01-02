# BINARY SEARCH
##  Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a
##  sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
##  Write a function to help Bob locate the card.

def locate_card(cards,query):

    left_li = 0
    right_li = len(cards)-1
    

    mid_p = (right_li+left_li)//2

    #print('left:',left_li,'right:',right_li,'mid:',mid_p,'len:',len(cards))
    #print(cards)

    #if len(cards) == 1:
        #if cards[0] == query:
            #return 0
        #else:
            #return -1    
    if len(cards)==0: 
        return -1
    #print(cards[mid_p]==query)
    if cards[mid_p] == query:
        return mid_p

    if cards[mid_p]< query:
        return locate_card(cards[left_li:mid_p],query)

    if cards[mid_p] > query:
        return locate_card(cards[mid_p+1:],query)

    return -1    


   


if __name__ == '__main__':

    tests = []

    tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
    })

    tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
    })
   
    tests.append({
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    })

    tests.append({
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0 
    })

    
    for i in tests:

        print(locate_card(**i['input'])==i['output'])