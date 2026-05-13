"""
Análise das respostas do formulário "LABTECH - COMPETÊNCIAS".

Processa o CSV com 13 respostas, contendo:
  - 17 itens em escala Likert 1-4 (EntreComp, Bacigalupo et al. 2016)
  - 20 itens em escala 1-5 (General Self-Efficacy Scale, Sherer et al. 1982;
    itens 8, 11, 13, 16, 18, 20 são reversos)
  - 1 resposta aberta (analisada por Bardin 2011)

Saídas em ./graficos/ e ./*.csv / ./tab_competencias.tex
"""
import os
import re
import unicodedata
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

CSV = '../../relatorios/LABTECH - COMPETÊNCIAS (Responses) - Form Responses 1.csv'
OUT_FIG = './graficos/'
os.makedirs(OUT_FIG, exist_ok=True)
plt.rcParams['font.family'] = 'DejaVu Sans'

df = pd.read_csv(CSV, encoding='utf-8')
df.columns = [unicodedata.normalize('NFC', c).strip() for c in df.columns]

# Mapeamento oficial de cursos
CURSOS = {
    'ADS': 'Análise e Desenvolvimento de Sistemas',
    'DG':  'Design Gráfico',
    'CCP': 'Ciência da Computação',
    'SI':  'Sistemas de Informação',
    'ENG': 'Engenharia de Software',
}
df['curso_nome'] = df['Curso vinculado no UDF'].map(CURSOS).fillna(df['Curso vinculado no UDF'])

# ---------- EntreComp (17 itens, Likert 1-4) ----------
EC_COLS = {
    'EC01': '1)Eu posso IDENTIFICAR minhas necessidades, desejos, interesses e objetivos.',
    'EC02': '2) Eu posso DESCREVER minhas necessidades, desejos, interesses e objetivos.',
    'EC03': '3) Posso identificar coisas em que sou bom e coisas em que não sou bom.',
    'EC04': '4) Eu posso julgar meus pontos fortes e fracos e os dos outros em relação às oportunidades de criação de valor.',
    'EC05': '5) Eu acredito na minha capacidade de fazer o que me DEMANDAM com sucesso.',
    'EC06': '6)Eu acredito na minha capacidade de ALCANÇAR o que pretendo.',
    'EC07': '7) Eu posso mostrar respeito pelos outros, seus antecedentes e situações.',
    'EC08': '8) Estou aberto ao valor que outros podem trazer para atividades criadoras de valor.',
    'EC09': '9) Eu posso mostrar empatia para com os outros.',
    'EC10': '10) Posso reconhecer o papel das minhas emoções, atitudes e comportamentos na formação das atitudes e comportamentos das outras pessoas e vice-versa.',
    'EC11': '11) Eu posso mostrar empatia para com os outros.',
    'EC12': '12) Posso discutir os benefícios de ouvir as ideias de outras pessoas para alcançar meus objetivos (ou de minha equipe).',
    'EC13': '13) Estou aberto a trabalhar sozinho e com os outros, desempenhando papéis diferentes e assumindo alguma responsabilidade.',
    'EC14': '14) Estou disposto a mudar minha maneira de trabalhar em grupo.',
    'EC15': '15) Estou aberto a envolver outras pessoas em minhas atividades criadoras de valor.',
    'EC16': '16) Eu posso contribuir para atividades simples de criação de valor.',
    'EC17': '17) Eu posso contribuir para a tomada de decisões em grupo de forma construtiva.',
}

ec = df[list(EC_COLS.values())].copy()
ec.columns = list(EC_COLS.keys())
ec = ec.apply(lambda s: s.astype(str).str.extract(r'^\s*(\d)').iloc[:, 0]).apply(pd.to_numeric, errors='coerce')

DIMS_EC = {
    'Autoconsciência\ne autoeficácia\n(Ideias e Oportunidades)': ['EC01', 'EC02', 'EC03', 'EC04', 'EC05', 'EC06'],
    'Mobilização\nde outros\n(Recursos)': ['EC07', 'EC08', 'EC09', 'EC10', 'EC11'],
    'Criação de valor\ncolaborativa\n(Em Ação)': ['EC12', 'EC13', 'EC14', 'EC15', 'EC16', 'EC17'],
}
ec_dim = pd.DataFrame({d: ec[cols].mean(axis=1) for d, cols in DIMS_EC.items()})

