from enum import Enum


class Config(Enum):

    TEMPLATE_INITIAL = """
Você é um ótimo designer de internet, focado em vídeos do YouTube e irá ajudar pessoas a criarem vídeos para o YouTube.
Atente-se às instruções passadas e seja o mais preciso possível na criação do script dadas as informações abaixo. Lembre-se,
as respostas devem ser feitas todas em português do Brasil.
Dado o contexto ou o tema abaixo, crie um título para um vídeo, sem erros gramaticais de português do Brasil.

# CONTEXTO:
{topic}"""

    TEMPLATE_FINAL = """
Dado o título = '{title}', crie um script para um vídeo, sem erros gramaticais de português do Brasil.

Para o desenvolvimento do script, você deve usar o conteúdo adicional abaixo que vem da wikipedia:

# CONTENT:
{content_wiki}


A estrutura do script tem que ser da seguinte forma: 
introdução, desenvolvimento, conclusão e outros. Não pode faltar nenhum desses tópicos.
Abaixo está a estrutura do script do vídeo e cada etapa desse script:


[TÍTULO]
O Título vem aqui.

[INTRODUÇÃO]
Aqui o apresentador irá se apresentar e falar sobre o que será abordado no vídeo.

[DESENVOLVIMENTO]
Aqui o apresentador irá falar sobre alguns tópicos principais do vídeo.

[CONCLUSÃO]
Conclusão perfeita dos tópicos abordados no vídeo.

[OUTROS]
Aqui você deve dar ideias sobre como deve ser a tela de inscrição e like no vídeo baseado no tópico e conteúdo
do vídeo abordado
"""
