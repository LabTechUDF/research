import pandas as pd
import matplotlib.pyplot as plt
import re
import os

# Criar diretório para salvar gráficos
os.makedirs('./graficos', exist_ok=True)

# Carregar o CSV processado
file_path = './processed_labtech_data_consolidated.csv'
data = pd.read_csv(file_path)

# Função para classificar experiência com base em palavras-chave
def classify_experience(experience):
    if pd.isnull(experience):
        return 'Indefinido'
    experience = experience.lower()
    if re.search(r'nenhuma|não tenho|sem experiência', experience):
        return 'Sem Experiência'
    if re.search(r'tecnologia|startup|projeto|desenvolvimento|busca de experiência', experience):
        return 'Com Experiência'
    return 'Indefinido'

# Aplicar a classificação
data['Classificação Experiência'] = data['Experience'].apply(classify_experience)

# Gráfico de barras - Classificação de Experiência
experience_counts = data['Classificação Experiência'].value_counts()
plt.figure(figsize=(8, 6))
experience_counts.plot(kind='bar', color=['skyblue', 'orange', 'gray'])
plt.title('Classificação de Experiência dos Participantes', fontsize=14)
plt.xlabel('Classificação', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('./graficos/experiencia_classificacao.png')
plt.show()

# Gráfico de pizza - Participação por Ano
data['Year'] = pd.to_datetime(data['Start Time'], errors='coerce').dt.year
year_counts = data['Year'].value_counts()
plt.figure(figsize=(8, 6))
year_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=True, colors=['lightblue', 'orange', 'green', 'red'])
plt.title('Participação por Ano', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.savefig('./graficos/participacao_por_ano.png')
plt.show()

# Histograma - Número de Estudantes por Curso
course_counts = data['Course'].value_counts()
plt.figure(figsize=(8, 6))
course_counts.plot(kind='bar', color='purple')
plt.title('Número de Estudantes por Curso', fontsize=14)
plt.xlabel('Curso', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./graficos/numero_estudantes_por_curso.png')
plt.show()

# Distribuição por Semestre
data['Semester'] = data['Semester'].astype(str)
semester_counts = data['Semester'].value_counts()
plt.figure(figsize=(8, 6))
semester_counts.sort_index().plot(kind='bar', color='cyan')
plt.title('Distribuição por Semestre', fontsize=14)
plt.xlabel('Semestre', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('./graficos/distribuicao_por_semestre.png')
plt.show()

# Linguagens mais citadas
languages = data['Languages'].str.split(', ').explode().value_counts()
plt.figure(figsize=(10, 6))
languages.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Linguagens Mais Citadas', fontsize=14)
plt.xlabel('Linguagem', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./graficos/top_linguagens_citadas.png')
plt.show()

# Processar a coluna "Preferred Activity" para entender vontades
def classify_preferred_activity(activity):
    if pd.isnull(activity):
        return 'Indefinido'
    activity = activity.lower()
    if re.search(r'análise|projeto|desenvolvimento|testes', activity):
        return 'Área Técnica'
    if re.search(r'gestão|coordenação|liderança', activity):
        return 'Gestão'
    return 'Outros'

data['Classificação Atividade'] = data['Preferred Activity'].apply(classify_preferred_activity)
activity_counts = data['Classificação Atividade'].value_counts()

# Gráfico de barras - Vontades dos Alunos
plt.figure(figsize=(8, 6))
activity_counts.plot(kind='bar', color=['blue', 'orange', 'gray'])
plt.title('Vontades dos Alunos', fontsize=14)
plt.xlabel('Área', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('./graficos/vontades_alunos.png')
plt.show()

# Salvar o arquivo com as novas colunas
processed_file_path = './graficos/processed_labtech_data_with_analysis.csv'
data.to_csv(processed_file_path, index=False)

print(f"Análise completa concluída. Gráficos gerados e salvos. Arquivo atualizado salvo em: {processed_file_path}")