# ---------- General Self-Efficacy Scale (20 itens, 1-5) ----------
GSE_COLS = {
    'GSE01': '1) Eu sou capaz de ATINGIR a maior parte dos objetivos que defino para mim.',
    'GSE02': '2. Eu sou capaz de SUPERAR muitos desafios.',
    'GSE03': '3. Costumo ser PERSISTENTE na busca de meus objetivos.',
    'GSE04': '4. Eu acredito que eu POSSO ter sucesso em quase qualquer coisa que eu resolva fazer.',
    'GSE05': '5. Eu POSSO fazer a maioria das coisas melhor do que as pessoas em geral.',
    'GSE06': '6. Mesmo quando as coisas estão difíceis, eu POSSO desempenhá-las muito bem.',
    'GSE07': '7. Quando faço planos, sei que POSSO fazer que eles deem certo.',
    'GSE08': '8. Se algo parece muito complicado eu nem TENTO fazer.',
    'GSE09': '9. Se eu não consigo fazer algo pela primeira vez, eu continuo TENTANDO até conseguir.',
    'GSE10': '10. Eu sou uma pessoa autoconfiante.',
    'GSE11': '11. Quando eu defino objetivos importantes para mim eu raramente os atinjo.',
    'GSE12': '12. Quando traço um objetivo, logo começo a colocá-lo em prática.',
    'GSE13': '13. Quando problemas inesperados acontecem, eu não lido bem com eles.',
    'GSE14': '14. Eu costumo PERSISTIR em meus planos.',
    'GSE15': '15. Sou confiante de que posso lidar bem com situações inesperadas.',
    'GSE16': '16. Eu desisto das coisas antes de completá-las.',
    'GSE17': '17. Quando enfrento problemas, geralmente posso encontrar várias soluções.',
    'GSE18': '18. Dificilmente eu vou me dar bem na vida.',
    'GSE19': '19. Quando eu falho, eu tenho vontade de tentar mais.',
    'GSE20': '20. Eu me sinto inseguro com relação a minha capacidade de fazer as coisas.',
}
REVERSE = {'GSE08', 'GSE11', 'GSE13', 'GSE16', 'GSE18', 'GSE20'}

gse = df[list(GSE_COLS.values())].copy()
gse.columns = list(GSE_COLS.keys())
gse = gse.apply(pd.to_numeric, errors='coerce')
for c in REVERSE:
    gse[c] = 6 - gse[c]
gse_total = gse.sum(axis=1)
gse_mean_per_resp = gse.mean(axis=1)

# ============== GRÁFICOS ==============

# 1) EntreComp: média ± std por item
plt.figure(figsize=(9, 7))
means = ec.mean()
stds = ec.std()
y = np.arange(len(means))
plt.barh(y, means, xerr=stds, color='#3b7dd8', alpha=0.85, capsize=3)
plt.yticks(y, list(EC_COLS.keys()))
plt.gca().invert_yaxis()
plt.xlim(1, 4.2)
plt.axvline(2.5, color='gray', linestyle='--', linewidth=0.7)
plt.xlabel('Média (escala 1–4)')
plt.title('EntreComp — média por item (n=13)')
plt.tight_layout()
plt.savefig(OUT_FIG + 'entrecomp_means_por_item.png', dpi=150, bbox_inches='tight')
plt.close()

# 2) EntreComp: média por dimensão
plt.figure(figsize=(8, 5))
dim_mean = ec_dim.mean()
dim_std = ec_dim.std()
x = np.arange(len(dim_mean))
plt.bar(x, dim_mean, yerr=dim_std, color=['#1f77b4', '#ff7f0e', '#2ca02c'], capsize=5, alpha=0.85)
plt.xticks(x, list(DIMS_EC.keys()), fontsize=9)
plt.ylim(1, 4.2)
plt.axhline(2.5, color='gray', linestyle='--', linewidth=0.7)
plt.ylabel('Média (escala 1–4)')
plt.title('EntreComp — média por dimensão (n=13)')
for i, (m, s) in enumerate(zip(dim_mean, dim_std)):
    plt.text(i, m + s + 0.05, f'{m:.2f}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig(OUT_FIG + 'entrecomp_means_por_dimensao.png', dpi=150, bbox_inches='tight')
plt.close()

# 3) EntreComp: distribuição Likert empilhada
levels = [1, 2, 3, 4]
labels = ['1 Discordo Totalmente', '2 Discordo Parcialmente', '3 Concordo Parcialmente', '4 Concordo Totalmente']
colors = ['#d73027', '#fdae61', '#a6d96a', '#1a9850']
counts = pd.DataFrame({lv: (ec == lv).sum() for lv in levels}, index=ec.columns)
pcts = counts.div(counts.sum(axis=1), axis=0) * 100

plt.figure(figsize=(11, 7))
y = np.arange(len(pcts))
left = np.zeros(len(pcts))
for lv, lbl, col in zip(levels, labels, colors):
    vals = pcts[lv].values
    plt.barh(y, vals, left=left, color=col, label=lbl, edgecolor='white', linewidth=0.5)
    left += vals
plt.yticks(y, pcts.index)
plt.gca().invert_yaxis()
plt.xlabel('Percentual de respondentes (%)')
plt.title('EntreComp — distribuição Likert por item (n=13)')
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=9)
plt.xlim(0, 100)
plt.tight_layout()
plt.savefig(OUT_FIG + 'entrecomp_distribuicao_likert.png', dpi=150, bbox_inches='tight')
plt.close()

