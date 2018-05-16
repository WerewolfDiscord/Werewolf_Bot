class Spectator:
    pass

# ===============================================
class Innocent(Spectator):
    
    def __init__(self):
        self.name = "Innocent"
    
    def power(self,me):
        pass
    
    def night(self,me):
        me.votes = 1
    
    def day(self,me):
        me.bitten = False
        me.fakerole = self.name
    
    def kill(self,me,murderer):
        if murderer not in self.killers:
            return False
    
    def death_phase(self,me,murderer):
        if len(self.amulets) > 0 and self.name not in ["Amulet Holder", "Town Elder"]:
            return "Amulets"
        

# ===============================================
class Alcoholic(Innocent):

    def __init__(self):
        self.name = "Alcoholic"

# ===============================================
class Amulet_Holder(Innocent):

    def __init__(self):
        self.name = "Amulet Holder"
        
    def power(self,me,playertable,victim):
        if me.uses > 0 and me.undead == False and me.id != victim.id:
            for player in playertable:
                if victim.id == player.id and player.role.name not in ["Spectator", "Dead"]:
                    player.amulets.append(self.id)
                    return True
        return False
                    
    def night(self,me,playertable):
        self.votes = 1
        for player in playertable:
            if me.id in player.amulets and player.role.name == "Dead":
                player.amulets.remove(self.id)
                self.uses += 1

# ===============================================
class Assassin(Innocent):

    def __init__(self):
        self.name = "Assassin"
        
    def power(self,me,playertable,victim):
        if me.uses > 0 and me.undead == False:
            for player in playertable:
                if victim.id == player.id and player.role.name not in ["Spectator", "Dead"]:
                    me.uses += -1
                    # TODO: add victim to kill queue
                    return True
        return False

    def night(self,me):
        me.votes = 1
        me.uses = 1
    
    def day(self,me):
        me.uses = 0
        me.bitten = False

# ===============================================
class Aura_Teller(Assassin):

    def __init__(self):
        self.name = "Aura Teller"

    #TODO: Add a function that returns one's aura.
    def power(self,me):
        pass

# ===============================================
class Baker(Innocent):
    pass

# ===============================================
class Butcher(Innocent):
    pass
