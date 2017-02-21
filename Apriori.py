# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 21:14:15 2016

@author: swamy
"""

import csv
import itertools


transactions = []
#loading csv file 
with open('transactions.csv') as csvfile:
  dbreader = csv.reader(csvfile, delimiter=',')
  for row in dbreader:
    transactions.append(tuple(sorted(row)))


# returns the number of times the itemset is present in db 

def itemset_count(db, itemset):
    count = 0
    #itemset = sets.Set(itemset)
    itemset = set(itemset)
    for transaction in db:
        if itemset.issubset(set(transaction)):
            count = count + 1
    return count
#returns all the items present in db in sorted order
def get_all_items(db):
    items = set()
    for transaction in db:
        items = items.union(transaction)
    return sorted(items)
#Returns a merged itemset if the two itemsets follow the rle to join in apriori algorithm
def join_itemsets(is1, is2):
    prefix1 = is1[0:-1]
    prefix2 = is2[0:-1]
    if prefix1 == prefix2:
        return tuple(sorted(set(is1+is2)))
    else:
        return ()

#Takes db as input and joins all the itemset that follows the join rule of apriori algorithm

def join_all_itemsets(itemsets):
    final_join_set = set()
    combinations = itertools.combinations(itemsets,2)
    for i,combination in enumerate(combinations):
        print("Combination:"+str(i),combination)
        joined_itemset = join_itemsets(combination[0],combination[1])
        print("joined_itemset:",joined_itemset)
        if joined_itemset:
            final_join_set.add(joined_itemset)
    return final_join_set
 
#Takes db ,itemsets and min sup and prunes as per algorithm
    
def prune_infrequent_sets(db, itemsets, min_sup):
    items_minsup = [] 
    for itemset in itemsets:
        count_subset = itemset_count(db,itemset)
        if count_subset >= (min_sup-1):
            items_minsup.append(itemset)
    return items_minsup
#print(join_all_itemsets(transactions))

#test_prun= [['Apples', 'Bread', 'Eggs'],['Apples'],['Eggs'],['Bread','Corn']]
#prune_test =  prune_infrequent_sets(transactions,test_prun,2)
#print("Min count itemset test:", prune_test)

def apriori(db, min_sup):
    items = get_all_items(db)
    
    items_gt = []
#Loop to print Single item set and their respective count
    for item in items:
        count_single = itemset_count(db,[item])
        print(item, str(count_single))
        if count_single > min_sup:
            items_gt.append(item)
    for item in items_gt:
        print(item)

apriori(transactions,2)