# 4) GSE: média por item (após inversão)
plt.figure(figsize=(9, 8))
means_g = gse.mean()
stds_g = gse.std()
y = np.arange(len(means_g))
labels_g = [f'{c} (R)' if c in REVERSE else c for c in gse.columns]
plt.barh(y, means_g, xerr=stds_g, color='#9467bd', alpha=0.85, capsize=3)
plt.yticks(y, labels_g)
plt.gca().invert_yaxis()
plt.xlim(1, 5.2)
plt.axvline(3, color='gray', linestyle='--', linewidth=0.7)
plt.xlabel('Média (escala 1–5; (R) = item recodificado)')
plt.title('GSE — média por item após inversão (n=13)')
plt.tight_layout()
plt.savefig(OUT_FIG + 'gse_means_por_item.png', dpi=150, bbox_inches='tight')
plt.close()

# 5) GSE: distribuição do escore total
plt.figure(figsize=(8, 5))
plt.hist(gse_total.dropna(), bins=10, range=(20, 100), color='#9467bd', edgecolor='white', alpha=0.85)
m = gse_total.mean()
plt.axvline(m, color='red', linestyle='--', linewidth=1.2, label=f'Média = {m:.1f}')
plt.xlabel('Escore total GSE (faixa teórica 20–100)')
plt.ylabel('Número de respondentes')
plt.title('GSE — distribuição do escore total (n=13)')
plt.legend()
plt.tight_layout()
plt.savefig(OUT_FIG + 'gse_total_distribuicao.png', dpi=150, bbox_inches='tight')
plt.close()

# 6) GSE: boxplot por item
plt.figure(figsize=(10, 6))
plt.boxplot([gse[c].dropna() for c in gse.columns], labels=labels_g, patch_artist=True,
            boxprops=dict(facecolor='#c5b0d5'), medianprops=dict(color='black'))
plt.xticks(rotation=60, fontsize=8)
plt.ylim(0.5, 5.5)
plt.ylabel('Resposta (1–5)')
plt.title('GSE — distribuição por item (n=13)')
plt.tight_layout()
plt.savefig(OUT_FIG + 'gse_boxplot_por_item.png', dpi=150, bbox_inches='tight')
plt.close()

# ============== CSVs DE SAÍDA ==============

# Resumo por dimensão
def stats_block(label, n_itens, series):
    return {'dimensao': label, 'n_itens': n_itens,
            'media': round(series.mean(), 3), 'desvio_padrao': round(series.std(), 3),
            'min': round(series.min(), 3), 'max': round(series.max(), 3)}

resumo = pd.DataFrame([
    stats_block(d.replace('\n', ' '), len(cols), ec[cols].mean(axis=1))
    for d, cols in DIMS_EC.items()
] + [
    stats_block('GSE — escore total (1–5 por item, agregado)', 20, gse.mean(axis=1)),
    stats_block('GSE — escore total (faixa 20–100)', 20, gse_total),
])
resumo.to_csv('./competencias_resumo_por_dimensao.csv', index=False, encoding='utf-8')

# Respostas processadas (auditoria)
audit = pd.concat([
    df[['Curso vinculado no UDF', 'curso_nome', 'Idade', 'SEXO', 'SEMESTRE',
        'Por quantos semestres você ficou vinculado ao Labtech?',
        'Você entrou no Labtech como:']].reset_index(drop=True),
    ec.reset_index(drop=True),
    gse.add_suffix('_inv').reset_index(drop=True),
    pd.DataFrame({
        'EC_dim_autoconsc': ec[DIMS_EC['Autoconsciência\ne autoeficácia\n(Ideias e Oportunidades)']].mean(axis=1).values,
        'EC_dim_mobilizacao': ec[DIMS_EC['Mobilização\nde outros\n(Recursos)']].mean(axis=1).values,
        'EC_dim_criacao': ec[DIMS_EC['Criação de valor\ncolaborativa\n(Em Ação)']].mean(axis=1).values,
        'GSE_total': gse_total.values,
        'GSE_media_item': gse_mean_per_resp.values,
    }),
], axis=1)
audit.to_csv('./competencias_respostas_processadas.csv', index=False, encoding='utf-8')

