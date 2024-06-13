#!/usr/bin/env python3

import sys, random, discord
from gachaconfig.banners import *

"""
Basic Wishing Functions
"""

invalidInput: str = "Invalid Input"
def warpString(results, pity, tenCount, guarantee):
    output = []
    output.append("You got...\n")
    output.append(results)
    output.append("\nYour current pity is {}".format(pity))
    output.append("Your G-4 star counter is at: {}".format(tenCount))
    output.append("Your 5 star guarantee status: {}".format(guarantee))
    output.append("\nWould you like to go again?\nY/N")

    return "\n".join(output)

def outputWish(result):

    if result == "***":
        embed = discord.Embed()

        file = discord.File("images/gacha/garbage.png")
        embed.set_thumbnail(url="attachment://garbage.png")
        embed.add_field(name="LOL!", value="Try again next time!")

        return [file, embed]

    else:
        stars = result.split("/")[0]
        embed = discord.Embed(
            title = "".join(["<:starStar:1248672337755242506>" for i in range(len(stars))]),
            description = result.split("/")[1]
        )

        return embed

def decideWish(banner, fourStar, guarantee, eventGuarantee):
    results = Wishing() ### Creating a wishing object, best way to 
                    ### access a range of commands that I have created
    
    result = results.wish(banner, fourStar, guarantee, eventGuarantee)
    # def wish(self, name, pity, pityStatus, tenCount):
    stars = result.split()[0]
    
    output = ""

    if stars == "***":
        output = stars

    else:
        output = result
    
    return result

# def wishOnce

"""
End of wishing functions
"""
class Wishing(object):

    def __init__(self):
        self.upTo = 29
        self.whatpity = "false"
    
    def wish(self, name, fourStar, guarantee, eventGuarantee):
        name = name[0]
        # esults.wish(banner, fourStar, guarantee, eventGuarantee)
        number = random.randint(1, 500)

        result = ""

        if fourStar == 10: #### 4 star guarantee
            fifty50 = random.randint(1, 2)
            coneOrChar = random.randint(1, 2)

            if coneOrChar == 1:
                result = "****/" + random.choice(standard4Cones)
            
            else:
                if fifty50 == 1:
                    print(eventBanners[name])
                    result = "****/" + random.choice(eventBanners[name])
                else:
                    result = "****/" + random.choice(standard4Star)
        
        elif eventGuarantee == "true":
            result = "****/" + name
        
        elif guarantee == "true":
            fifty50 = random.choice([0, 1])

            if fifty50 == 0:
                result = "****/" + name
            else:
                result = "*****/" + random.choice(standard5Star)
        
        else:
            if number >= 27 and number <= self.upTo:
                fifty50 = random.randint(1, 2)
                pity = 0

                if fifty50 == 1:
                    result = "****/" + name
                else:
                    result = "*****/" + random.choice(standard5Star)
            
            elif (number >= 1 and number <= 26):
                fifty50 = random.randint(1, 2)
                coneOrChar = random.randint(1, 2)

                if coneOrChar == 1:
                    result = "****/" + random.choice(standard4Cones)
                
                else:
                    if fifty50 == 1:
                        print(random.choice(eventBanners[name]))
                        result = "****/" + random.choice(eventBanners[name])
                    else:
                        result = "****/" + random.choice(standard4Star)
                
            else:
                result = "***/" + random.choice(standard3Cones)

        return result

        