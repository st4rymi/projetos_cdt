'''
Primicias
 Define o nome do arquivo onde os desejos serão salvos;
 será definido o nome do arquivo;
 o app será escrito e lido;
 será definido se o arquivo será feito ou não;
 usando o log win+, se cria o emoji;
 a lista SEMPRE começa vazia;
 ao escrver o nitem será colocado em novas linhas;

'''
try:
    with open(NOME_ARQUIVO), 'r', encoding='utf-8)' as arquivos:
        for linha in arquivo:
        
    desejos.append(linha.strip())
    print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}")'!\n")
except FileNotFoundError:
print("Parece que é sua primeira vez! Vamos criar sua lista de desejos.!\n")
except Exception as e:
print(f"Ocorreu um erro ao carregar os desejos: {e}")

def salvar_desejos(lista_de_desejos):
try:
   with open(NOME_ARQUIVO, 'w', encoding='uft-8') as arquivos:
    for desejo in lista_de_desejos:
        arquivo.write(desejo + "\n") 
print("\n✅ Seus desejos foram salvos com sucesso!")
except Exception as e:
print(f"\n❌ Erro ao salvar os desejos: {e}")

while True
   print()