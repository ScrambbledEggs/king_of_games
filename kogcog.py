import discord # type: ignore
from discord.ext import commands # type: ignore
from discord.ext.commands import errors

#used to check if inputs are int
def is_integer(number):
    try:
        int(number)
        return True
    
    except ValueError:
        return False

class Users():
    def __init__(self, member:discord.Member, points: int, KOG: bool):
        self.member = member
        self.points = points
        self.KOG = KOG
    
    def getMember(self):
        return self.member
    
    def setMember(self, newMember):
        self.member = newMember
        return

    def getUsername(self):
        if self.member.nick:
            return self.member.nick
        return self.member.display_name
    
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




class KoG_Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list_of_users = [] #list of objects
    


    @commands.command(aliases = ['kogr'])
    async def kog_register(self, ctx, *args):
        embed = discord.Embed(color=discord.Color.blurple())
        if len(args) == 0:
            embed.title = 'ERROR'
            embed.description = "no username has been input"
            await ctx.send(embed=embed)
            return
        
        try:
            member = await commands.converter.MemberConverter().convert(ctx, args[0])
        except:
            embed.title = 'ERROR'
            embed.description = 'user not found'
            await ctx.send(embed=embed)
            return
        
        

        for user in self.list_of_users:
            if member == user.getUsername():
                embed.title = 'ERROR'
                embed.description = 'username taken, contact admin'
                await ctx.send(embed=embed)
                return
            
        newUser = Users(member, 0, False)
        self.list_of_users.append(newUser)
        embed.title = 'Notice'
        embed.description = newUser.getUsername() + ' has been registered'
        await ctx.send(embed=embed)



    @commands.command(aliases = ['kogdel'])
    async def kog_deleteuser(self, ctx, *args):
        embed = discord.Embed(color=discord.Color.blurple())
        if len(args) == 0:
            embed.title = 'ERROR'
            embed.description = "no username has been input"
            await ctx.send(embed=embed)
            return
        
        try:
            member = await commands.converter.MemberConverter().convert(ctx, args[0])
        except:
            embed.title = 'ERROR'
            embed.description = 'user not found'
            await ctx.send(embed=embed)
            return


        for user in self.list_of_users:
            if user.getMember() == member:
                self.list_of_users.remove(user)
                embed.title = 'Notice'
                embed.description = user.getUsername() + ' has been removed'
                await ctx.send(embed=embed)
                return
            
        embed.title = 'ERROR'
        embed.description = 'username not found'
        await ctx.send(embed=embed)



    @commands.command(aliases = ['kogds'])
    async def kog_scores(self, ctx):
        embed = discord.Embed(color=discord.Color.blurple())
        embed.title = 'Scoreboard'
        embed.description = ''
        for user in self.list_of_users:
            embed.description += str(user.getUsername()) + ' ' + str(user.getPoints()) + '\n'
        await ctx.send(embed=embed)
        #find way to order the scoreboard in order of highest points to lowest points
        #find way to make score cap at top point earners 25




    @commands.command(aliases = ['kogpk'])
    async def who_is_kog(self, ctx):
        embed = discord.Embed(color=discord.Color.blurple())
        for user in self.list_of_users:
            if user.getKOG():
                embed.title = 'King Of Games'
                embed.description = str(user.getUsername()) + " is the King of Games, with a point value of " + str(user.getPoints())
                await ctx.send(embed=embed)
                #need to add what happens when there is no KOG




    @commands.command(aliases = ['kogot'])
    async def kog_overthrow(self, ctx, *args):
        embed = discord.Embed(color=discord.Color.blurple())
        if len(args) == 0:
            embed.title = 'ERROR'
            embed.description = "no username has been input"
            await ctx.send(embed=embed)
            return
        
        ifUserExists = False
        
        try:
            member = await commands.converter.MemberConverter().convert(ctx, args[0])
        except:
            embed.title = 'ERROR'
            embed.description = 'user not found'
            await ctx.send(embed=embed)
            return
        
        for user in self.list_of_users:
            if user.getMember() == member and not user.getKOG():
                user.setKOG(True)
            elif user.getMember() == member and user.getKOG():
                embed.title = 'ERROR'
                embed.description = "Username is already King of Games"
                await ctx.send(embed=embed)
                return
        
        for user in self.list_of_users:
            if user.getKOG() and user.getMember() != member:
                user.setKOG(False)
        #does not have affirmatory message for other throwing kog




    @commands.command(aliases = ['kogup'])
    async def UpdatePoints(self, ctx, *args):
        embed = discord.Embed(color=discord.Color.blurple())
        if len(args) == 0:
            embed.title = 'ERROR'
            embed.description = "no username has been input"
            await ctx.send(embed=embed)
            return
        
        if len(args) == 1:
            embed.title = 'ERROR'
            embed.description = "no points have been input"
            await ctx.send(embed=embed)
            return
        
        number_check = is_integer(args[1])
        if not number_check:
            embed.title = 'ERROR'
            embed.description = 'Points were not a numerical value'
            await ctx.send(embed=embed)
            return
        
        username = args[0]
        points = int(args[1])
        ifUserExists = False
        for user in self.list_of_users:
            if user.getUsername() == username:
                user.addPoints(int(points))
                embed.title = 'Point Update'
                embed.description = str(user.getUsername()) + " now has " + str(user.getPoints()) + " points"
                ifUserExists = True
                await ctx.send(embed=embed)
                break

        if not ifUserExists:
            embed.title = 'Error'
            embed.description = "Username not found"
            await ctx.send(embed=embed)
            return
        



async def setup(bot):
    await bot.add_cog(KoG_Bot(bot))