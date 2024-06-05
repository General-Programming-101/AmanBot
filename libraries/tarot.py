"""
    Tarot Card Stuff
"""
import random

TAROT_CARD_CONFIG: dict = {
    "The Fool" : ["beginnings, innocence, a free spirit", "recklessness", "fool.jpg"],
    "The Magician" : ["manifestation, power, resourcefulness", "manipulation, poor planning", "magician.jpg"],
    "The High Priestess" : ["Desirability, mystery, creativity", "Repression of intuition", "highpriestess.jpg" ],
    "The Empress" : ["Beauty, nature, art", "Insecurity, lack of confidence, negligence", "empress.jpg"],
    "The Emperor" : ["Stability, authority", "Abuse of power, stubborness", "emperor.jpg"],
    "The Hierophant" : ["Conformity, conventional", "Non-conformity, unconventional Relationships", "hierophant.jpg"],
    "The Lovers" : ["Perfect Unions, partnerships, relationships", "Disharmony, imbalance, conflict", "lovers.jpg"],
    "The Chariot" : ["Victory, success, ambition", "Forcefulness, aggresion, coercion", "chariot.jpg"],
    "Strength" : ["Inner Strength, courage, bravery", "Vulnerability, low self-esteem", "strength.jpg"],
    "The Hermit" : ["Soul searching, contemplation, solitude", "Loneliness, paranoia, isolation", "hermit.jpg"],
    "The Wheel of Fortune" : ["Good luck, destiny, change", "Bad luck, upheaval", "wheel.jpg"],
    "Justice" : ["Justice, honesty", "injustice, karmic retribution, dishonesty", "justice.jpg"],
    "The Hanged Man" : ["Confined, lack of direction", "Discontentment, apathy", "hangedman.jpg"],
    "Death" : ["New beginnings, change", "Inability to move forward, dependency", "death.jpg"],
    "Temperance" : ["Balance, peace, patience", "Imbalance, excess, discord", "temperance.jpg"],
    "The Devil" : ["Addiction, depression, bondage", "Detachment, independence", "devil.jpg"],
    "The Tower" : ["Chaos, destruction, abuse", "Resisting change, averting disaster", "tower.jpg"],
    "The Star" : ["Hope, inspiration, creativity", "Hopelessness, despair", "star.jpg"],
    "The Moon" : ["Intuition, illusion, dreams", "Releasing fear, self-deception, truth", "moon.jpg"],
    "The Sun" : ["Positivity, freedom, fun", "Lack of enthusiasm, sadness, pessimism", "sun.jpg"],
    "Judgement" : ["Judgement, self-evaluation, awakening", "Self-doubt, indecisiveness", "judgement.jpg"],
    "The World" : ["Success, achievement", "Lack of success, stagnation, burden", "world.jpg"]
}

# print(len(TAROT_CARD_CONFIG))
# print(list(TAROT_CARD_CONFIG.keys()))

class Tarot:

    def __init__(self):
        self.cards = TAROT_CARD_CONFIG
        self.hand = {}
    
    def createHand(self):
        found = []

        for i in range(0, 3):
            randNum = random.randint(0, 3)
            while randNum in found:
                randNum = random.randint(0, 3)
            
            found.append(randNum)
            #### Get our values

            # randNum = 0

            cardTitle = list(TAROT_CARD_CONFIG.keys())[randNum]

            self.hand[cardTitle] = TAROT_CARD_CONFIG[cardTitle]

    def getHand(self):

        if not self.hand:
            self.createHand()

        # print(self.hand)

        return self.hand

    # def __str__(self):

        # return START_UP