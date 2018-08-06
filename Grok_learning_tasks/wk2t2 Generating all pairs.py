import itertools as it
splitat = 1
def all_pairs(hand):
  pairs = []
  # TODO implement this function
  #use itertools to permute all possible combinations
  for pair in it.combinations(hand, 2):
     #check if each of the combinations is a pair
    if pair[0][:splitat] == pair[1][:splitat]:
       #if it is , append it to a list
      pairs.append(list(pair))
 
 
  #return the list
  return pairs


if __name__ == '__main__':
  print(all_pairs(['5D', '5C', '5H']))
  print(all_pairs(['7H', '6H', '9S', '6S']))
  print(all_pairs(['AH', '9D', '2S']))
