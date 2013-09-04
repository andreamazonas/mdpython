# Autor : Andre Amazonas
# 
#
# Probabilidade
# P(E) = N(E)
#        N(S) 

# Exemplo - Cara ou Coroa
# P(1) = 1
#        2



print (" __  __     _      _____                                 _   _             ")
print ("|  \/  |   | |    / ____|                               | | (_)            ")
print ("| \  / | __| |   | |     ___  _ __ _ __   ___  _ __ __ _| |_ _  ___  _ __  ")
print ("| |\/| |/ _` |   | |    / _ \| '__| '_ \ / _ \| '__/ _` | __| |/ _ \| '_ \ ")
print ("| |  | | (_| |_  | |___| (_) | |  | |_) | (_) | | | (_| | |_| | (_) | | | |")
print ("|_|  |_|\__,_(_)  \_____\___/|_|  | .__/ \___/|_|  \__,_|\__|_|\___/|_| |_|")
print ("                                  | |                                      ")
print ("                                  |_|                                      ")


# Resolvendo a Equacao
ns = input( "Digite o Espaco Amostral:")
ne = input( "Digite o Evento:")
ne = int(ne)
ns = int (ns)
p = ne/ns
p = float (p)
print (" A probabilidade eh :",p)
