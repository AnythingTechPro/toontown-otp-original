from direct.distributed.DistributedSmoothNodeAI import DistributedSmoothNodeAI
from direct.task.TaskManagerGlobal import *
from direct.task.Task import Task

class DistributedToonAI(DistributedSmoothNodeAI):

    def __init__(self, air):
        DistributedSmoothNodeAI.__init__(self, air)

        self.name = ''
        self.dnaString = ''
        self.maxBankMoney = 1000
        self.bankMoney = 0
        self.maxMoney = 40
        self.money = 0
        self.maxHp = 15
        self.hp = 0
        self.experience = ''
        self.maxCarry = 20
        self.trackAccess = [0, 0, 0, 0, 1, 1, 0]
        self.trackProgress = [-1, 0]
        self.inventory = ''
        self.friendsList = []
        self.defaultShard = 200000000
        self.defaultZone = 2000
        self.shtickerBook = ''
        self.zonesVisited = [2000]
        self.hoodsVisited = [2000]
        self.interface = ''
        self.accountName = ''
        self.lastHood = 0
        self.tutorialAck = 0
        self.maxClothes = 10
        self.clothesTopsList = []
        self.clothesBottomsList = []
        self.emoteAccess = []
        self.teleportAccess = []
        self.cogStatus = [1] * 32
        self.cogCount = [0] * 32
        self.cogRadar = [0] * 4
        self.buildingRadar = [0] * 4
        self.fishes = []
        self.houseId = 0
        self.quests = []
        self.questHistory = []
        self.rewardHistory = [0, []]
        self.questCarryLimit = 1
        self.cheesyEffect = [0, 0, 0]
        self.posIndex = 0

    def setName(self, name):
        self.name = name

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def getName(self):
        return self.name

    def setDNAString(self, dnaString):
        self.dnaString = dnaString

    def getDNAString(self):
        return self.dnaString

    def setMaxBankMoney(self, maxBankMoney):
        self.maxBankMoney = maxBankMoney

    def getMaxBankMoney(self):
        return self.maxBankMoney

    def setBankMoney(self, bankMoney):
        self.bankMoney = bankMoney

    def getBankMoney(self):
        return self.bankMoney

    def setMaxMoney(self, maxMoney):
        self.maxMoney = maxMoney

    def getMaxMoney(self):
        return self.maxMoney

    def setMoney(self, money):
        self.money = money

    def d_setMoney(self, money):
        self.sendUpdate("setMoney", money)

    def b_setMoney(self, money):
        self.setMoney(money)
        self.d_setMoney(money)

    def getMoney(self):
        return self.money

    def setMaxHp(self, maxHp):
        self.maxHp = maxHp

    def getMaxHp(self):
        return self.maxHp

    def setHp(self, hp):
        self.hp = hp

    def getHp(self):
        return self.hp

    def setExperience(self, experience):
        self.experience = experience

    def getExperience(self):
        return self.experience

    def setMaxCarry(self, maxCarry):
        self.maxCarry = maxCarry

    def getMaxCarry(self):
        return self.maxCarry

    def setTrackAccess(self, trackAccess):
        self.trackAccess = trackAccess

    def getTrackAccess(self):
        return self.trackAccess

    def setTrackProgress(self, track, progress):
        self.trackProgress = [track, progress]

    def getTrackProgress(self):
        return self.trackProgress

    def setInventory(self, inventory):
        self.inventory = inventory

    def getInventory(self):
        return self.inventory

    def setFriendsList(self, friendsList):
        self.friendsList = friendsList

    def getFriendsList(self):
        return self.friendsList

    def setDefaultShard(self, defaultShard):
        self.defaultShard = defaultShard

    def getDefaultShard(self):
        return self.defaultShard

    def setDefaultZone(self, defaultZone):
        self.defaultZone = defaultZone

    def d_setDefaultZone(self, defaultZone):
        self.sendUpdate("setDefaultZone", [defaultZone])

    def b_setDefaultZone(self, defaultZone):
        self.setDefaultZone(defaultZone)
        self.d_setDefaultZone(defaultZone)

    def getDefaultZone(self):
        return self.defaultZone

    def setShtickerBook(self, shtickerBook):
        self.shtickerBook = shtickerBook

    def getShtickerBook(self):
        return self.shtickerBook

    def setZonesVisited(self, zonesVisited):
        self.zonesVisited = zonesVisited

    def getZonesVisited(self):
        return self.zonesVisited

    def setHoodsVisited(self, hoodsVisited):
        self.hoodsVisited = hoodsVisited

    def d_setHoodsVisited(self, hoodsVisited):
        self.sendUpdate("setHoodsVisited", [hoodsVisited])

    def b_setHoodsVisited(self, hoodsVisited):
        self.setHoodsVisited(hoodsVisited)
        self.d_setHoodsVisited(hoodsVisited)

    def getHoodsVisited(self):
        return self.hoodsVisited

    def setInterface(self, interface):
        self.interface = interface

    def getInterface(self):
        return self.interface

    def setAccountName(self, accountName):
        self.accountName = accountName

    def getAccountName(self):
        return self.accountName

    def setLastHood(self, lastHood):
        self.lastHood = lastHood

    def d_setLastHood(self, lastHood):
        self.sendUpdate("setLastHood", [lastHood])

    def b_setLastHood(self, lastHood):
        self.setLastHood(lastHood)
        self.d_setLastHood(lastHood)

    def getLastHood(self):
        return self.lastHood

    def setTutorialAck(self, tutorialAck):
        self.tutorialAck = tutorialAck

    def getTutorialAck(self):
        return self.tutorialAck

    def setMaxClothes(self, maxClothes):
        self.maxClothes = maxClothes

    def getMaxClothes(self):
        return self.maxClothes

    def setClothesTopsList(self, clothesTopsList):
        self.clothesTopsList = clothesTopsList

    def getClothesTopsList(self):
        return self.clothesTopsList

    def setClothesBottomsList(self, clothesBottomsList):
        self.clothesBottomsList = clothesBottomsList

    def getClothesBottomsList(self):
        return self.clothesBottomsList

    def setEmoteAccess(self, emoteAccess):
        self.emoteAccess = emoteAccess

    def getEmoteAccess(self):
        return self.emoteAccess

    def setTeleportAccess(self, teleportAccess):
        self.teleportAccess = teleportAccess

    def getTeleportAccess(self):
        return self.teleportAccess

    def setCogStatus(self, cogStatus):
        self.cogStatus = cogStatus

    def getCogStatus(self):
        return self.cogStatus

    def setCogCount(self, cogCount):
        self.cogCount = cogCount

    def getCogCount(self):
        return self.cogCount

    def setCogRadar(self, cogRadar):
        self.cogRadar = cogRadar

    def getCogRadar(self):
        return self.cogRadar

    def setBuildingRadar(self, buildingRadar):
        self.buildingRadar = buildingRadar

    def getBuildingRadar(self):
        return self.buildingRadar

    def setFishes(self, fishes):
        self.fishes = fishes

    def getFishes(self):
        return self.fishes

    def setHouseId(self, houseId):
        self.houseId = houseId

    def getHouseId(self):
        return self.houseId

    def setQuests(self, quests):
        self.quests = quests

    def getQuests(self):
        return self.quests

    def setQuestHistory(self, questHistory):
        self.questHistory = questHistory

    def getQuestHistory(self):
        return self.questHistory

    def setRewardHistory(self, rewardTier, rewardList):
        self.rewardHistory = [rewardTier, rewardList]

    def getRewardHistory(self):
        return self.rewardHistory

    def setQuestCarryLimit(self, questCarryLimit):
        self.questCarryLimit = questCarryLimit

    def getQuestCarryLimit(self):
        return self.questCarryLimit

    def setCheesyEffect(self, effect, hoodId, expireTime):
        self.cheesyEffect = [effect, hoodId, expireTime]

    def getCheesyEffect(self):
        return self.cheesyEffect

    def setPosIndex(self, posIndex):
        self.posIndex = posIndex

    def getPosIndex(self):
        return self.posIndex
