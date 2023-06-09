def verificar_reacao_sheldon(escolha_sheldon, escolha_raj):
    if escolha_sheldon == escolha_raj:
        return "De novo!"
    elif (
        (escolha_sheldon == "tesoura" and (escolha_raj == "papel" or escolha_raj == "lagarto"))
        or (escolha_sheldon == "papel" and (escolha_raj == "pedra" or escolha_raj == "Spock"))
        or (escolha_sheldon == "pedra" and (escolha_raj == "lagarto" or escolha_raj == "tesoura"))
        or (escolha_sheldon == "lagarto" and (escolha_raj == "Spock" or escolha_raj == "papel"))
        or (escolha_sheldon == "Spock" and (escolha_raj == "tesoura" or escolha_raj == "pedra"))
    ):
        return "Bazinga!"
    else:
        return "Raj trapaceou!"
        
