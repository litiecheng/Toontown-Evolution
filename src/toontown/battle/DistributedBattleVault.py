from toontown.battle.DistributedBattleWaiters import DistributedBattleWaiters

import random
from pandac.PandaModules import VBase3, Point3
from direct.interval.IntervalGlobal import Sequence, Func, Parallel, Track
from toontown.battle import DistributedBattleFinal
from toontown.suit import SuitTimings
from toontown.toonbase import ToontownGlobals

class DistributedBattleVault(DistributedBattleWaiters):

    def announceGenerate(self):
        DistributedBattleFinal.DistributedBattleFinal.announceGenerate(self)
        # self.moveSuitsToInitialPos()

    def doInitialFlyDown(self):
        self.showSuitsFalling(self.suits, 0, self.uniqueName('initial-FlyDown'), self.flyDownDone)

    def flyDownDone(self):
        print 'flyDownDone'

    def showSuitsFalling(self, suits, ts, name, callback):
        if self.bossCog == None:
            return
        suitTrack = Parallel()
        delay = 0
        for suit in suits:
            suit.makeVirtual(healthColored=True)
            suit.setState('Battle')
            if suit.dna.dept == 'l':
                suit.reparentTo(self.bossCog)
                suit.setPos(0, 0, 0)
            if suit in self.joiningSuits:
                i = len(self.pendingSuits) + self.joiningSuits.index(suit)
                destPos, h = self.suitPendingPoints[i]
                destHpr = VBase3(h, 0, 0)
            else:
                destPos, destHpr = self.getActorPosHpr(suit, self.suits)
            startPos = destPos + Point3(0, 0, SuitTimings.fromSky * ToontownGlobals.SuitWalkSpeed)
            self.notify.debug('startPos for %s = %s' % (suit, startPos))
            suit.reparentTo(self)
            suit.setPos(startPos)
            suit.headsUp(self)
            flyIval = suit.beginSupaFlyMove(destPos, True, 'flyIn')
            suitTrack.append(Track((delay, Sequence(flyIval, Func(suit.loop, 'neutral')))))
            delay += 1

        if self.hasLocalToon():
            base.camera.reparentTo(self)
            if random.choice([0, 1]):
                base.camera.setPosHpr(20, -4, 7, 60, 0, 0)
            else:
                base.camera.setPosHpr(-20, -4, 7, -60, 0, 0)
        done = Func(callback)
        track = Sequence(suitTrack, done, name=name)
        track.start(ts)
        self.storeInterval(track, name)
        return
