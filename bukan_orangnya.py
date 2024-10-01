from time import sleep
import sys

def print_lirik(): 

    line = [
        ("Lingkaranku kerap bertanya...", 0.12),
        ("Mengapa ku tampak biasa-biasa saja?", 0.11),
        ("Jalani hari dan tertawa\n(hu-uh, dan tertawa)", 0.13),
        ("Apa selama ini ku tak benar cinta?", 0.1),
        ("Tak harus kualirkan air mata untuk tunjukkan derita", 0.12),
        ("Dia tinggalkanku seketika", 0.09),
        ("Tak perlu ku terus-terus bertanya apa alasannya", 0.11),
        ("Mungkin dia bukan orangnya", 0.13),
        ("\nJuicy Luicy - Bukan Orangnya", 0.2 )
    ]

    delays = [2.0,
              2.0,
              0.5,
              0.7,
              0.7,
              2.1,
              1.5,
              2.5,
              1.0]


    for i, (lyric, char_delay) in enumerate(line):
        for char in lyric:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(char_delay)
        print() 
        sleep(delays[i])  

print_lirik()

#KenzieCarlen13