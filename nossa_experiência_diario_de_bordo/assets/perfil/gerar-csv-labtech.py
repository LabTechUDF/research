import pandas as pd
import re

# Carregar os dados do Excel
file_path = './dados_alunos_LABTECH_UDF_2024_2.xlsx'
data = pd.read_excel(file_path)

# Renomear colunas para facilitar o processamento
data.columns = [
    "ID", "Start Time", "End Time", "Email", "Name", "Stage Mandatory Participation",
    "Full Name", "RGM", "Phone", "Contact Email", "Course", "Semester",
    "Experience", "Interest Area", "Languages", "Availability", "Software Factory Knowledge",
    "Preferred Activity", "Infrastructure"
]

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

# Aplicar a classificação de experiência
data['Classificação Experiência'] = data['Experience'].apply(classify_experience)

# Função para classificar atividades preferidas
def classify_preferred_activity(activity):
    if pd.isnull(activity):
        return 'Indefinido'
    activity = activity.lower()
    if re.search(r'análise|projeto|desenvolvimento|testes', activity):
        return 'Área Técnica'
    if re.search(r'gestão|coordenação|liderança', activity):
        return 'Gestão'
    return 'Outros'

# Aplicar a classificação de atividades preferidas
data['Classificação Atividade'] = data['Preferred Activity'].apply(classify_preferred_activity)

# Processar ano de participação
data['Year'] = pd.to_datetime(data['Start Time'], errors='coerce').dt.year

# Salvar o arquivo consolidado
processed_file_path = './processed_labtech_data_consolidated.csv'
data.to_csv(processed_file_path, index=False)

print(f"Dados consolidados salvos em: {processed_file_path}")
