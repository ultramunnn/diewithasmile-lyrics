import sys
import time

def play_music():
    lyrics = [
        ("Wherever you go, that's where I'll follow", 0.09),
        ("Nobody's promised tomorrow", 0.09),
        ("So I'ma love you every night like it's the last night", 0.09),
        ("Like it's the last night", 0.09),
        ("If the world was ending, I'd wanna be next to you", 0.11),
        ("If the party was over and our time on Earth was through", 0.11),
        ("I'd wanna hold you just for a while and die with a smile", 0.12),
        ("If the world was ending, I'd wanna be next to you", 0.11),
    ]

    delay = [1.4, 1.2, 0.6, 0.7, 2.0, 2.2, 2.1, 2.2]  # Delay antar baris

    print("\n🎵 Die With A Smile - Bruno Mars & Lady Gaga 🎵\n")
    time.sleep(1.5)  # Jeda awal sebelum mulai lirik

    for i, (line_music, delay_character) in enumerate(lyrics):
        for character in line_music:
            print(character, end='', flush=True)
            time.sleep(delay_character)  
        time.sleep(delay[i])  # Jeda setelah satu baris selesai
        print('')

play_music()
