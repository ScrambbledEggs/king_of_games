class Users():
    def __init__(self, username: str, points: int, KOG: bool):
        self.username = username
        self.points = points
        self.KOG = KOG
    
    def getUsername(self):
        return self.username
    
    def setUsername(self, newUsername):
        self.username = newUsername
    
    def getPoints(self):
        return self.points
    
    def setPoints(self, newPoints):
        self.points = newPoints

    def addPoints(self, newPoints):
        self.points += newPoints

    def getKOG(self):
        return self.KOG
    
    def setKOG(self, newKOG):
        self.KOG = newKOG

class DiscordBot():
    def __init__(self):
        self.list_of_users = [] #list of objects

    def AddUser(self, username: str):
        for user in self.list_of_users:
            if username == user.getUsername():
                print("Username taken. Contact Admin")
                return
        newUser = Users(username, 0, False)
        self.list_of_users.append(newUser)

    def DeleteUser(self, username: str):
        for user in self.list_of_users:
            if user.getUsername() == username:
                self.list_of_users.remove(user)
                return
        print("No username found")

    def DisplayScoreboard(self):
        for user in self.list_of_users:
            print(str(user.getUsername()), user.getPoints())

    def PrintKOG(self):
        for user in self.list_of_users:
            if user.getKOG():
                print(str(user.getUsername()) + " is the King of Games, with a point value of " + str(user.getPoints()))

    def UpdateKOG(self, username: str):
        ifUserExists = False
        for user in self.list_of_users:
            if user.getUsername() == username and not user.getKOG():
                user.setKOG(True)
                ifUserExists = True
                break

        if not ifUserExists:
            print("Username not found/Username is already King of Games")
            return

        #remove old KOG
        for user in self.list_of_users:
            if user.getKOG() and user.getUsername() != username:
                user.setKOG(False)

    def UpdatePoints(self, username: str, points: int):
        ifUserExists = False
        for user in self.list_of_users:
            if user.getUsername() == username:
                user.addPoints(points)
                print(str(user.getUsername()) + " now has " + str(user.getPoints()) + " points")
                ifUserExists = True
                break
        
        if not ifUserExists:
            print("Username not found")
            return
        
if __name__ == "__main__":
    bot = DiscordBot()
    bot.AddUser("OverValley")
    bot.AddUser("owenm19")
    bot.DisplayScoreboard()
    bot.UpdateKOG("OverValley")
    bot.PrintKOG()
    bot.UpdatePoints("owenm19", 5)
    bot.DisplayScoreboard()
    bot.UpdatePoints("owenm19", -5)
    bot.DisplayScoreboard()
    bot.UpdatePoints("owenm19", -5)
    bot.DisplayScoreboard()
    bot.UpdateKOG("owenm19")
    bot.PrintKOG()
    bot.UpdateKOG("gooddaygoodluck")
    bot.DeleteUser("OverValley")
    bot.DisplayScoreboard()

