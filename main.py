import json
from os import path

import random

import discord
from discord.ext import commands

bot = commands.Bot()

@bot.slash_command(
    name = "roll",
    description = "Rolls an amount of dice an amount of times."
)
async def roll(
    ctx,
    dice: discord.Option(discord.SlashCommandOptionType.integer,description="The amount of faces each dice has.",name="faces"),
    amt: discord.Option(discord.SlashCommandOptionType.integer,description="The amount of dice to roll.",name="rolls")
): 
    total = 0
    final_str_rand = ""
    arg1 = dice
    arg2 = amt
    for i in range(arg2):
        tempRand = random.randrange(1, arg1)
        total = tempRand + total
        if i > 0:
            final_str_rand = final_str_rand + " + "
        final_str_rand = final_str_rand + str(tempRand)
    await ctx.respond(f"Rolled __**{arg2} d{arg1}**__.\n**{final_str_rand}**\n## Result: __{total}__")

@bot.slash_command(
    name = "roll_custom",
    description = "Rolls an amount of dice an amount of times."
)
async def roll_custom(
    ctx,
    dicemin: discord.Option(discord.SlashCommandOptionType.integer,description="The minimum amount that the dice can roll.",name="min"),
    dicemax: discord.Option(discord.SlashCommandOptionType.integer,description="The maximum amount that the dice can roll.",name="max"),
    amt: discord.Option(discord.SlashCommandOptionType.integer,description="The amount of dice to roll.",name="rolls")
): 
    total = 0
    final_str_rand = ""
    arg1 = dicemax
    arg3 = dicemin
    arg2 = amt
    for i in range(arg2):
        tempRand = random.randrange(arg3, arg1)
        total = tempRand + total
        if i > 0:
            final_str_rand = final_str_rand + " + "
        final_str_rand = final_str_rand + str(tempRand)
    await ctx.respond(f"Rolled __**{arg2} d{arg1}** above **face value {arg3}**__.\n**{final_str_rand}**\n## Result: __{total}__")

@bot.slash_command(
    name = "check_move",
    description = "Gets the data of a move."
)
async def check_move(
    ctx,
    name: discord.Option(discord.SlashCommandOptionType.string)
): 
    print("user", ctx.author, f"wants to see move {name}.")
    with open("data/static/moves.json", "r") as cur_file:
        data = json.load(cur_file)
    for name in data:
        nameMove = data[name]["Name"]
        typing = data[name]["Type"]
        if typing == "Bug":
            typeEmote = "<:TypeBug:1327612275212947536> "
        elif typing == "Dark":
            typeEmote = "<:TypeDark:1327612388127539304> "
        elif typing == "Dragon":
            typeEmote = "<:TypeDragon:1327612399284654142> "
        elif typing == "Electric":
            typeEmote = "<:TypeElectric:1327612410789625866> "
        elif typing == "Fairy":
            typeEmote = "<:TypeFairy:1327612429244432435> "
        elif typing == "Fighting":
            typeEmote = "<:TypeFighting:1327612439310761984> "
        elif typing == "Fire":
            typeEmote = "<:TypeFire:1327612449524027484> "
        elif typing == "Flying":
            typeEmote = "<:TypeFlying:1327612458541649922> "
        elif typing == "Ghost":
            typeEmote = "<:TypeGhost:1327612472223465482> "
        elif typing == "Grass":
            typeEmote = "<:TypeGrass:1327612487679344673> "
        elif typing == "Ground":
            typeEmote = "<:TypeGround:1327612504351969290> "
        elif typing == "Ice":
            typeEmote = "<:TypeIce:1327612517400449066> "
        elif typing == "Normal":
            typeEmote = "<:TypeNormal:1327612531883376681> "
        elif typing == "Poison":
            typeEmote = "<:TypePoison:1327612544772210738> "
        elif typing == "Psychic":
            typeEmote = "<:TypePsychic:1327612556558336051> "
        elif typing == "Rock":
            typeEmote = "<:TypeRock:1327612569778913341> "
        elif typing == "Steel":
            typeEmote = "<:TypeSteel:1327612586622976082> "
        elif typing == "Water":
            typeEmote = "<:TypeWater:1327612601798099044> "
        elif typing == "Stellar":
            typeEmote = "<:TypeStellar:1327612619304992768> "
        elif typing != "":
            typeEmote = "<:TypeUnknown:1327612631875321876> "
        cat = data[name]["Category"]

        bp = data[name]["Power"]
        bp = str(bp)
        pp = data[name]["PP"]
        maxpp = (((pp-pp%5)/5)*8)+(pp%5)
        maxpp = int(maxpp)
        pp = str(pp)
        maxpp = str(maxpp)
        acc = data[name]["ACC"]
        if acc > 100:
            acc = "Never misses."
        elif acc < 0:
            acc = "Targets self."
        else:
            acc = str(acc)+"% Accuracy."
        desc = data[name]["Desc"]
        target = data[name]["Target"]

        effects = data[name]["Effects"]
        effectsString = ""
        for effect in effects:
            effectsString = effectsString + "- " + effect + "\n"

        if data[name]["Ultimate"]:
            ult = "**This Ultimate move belongs to "+data[name]["UltimateChr"]+".**\n"
        else:
            ult = ""

        await ctx.respond(f"## __{nameMove}__\n**{typeEmote}{typing}-Type {cat} Move**\n- {bp} Base Power\n- {pp} PP ({maxpp} Max)\n- {acc}\n> {desc}\n- Targets {target}.\n{ult}\n---Effects---\n{effectsString}")
    else:
        await ctx.respond(f"The move **__{nameMove}__** does not exist in the database! Please kindly add it!")

