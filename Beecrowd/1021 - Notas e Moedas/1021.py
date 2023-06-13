#1021 

entrada, centavos = input().split('.')

entrada = int(entrada)
centavos = int(centavos)

############################################CÉDULAS#################################################

cem,       resto = divmod(entrada, 100)
cinquenta, resto = divmod(resto,    50)
vinte,     resto = divmod(resto,    20)
dez,       resto = divmod(resto,    10)
cinco,     resto = divmod(resto,     5)
dois,      resto = divmod(resto,     2)

############################################MOEDAS##################################################
um                        = resto
cinquenta_centavos, resto = divmod(centavos, 50)
vinte_centavos,     resto = divmod(resto,    25)
dez_centavos,       resto = divmod(resto,    10)
cinco_centavos,     resto = divmod(resto,    5)
um_centavo                = resto

cem = int(cem)
cinquenta = int(cinquenta)
vinte = int(vinte)
dez = int(dez)
cinco = int(cinco)
dois = int(dois)
um = int(um)
cinquenta_centavos = int(cinquenta_centavos)
vinte_centavos = int(vinte_centavos)
dez_centavos = int(dez_centavos)
cinco_centavos = int(cinco_centavos)
um_centavo = int(um_centavo)


print('''NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00
MOEDAS:
{} moeda(s) de R$ 1.00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{} moeda(s) de R$ 0.01'''.format(cem, cinquenta, vinte, dez, cinco, dois, um, cinquenta_centavos, vinte_centavos, dez_centavos, cinco_centavos, um_centavo))
