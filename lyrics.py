import time
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def print_lyrics():

    lyrics = [
        "jodi Biroh Thake, Amio Thaki.",
        "Ke Bolo Shesh Hobe Age?",
        "Keno Je Eto Bhalobasha More Jay,",
        "Shudhu Shomoy Mone Rakhe.",
        "Eto Shunnota, E Mone Rakhi Je Ami.",
        "Dekhe Na Keu To Ar, Bole Eshob-I Paglami.",
        "Kate Na Jamini, Biroho Jeno Kete Jaye.",
        "Thame Na Borsha, Tomare Daki Je Ami.",
        ]

    delays = [0.3, 1.9, 1.2, 0.9, 0.9, 0.2, 0.5, 0.7]

  
    char_delay = 0.11

    for i, line in enumerate(lyrics):
        

        for char in line:
            sys.stdout.write(char)  
            sys.stdout.flush()      
            time.sleep(char_delay)  
        
        print() 
        
        
        time.sleep(delays[i % len(delays)])


if __name__ == "__main__":
    print_lyrics()