@bot.slash_command(
    name = "add_move",
    description = "Adds the data of a move.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def add_move(
    ctx,
    moveindex: discord.Option(discord.SlashCommandOptionType.string),
    movename: discord.Option(discord.SlashCommandOptionType.string),
    typing: discord.Option(discord.SlashCommandOptionType.string),
    category: discord.Option(discord.SlashCommandOptionType.string),
    power: discord.Option(discord.SlashCommandOptionType.integer),
    pp: discord.Option(discord.SlashCommandOptionType.integer),
    accuracy: discord.Option(discord.SlashCommandOptionType.integer,description="-1 if the move targets the user, ex. Calm Mind. 101 if the move can never miss, ex. Swift."),
    desc: discord.Option(discord.SlashCommandOptionType.string),
    target: discord.Option(discord.SlashCommandOptionType.string),
    ult: discord.Option(discord.SlashCommandOptionType.boolean),
    ultchr: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
): 
    tempDict = {
        moveindex: {
            "Name": movename,
            "Type": typing,
            "Category": category,
            "Power": power,
            "Desc": desc,
            "PP": pp,
            "ACC": accuracy,
            "Target": target,
            "Effects": [],
            "Ultimate": ult,
            "UltimateChr": ultchr
        }
    }
    filename = './data/static/moves.json'
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)

    if moveindex in dictObj:
        await ctx.respond(f"Move {movename} already exists!")
    else:
        dictObj.update(tempDict)
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"Added move {movename} into the database.\nPlease add the Effects with the `/fix_effects` command.")

@bot.slash_command(
    name = "fix_effects",
    description = "Fixes the effect data of a move.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def fix_effects(
    ctx,
    moveindex: discord.Option(discord.SlashCommandOptionType.string),
    effect1: discord.Option(discord.SlashCommandOptionType.string),
    effect2: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
    effect3: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
    effect4: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
    effect5: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
    effect6: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
    effect7: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
    effect8: discord.Option(discord.SlashCommandOptionType.string,required=False,default=""),
    effect9: discord.Option(discord.SlashCommandOptionType.string,required=False,default="")
):
    effects = []
    if effect1 != "":
        effects.append(effect1)
    if effect2 != "":
        effects.append(effect2)
    if effect3 != "":
        effects.append(effect3)
    if effect4 != "":
        effects.append(effect4)
    if effect5 != "":
        effects.append(effect5)
    if effect6 != "":
        effects.append(effect6)
    if effect7 != "":
        effects.append(effect7)
    if effect8 != "":
        effects.append(effect8)
    if effect9 != "":
        effects.append(effect9)
    filename = './data/static/moves.json'
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)

    if moveindex in dictObj:
        dictObj[moveindex]["Effects"] = effects
        movename = dictObj[moveindex]["Name"]
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"{movename}'s effects fixed, please run `/check_move {moveindex}` to verify.")
    else:
        await ctx.respond(f"Move {moveindex} does not exist!")

@bot.slash_command(
    name = "update_move",
    description = "Updates the data of a move.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_move(
    ctx,
    moveindex: discord.Option(discord.SlashCommandOptionType.string),
    movename: discord.Option(discord.SlashCommandOptionType.string,default=""),
    typing: discord.Option(discord.SlashCommandOptionType.string,default=""),
    category: discord.Option(discord.SlashCommandOptionType.string,default=""),
    power: discord.Option(discord.SlashCommandOptionType.integer,default=0),
    pp: discord.Option(discord.SlashCommandOptionType.integer,default=0),
    accuracy: discord.Option(discord.SlashCommandOptionType.integer,default=0,description="-1 if the move targets the user, ex. Calm Mind. 101 if the move can never miss, ex. Swift."),
    desc: discord.Option(discord.SlashCommandOptionType.string,default=""),
    target: discord.Option(discord.SlashCommandOptionType.string,default=""),
):
    filename = './data/static/moves.json'
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)

    if moveindex in dictObj:
        if movename != "":
            dictObj[moveindex]["Name"] = movename
        if typing != "":
            dictObj[moveindex]["Type"] = typing
        if category != "":
            dictObj[moveindex]["Category"] = category
        if power != 0:
            dictObj[moveindex]["Power"] = power
        if pp != 0:
            dictObj[moveindex]["PP"] = pp
        if accuracy != 0:
            dictObj[moveindex]["ACC"] = accuracy
        if desc != "":
            dictObj[moveindex]["Deac"] = desc
        if target != "":
            dictObj[moveindex]["Target"] = target
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"{movename}'s data updated, please run `/check_move {moveindex}` to verify.")
    else:
        await ctx.respond(f"Move {moveindex} does not exist!")

