from os import system, name
import time

class Screen:

    width = 60

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def display_splash_page(self):
        self.clear()
        lines = """
                                                                                        
     _____ _____  _____ _____ _  ________ _______        _____ _______ _____ _____ _    
    / ____|  __ \|_   _/ ____| |/ /  ____|__   __|/\    / ____|__   __|_   _/ ____| |   
   | |    | |__) | | || |    | ' /| |__     | |  /  \  | (___    | |    | || |    | |   
   | |    |  _  /  | || |    |  < |  __|    | | / /\ \  \___ \   | |    | || |    | |   
   | |____| | \ \ _| || |____| . \| |____   | |/ ____ \ ____) |  | |   _| || |____|_|   
    \_____|_|  \_\_____\_____|_|\_\______|  |_/_/    \_\_____/   |_|  |_____\_____(_)   
                                                                                        
                                                                                        
"""
        for line in lines.split("\n"):
            time.sleep(0.1)
            print(line)
        time.sleep(2)

    def display_wicket_flash(self):
        self.display_flash("""
                                                          
    __          _______ _____ _  ________ _______ _       
    \ \        / /_   _/ ____| |/ /  ____|__   __| |      
     \ \  /\  / /  | || |    | ' /| |__     | |  | |      
      \ \/  \/ /   | || |    |  < |  __|    | |  | |      
       \  /\  /   _| || |____| . \| |____   | |  |_|      
        \/  \/   |_____\_____|_|\_\______|  |_|  (_)      
                                                          
                                                          
""")

    def display_six_flash(self):
        self.display_flash("""
                                  
       _____ _______   ___        
      / ____|_   _\ \ / / |       
     | (___   | |  \ V /| |       
      \___ \  | |   > < | |       
      ____) |_| |_ / . \|_|       
     |_____/|_____/_/ \_(_)       
                                  
                                  
""")


    def display_four_flash(self):
        self.display_flash("""
                                         
       ______ ____  _    _ _____  _      
      |  ____/ __ \| |  | |  __ \| |     
      | |__ | |  | | |  | | |__) | |     
      |  __|| |  | | |  | |  _  /| |     
      | |   | |__| | |__| | | \ \|_|     
      |_|    \____/ \____/|_|  \_(_)     
                                         
                                         
""")

    def display_flash(self, message):
        for i in range(3):
            self.clear()
            time.sleep(0.1)
            print(message)
