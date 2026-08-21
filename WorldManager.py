from pathlib import Path
import linecache
import random

# Defining Variables
Months = [
    "Juani",
    "Estran",
    "Fuanti",
    "Guama",
    "Ketra",
    "Petrola",
    "Luala",
    "Jetran",
    "Obara",
    "Neitan",
    "Meleo",
    "Restralia",
    "Wellia"
]

Seasons = [
    "Spring",
    "Summer",
    "Autumn",
    "Winter"
]

Hot_Weather = [
    "Thunderstorm",
    "Heavy Rain",
    "Light Rain",
    "Cloudy",
    "Partly Cloudy",
    "Sunny",
    "Blazing Heat"
]

Warm_Weather = [
    "Heavy Rain",
    "Light Rain",
    "Cloudy",
    "Partly Cloudy",
    "Sunny"
]

Cool_Weather = [
    "Heavy Snow",
    "Gentle Snow",
    "Cloudy",
    "Partly Cloudy",
    "Sunny"
]

Cold_Weather = [
    "Blizzard",
    "Heavy Snow",
    "Gentle Snow",
    "Cloudy",
    "Partly Cloudy",
    "Sunny"
]

Crimes = {
    "Theft": 30,
    "Property Theft": 50,
    "Grand Theft": 200,
    "Horse Theft": 300,
    "Assault": 20,
    "Battery": 50,
    "Attempted Murder": 150,
    "Murder": 300,
    "Mass Murder": 3000,
    "Vandalism": 10,
    "Destruction of Property": 50,
    "Kidnapping": 100,
    "Fraud": 50,
    "Disturbing the Peace": 10,
    "Breaking and Entering": 30,
    "Trespassing": 10,
}

Players = [
    "Monkey (Wukong)",
    "Seraphine Nightveil", 
    "Lyra Avalon",
    "Polaris",
    "Drakar (Saxaroth)",
    "Brom Barlycorn",
    "Gideon Waywright"
]

# Functions
def Get_Date(a):     
    line_number = 18  # Reads the 18th line

    # Fetch the specific line
    line = linecache.getline(str(a), line_number)

    return line[22:].strip()

def Get_Season(a):
    line_number = 19  # Reads the 18th line

    # Fetch the specific line
    line = linecache.getline(str(a), line_number)
        
    return line[8:].strip()

def Get_Weather(a):
    line_number = 20  # Reads the 18th line
    # Fetch the specific line
    line = linecache.getline(str(a), line_number)
        
    return line[9:].strip()

def Calculate_Weather(m):
    i = random.randint(1,100)
    match m:
        case 11 | 12: # Cold
            if (i<8):
                return Cold_Weather[0]
            elif (i<20):
                return Cold_Weather[1]
            elif (i<40):
                return Cold_Weather[2]
            elif (i<70):
                return Cold_Weather[3]
            elif (i<90):
                return Cold_Weather[4]
            elif (i<=100):
                return Cold_Weather[5]
        case 1 | 9 | 10 | 13: # Cool
            if (i<15):
                return Cool_Weather[0]
            elif (i<30):
                return Cool_Weather[1]
            elif (i<60):
                return Cool_Weather[2]
            elif (i<80):
                return Cool_Weather[3]
            elif (i<=100):
                return Cool_Weather[4]
        case 2 | 3 | 4 | 7 | 8: # Warm
            if (i<15):
                return Warm_Weather[0]
            elif (i<30):
                return Warm_Weather[1]
            elif (i<60):
                return Warm_Weather[2]
            elif (i<80):
                return Warm_Weather[3]
            elif (i<=100):
                return Warm_Weather[4]
        case 5 | 6: # Hot
            if (i<10):
                return Hot_Weather[0]
            elif (i<25):
                return Hot_Weather[1]
            elif (i<40):
                return Hot_Weather[2]
            elif (i<55):
                return Hot_Weather[3]
            elif (i<70):
                return Hot_Weather[4]
            elif (i<95):
                return Hot_Weather[5]
            elif (i<=100):
                return Hot_Weather[6]

