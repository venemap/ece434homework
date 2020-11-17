#!/usr/bin/env python3
import os, pygame, time, math, blynklib, sys, math, schedule
import tweepy as tw
from datetime import date
import datetime
import calendar
from pyowm import OWM
import config

alarmSet = 0 
a = 0

class pyclock :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        # disp_no = os.getenv("DISPLAY")
        # if disp_no:
        #     print("I'm running under X display = " + format(disp_no))
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        # os.putenv('SDL_FBDEV',   '/dev/fb0')
        os.putenv('SDL_NOMOUSE', '1')
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print('Driver: ' + format(driver) + ' failed.')
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print("Framebuffer size: ", size[0], "x", size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))   
        # Turn off cursor
        pygame.mouse.set_visible(False)
        # Initialise font support
        pygame.font.init()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def drawClock(self, blynk):
        global a
        timer = 0
        consumer_key = config.consumer_key
        consumer_secret = config.consumer_secret
        access_token = config.access_token
        access_token_secret =  config.access_token_secret
        
        owm = OWM(config.owmkey)
        mgr = owm.weather_manager()

        weatherCondition, currentTemp = updateWeather(mgr)
        
        dayWord, monthNum, dayNum = parseDate(date.today())
        
        auth = tw.OAuthHandler(consumer_key, consumer_secret)   
        auth.set_access_token(access_token, access_token_secret)

        api = tw.API(auth)
        
        # https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
        myfont = pygame.font.Font('LCD_test/DS-DIGI.TTF', 60)
        myfont2 = pygame.font.SysFont('Arial', 45)
        myfontTZ = pygame.font.SysFont('Arial', 25)
        weatherFont = pygame.font.SysFont('Arial', 35)
        weatherStatus = pygame.font.SysFont('Arial', 30)
        #weatherFont.set_bold(True)
        
        bg = pygame.image.load("LCD_test/swirlyBackground.jpg")
        bg = pygame.image.load("LCD_test/basicGrey.jpg")
        self.screen.blit(bg, (0, 0))
        

        
        api = tw.API(auth)

        #public_tweets = api.home_timeline()

        #user = api.get_user('ece343final')
        #print(user.screen_name)
        #for tweet in public_tweets:
        #    print(tweet.text)
                
        while True:
            blynk.run()
            if(timer > 300):
                weatherCondition, currentTemp = updateWeather(mgr)
                timer = 0

            if(alarmSet):
                schedule.run_pending()
                
            currentTime = time.localtime()
            hour = currentTime[3]    # Convert to 12 hour time
            minute = currentTime[4]
            second = currentTime[5]
            #hour -= 5 #random utc timezone issue
            
            if second < 10:
                second = "0" + str(second)
            else:
                second = str(second)    
            if minute < 10:
                minute = "0" + str(minute)
            else:
                minute = str(minute)  
            if hour < 5:
                if hour == 0: hour = 19
                if hour == 1: hour = 20
                if hour == 2: hour = 21
                if hour == 3: hour = 22
                if hour == 4: hour = 23
            else:
                hour -= 5
            #set am/pm
            if hour > 13:
                tz = "PM"
            else:
                tz = "AM"
                
            hour = hour % 12 #conver to 12hour time
                
            dateString = dayWord + " " + monthNum + "/" + dayNum
                
            ## Draw Time on Left
            if hour < 10:
                hour = " " + str(hour)
            else: 
                hour = str(hour)
            textsurface = myfont.render(
                    hour+":"+ minute, 
                    True, (0, 0, 0))
            self.screen.blit(textsurface,(25, 120))
            textsurface = myfontTZ.render(tz, True, (0,0,0))
            self.screen.blit(textsurface, (140, 130))
            
            ## Divider
            pygame.draw.line(self.screen, (0,0,0), (200, 120), (200, 200), 3)
            
            
            ## Draw Date at top
            textSurface2 = myfont2.render(dateString, True, (0,0,0))
            self.screen.blit(textSurface2, (20, 30))
            
            
            ## Draw Weather at right
            weatherSurface = weatherFont.render(
                str(currentTemp) + "`F", True, (0,0,0))
            self.screen.blit(weatherSurface, (220, 120))
            ## weather condition
            weatherConditionString = weatherStatus.render(
                str(weatherCondition).lower(), True, (0,0,0))
            self.screen.blit(weatherConditionString, (220, 170))
                
            #wait 1s and redraw
            pygame.display.update()
            pygame.time.wait(1000)
            timer += 1
            
            #clear screen, allow for updates
            self.screen.blit(bg, (0, 0))
            
def main(blynk):
    clock = pyclock()
    clock.drawClock(blynk)
    
def initBlynk():
    # Get the autherization code (See setup.sh)
    BLYNK_AUTH = os.getenv('BLYNK_AUTH', default="")
    BLYNK_AUTH = "LrwqMOl2bfhoo7EKqAhx-0ahGRge92r_"
    if(BLYNK_AUTH == ""):
        print("BLYNK_AUTH is not set")
        sys.exit()
    # Initialize Blynk
    blynk = blynklib.Blynk(BLYNK_AUTH)
    return blynk

blynk = initBlynk()
@blynk.handle_event('write V0')
def my_write_handler(pin, value):
    global alarmSet, a
    print("v0 write")
    timeInSeconds = int(value[0])
    hours = math.floor(timeInSeconds/3600)
    minutes = math.floor((timeInSeconds - hours*3600)/60)
    seconds = timeInSeconds - hours*3600 - minutes*60
    timeString = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    if len(str(seconds))==1:
        seconds = "0" + str(seconds)
    secondsString = ":" + str(seconds)
                    
    print(secondsString)
    if(alarmSet):
       schedule.cancel_job(a)
    a = schedule.every().minute.at(secondsString).do(soundAlarm)
    #print(a)
    alarmSet = 1
    print(timeString)
    
def soundAlarm():
    print("insert applicable alarm here")
    
def parseDate(date):
    # Textual month, day and year	
    d2 = date.today().strftime("%A %b %d %m")
    monthNum = date.today().strftime("%m")
    dayWord = date.today().strftime("%A")
    dayNum = date.today().strftime("%d")
    return dayWord, monthNum, dayNum
    
def updateWeather(mgr):
    currWeather = mgr.weather_at_place('Terre Haute')
    weatherCondition = currWeather.weather.status
    weatherPreString = currWeather.weather.temperature('fahrenheit')
    currentTemp = int(weatherPreString["temp"])
    return weatherCondition, currentTemp
    
main(blynk)