@bot.slash_command(
    name = "damage_calc",
    description = "Calculates approximate damage (before items, abilities, weather, STAB, or weaknesses.)"
)
async def damage_calc(
    ctx,
    movepower: discord.Option(discord.SlashCommandOptionType.integer),
    selfatkstat: discord.Option(discord.SlashCommandOptionType.integer),
    foedefstat: discord.Option(discord.SlashCommandOptionType.integer),
    levelself: discord.Option(discord.SlashCommandOptionType.integer, default=100)
):
    tempRand = random.randrange(85, 100)
    damage = ((((((2*levelself)/5) +2) * movepower * (selfatkstat/foedefstat))/50) +2) * (tempRand/100)
    damage = damage*10000
    damage = damage-(damage%100)
    damage = damage/10000
    await ctx.respond(f"**The approximate damage a move with *{movepower}BP*, at *Level {levelself}*, where the offensive stat is __{selfatkstat}__, and the defensive stat is __{foedefstat}__, would be...**\n## *{damage} HP*.\n**This calculation already factored in the random 0.85 to 1.00 multiplier, round that as you will. ({tempRand/100})**\n\nI hope you already calculated the stat stages and etc.")

@bot.slash_command(
    name = "stat_calc",
    description = "Calculates the exact stat of a Pokemon at a specific level."
)
async def stat_calc(
    ctx,
    level: discord.Option(discord.SlashCommandOptionType.integer),
    ishealth: discord.Option(discord.SlashCommandOptionType.boolean, description="The calculation for HP and other stats are not the same."),
    basestat: discord.Option(discord.SlashCommandOptionType.integer),
    ivs: discord.Option(discord.SlashCommandOptionType.integer, default=20),
    evs: discord.Option(discord.SlashCommandOptionType.integer, default=0),
    nature: discord.Option(discord.SlashCommandOptionType.integer, default=0, description="1 if positive, -1 if detrimental, 0 if neutral."),
    stages: discord.Option(discord.SlashCommandOptionType.integer, default=0, description="This is for in-battle stat stages. Ranges from -6 to +6.")
):
    if ishealth:
        stat = ((2*basestat) + ivs + ((evs-(evs%4))/4))*level
        stat = (stat-(stat%100))/100
        stat = int(stat + level + 10)
        await ctx.respond(f"***Base {basestat} HP***, **{ivs} IVs**, **{evs} EVs**, at __Level {level}__:\n## *{stat} Max Health Pool*.")
    else:
        stat = ((2*basestat) + ivs + ((evs-(evs%4))/4))*level
        stat = (stat-(stat%100))/100
        stat = (stat + 5)
        if nature == 1:
            stat = stat * 110
            naturestr = "boosting"
        if nature == 0:
            stat = stat * 100
            naturestr = "neutral"
        if nature == -1:
            stat = stat * 90
            naturestr = "detrimental"
        stat = int((stat-(stat%100))/100)
        if stages > 0:
            statfinal = stat * (1+(0.5*stages))
            plural = ""
            if stages > 1:
                plural = "s"
            await ctx.respond(f"***Base {basestat} Stat***, **{ivs} IVs**, **{evs} EVs**, and a **{naturestr} nature**, at __Level {level}__:\n## *{stat}*.\n### With {stages} boost{plural}, *{statfinal}*.")
        elif stages < 0:
            statfinal = stat * (1/(1-(stages*0.5)))
            plural = ""
            if stages < -1:
                plural = "s"
            await ctx.respond(f"***Base {basestat} Stat***, **{ivs} IVs**, **{evs} EVs**, and a **{naturestr} nature**, at __Level {level}__:\n## *{stat}*.\n### With {-stages} drop{plural}, *{statfinal}*.")
        else:
            await ctx.respond(f"***Base {basestat} Stat***, **{ivs} IVs**, **{evs} EVs**, and a **{naturestr} nature**, at __Level {level}__:\n## *{stat}*.")