def Advance_Day(a, b, num):
    #Info
    with open(a, 'r', encoding='utf-8') as file:
        Info = file.readlines()
        
    days = (int(Info[17][22:24])-1)*28 + int(Info[17][25:27])
    
    year = int(Info[17][28:32])
    days = days - 1 + num
        
    while (days > 364):
        days = days - 364
        year = year + 1
    
    month = int((days)/28+1)
    day = str(int(days)%28+1)
        
    if int(day) < 10:
        day = str(0) + str(day)
    
    if month < 10:
        month = str(0) + str(month)
            
    #Converts days into Date
    Date_Nums =  str(month) + "-" + day + "-" + str(year)
    
    #Converts days into Date in speaking terms
    Date_Text = Months[int((days)/28)] + " " + day + ", " + str(year)
    
    Info[17] = "[[Secret of Alania]]: " + Date_Nums + " | " + Date_Text + "\n"
    Info[18] = "Season: " + Seasons[int(days/91)] + "\n"
    Info[19] = "Weather: " + str(Calculate_Weather(int(month))) + "\n"
    
    with open(a, 'w', encoding='utf-8') as file:
         file.writelines(Info)
         
    #Update Bounties
    Update_Bounties(b, num)
        
    linecache.checkcache(str(a))
    linecache.checkcache(str(b))    

def Get_Date_Info(a):
    return "Date: " + Get_Date(a) + "\n Season: " + Get_Season(a) + "\n Weather: " + Get_Weather(a)

def Get_Total_Days(a):
    #Info
    with open(a, 'r', encoding='utf-8') as file:
        Info = file.readlines()
    days = (int(Info[17][22])*10 + int(Info[17][23]))*28 + int(Info[17][25])*10 + int(Info[17][26]) 
    year  = year = int(Info[17][28:32])

    return (364 * year + days)

