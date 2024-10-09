import pandas as pd

file= "Ciências Biológicas I, Educação e Engenharias II.xlsx"  # Substitua com o caminho correto do seu arquivo
df = pd.read_excel(file)

#Esta função remove espaços em branco do início e do fim de cada string.
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Padronizando a coluna "Título" para evitar problemas com títulos semelhantes
df['Título'] = df['Título'].str.strip().str.upper()

# Agrupando por título e concatenando as informações de "Área de Avaliação", "Estrato" e "ISSN"
df_agrupado = df.groupby('Título').agg({
    'Área de Avaliação': lambda x: ', '.join(x.unique()),  # Combinar as áreas de avaliação
    'Estrato': lambda x: ', '.join(x.unique()),           # Combinar os estratos
    'ISSN': lambda x: ', '.join(x.unique())               # Combinar os ISSNs
}).reset_index()

# Exibindo o resultado
#print(df_agrupado.head(20))

# Exportando o DataFrame para um arquivo .txt
#df_agrupado.to_csv('output.txt', sep='\t', index=False, encoding='utf-8')

#Selecionando apenas aquelas revistas que tenham Educação e Engenharia II
df = df_agrupado[df_agrupado['Área de Avaliação'].str.contains('CIÊNCIAS BIOLÓGICAS I, EDUCAÇÃO, ENGENHARIAS II', case=False)]
df.to_csv('output2.txt', sep='\t', index=False, encoding='utf-8')
