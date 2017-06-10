from SpecImports import *
from toontown.toonbase import ToontownGlobals
import random
CogParent = 10000
FrontCogParent = 10002
LeftCogParent = 10007
RightCogParent = 10010
BattleCellId = 0
FrontBattleCellId = 1
LeftBattleCellId = 2
RightBattleCellId = 3
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)},
 FrontBattleCellId: {'parentEntId': FrontCogParent,
                     'pos': Point3(0, 0, 0)},
 LeftBattleCellId: {'parentEntId': LeftCogParent,
                    'pos': Point3(0, 0, 0)},
 RightBattleCellId: {'parentEntId': RightCogParent,
                     'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': FrontBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': FrontBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': FrontBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': FrontBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': LeftBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': LeftBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': LeftBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': LeftBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': RightBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': RightBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': RightBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': RightBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': random.choice([1, 2, 3, 4])}]
ReserveCogData = []
