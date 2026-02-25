import time

# Cronómetro de 1 hora

for hora in range(0, 1):        # Solo 1 hora
    for minuto in range(0, 60):
        for segundo in range(0, 60):
            
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
            time.sleep(1)

            #fin