def Read_File(a):
    # Open and read the markdown file
    with open(a, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    
    return markdown_content

def Calculate_Bounty(bounty, severity):
    
    return int(bounty/10*severity + bounty)

def Write_Bounty(a, b, player, crime, bounty, location, severity):
    day = Get_Total_Days(a)
        
    # Bounties 
    with open(b, 'r', encoding='utf-8') as file:
        Bounties = file.readlines()
        
    index = "None"
    
    for dex, line in enumerate(Bounties):
        if player in line:
            bounties = int(line[-2:])
            index = int(dex) + 1 + bounties
            bounties += 1
            Bounties[dex] = "[[" + player + "]]: " + str(int(bounties/10)) + str(int(bounties%10)) + "\n"
            break
            
    if index == "None":
        return "\nPlayer not found.\n"
    
    new_line = "\t" + str(crime)+" | " + str(bounty) + "cp | " + str(location) + " | " + Get_Date(a) + " (Heat Time: " + str(int(Crimes[crime]/10 + int(severity)/10)) + " days)\n"
    Bounties.insert(index, new_line)
    
    # Writes to File
    with open(b, "w", encoding="utf-8") as file:
        file.writelines(Bounties) 
    
    linecache.checkcache(str(b)) 
    
def Update_Bounties(b, days):
    # Bounties 
    with open(b, 'r', encoding='utf-8') as file:
        Bounties = file.readlines()
        
    bountyDex = 0
    playerDex = 0
    player = ""
    removeArray = []
    for dex, line in enumerate(Bounties):
        if "[[" in line:
            player = line[2:-7] 
            playerDex = dex
            bountyDex = 0
        elif line[0] != "#":
            bountyDex += 1
            
            #Extracting heat time remaining
            heat = int(line.partition("Heat Time: ")[2][0:-6])
            num = int(heat - days)
            
            #Extracting remaining bounty
            remainingBounty = int(line.partition(" | ")[2].partition(" | ")[0][0:-2])
            if num > 0:
                heat = num
            else:
                heat = 0
                remainingBounty -= (-num) * 15
            if remainingBounty > 0:
                bounty = remainingBounty
                new_line = line.partition(" | ")[0] + " | " + str(bounty) + "cp | " + line.partition("cp | ")[2].partition("Time: ")[0] + "Time: " + str(heat) + " days)\n"
                Bounties[dex] = new_line
            else:
                removeArray.append([player, playerDex, bountyDex])
    
    # Updates changed bounties
        with open(b, "w", encoding="utf-8") as file:
                file.writelines(Bounties) 
            
        linecache.checkcache(str(b)) 
    
    # For each item in the remove array, it removes the item from the bounty list
    for item in reversed(removeArray): #(MUST GO IN REVERSE ORDER TO FUNCTION)
        Remove_Bounty(b, item[0], item[1], item[2])  
    
    #Display bounties for each player
    for player in Players:
        print(player + "'s bounties:")
        print(Display_Bounties(b, player)[1])

def Display_Bounties(b, player):
    with open(b, 'r', encoding='utf-8') as file:
            Bounties = file.readlines()   
    bounties = -1  
    nums = 1
    display = ""
    idex = 0
    for dex, line in enumerate(Bounties):
        if bounties != 0:
            if player in line:
                bounties = int(line[-2:])  
                idex = dex
                if bounties != 0:
                    display = "----------------Bounty----------------"
            elif bounties > 0:
                display += "\n" + str(nums) + ".     " + str(line)
                bounties -= 1
                nums += 1
    if display == "":
        return(idex, "--------------No Bounties--------------\n")
    else:
        return(idex, display)

def Remove_Bounty(b, player, idex, select):
    with open(b, 'r', encoding='utf-8') as file:
        Bounties = file.readlines()  
                
    bounties = int(Bounties[idex][-2:])
    if bounties > 0:
        bounties -= 1
    Bounties[idex] = "[[" + player + "]]: " + str(int(bounties/10)) + str(int(bounties%10)) + "\n"
    
    del Bounties[idex+select]
    
    # Writes to File
    with open(b, "w", encoding="utf-8") as file:
        file.writelines(Bounties) 
    
    linecache.checkcache(str(b))  

def main():
    cont = True
        
    # Gathering Paths
    data_folder = Path("C:/Users/lucas/Documents/Buratah")
    Bounties = data_folder / "Campaign Notes" / "Bounties.md"
    Current_Info = data_folder / "Campaign Notes" / "Homebrew & World Rules.md" 
      
    print("Welcome to you very own DnD world manager!\n")
    
    while cont: #Repeating application until valid response and confirmation
        ans = input("Would you like to see the current date, advance the days, make a bounty, clear a player's bounty, view all bounties, or close the application?\n(1,2,3,4,5,6):  ")
        
        match ans:
            case "1":
                print("\n--------------Current Day--------------\n", Get_Date_Info(Current_Info), "\n---------------------------------------\n")
            case "2":
                while cont: #Repeating day progression until valid response and confirmation
                    days = input("\nHow many days do you want to advance by?   ")
                    
                    # Error checking for invalid type
                    #try:
                    confirm = True
                    while confirm:
                        inp = "Is this the days intended -> " + str(int(days)) + "? (Y or N)   "
                        ans = input(inp)
                        match ans:
                            case "Y":
                                confirm = False
                                if int(days) <= 0:
                                    print("\nCanceling day progression...\n")
                                elif int(days) == 1:
                                    print("\n\nProgressing by 1 day...")
                                    Advance_Day(Current_Info,Bounties,1)
                                    print("\n----------------New Day----------------\n", Get_Date_Info(Current_Info), "\n---------------------------------------\n")
                                else:
                                    print("\n\nProgressing by", int(days), "days...")
                                    Advance_Day(Current_Info,Bounties,int(days))
                                    print("\n----------------New Day----------------\n", Get_Date_Info(Current_Info), "\n---------------------------------------\n")
                                cont = False
                            case "N":
                                confirm = False
                            case _:
                                print("\nInvalid Response.")
                    #except:
                        #print("\nInvalid response.")                    
                cont = True
            case "3":
                #Assigning local variables
                convicted = []
                display = ""
                
                # Checking the crime
                while cont:
                    crime = input("\nWhat crime have they been conviceted of?   ")
                    try:
                        bounty = Crimes[crime]
                        cont = False
                    except:
                        print("\nCrime not found.")
                cont = True
                
                # Calculating the bounty
                while cont:
                    severity = input("What is the severity of the crime (1-100)\n(1: Homelessguy   20: Commoner   40: Shopkeeper   60: Nobleman   80: Diplomats   100: Royalty)?   ")
                    if int(severity) <= 100 and int(severity) >= 1:
                        bounty = Calculate_Bounty(bounty, int(severity))
                        cont = False
                    else:
                        print("\nInvalid Severity.\n")
                cont = True
                
                # Bounty Location
                while cont:    
                    location = input("What is the location of the bounty?   ")
                    confirm = True
                    while confirm:
                        inp = "Is this the location intended -> " + location + "? (Y or N)   "
                        ans = input(inp)
                        match ans:
                            case "Y":
                                confirm = False
                                cont = False
                            case "N":
                                confirm = False
                            case _:
                                print("\nInvalid Response.\n")
                cont = True
                  
                # Players with bounty
                print("Which players have been charged? (Y or N)   ")
                
                for player in Players:
                    while cont:
                        inp = player + "?   "
                        ans = input(inp)
                        match ans:
                            case "Y":
                                cont = False
                                convicted.append(player)
                            case "N":
                                cont = False
                            case _:
                                print("\nInvalid Response.\n")                            
                    cont = True

                #Create display text
                if len(convicted) == 0:
                    display = "Nobody was convicted of the crime."
                elif len(convicted) == 1:
                    display = convicted[0] + " has been convicted of " + str(crime) + " in " + str(location) + ".\n Their bounty is " + str(bounty) + " copper pieces, and the heat expires in " + str(int(Crimes[crime]/10 + int(severity)/10)) + " days."
                elif len(convicted) == 2:
                    display = convicted[1] + " and " + convicted[0] + " have been convicted of " + str(crime) + " in " + str(location) + ".\n Their bounty is " + str(bounty) + " copper pieces, and the heat expires in " + str(int(Crimes[crime]/10 + int(severity)/10)) + " days."
                else:
                    for player in convicted:
                        if player != convicted[-1]:
                            display += player + ", "
                        else:
                            display += "and " + player
                    display += " have been convicted of " + str(crime) + " in " + str(location) + ".\n Their bounty is " + str(bounty) + " copper pieces, and the heat expires in " + str(int(Crimes[crime]/10 + int(severity)/10)) + " days."
                
                #Write the bounties
                for player in convicted:
                    Write_Bounty(Current_Info, Bounties, player, crime, bounty, location, severity)
                
                #prints the bounty display message
                print("\n---------------------------------------\n",display,"\n---------------------------------------\n")
            case "4":
                print("\nWhich player would you like to clear a bounty from? (Y or N)")
                removal = "None"
                
                for player in Players:
                    if ans != "Y":
                        while cont:
                            question = player + "?   "
                            ans = input(question)
                            match ans:
                                case "Y":
                                    removal = player
                                    cont = False
                                case "N":
                                    cont = False
                                case _:
                                    print("\nInvalid Response.\n")                            
                        cont = True
                if removal != "None":
                    print("\nWhich bounty would you like to remove from " + str(removal) + "?")
                    disp = Display_Bounties(Bounties, removal)
                    print(disp[1])
                    if disp[1] != "--------------No Bounties--------------\n":
                        ans = input("Please type a number:   ")
                        try:
                            if int(ans) > 0:
                                Remove_Bounty(Bounties, removal,  disp[0], int(ans))
                                print("\nBounty #" + ans + " has been removed from " + removal + "...\n")
                            else:
                                print("\nCanceling bounty removal...\n")
                        except:
                            print("\nInvalid Input...\nCanceling bounty removal...\n")
                    else:
                        print("\nCanceling bounty removal...\n")
                    
                else:
                    print("\nCanceling bounty removal...\n")    
            case "5":
                print("\n--------------All Bounties--------------\n")
                #Display bounties for each player
                for player in Players:
                    print(player + "'s bounties:")
                    print(Display_Bounties(Bounties, player)[1])
            case "6":
                print("\nGood Bye.\n")
                cont = False
            case _:
                print("\nInvalid Response, try again.\n")
    
if __name__ == "__main__":
    main()