@bot.slash_command(
    name = "check_oc",
    description = "Checks the data for the specified OC. (Uses a User ID to identify who's is who's.)",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def check_oc(
    ctx,
    oc: discord.Option(discord.SlashCommandOptionType.string),
    userid: discord.Option(discord.SlashCommandOptionType.string, default="NONE", description="the User ID of the person you want to search. Defaults to your own ID.")
):
    if userid == "NONE":
        userid = str(ctx.author.id)
    print("user", ctx.author, "wants to see ", userid, "Json file.", ctx.author.id)
    with open("data/users/"+userid+".json", "r") as readfile:
        data = json.load(readfile)
    cur_handleID = str(data["ID"])
    for cur_OC in data["OCs"]:
        if oc == cur_OC:
            cur_OC_Data = data["OCs"][cur_OC]
            print("sending OC", cur_OC, "from the data of", cur_handleID)
            ocName = cur_OC_Data["FullName"]
            ocNameSmall = cur_OC_Data["Name"]
            species = cur_OC_Data["Species"]
            pronouns = cur_OC_Data["Pronouns"]
            age = cur_OC_Data["Age"]
            nature = cur_OC_Data["Nature"]

            type1 = cur_OC_Data["Type"][0]
            typing = type1
            if typing == "Bug":
                typeEmote = "<:TypeBug:1327612275212947536> "
            elif typing == "Dark":
                typeEmote = "<:TypeDark:1327612388127539304> "
            elif typing == "Dragon":
                typeEmote = "<:TypeDragon:1327612399284654142> "
            elif typing == "Electric":
                typeEmote = "<:TypeElectric:1327612410789625866> "
            elif typing == "Fairy":
                typeEmote = "<:TypeFairy:1327612429244432435> "
            elif typing == "Fighting":
                typeEmote = "<:TypeFighting:1327612439310761984> "
            elif typing == "Fire":
                typeEmote = "<:TypeFire:1327612449524027484> "
            elif typing == "Flying":
                typeEmote = "<:TypeFlying:1327612458541649922> "
            elif typing == "Ghost":
                typeEmote = "<:TypeGhost:1327612472223465482> "
            elif typing == "Grass":
                typeEmote = "<:TypeGrass:1327612487679344673> "
            elif typing == "Ground":
                typeEmote = "<:TypeGround:1327612504351969290> "
            elif typing == "Ice":
                typeEmote = "<:TypeIce:1327612517400449066> "
            elif typing == "Normal":
                typeEmote = "<:TypeNormal:1327612531883376681> "
            elif typing == "Poison":
                typeEmote = "<:TypePoison:1327612544772210738> "
            elif typing == "Psychic":
                typeEmote = "<:TypePsychic:1327612556558336051> "
            elif typing == "Rock":
                typeEmote = "<:TypeRock:1327612569778913341> "
            elif typing == "Steel":
                typeEmote = "<:TypeSteel:1327612586622976082> "
            elif typing == "Water":
                typeEmote = "<:TypeWater:1327612601798099044> "
            elif typing == "Stellar":
                typeEmote = "<:TypeStellar:1327612619304992768> "
            elif typing != "":
                typeEmote = "<:TypeUnknown:1327612631875321876> "
            type1 = typeEmote + type1

            type2 = cur_OC_Data["Type"][1]
            typing = type2
            if typing == "Bug":
                typeEmote = "<:TypeBug:1327612275212947536> "
            elif typing == "Dark":
                typeEmote = "<:TypeDark:1327612388127539304> "
            elif typing == "Dragon":
                typeEmote = "<:TypeDragon:1327612399284654142> "
            elif typing == "Electric":
                typeEmote = "<:TypeElectric:1327612410789625866> "
            elif typing == "Fairy":
                typeEmote = "<:TypeFairy:1327612429244432435> "
            elif typing == "Fighting":
                typeEmote = "<:TypeFighting:1327612439310761984> "
            elif typing == "Fire":
                typeEmote = "<:TypeFire:1327612449524027484> "
            elif typing == "Flying":
                typeEmote = "<:TypeFlying:1327612458541649922> "
            elif typing == "Ghost":
                typeEmote = "<:TypeGhost:1327612472223465482> "
            elif typing == "Grass":
                typeEmote = "<:TypeGrass:1327612487679344673> "
            elif typing == "Ground":
                typeEmote = "<:TypeGround:1327612504351969290> "
            elif typing == "Ice":
                typeEmote = "<:TypeIce:1327612517400449066> "
            elif typing == "Normal":
                typeEmote = "<:TypeNormal:1327612531883376681> "
            elif typing == "Poison":
                typeEmote = "<:TypePoison:1327612544772210738> "
            elif typing == "Psychic":
                typeEmote = "<:TypePsychic:1327612556558336051> "
            elif typing == "Rock":
                typeEmote = "<:TypeRock:1327612569778913341> "
            elif typing == "Steel":
                typeEmote = "<:TypeSteel:1327612586622976082> "
            elif typing == "Water":
                typeEmote = "<:TypeWater:1327612601798099044> "
            elif typing == "Stellar":
                typeEmote = "<:TypeStellar:1327612619304992768> "
            elif typing != "":
                typeEmote = "<:TypeUnknown:1327612631875321876> "
            if type2 != "":
                type2 = " | " + typeEmote + type2

            type3 = cur_OC_Data["Type"][2]
            typing = type3
            if typing == "Bug":
                typeEmote = "<:TypeBug:1327612275212947536> "
            elif typing == "Dark":
                typeEmote = "<:TypeDark:1327612388127539304> "
            elif typing == "Dragon":
                typeEmote = "<:TypeDragon:1327612399284654142> "
            elif typing == "Electric":
                typeEmote = "<:TypeElectric:1327612410789625866> "
            elif typing == "Fairy":
                typeEmote = "<:TypeFairy:1327612429244432435> "
            elif typing == "Fighting":
                typeEmote = "<:TypeFighting:1327612439310761984> "
            elif typing == "Fire":
                typeEmote = "<:TypeFire:1327612449524027484> "
            elif typing == "Flying":
                typeEmote = "<:TypeFlying:1327612458541649922> "
            elif typing == "Ghost":
                typeEmote = "<:TypeGhost:1327612472223465482> "
            elif typing == "Grass":
                typeEmote = "<:TypeGrass:1327612487679344673> "
            elif typing == "Ground":
                typeEmote = "<:TypeGround:1327612504351969290> "
            elif typing == "Ice":
                typeEmote = "<:TypeIce:1327612517400449066> "
            elif typing == "Normal":
                typeEmote = "<:TypeNormal:1327612531883376681> "
            elif typing == "Poison":
                typeEmote = "<:TypePoison:1327612544772210738> "
            elif typing == "Psychic":
                typeEmote = "<:TypePsychic:1327612556558336051> "
            elif typing == "Rock":
                typeEmote = "<:TypeRock:1327612569778913341> "
            elif typing == "Steel":
                typeEmote = "<:TypeSteel:1327612586622976082> "
            elif typing == "Water":
                typeEmote = "<:TypeWater:1327612601798099044> "
            elif typing == "Stellar":
                typeEmote = "<:TypeStellar:1327612619304992768> "
            elif typing != "":
                typeEmote = "<:TypeUnknown:1327612631875321876> "
            if type3 != "":
                type3 = "\nTera " + typeEmote + type3

            move1 = cur_OC_Data["Moves"]["Normal"][0]
            move2 = cur_OC_Data["Moves"]["Normal"][1]
            move3 = cur_OC_Data["Moves"]["Normal"][2]
            move4 = cur_OC_Data["Moves"]["Normal"][3]
            move5 = cur_OC_Data["Moves"]["Normal"][4]
            move6 = cur_OC_Data["Moves"]["Normal"][5]
            moveU = cur_OC_Data["Moves"]["Ultimate"][0]

            ability = cur_OC_Data["Ability"]
            innate1 = cur_OC_Data["Innates"]["Innate1"]
            innate2 = cur_OC_Data["Innates"]["Innate2"]
            innate3 = cur_OC_Data["Innates"]["Innate3"]

            item1 = cur_OC_Data["Item1"]
            item2 = cur_OC_Data["Item2"]

            stats = cur_OC_Data["Stats"]

            bhp = stats["BASE"]["HP"]
            if bhp/10 < 1:
                bhp = "00"+str(bhp)
            elif bhp/100 < 1:
                bhp = "0"+str(bhp)
            bat = stats["BASE"]["ATK"]
            if bat/10 < 1:
                bat = "00"+str(bat)
            elif bat/100 < 1:
                bat = "0"+str(bat)
            bdf = stats["BASE"]["DEF"]
            if bdf/10 < 1:
                bdf = "00"+str(bdf)
            elif bdf/100 < 1:
                bdf = "0"+str(bdf)
            bsp = stats["BASE"]["SPC"]
            if bsp/10 < 1:
                bsp = "00"+str(bsp)
            elif bsp/100 < 1:
                bsp = "0"+str(bsp)
            brs = stats["BASE"]["RES"]
            if brs/10 < 1:
                brs = "00"+str(brs)
            elif brs/100 < 1:
                brs = "0"+str(brs)
            bag = stats["BASE"]["AGI"]
            if bag/10 < 1:
                bag = "00"+str(bag)
            elif bag/100 < 1:
                bag = "0"+str(bag)

            ihp = stats["IV"]["HP"]
            if ihp/10 < 1:
                ihp = "0"+str(ihp)
            iat = stats["IV"]["ATK"]
            if iat/10 < 1:
                iat = "0"+str(iat)
            idf = stats["IV"]["DEF"]
            if idf/10 < 1:
                idf = "0"+str(idf)
            isp = stats["IV"]["SPC"]
            if isp/10 < 1:
                isp = "0"+str(isp)
            irs = stats["IV"]["RES"]
            if irs/10 < 1:
                irs = "0"+str(irs)
            iag = stats["IV"]["AGI"]
            if iag/10 < 1:
                iag = "0"+str(iag)

            ehp = stats["EV"]["HP"]
            if ehp/10 < 1:
                ehp = "00"+str(ehp)
            elif ehp/100 < 1:
                ehp = "0"+str(ehp)
            eat = stats["EV"]["ATK"]
            if eat/10 < 1:
                eat = "00"+str(eat)
            elif eat/100 < 1:
                eat = "0"+str(eat)
            edf = stats["EV"]["DEF"]
            if edf/10 < 1:
                edf = "00"+str(edf)
            elif edf/100 < 1:
                edf = "0"+str(edf)
            esp = stats["EV"]["SPC"]
            if esp/10 < 1:
                esp = "00"+str(esp)
            elif esp/100 < 1:
                esp = "0"+str(esp)
            ers = stats["EV"]["RES"]
            if ers/10 < 1:
                ers = "00"+str(ers)
            elif ers/100 < 1:
                ers = "0"+str(ers)
            eag = stats["EV"]["AGI"]
            if eag/10 < 1:
                eag = "00"+str(eag)
            elif eag/100 < 1:
                eag = "0"+str(eag)

            await ctx.respond(f"## *{ocName}*\n-# AKA {ocNameSmall}\n-# This character belongs to <@{cur_handleID}>\n- {species}\n- {pronouns}\n- {age}\n\n---Type---\n{type1}{type2}{type3}\n\n---Stats---\n`BASE {bhp} | {bat} | {bdf} | {bsp} | {brs} | {bag}`\n`IVs   {ihp} |  {iat} |  {idf} |  {isp} |  {irs} |  {iag}`\n`EVs  {ehp} | {eat} | {edf} | {esp} | {ers} | {eag}`\n> {nature} Nature\n\n---Moves---\n{move1}\n{move2}\n{move3}\n{move4}\n{move5}\n{move6}\n**---Ultimate---\n{moveU}**\n\n---Ability---\n> {ability}\n---Innates---\n> {innate1}\n> {innate2}\n> {innate3}\n\n---Held Items---\n> {item1}\n> {item2}")
    if oc not in data["OCs"]:
        await ctx.respond(f"OC {oc} does not exist in your/their database!")

@bot.slash_command(
    name = "oc_list",
    description = "Lists your entire OC data list.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def oc_list(
    ctx,
    userid: discord.Option(discord.SlashCommandOptionType.string, default="NONE", description="the User ID of the person you want to search. Defaults to your own ID.")
):
    if userid == "NONE":
        userid = str(ctx.author.id)
    print("user", ctx.author, "wants to see", userid, "OC list.", ctx.author.id)
    with open("data/users/"+userid+".json", "r") as readfile:
        data = json.load(readfile)
    cur_handleID = str(data["ID"])
    ocList = ""
    for cur_OC in data["OCs"]:
        ocList = ocList + data["OCs"][cur_OC]["Name"] + f" (Identifier: {cur_OC}), "
    ocList = ocList + "GAY...WHAT...HOWDIDYOUGUESSTHIS67894320"
    ocList = ocList.replace(", GAY...WHAT...HOWDIDYOUGUESSTHIS67894320", "")
    await ctx.respond(f"User <@{cur_handleID}> has the following OCs.\n## {ocList}")

@bot.slash_command(
    name = "add_oc",
    description = "Adds the data for the specified OC. (You'll be able to add more details after using this command.)",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def add_oc(
    ctx,
    oc: discord.Option(discord.SlashCommandOptionType.string),
    fullname: discord.Option(discord.SlashCommandOptionType.string),
    species: discord.Option(discord.SlashCommandOptionType.string),
    pronouns: discord.Option(discord.SlashCommandOptionType.string, description="Please use the They/Them format."),
    age: discord.Option(discord.SlashCommandOptionType.integer),
    type1: discord.Option(discord.SlashCommandOptionType.string),
    type2: discord.Option(discord.SlashCommandOptionType.string, default=""),
    type3: discord.Option(discord.SlashCommandOptionType.string, default="",name="teratype"),
    nature: discord.Option(discord.SlashCommandOptionType.string,default="")
):
    ocIndex = oc.lower()

    emptyOCDict = {ocIndex:
        {
            "Name": oc,
            "FullName": fullname,
            "Species": species,
            "Pronouns": pronouns,
            "Age": age,
            "Type": [type1, type2, type3],
            "Stats": {
                "BASE": {"HP": 0, "ATK": 0, "DEF": 0, "SPC": 0, "RES": 0, "AGI": 0},
                "IV": {"HP": 20, "ATK": 20, "DEF": 20, "SPC": 20, "RES": 20, "AGI": 20},
                "EV": {"HP": 0, "ATK": 0, "DEF": 0, "SPC": 0, "RES": 0, "AGI": 0}
                },
            "Ability": "None",
            "Innates": {
                "Innate1": "None",
                "Innate2": "None",
                "Innate3": "None"
                },
            "Item1": "Empty",
            "Item2": "Empty",
            "Moves": {
                "Normal": ["Struggle", "None", "None", "None", "None", "None"],
                "Ultimate": ["None"]
                },
            "Nature": nature
            }
        }

    print("user", ctx.author, "wants to add to their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {
        "ID": ctx.author.id,
        "OCs": {
        }
    }
    # Check if file exists
    if path.isfile(filename) is True:
        # Read JSON file
        with open(filename) as fp:
            dictObj = json.load(fp)

    if ocIndex in dictObj["OCs"]:
        name = dictObj["OCs"][ocIndex]["FullName"]
        await ctx.respond(f"Character {fullname} already exists as {name}!")
    else:
        dictObj["OCs"].update(emptyOCDict)
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"Added character {fullname} into your database.\nPlease add the other data pieces with the `/update_oc_...` commands.")

@bot.slash_command(
    name = "update_oc_ability",
    description = "Updates the ability data for the specified OC.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_oc_ability(
    ctx,
    ocindex: discord.Option(discord.SlashCommandOptionType.string),
    ability: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    innate1: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    innate2: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    innate3: discord.Option(discord.SlashCommandOptionType.string,default="None")
):
    print("user", ctx.author, "wants to edit their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        await ctx.respond("Please use the command `/add_oc` first!")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)
    if ocindex in dictObj["OCs"]:
        if ability != "None":
            dictObj["OCs"][ocindex]["Ability"] = ability
        if innate1 != "None":
            dictObj["OCs"][ocindex]["Innates"]["Innate1"] = innate1
        if innate2 != "None":
            dictObj["OCs"][ocindex]["Innates"]["Innate2"] = innate2
        if innate3 != "None":
            dictObj["OCs"][ocindex]["Innates"]["Innate3"] = innate3
        fullname = dictObj["OCs"][ocindex]["FullName"]
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"Updated character {fullname} in your database.")
    else:
        await ctx.respond(f"Character {ocindex} does not exist!")

@bot.slash_command(
    name = "update_oc_moves",
    description = "Updates the move data for the specified OC.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_oc_move(
    ctx,
    ocindex: discord.Option(discord.SlashCommandOptionType.string),
    move1: discord.Option(discord.SlashCommandOptionType.string,default="Struggle"),
    move2: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    move3: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    move4: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    move5: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    move6: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    moveu: discord.Option(discord.SlashCommandOptionType.string,default="None",name="ult")
):
    print("user", ctx.author, "wants to edit their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        await ctx.respond("Please use the command `/add_oc` first!")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)
    if ocindex in dictObj["OCs"]:
        if move1 != "Struggle":
            dictObj["OCs"][ocindex]["Moves"]["Normal"][0] = move1
        if move2 != "None":
            dictObj["OCs"][ocindex]["Moves"]["Normal"][1] = move2
        if move3 != "None":
            dictObj["OCs"][ocindex]["Moves"]["Normal"][2] = move3
        if move4 != "None":
            dictObj["OCs"][ocindex]["Moves"]["Normal"][3] = move4
        if move5 != "None":
            dictObj["OCs"][ocindex]["Moves"]["Normal"][4] = move5
        if move6 != "None":
            dictObj["OCs"][ocindex]["Moves"]["Normal"][5] = move6
        if moveu != "None":
            dictObj["OCs"][ocindex]["Moves"]["Ultimate"][0] = moveu
        fullname = dictObj["OCs"][ocindex]["FullName"]
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"Updated character {fullname} in your database.")
    else:
        await ctx.respond(f"Character {ocindex} does not exist!")

@bot.slash_command(
    name = "update_oc_items",
    description = "Updates the item data for the specified OC.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_oc_items(
    ctx,
    ocindex: discord.Option(discord.SlashCommandOptionType.string),
    item1: discord.Option(discord.SlashCommandOptionType.string,default="Empty"),
    item2: discord.Option(discord.SlashCommandOptionType.string,default="Empty")
):
    print("user", ctx.author, "wants to edit their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        await ctx.respond("Please use the command `/add_oc` first!")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)
    if ocindex in dictObj["OCs"]:
        if item1 != "Empty":
            dictObj["OCs"][ocindex]["Item1"] = item1
        if item2 != "Empty":
            dictObj["OCs"][ocindex]["Item2"] = item2
        fullname = dictObj["OCs"][ocindex]["FullName"]
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"Updated character {fullname} in your database.")
    else:
        await ctx.respond(f"Character {ocindex} does not exist!")

@bot.slash_command(
    name = "update_oc_basestats",
    description = "Updates the Base Stat data for the specified OC.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_oc_basestats(
    ctx,
    ocindex: discord.Option(discord.SlashCommandOptionType.string),
    hp: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=255),
    attack: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=255),
    defense: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=255),
    specialatk: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=255),
    specialdef: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=255),
    speed: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=255)
):
    print("user", ctx.author, "wants to edit their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        await ctx.respond("Please use the command `/add_oc` first!")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)
    if ocindex in dictObj["OCs"]:
        if hp != 0:
            dictObj["OCs"][ocindex]["Stats"]["BASE"]["HP"] = hp
        if attack != 0:
            dictObj["OCs"][ocindex]["Stats"]["BASE"]["ATK"] = attack
        if defense != 0:
            dictObj["OCs"][ocindex]["Stats"]["BASE"]["DEF"] = defense
        if specialatk != 0:
            dictObj["OCs"][ocindex]["Stats"]["BASE"]["SPC"] = specialatk
        if specialdef != 0:
            dictObj["OCs"][ocindex]["Stats"]["BASE"]["RES"] = specialdef
        if speed != 0:
            dictObj["OCs"][ocindex]["Stats"]["BASE"]["AGI"] = speed
        fullname = dictObj["OCs"][ocindex]["FullName"]
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"Updated character {fullname} in your database.")
    else:
        await ctx.respond(f"Character {ocindex} does not exist!")

