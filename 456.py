import re

# Abre o arquivo original para leitura
with open('seu_arquivo.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Novo conteúdo com numeração adicionada
new_lines = []
episode_number = 1

for line in lines:
    # Remove o trecho "Sxx Exx"
    line = re.sub(r'S\d{2} E\d{2}', '', line)
    # Adiciona a numeração do episódio ao final do nome do arquivo
    line = line.strip() + f" E{episode_number:02d}\n"
    new_lines.append(line)
    episode_number += 1

# Salva o novo conteúdo em um novo arquivo
with open('seu_novo_arquivo.txt', 'w', encoding='utf-8') as file:
    file.writelines(new_lines)

print("Processo concluído!")