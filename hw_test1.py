

import random
import time

greetings = ["Hello, World!", "Hola, Mundo!", "Bonjour, Monde!", "Ciao, Mondo!", "Hallo, Welt!", "こんにちは、世界！", "안녕하세요, 세계!"]

# Surprise each time with a random greeting
greeting = random.choice(greetings)

# Get fancy with slow typing effect
for char in greeting:
    print(char, end='', flush=True)
    time.sleep(0.1)

# Just in case it wasn't clear...
print("\nDid you get that? It's a 'HELLO WORLD' in style! 😎")


