# main.py

# Carrega a chave de API do arquivo .env
from dotenv import load_dotenv
load_dotenv()

# Não precisamos mais importar o LLM, o CrewAI fará isso por nós!
from crewai import Agent, Task, Crew, Process

# --------------------------------------------------------------------------------
# DEFINIÇÃO DOS AGENTES
# --------------------------------------------------------------------------------
# Não precisamos mais passar o `llm` para cada agente.
# Eles automaticamente usarão o padrão (OpenAI) que está no nosso ambiente.

seo_researcher = Agent(
  role='Especialista em Pesquisa de SEO',
  goal='Analisar o tópico {topic} e fornecer um relatório com palavras-chave e subtítulos.',
  backstory='Um analista de SEO experiente focado em dados para estratégia de conteúdo.',
  verbose=True,
  allow_delegation=False
)

content_writer = Agent(
  role='Redator de Conteúdo',
  goal='Escrever um post de blog envolvente sobre {topic} baseado na pesquisa.',
  backstory='Um redator criativo que transforma insights em narrativas cativantes.',
  verbose=True,
  allow_delegation=False
)

content_reviewer = Agent(
  role='Editor Chefe',
  goal='Revisar e formatar o post do blog para garantir a máxima qualidade.',
  backstory='Um editor meticuloso que garante que todo conteúdo seja impecável.',
  verbose=True,
  allow_delegation=False
)

# --------------------------------------------------------------------------------
# DEFINIÇÃO DAS TAREFAS
# --------------------------------------------------------------------------------
research_task = Task(
  description="Analisar o tópico '{topic}' e compilar um relatório com 10 palavras-chave de cauda longa e 5 subtítulos.",
  expected_output='Um relatório formatado contendo uma lista de 10 palavras-chave e 5 subtítulos.',
  agent=seo_researcher
)

writing_task = Task(
  description="Usando o relatório de pesquisa, escrever um post de blog detalhado sobre {topic}.",
  expected_output='O texto completo do post do blog em formato Markdown.',
  agent=content_writer,
  context=[research_task]
)

review_task = Task(
  description="Revisar o rascunho do post, corrigindo erros e melhorando a formatação para publicação.",
  expected_output='O post final e polido em formato Markdown.',
  agent=content_reviewer,
  context=[writing_task],
  output_file='blog_post_final.md'
)

# --------------------------------------------------------------------------------
# MONTAGEM E EXECUÇÃO DA CREW
# --------------------------------------------------------------------------------
# Não precisamos mais passar o `llm` para a Crew. Ela também usará o padrão.
blog_crew = Crew(
  agents=[seo_researcher, content_writer, content_reviewer],
  tasks=[research_task, writing_task, review_task],
  process=Process.sequential,
  verbose=True
)

# --- EXECUÇÃO ---
print("## Iniciando a Geração do Post de Blog com OpenAI...")
result = blog_crew.kickoff(inputs={'topic': 'O Futuro da Inteligência Artificial em Carros Autônomos'})

print("\n\n##################################################")
print("## Post do Blog Gerado com Sucesso!               ##")
print("##################################################\n")
print(f"O resultado foi salvo no arquivo 'blog_post_final.md'\n\nConteúdo Final:\n{result}")