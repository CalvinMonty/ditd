#Wagers:
#"How many lines of code" bets: Calvin says less then 8100 Kira says more then 8100
#
#--------------------------------------
#Inventory - items, gold, silver, 
#Stats - Lv, Str, Hp, Dex, Dmg, MagDmg, Xp
#Equipment - armor, items, weapon


import random 
import math 


ID001 = {
  	'Name': 'A Dull Rusty Sword',
    'Weight': 5,
    'Price': 105,
  	'Acc': 0,
  	'Str': 3,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID002 = {
  	'Name': '2 Dull Rusty Daggers',
    'Weight': 2,
    'Price': 90,
  	'Acc': 0,
  	'Str': 3,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID003 = {
  	'Name': 'A Broken Mace',
    'Weight':3 ,
    'Price': 85,
  	'Acc': 0,
  	'Str': 2,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  'LevReq': 1
}

ID004 = {
  	'Name': 'A Wooden Bow',
    'Weight': 1,
    'Price': 110,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 3,
  	'Hp': 0,
  	'MagDmg': 0,
  'LevReq': 1
}

ID005 = {
  	'Name': 'A Wooden Crossbow',
    'Weight': 4,
    'Price': 95,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 3,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID006 = {
  	'Name': 'An Old Slingshot',
    'Weight': 1,
    'Price': 85,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 4,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID007 = {
  	'Name': 'An Old Wooden Staff',
    'Weight': 4,
    'Price': 65,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 1,
  	'LevReq': 0
}

ID008 = {
  	'Name': 'A Hide Hat',
    'Weight': 6,
    'Price': 100,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 1,
  	'MagDmg': 0,
  	'LevReq': 0
}

ID009 = {
  	'Name': 'A Pair of Hide Gloves',
    'Weight': 6,
    'Price': 100,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 1,
  	'MagDmg': 0,
  	'LevReq': 0
}

ID010 = {
  	'Name': 'A Pair of Hide Boots',
    'Weight': 6,
    'Price': 100,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 1,
  	'MagDmg': 0,
  	'LevReq': 0
}

ID011 = {
  	'Name': 'A Hide Tunic',
    'Weight': 6,
    'Price': 100,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 1,
  	'MagDmg': 0,
  	'LevReq': 0
}

ID012 = {
  	'Name': 'A Wooden Sword',
    'Weight': 4,
    'Price': 140,
  	'Acc': 0,
  	'Str': 2,
  	'Dex': 1,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID013 = {
  	'Name': '2 Wooden Daggers',
    'Weight': 1,
    'Price': 120,
  	'Acc': 0,
  	'Str': 2,
  	'Dex': 1,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID014 = {
  	'Name': 'A Wooden Mace',
    'Weight': 3,
    'Price': 113,
  	'Acc': 0,
  	'Str': 2,
  	'Dex': 1,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID015 = {
  	'Name': 'A Hollow Bow',
    'Weight': 2,
    'Price': 147,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 4,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID016 = {
  	'Name': 'A Cool Looking Crossbow',
    'Weight': 4,
    'Price': 127,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 4,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID017 = {
  	'Name': 'An Wooden Slingshot',
    'Weight': 1,
    'Price': 113,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID018 = {
  	'Name': 'A Wooden Staff',
    'Weight': 6,
    'Price': 87,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 2,
  	'LevReq': 1
}

ID019 = {
  	'Name': 'A Cloth Hat',
    'Weight': 8,
    'Price': 133,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 2,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID020 = {
  	'Name': 'A Cloth Pair of Gloves',
    'Weight': 8,
    'Price': 133,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 2,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID021 = {
  	'Name': 'A Cloth Pair of Boots',
    'Weight': 8,
    'Price': 133,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 2,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID022 = {
  	'Name': 'A Cloth Tunic',
    'Weight': 8,
    'Price': 133,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 2,
  	'MagDmg': 0,
  	'LevReq': 1
}

ID023 = {
  	'Name': 'A Stone Sword',
    'Weight': 5,
    'Price': 187,
  	'Acc': 0,
  	'Str': 4,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID024 = {
  	'Name': '2 Stone Daggers',
    'Weight': 2,
    'Price': 160,
  	'Acc': 0,
  	'Str': 4,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID025 = {
  	'Name': 'A Stone Mace',
    'Weight': 4,
    'Price': 128,
  	'Acc': 0,
  	'Str': 2,
  	'Dex': 1,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID026 = {
  	'Name': 'A Study Bow',
    'Weight': 2,
    'Price': 162,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID027 = {
  	'Name': 'A Sturdy Crossbow',
    'Weight': 4,
    'Price': 142,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID028 = {
  	'Name': 'A Powerful Slingshot',
    'Weight': 2,
    'Price': 128,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 6,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID029 = {
  	'Name': 'An Old staff',
    'Weight': 4,
    'Price': 102,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 3,
  	'LevReq': 2
}

ID030 = {
  	'Name': 'A Reinforced Hide Hat',
    'Weight': 8,
    'Price': 282,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 3,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID031 = {
  	'Name': 'A Cloth Pair of  Reinforced Gloves',
    'Weight': 8,
    'Price': 282,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 3,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID032 = {
  	'Name': 'A Cloth Pair of Reinforced Boots',
    'Weight': 8,
    'Price': 282,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 3,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID033 = {
  	'Name': 'A Reinforced Cloth Tunic',
    'Weight': 8,
    'Price': 282,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 3,
  	'MagDmg': 0,
  	'LevReq': 2
}

ID034 = {
  	'Name': 'A Stronger Stone Sword',
    'Weight': 4,
    'Price': 202,
  	'Acc': 5,
  	'Str': 5,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID035 = {
  	'Name': '2 Stony Daggers',
    'Weight': 3,
    'Price': 175,
  	'Acc': 0,
  	'Str': 5,
  	'Dex': 1,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID036 = {
  	'Name': 'A Stone Mace',
    'Weight': 4,
    'Price': 143,
  	'Acc': 0,
  	'Str': 4,
  	'Dex': 2,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID037 = {
  	'Name': 'A Powerful Bow',
    'Weight': 3,
    'Price': 177,
  	'Acc': 5,
  	'Str': 0, 
 	'Dex': 4,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID038 = {
  	'Name': 'A Turboflex Crossbow',
    'Weight': 1,
    'Price': 157,
  	'Acc': 0,
  	'Str': 2,
  	'Dex': 4,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID039 = {
  	'Name': 'A Wooden Slingshot',
    'Weight': 2,
    'Price': 143,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID040 = {
  	'Name': 'A Stone staff',
    'Weight': 9,
    'Price': 117,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 4,
  	'LevReq': 3
}

ID041 = {
  	'Name': 'A Wooden Helmet',
    'Weight': 9,
    'Price': 163,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 4,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID042 = {
  	'Name': 'A Wooden Pair of Gloves',
    'Weight': 9,
    'Price': 163,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 4,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID043 = {
  	'Name': 'A Stone Pair of Reinforced Boots',
    'Weight': 9,
    'Price': 163,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 4,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID044 = {
  	'Name': 'A Wooden Chestplate',
    'Weight': 9,
    'Price': 163,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 4,
  	'MagDmg': 0,
  	'LevReq': 3
}

ID045 = {
  	'Name': 'A Tin Sword',
    'Weight': 4,
    'Price': 217,
  	'Acc': 10,
  	'Str': 6,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID046 = {
  	'Name': '2 Tin Daggers',
    'Weight': 3,
    'Price': 190,
  	'Acc': 0,
  	'Str': 6,
  	'Dex': 2,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID047 = {
  	'Name': 'A Tin Mace',
    'Weight': 3,
    'Price': 158,
  	'Acc': 0,
  	'Str': 5,
  	'Dex': 4,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID048 = {
  	'Name': 'A Tin Bow',
    'Weight': 2,
    'Price': 192,
  	'Acc': 10,
  	'Str': 0,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID049 = {
  	'Name': 'A Tin Crossbow',
    'Weight': 4,
    'Price': 0,
  	'Acc': 0,
  	'Str': 3,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID050 = {
  	'Name': 'A Tin Slingshot',
    'Weight': 3,
    'Price': 158,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 6,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID051 = {
  	'Name': 'A Decently Ancient staff',
    'Weight': 9,
    'Price': 142,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 5,
  	'LevReq': 4
}

ID052 = {
  	'Name': 'A Tin Helmet',
    'Weight': 10,
    'Price': 178,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 5,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID053 = {
  	'Name': 'A Tin Pair of Gloves',
    'Weight': 10,
    'Price': 178,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 5,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID054 = {
  	'Name': 'A Tin Pair of Boots',
    'Weight': 10,
    'Price': 178,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 5,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID055 = {
  	'Name': 'A Tin Chestplate',
    'Weight': 10,
    'Price': 178,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 5,
  	'MagDmg': 0,
  	'LevReq': 4
}

ID056 = {
  	'Name': 'A Lead Sword',
    'Weight': 5,
    'Price': 232,
  	'Acc': 15,
  	'Str': 7,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 5
}

ID057 = {
  	'Name': '2 Lead Daggers',
    'Weight': 3,
    'Price': 205,
  	'Acc': 0,
  	'Str': 7,
  	'Dex': 3,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 5
}

ID058 = {
  	'Name': 'A Lead Mace',
    'Weight': 4,
    'Price': 173,
  	'Acc': 0,
  	'Str': 6,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 5
}

ID059 = {
  	'Name': 'A Lead Bow',
    'Weight': 3,
    'Price': 207,
  	'Acc': 15,
  	'Str': 0,
  	'Dex': 6,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 5
}

ID060 = {
  	'Name': 'A Lead Crossbow',
    'Weight': 5,
    'Price': 187,
  	'Acc': 0,
  	'Str': 3,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 5
}

ID061 = {
  	'Name': 'A Lead Slingshot',
    'Weight': 2,
    'Price': 173,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 7,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 5
}

ID062 = {
  	'Name': 'An Ancient staff',
    'Weight': 7,
    'Price': 147,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 6,
   	'LevReq': 5
}

ID063 = {
  	'Name': 'A Lead Helmet',
    'Weight': 11,
    'Price': 193,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 6,
  	'MagDmg': 0,
  	'LevReq': 5
}

ID064 = {
  	'Name': 'A Lead Pair of Gloves',
    'Weight': 11,
    'Price': 193,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 6,
  	'MagDmg': 0,
   	'LevReq': 5
}

ID065 = {
  	'Name': 'A Lead Pair of Boots',
    'Weight': 11,
    'Price': 193,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 6,
  	'MagDmg': 0,
   	'LevReq': 5
}

ID066 = {
  	'Name': 'A Lead Chestplate',
    'Weight': 11,
    'Price': 193,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 6,
  	'MagDmg': 0,
   	'LevReq': 5
}

ID067 = {
  	'Name': 'A Gold Sword',
    'Weight': 50,
    'Price': 247,
  	'Acc': 25,
  	'Str': 8,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID068 = {
  	'Name': '2 GoldDaggers',
    'Weight': 30,
    'Price': 220,
  	'Acc': 0,
  	'Str': 8,
  	'Dex': 3,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID069 = {
  	'Name': 'A Gold Mace',
    'Weight': 40,
    'Price': 188,
  	'Acc': 0,
  	'Str': 7,
  	'Dex': 6,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID070 = {
  	'Name': 'A Gold Bow',
    'Weight': 30,
    'Price': 222,
  	'Acc': 25,
  	'Str': 0,
  	'Dex': 7,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 6
}

ID071 = {
  	'Name': 'A Gold Crossbow',
    'Weight': 50,
    'Price': 202,
  	'Acc': 0,
  	'Str': 4,
  	'Dex': 6,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID072 = {
  	'Name': 'A Gold Slingshot',
    'Weight': 20,
    'Price': 188,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 8,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID073 = {
  	'Name': 'A Gold staff',
    'Weight': 70,
    'Price': 162,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 7,
   	'LevReq': 6
}

ID074 = {
  	'Name': 'A Gold Helmet',
    'Weight': 120,
    'Price':342 ,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 7,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID075 = {
  	'Name': 'A Golt Pair of Gloves',
    'Weight': 120,
    'Price': 342,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 7,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID076 = {
  	'Name': 'A Gold Pair of Boots',
    'Weight': 120,
    'Price': 342,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 7,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID077 = {
  	'Name': 'A GoldChestplate',
    'Weight': 120,
    'Price': 342,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 7,
  	'MagDmg': 0,
   	'LevReq': 6
}

ID078 = {
  	'Name': 'An Iron Sword',
    'Weight': 5,
    'Price': 262,
  	'Acc': 30,
  	'Str': 9,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 7
}

ID079 = {
  	'Name': '2 Iron Daggers',
    'Weight': 3,
    'Price': 235,
  	'Acc': 0,
  	'Str': 9,
  	'Dex': 5,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 7
}

ID080 = {
  	'Name': 'An Iron Mace',
    'Weight': 4,
    'Price': 203,
  	'Acc': 0,
  	'Str': 8,
  	'Dex': 7,
  	'Hp': 0,
  	'MagDmg': 0,
   	'LevReq': 7
}

ID081 = {
  	'Name': 'An Iron Bow',
    'Weight': 2,
    'Price': 237,
  	'Acc': 30,
  	'Str': 0,
  	'Dex': 8,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 7
}

ID082 = {
  	'Name': 'An Iron Crossbow',
    'Weight': 6,
    'Price': 217,
  	'Acc': 0,
  	'Str': 5,
  	'Dex': 7,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 7
}

ID083 = {
  	'Name': 'An Iron Slingshot',
    'Weight': 2,
    'Price': 203,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 9,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 7
}

ID084 = {
  	'Name': 'An Rare staff',
    'Weight': 8,
    'Price': 177,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 8,
  	'LevReq': 7
}

ID085 = {
  	'Name': 'An Iron Helmet',
    'Weight': 13,
    'Price': 223,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 8,
  	'MagDmg': 0,
  	'LevReq': 7
}

ID086 = {
  	'Name': 'An Iron Pair of Gloves',
    'Weight': 13,
    'Price': 223,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 8,
  	'MagDmg': 0,
  	'LevReq': 7
}

ID087 = {
  	'Name': 'An Iron Pair of Boots',
    'Weight': 13,
    'Price': 223,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 8,
  	'MagDmg': 0,
  	'LevReq': 7
}

ID088 = {
  	'Name': 'An Iron Chestplate',
    'Weight': 13,
    'Price': 223,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 8,
  	'MagDmg': 0,
  	'LevReq': 7
}

ID089 = {
  	'Name': 'A Tungsten Sword',
    'Weight': 5,
    'Price': 277,
  	'Acc': 35,
  	'Str': 10,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID090 = {
  	'Name': '2 Tungsten Daggers',
    'Weight': 2,
    'Price': 250,
  	'Acc': 0,
  	'Str': 10,
  	'Dex': 6,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID091 = {
  	'Name': 'A Tungsten Mace',
    'Weight': 4,
    'Price': 218,
  	'Acc': 0,
  	'Str': 9,
  	'Dex': 8,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID092 = {
  	'Name': 'A Tungsten Bow',
    'Weight': 3,
    'Price': 252,
  	'Acc': 35,
  	'Str': 0,
  	'Dex': 9,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID093 = {
  	'Name': 'A Tungsten Crossbow',
    'Weight': 6,
    'Price': 232,
  	'Acc': 0,
  	'Str': 6,
  	'Dex': 8,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID094 = {
  	'Name': 'A Tungsten Slingshot',
    'Weight': 2,
    'Price': 218,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 10,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID095 = {
  	'Name': 'An Tungsten staff',
    'Weight': 9,
    'Price': 192,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 9,
  	'LevReq': 8
}

ID096 = {
  	'Name': 'A Tungsten Helmet',
    'Weight': 14,
    'Price': 238,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 9,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID097 = {
  	'Name': 'A Tungsten Pair of Gloves',
    'Weight': 14,
    'Price': 238,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 9,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID098 = {
  	'Name': 'A Tungsten Pair of Boots',
    'Weight': 14,
    'Price': 238,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 9,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID099 = {
  	'Name': 'A Tungsten Chestplate',
    'Weight': 14,
    'Price': 238,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 9,
  	'MagDmg': 0,
  	'LevReq': 8
}

ID100 = {
  	'Name': 'A Titanium Sword',
    'Weight': 6,
    'Price': 292,
  	'Acc': 40,
  	'Str': 11,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID101 = {
  	'Name': '2 Titanium Daggers',
    'Weight': 4,
    'Price': 265,
  	'Acc': 0,
  	'Str': 11,
  	'Dex': 7,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID102 = {
  	'Name': 'A Titanium Mace',
    'Weight': 5,
    'Price': 233,
  	'Acc': 0,
  	'Str': 10,
  	'Dex': 9,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID103 = {
  	'Name': 'A Titanium Bow',
    'Weight': 2,
    'Price': 268,
  	'Acc': 40,
  	'Str': 0,
  	'Dex': 10,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID104 = {
  	'Name': 'A Titanium Crossbow',
    'Weight': 6,
    'Price': 247,
  	'Acc': 0,
  	'Str': 7,
  	'Dex': 9,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID105 = {
  	'Name': 'A Titanium Slingshot',
    'Weight': 3,
    'Price': 233,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 11,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID106 = {
  	'Name': 'An Titanium staff',
    'Weight': 10,
    'Price': 207,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 10,
  	'LevReq': 9
}

ID107 = {
  	'Name': 'A Titanium Helmet',
    'Weight': 15,
    'Price': 253,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 10,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID108 = {
  	'Name': 'A Titanium Pair of Gloves',
    'Weight': 15,
    'Price': 253,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 10,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID109 = {
  	'Name': 'A Titanium Pair of Boots',
    'Weight': 15,
    'Price': 253,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 10,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID110 = {
  	'Name': 'A Titanium Chestplate',
    'Weight': 15,
    'Price': 253,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 10,
  	'MagDmg': 0,
  	'LevReq': 9
}

ID111 = {
  	'Name': 'An Adamantite Sword',
    'Weight': 7,
    'Price': 307,
  	'Acc': 45,
  	'Str': 12,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID112 = {
  	'Name': '2 Adamantite Daggers',
    'Weight': 4,
    'Price': 280,
  	'Acc': 0,
  	'Str': 12,
  	'Dex': 8,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID113 = {
  	'Name': 'An Adamantine Mace',
    'Weight': 6,
    'Price': 248,
  	'Acc': 0,
  	'Str': 11,
  	'Dex': 10,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID114 = {
  	'Name': 'An Adamantite Bow',
    'Weight': 3,
    'Price': 281,
  	'Acc': 45,
  	'Str': 0,
  	'Dex': 11,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID115 = {
  	'Name': 'An Adamantite Crossbow',
    'Weight': 6,
    'Price': 262,
  	'Acc': 0,
  	'Str': 8,
  	'Dex': 10,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID116 = {
  	'Name': 'An Adamantite Slingshot',
    'Weight': 4,
    'Price': 248,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 12,
  	'Hp': 0,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID117 = {
  	'Name': 'An Adamantite staff',
    'Weight': 12,
    'Price': 222,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 0,
  	'MagDmg': 11,
  	'LevReq': 10
}

ID118 = {
  	'Name': 'An Adamantite Helmet',
    'Weight': 16,
    'Price': 290,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 11,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID119 = {
  	'Name': 'An Adamantite Pair of Gloves',
    'Weight': 16,
    'Price': 290,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 11,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID120 = {
  	'Name': 'An Adamantite Pair of Boots',
    'Weight': 16,
    'Price': 290,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 11,
  	'MagDmg': 0,
  	'LevReq': 10
}

ID121 = {
  	'Name': 'An Adamantite Chestplate',
    'Weight': 16,
    'Price': 290,
  	'Acc': 0,
  	'Str': 0,
  	'Dex': 0,
  	'Hp': 11,
  	'MagDmg': 0,
  	'LevReq': 10
}

IDlist = ( ID002,
    ID003,
    ID004,
    ID005,
    ID006,
    ID007,
    ID008,
    ID009,
    ID010,
    ID011,
    ID012,
    ID013,
    ID014,
    ID015,
    ID016,
    ID017,
    ID018,
    ID019,
    ID020,
    ID021,
    ID022,
    ID023,
    ID024,
    ID025,
    ID026,
    ID027,
    ID028,
    ID029,
    ID030,
    ID031,
    ID032,
    ID033,
    ID034,
    ID035,
    ID036,
    ID037,
    ID038,
    ID039,
    ID040,
    ID041,
    ID042,
    ID043,
    ID044,
    ID045,
    ID046,
    ID047,
    ID048,
    ID049,
    ID050,
    ID051,
    ID052,
    ID053,
    ID054,
    ID055,
    ID056,
    ID057,
    ID058,
    ID059,
    ID060,
    ID061,
    ID062,
    ID063,
    ID064,
    ID065,
    ID066,
    ID067,
    ID068,
    ID069,
    ID070,
    ID071,
    ID072,
    ID073,
    ID074,
    ID075,
    ID076,
    ID077,
    ID078,
    ID079,
    ID080,
    ID081,
    ID082,
    ID083,
    ID084,
    ID085,
    ID086,
    ID087,
    ID088,
    ID089,
    ID090,
    ID091,
    ID092,
    ID093,
    ID094,
    ID095,
    ID096,
    ID097,
    ID098,
    ID099,
    ID100,
    ID101,
    ID102,
    ID103,
    ID104,
    ID105,
    ID106,
    ID107,
    ID108,
    ID109,
    ID110,
    ID111,
    ID112,
    ID113,
    ID114,
    ID115,
    ID116,
    ID117,
    ID118,
    ID119,
    ID120,
    ID121,
)

def shopLoopBack():
    global shopX
    global shopY
    global shop2X
    global shop2Y
    global shop3X
    global shop3Y


    if shopX > 25:
        shopX = shopX - 25
        shopLoopBack()
    if shopY > 25:
        shopY = shopY - 25
        shopLoopBack()
    if shopX < 1:
        shopX = shopX + 25
        shopLoopBack()
    if shopY < 1:
        shopY = shopY + 25
        shopLoopBack()
        
    if shop2X > 25:
        shop2X = shop2X - 25
        shopLoopBack()
    if shop2Y > 25:
        shop2Y = shop2Y - 25
        shopLoopBack()
    if shop2X < 1:
        shop2X = shop2X + 25
        shopLoopBack()
    if shop2Y < 1:
        shop2Y = shop2Y + 25
        shopLoopBack()
      
    if shop3X > 25:
        shop3X = shop3X - 25
        shopLoopBack()
    if shop3Y > 25:
        shop3Y = shop3Y - 25
        shopLoopBack()
    if shop3X < 1:
        shop3X = shop3X + 25
        shopLoopBack()
    if shop3Y < 1:
        shop3Y = shop3Y + 25
        shopLoopBack()
      





coinBag = 500
x = 1
y = 1
mapX = 1
mapY = 1
shopX = random.randint(1,25)
shopY = random.randint(1,25)
shop2X = random.randint(1,25)
shop2Y = random.randint(1,25)
shop3X = random.randint(1,25)
shop3Y = random.randint(1,25)
shop3 = [shop3X,shop3Y]
shop1 = [shopX,shopY]
shop2 = [shop2X,shop2Y]
if 12 > mapX:
    distenceToMiddleX = 12 - mapX
if 12 < mapX: 
    distenceToMiddleX = mapX - 12
if 12 > mapY:
    distenceToMiddleY = 12 - mapY
if 12 < mapY: 
    distenceToMiddleY = mapY - 12
    


totalDistence = distenceToMiddleY + distenceToMiddleX


if totalDistence == 22 or totalDistence == 21 or totalDistence == 20:
    Tsale = [ID001,ID002,ID003,ID004,ID005,ID006,ID007,ID008,ID009,ID010,ID011]
if totalDistence == 19 or totalDistence == 18:
    Tsale = [ID012,ID013,ID014,ID015,ID016,ID017,ID018,ID019,ID020,ID021,ID022]
if totalDistence == 17 or totalDistence == 16:
    Tsale = [ID023,ID024,ID025,ID026,ID027,ID028,ID029,ID030,ID031,ID032,ID033]
if totalDistence == 15 or totalDistence == 14:
    Tsale = [ID034,ID035,ID036,ID037,ID038,ID039,ID040,ID041,ID042,ID043,ID044]
if totalDistence == 13 or totalDistence == 12:
    Tsale = [ID045,ID046,ID047,ID048,ID049,ID050,ID051,ID052,ID053,ID054,ID055]
if totalDistence == 11 or totalDistence == 10:
    Tsale = [ID067,ID068,ID069,ID070,ID071,ID072,ID073,ID074,ID075,ID076,ID077]
if totalDistence == 9 or totalDistence == 8:
    Tsale = [ID078,ID079,ID080,ID081,ID082,ID083,ID084,ID085,ID086,ID087,ID088]
if totalDistence == 7 or totalDistence == 6:
    Tsale = [ID089,ID090,ID091,ID092,ID093,ID094,ID095,ID096,ID097,ID098,ID099]
if totalDistence == 5 or totalDistence == 4:
    Tsale = [ID100,ID101,ID102,ID103,ID104,ID105,ID106,ID107,ID108,ID109,ID110]
if totalDistence == 3 or totalDistence == 2 or totalDistence == 1 or totalDistence == 0:
    Tsale = [ID111,ID112,ID113,ID114,ID115,ID116,ID117,ID118,ID119,ID120,ID121]



    
#distenceToMiddleX = 
#print('before change:', 'shop:',shop1, 'shop2:',shop2,'shop3',shop3)
if shop1 == shop2 :
        shop2X = random.randint(1,25)
        shop2Y = random.randint(1,25)
        shopX = random.randint(1,25)
        shopY = random.randint(1,25)
if shop3 == shop1 or shop3 == shop2:
    shop3X = random.randint(1,25)
    shop3Y = random.randint(1,25)
    

cRoom = [x,y]
Map = [mapX,mapY]
shop1 = [shopX,shopY]
shop2 = [shop2X,shop2Y]
shop3 = [shop3X,shop3Y]
      


print('Room',cRoom,'Map:',Map)
shop1 = [shopX,shopY]
shop2 = [shop2X,shop2Y]
shop3 = [shop3X,shop3Y]
#print('shop1:',shop1,'shop2:',shop2,'shop3:',shop3)

locateShop1 = [Map,shop1]
locateShop2 = [Map,shop2]
locateShop3 = [Map,shop3]

def locateAllShops():
    locateShop1 = [Map,shop1]
    locateShop2 = [Map,shop2]
    locateShop3 = [Map,shop3]


def shoping():
    print("The shop is selling:")
    for item in Tsale:
            for g in item:
                print(f'{g}: {item[g]}')
            print()
            
invintory = [ID001,ID002,ID003,ID004,ID005,ID006,ID007,ID008,ID009,ID010,ID011,]
quiver = int('10')
            
while True:
    print("")
       
    
        
    def movement():
        global cRoom
        global options
        global x
        global y
        global mapX
        global mapY
        global shop1
        global shop2
        global shop3
        global shopX
        global shop2X
        global shop3X
        global shopY
        global shop2Y
        global shop3Y
        global TSale
        
        
        
    
        
        print('')
        direction = input('do you want to move north(1), east(2) south(3) of west(4): ')
        if direction == '1':
            y = y + 1
            
            if y > 25:
                y = 1
                shopX = shopX - 2
                shopY = shopY - 3
                shop2X = shop2X - 1
                shop2Y = shop2Y - 2
                shop3X = shop3X - 3
                shop3Y = shop3Y - 1
                shopLoopBack()
                shop1 = [shopX,shopY]
                shop2 = [shop2X,shop2Y]
                shop3 = [shop3X,shop3Y]
                mapY = mapY + 1
                cRoom = [x,y]

                if mapY > 25:
                    mapY = 1
                Map = [mapX,mapY]
                print('Room',cRoom,'Map:',Map)
                shopLoopBack()
                locateAllShops()
                
                if shopX > 25:
                    print('Room',cRoom,'Map:',Map)
            else:
                cRoom = [x,y]
                Map = [mapX,mapY]
                print('Room',cRoom,'Map:',Map)
                
                
                
        if direction == '2':
            x = x + 1
            
            if x > 25:
                x = 1
                mapX = mapX + 1
                shopX = shopX + 3
                shopY = shopY +  1
                shop2X = shop2X + 2
                shop2Y = shop2Y + 0
                shop3X = shop3X - 2
                shop3Y = shop3Y - 1
                shop1 = [shopX,shopY]
                shop2 = [shop2X,shop2Y]
                shop3 = [shop3X,shop3Y]
                locateAllShops()
                
                if mapY > 25:
                    mapY = 1
                Map = [mapX,mapY]
                shop3 = [shop3X,shop3Y]
                shop1 = [shopX,shopY]
                shop2 = [shop2X,shop2Y]
                shopLoopBack()
                cRoom = [x,y]
                locateAllShops()
                print('Room',cRoom,'Map:',Map)
            else:
                cRoom = [x,y]    
                Map = [mapX,mapY]
                print('Room',cRoom,'Map:',Map)
                
        if direction == '3':
            y = y - 1
            
            if y < 1:
                y = 25
                mapY = mapY - 1
                shopX = shopX + 2
                shopY = shopY + 3
                shop2X = shop2X + 1
                shop2Y = shop2Y + 2
                shop3X = shop3X + 3
                shop3Y = shop3Y + 1
                shop1 = [shopX,shopY]
                shop2 = [shop2X,shop2Y]
                shop3 = [shop3X,shop3Y]
                locateAllShops()
                if mapX < 1:
                    mapX = 25
                if mapY < 1:
                    mapY = 25
                Map = [mapX,mapY]
                shop3 = [shop3X,shop3Y]
                shop1 = [shopX,shopY]
                shop2 = [shop2X,shop2Y]
                shopLoopBack()
                cRoom = [x,y]
                print('Room',cRoom,'Map:',Map)
            else:
                cRoom = [x,y]
                Map = [mapX,mapY]
                print('Room',cRoom,'Map:',Map)
        if direction == '4':
            x = x - 1
            
            if x < 1:
                x = 25
                mapX = mapX - 1
                if mapX < 1:
                    mapX = 25
                    shopX = shopX - 3
                    shopY = shopY - 1
                    shop2X = shop2X - 2
                    shop2Y = shop2Y - 0
                    shop3X = shop3X + 2
                    shop3Y = shop3Y + 1
                    shop1 = [shopX,shopY]
                    shop2 = [shop2X,shop2Y]
                    shop3 = [shop3X,shop3Y]
                if mapY < 1:
                    mapY = 25
                Map = [mapX,mapY]
                cRoom = [x,y]
                shop3 = [shop3X,shop3Y]
                shop1 = [shopX,shopY]
                shop2 = [shop2X,shop2Y]
                shopLoopBack()
                print('Room',cRoom,'Map:',Map)
            else:
                cRoom = [x,y]  
                Map = [mapX,mapY]
                print('Room',cRoom,'Map:',Map)
                
        if cRoom == shop1:
            print("You are at a shop.")
            print()
        if cRoom == shop2:
            print("You are at a shop.")
            print()
        if cRoom == shop3:
            print("You are at a shop.")
            print()
        locateAllShops()
        
    if 12 > mapX:
        distenceToMiddleX = 12 - mapX
    if 12 < mapX: 
        distenceToMiddleX = mapX - 12
        
    if 12 > mapY:
        distenceToMiddleY = 12 - mapY
    if 12 < mapY: 
        distenceToMiddleY = mapY - 12
    
    
    def shopKeeperPhrase():
        SKP = random.randint(1,10)
        if SKP == 1:
            print("Have you hear about Razurath? Some adventurares said he defeted the entire Old One's army.")
        
        if SKP == 2:
            print("Some monsters have gold and gear on them, if you cant buy it off them may as well take it.")
        
        if SKP == 3:
            print("I heard theres some larger shops down in the center of the dungon.")
        
        if SKP == 4:
            print("Those dam slimes keep getting on my nerves, if only there was someone to ki-... exterminate them.")
        
        if SKP == 5:
            print("I dont get many customers nowadays...")
        
        if SKP == 6:
            print("How heavy is your coin pouch?")
            
        if SKP == 7:
            print("Fun Fact! The siver and copper coin where disconued due to the extra amout of code needed to make them!")
            
        if SKP == 8:
            print("Aparently there's some stronger enimes near the center of the dungon.")
            
        if SKP == 9:
            print("Rumor has it that there's a way out if you're able to defet Razurath in combat.")
            
        if SKP == 10:
            print("If you run out of arrows I'm always avalible!")
            
    
    options = input("1 move to next room, 2 for interact with room, 3 for open invintory: ")


    shopX = 1
    shopY = 1
    shop1 = [shopX,shopY]

    if options == '1':
        print("")
        movement()
        print("") 
        
    if options == '2':
        if cRoom == shop1 or cRoom == shop2 or cRoom == shop3:
            print(f"You have {coinBag} gold")
            shoping()
            interactWithShop = (float(input("1 to buy, 2 to talk to shop keeper, 3 to exit shop: ")))
            if interactWithShop == 3: 
                print("")

                print('Room',cRoom,'Map:',Map)
                print("")
                
            if interactWithShop == 2:
                print("")
                shopKeeperPhrase()
                print("")
                
            if interactWithShop == 1:
                whatToBuy = input("Input the name of your item: ")
                for item in Tsale:
                    if whatToBuy == item['Name']:
                        print(f"The price is {item['Price']}")
                        if item['Price'] > coinBag:
                            print("You dont have enough money.")
                        else:
                            yesToBuy = input("Y to buy N to leave: ")
                            if yesToBuy == "Y" or yesToBuy == "y":
                                coinBag = coinBag - item['Price']
                                invintory.append(item)
                                print(f'Coinbag total is now: {coinBag}')
                            else:
                                print("")
                
        else:
            print("You are not at a speacal room.")

        
        
    if options == '3':
        print("")
        mapper = {}
        for i, item in enumerate(invintory):
            mapper[i] = item['Name']
            print("%d: %s" % (i, item['Name']))
        print("")
        
        invintioryOp = input("1 to see stats of an item, 2 to equip an item 3 to trash an item: ")
        if int(invintioryOp) == 1:
            itemNumber = int(input('Type the name number: '))
            for key in mapper.keys():
              print(key)
              print(mapper[key])
                           
		#if int(invintioryOp) == 3:
        	

            
		
        
        