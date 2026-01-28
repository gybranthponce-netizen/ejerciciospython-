#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
#después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos 
#o 10 céntimos).

# Cálculo de euros Moneda de España
total_euros = euro2 * 2 + euro1

# Cálculo de céntimos parte de los euros
total_centimos = cent50 * 50 + cent20 * 20 + cent10 * 10

# Conversión de céntimos a euros
total_euros += total_centimos // 100
total_centimos = total_centimos % 100

# Salida
print(total_euros, "euros y", total_centimos, "céntimos.")

#fin_del_proceso_de_practicas.