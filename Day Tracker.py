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
            elif (i<100):
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
            elif (i<100):
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
            elif (i<100):
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
            elif (i<100):
                return Hot_Weather[6]

def Advance_Day(a, b, num):
    #Info
    with open(a, 'r', encoding='utf-8') as file:
        Info = file.readlines()
        
    days = (int(Info[17][22])*10 + int(Info[17][23]))*28 + int(Info[17][25])*10 + int(Info[17][26])
    
    year = int(Info[17][28:32])
    days = days - 1 + num
    
    while (days > 364):
        days = days - 364
        year = year + 1
    
    month = int((days)/28)
    day = str(int(days%28)+1)
    
    if (days%28+1) < 10:
        day = str(0) + day
    
    if month < 10:
        month = str(0) + str(month)
            
    #Converts days into Date
    Date_Nums =  month + "-" + day + "-" + str(year)
    
    #Converts days into Date in speaking terms
    Date_Text = Months[int((days)/28)-1] + " " + day + ", " + str(year)
    
    Info[17] = "[[Secret of Alania]]: " + Date_Nums + " | " + Date_Text + "\n"
    Info[18] = "Season: " + Seasons[int(days/91)] + "\n"
    Info[19] = "Weather: " + str(Calculate_Weather(int((days)/28))) + "\n"
    
    with open(a, 'w', encoding='utf-8') as file:
         file.writelines(Info)
    
    # Bounties 
    with open(b, 'r', encoding='utf-8') as file:
        Bounties = file.readlines()
        
    linecache.checkcache(str(a))
    linecache.checkcache(str(b))
    

def Get_Date_Info(a):
    return "Date: " + Get_Date(a) + "\nSeason: " + Get_Season(a) + "\nWeather: " + Get_Weather(a)

def Read_File(a):
    # Open and read the markdown file
    with open(a, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    
    return markdown_content

def Print_Contents(a):
    # Display the raw Markdown text
    print(Read_File(a))

def main():
    cont = True
    
    # Gathering Paths
    data_folder = Path("C:/Users/lucas/Documents/Buratah")
    Bounties = data_folder / "Campaign Notes" / "Bounties.md"
    Current_Info = data_folder / "Campaign Notes" / "Homebrew & World Rules.md"   
    
    while cont: #Repeating application until valid response and confirmation
        
        ans = input("Welcome to you very own DnD time manager!\n\nWould you like to see the current date, advance the days, or close the application? (1,2,3)")
        
        match ans:
            case 1:
                print("\n------------------------------------------------\n", Get_Date_Info(Current_Info), "\n")
            case 2:
                while cont: #Repeating day progression until valid response and confirmation
                    ans = input("How many days would you like to advance time by, or would you like to go back?")
                    
                    #Check if integer
                        #If integer then confirm?
                            #If confirm then advance days by X Days
                            #Would you like to advance days again?
                                #No -> cont = False
                                #Yes -> Pass
                                #Other -> Invalid Response
                        #Else
                            #Not a valid response
                    #Check if Back?
                        #Going back
                        #Cont = False
                    #Else
                        #Invalid Response
                cont = True
            case 3:
                print("\nGood Bye.\n")
                cont = false
            case _:
                print("\nInvalid Response, try again.\n")
    
if __name__ == "__main__":
    main()