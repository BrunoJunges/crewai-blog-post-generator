# Projeto Multiagente com CrewAI: Gerador de Post de Blog

Este projeto cumpre a atividade prática de construir um sistema multiagente com a biblioteca CrewAI.

## Objetivo

O sistema consiste em uma equipe (crew) de 3 agentes de IA que colaboram para criar um post de blog otimizado para SEO sobre um tópico específico.

### Agentes

1.  **Especialista em Pesquisa de SEO:** Responsável por analisar o tópico e gerar palavras-chave e subtítulos relevantes.
2.  **Redator de Conteúdo:** Escreve o post do blog com base nos dados do pesquisador.
3.  **Editor Chefe:** Revisa e formata o texto final para garantir qualidade e legibilidade.

## Como Executar

1.  **Clone o repositório.**

2.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a Chave de API:**
    *   Crie um arquivo chamado `.env` na raiz do projeto.
    *   Dentro dele, adicione sua chave de API da OpenAI:
        ```
        OPENAI_API_KEY="sk-SUA_CHAVE_AQUI"
        ```
    *   **Nota Importante:** A execução do código requer créditos na plataforma da OpenAI. Se a conta não tiver saldo ou um método de pagamento configurado, a execução falhará com um erro de "quota insuficiente" (RateLimitError 429).

5.  **Execute o programa:**
    ```bash
    python main.py
    ```