@bot.slash_command(
    name = "update_oc_ivs",
    description = "Updates the IV data for the specified OC. They default to 20 and overwrite existing IVs.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_oc_ivs(
    ctx,
    ocindex: discord.Option(discord.SlashCommandOptionType.string),
    hp: discord.Option(discord.SlashCommandOptionType.integer,default=20,max_value=31),
    attack: discord.Option(discord.SlashCommandOptionType.integer,default=20,max_value=31),
    defense: discord.Option(discord.SlashCommandOptionType.integer,default=20,max_value=31),
    specialatk: discord.Option(discord.SlashCommandOptionType.integer,default=20,max_value=31),
    specialdef: discord.Option(discord.SlashCommandOptionType.integer,default=20,max_value=31),
    speed: discord.Option(discord.SlashCommandOptionType.integer,default=20,max_value=31)
):
    print("user", ctx.author, "wants to edit their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        await ctx.respond("Please use the command `/add_oc` first!")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)
    if ocindex in dictObj["OCs"]:
        dictObj["OCs"][ocindex]["Stats"]["IV"]["HP"] = hp
        dictObj["OCs"][ocindex]["Stats"]["IV"]["ATK"] = attack
        dictObj["OCs"][ocindex]["Stats"]["IV"]["DEF"] = defense
        dictObj["OCs"][ocindex]["Stats"]["IV"]["SPC"] = specialatk
        dictObj["OCs"][ocindex]["Stats"]["IV"]["RES"] = specialdef
        dictObj["OCs"][ocindex]["Stats"]["IV"]["AGI"] = speed
        fullname = dictObj["OCs"][ocindex]["FullName"]
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        await ctx.respond(f"Updated character {fullname} in your database.")
    else:
        await ctx.respond(f"Character {ocindex} does not exist!")

@bot.slash_command(
    name = "update_oc_evs",
    description = "Updates the EV data for the specified OC. They default to 0 and overwrite existing EVs.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_oc_evs(
    ctx,
    ocindex: discord.Option(discord.SlashCommandOptionType.string),
    hp: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=252),
    attack: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=252),
    defense: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=252),
    specialatk: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=252),
    specialdef: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=252),
    speed: discord.Option(discord.SlashCommandOptionType.integer,default=0,max_value=252)
):
    print("user", ctx.author, "wants to edit their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        await ctx.respond("Please use the command `/add_oc` first!")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)
    if ocindex in dictObj["OCs"]:
        if hp+attack+defense+specialatk+specialdef+speed > 510:
            await ctx.respond("Sorry, but the value for all of your EV points added up has to be at most 510.")
        else:
            dictObj["OCs"][ocindex]["Stats"]["EV"]["HP"] = hp
            dictObj["OCs"][ocindex]["Stats"]["EV"]["ATK"] = attack
            dictObj["OCs"][ocindex]["Stats"]["EV"]["DEF"] = defense
            dictObj["OCs"][ocindex]["Stats"]["EV"]["SPC"] = specialatk
            dictObj["OCs"][ocindex]["Stats"]["EV"]["RES"] = specialdef
            dictObj["OCs"][ocindex]["Stats"]["EV"]["AGI"] = speed
            fullname = dictObj["OCs"][ocindex]["FullName"]
            with open(filename, 'w') as json_file:
                json.dump(dictObj, json_file, indent=4, separators=(',',': '))
            print('Successfully written to the JSON file')
            await ctx.respond(f"Updated character {fullname} in your database.")
    else:
        await ctx.respond(f"Character {ocindex} does not exist!")

@bot.slash_command(
    name = "update_oc_info",
    description = "Updates the data for the specified OC.",
    guild_ids = [1327540933675454524, 1225661496525066251]
)
async def update_oc_items(
    ctx,
    ocindex: discord.Option(discord.SlashCommandOptionType.string),
    name: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    fullname: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    species: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    pronouns: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    age: discord.Option(discord.SlashCommandOptionType.integer,default=-1),
    type1: discord.Option(discord.SlashCommandOptionType.string,default="None"),
    type2: discord.Option(discord.SlashCommandOptionType.string,default=""),
    type3: discord.Option(discord.SlashCommandOptionType.string, default="",name="teratype"),
    nature: discord.Option(discord.SlashCommandOptionType.string,default="")
):
    print("user", ctx.author, "wants to edit their Json file.", ctx.author.id)
    filename = "./data/users/"+str(ctx.author.id)+".json"
    dictObj = {}
    
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        await ctx.respond("Please use the command `/add_oc` first!")
    
    # Read JSON file
    with open(filename) as fp:
        dictObj = json.load(fp)
    if ocindex in dictObj["OCs"]:
        fullnameOLD = dictObj["OCs"][ocindex]["FullName"]
        if name != "None":
            dictObj["OCs"][ocindex]["Name"] = name
        if fullname != "None":
            dictObj["OCs"][ocindex]["FullName"] = fullname
        if species != "None":
            dictObj["OCs"][ocindex]["Species"] = species
        if pronouns != "None":
            dictObj["OCs"][ocindex]["Pronouns"] = pronouns
        if age != -1:
            dictObj["OCs"][ocindex]["Age"] = age
        if type1 != "None":
            dictObj["OCs"][ocindex]["Type"][0] = type1
        if type2 != "":
            dictObj["OCs"][ocindex]["Type"][1] = type2
        if type3 != "":
            dictObj["OCs"][ocindex]["Type"][1] = type3
        if nature != "":
            dictObj["OCs"][ocindex]["Nature"] = nature
        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4, separators=(',',': '))
        print('Successfully written to the JSON file')
        if fullname != "None":
            await ctx.respond(f"Updated character {fullname} (was {fullnameOLD}) in your database.")
        else:
            await ctx.respond(f"Updated character {fullnameOLD} in your database.")
    else:
        await ctx.respond(f"Character {ocindex} does not exist!")




bot.run(BOT_TOKEN)

#ApplicationID = 1327538111999377418
#Token = GITHUB_SECRET_ENCODE
