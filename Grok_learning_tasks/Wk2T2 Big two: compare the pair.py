rank_order = '134567890JQKA2'
suit_order = 'DCHS'
def is_higher_pair(pair1, pair2):
  splitat = 1
  
  # TODO implement this function
  # find rank of each pair
  pair1_rank = pair1[0][:splitat]
  pair1_rank = rank_order.index(pair1_rank)
  pair2_rank = pair2[0][:splitat]
  pair2_rank = rank_order.index(pair2_rank)
  # print(pair1_rank, pair2_rank)
  # if rank is the same then find the highest suit of each pair
  if pair1_rank == pair2_rank:
    # if pair1's first suit is higher than its second record that
    if suit_order.index(pair1[0][splitat:]) > suit_order.index(pair1[1][splitat:]):
      pair1_suit = suit_order.index(pair1[0][splitat:])
    else:
      pair1_suit = suit_order.index(pair1[1][splitat:])
    # if pair2's first suit is higher than its second record that
    if suit_order.index(pair2[0][splitat:]) > suit_order.index(pair2[1][splitat:]):
      pair2_suit = suit_order.index(pair2[0][splitat:])
    else:
      pair2_suit = suit_order.index(pair2[1][splitat:])
  #find highest pair
  # print(pair1_rank, pair1_suit, pair2_rank, pair2_suit)
  if pair1_rank == pair2_rank:
    if pair1_suit > pair2_suit:
      return True
    else:
      return False
  elif pair1_rank > pair2_rank:
    return True
  else:
    return False
    

if __name__ == '__main__':
  print(is_higher_pair(['AH', 'AD'], ['8D', '8S']))
  print(is_higher_pair(['JS', 'JD'], ['2D', '2S']))
  print(is_higher_pair(['6D', '6S'], ['6H', '6C']))
  print(is_higher_pair(['KH', 'KS'], ['KD', 'KC']))
  print(is_higher_pair(['0H', '0D'], ['0S', '0C']))