# Respostas abertas anonimizadas (R01..Rnn)
quote_col = 'Você gostaria de deixar uma ideia ou critica sobre a sua participação, teve algo que não deu certo ou que deu muito certo?'
opens = df[[quote_col, 'curso_nome', 'Curso vinculado no UDF', 'Idade', 'SEXO',
            'Por quantos semestres você ficou vinculado ao Labtech?']].copy()
opens.columns = ['texto', 'curso_nome', 'curso_sigla', 'idade', 'sexo', 'semestres_labtech']
mask_valid = opens['texto'].fillna('').str.strip().str.lower().replace(
    {'sem ideia ou crítica': '', 'top': '', 'não': '', 'não ': ''}
) != ''
opens = opens[mask_valid].reset_index(drop=True)
opens.insert(0, 'id', [f'R{i+1:02d}' for i in range(len(opens))])
opens.to_csv('./quotes_abertas.csv', index=False, encoding='utf-8')

# Frequências dos códigos-semente (Bardin: pré-análise)
SEEDS = {
    'troca_conhecimento':       r'troc(a|as)\s+de\s+conhecimen|aprend',
    'diversidade_perspectivas': r'perspectiv|diferentes\s+cursos|colegas\s+de\s+outros|diversas\s+áreas',
    'mentoria_bolsa':           r'mentor|orienta|bolsa',
    'gestao_didatica':          r'organiza|tempo|did[áa]tica',
    'autonomia_tecnica':        r'c[óo]digo|contato.*c[óo]digo|desenvolvimen|programa',
    'ciclo_desenvolvimento':    r'ciclo|imers[ãa]o|planejamento.*entreg|sistema',
    'sustentabilidade_externa': r'f[áa]brica\s+junior|empresa|sustent|renda',
}
freq = []
for code, pat in SEEDS.items():
    n = opens['texto'].fillna('').str.contains(pat, case=False, regex=True, na=False).sum()
    freq.append({'codigo': code, 'frequencia': int(n), 'pct_n9': round(100 * n / max(len(opens), 1), 1)})
pd.DataFrame(freq).sort_values('frequencia', ascending=False).to_csv(
    './codigos_frequencia.csv', index=False, encoding='utf-8'
)

# ============== FRAGMENTO LATEX ==============

tab_lines = []
tab_lines.append(r'\begin{table}[!htbp]')
tab_lines.append(r'\centering')
tab_lines.append(r'\caption{Resumo descritivo das dimensões EntreComp e GSE (n=' + str(len(df)) + r').}')
tab_lines.append(r'\label{tab:competencias-resumo}')
tab_lines.append(r'\small')
tab_lines.append(r'\begin{tabular}{lccccc}')
tab_lines.append(r'\hline')
tab_lines.append(r'\textbf{Dimensão} & \textbf{Itens} & \textbf{Média} & \textbf{Desvio} & \textbf{Mín.} & \textbf{Máx.} \\')
tab_lines.append(r'\hline')
for _, row in resumo.iterrows():
    nome = row['dimensao'].replace('&', r'\&').replace('—', '--')
    tab_lines.append(
        f"{nome} & {row['n_itens']} & {row['media']:.2f} & {row['desvio_padrao']:.2f} "
        f"& {row['min']:.2f} & {row['max']:.2f} \\\\"
    )
tab_lines.append(r'\hline')
tab_lines.append(r'\end{tabular}')
tab_lines.append(r'\end{table}')
with open('./tab_competencias.tex', 'w', encoding='utf-8') as f:
    f.write('\n'.join(tab_lines) + '\n')

# ============== RESUMO DE EXECUÇÃO ==============

print('=' * 60)
print('Análise concluída.')
print(f'Respondentes (n)                   : {len(df)}')
print(f'Respostas abertas válidas          : {len(opens)}')
print(f'Cursos representados               : {df["curso_nome"].nunique()}')
print()
print('--- EntreComp (médias por dimensão) ---')
for d, cols in DIMS_EC.items():
    s = ec[cols].mean(axis=1)
    print(f'  {d.replace(chr(10), " "):60s} média={s.mean():.2f}  σ={s.std():.2f}')
print()
print('--- GSE ---')
print(f'  Escore total: média={gse_total.mean():.1f}  σ={gse_total.std():.2f}  '
      f'(min={gse_total.min():.0f}, max={gse_total.max():.0f})')
print()
print(f'PNGs salvos em : {os.path.abspath(OUT_FIG)}')
print(f'CSVs salvos em : {os.path.abspath(".")}')
print('=' * 60)
