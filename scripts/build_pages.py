# -*- coding: utf-8 -*-
import os
import re
import sys

# Ensure scripts folder in path
sys.path.append(os.path.dirname(__file__))
from update_autores_cards import authors_data

def save_file(rel_path, content):
    parent = os.path.dirname(rel_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'Wrote: {rel_path}')

# =========================================================================
# 1. 404 PAGE (src/404.html)
# =========================================================================
def generate_404():
    content = """<!DOCTYPE html>
<html class="scroll-smooth" lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>404 - Página Não Encontrada | ELOOO International Group</title>
    <meta name="description" content="A página que você procura não está disponível no ecossistema ELOOO International Group.">
    <meta property="og:title" content="404 - Página Não Encontrada | ELOOO International Group">
    <meta property="og:description" content="A editora de elite de maior impacto no mercado internacional.">
    <meta property="og:image" content="static/images/og-share.png">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        display: ['Space Grotesk', 'sans-serif'],
                    },
                    colors: {
                        stone: {
                            850: '#211f1d',
                            900: '#1c1917',
                            950: '#0c0a09',
                        }
                    },
                    backgroundImage: {
                        'noise': "url(\\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\\")",
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #0c0a09;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        .gold-text-sweep {
            background: linear-gradient(90deg, #d6bc8c 0%, #f6e3c5 25%, #d6bc8c 50%, #f6e3c5 75%, #d6bc8c 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: goldSweep 6s linear infinite;
        }
        @keyframes goldSweep {
            0% { background-position: 0% center; }
            100% { background-position: -200% center; }
        }
        .ambient-glow {
            position: absolute;
            width: 500px;
            height: 500px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(214,188,140,0.12) 0%, transparent 70%);
            top: 25%;
            left: 50%;
            transform: translate(-50%, -50%);
            pointer-events: none;
            z-index: 0;
        }
    </style>
</head>
<body class="relative min-h-screen flex flex-col justify-between">
    <div class="fixed inset-0 w-full h-full bg-noise opacity-[0.02] pointer-events-none z-50"></div>
    <div class="ambient-glow"></div>

    <!-- INCLUDE_NAVBAR -->

    <main class="relative z-10 flex-grow flex items-center justify-center pt-36 pb-24 px-6">
        <div class="max-w-3xl mx-auto text-center">
            
            <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-stone-900/80 border border-stone-800 text-[#d6bc8c] text-[10px] font-mono uppercase tracking-[0.25em] mb-6">
                <iconify-icon icon="solar:compass-bold-duotone" class="text-sm"></iconify-icon>
                <span>Erro 404 · Rota Desconhecida</span>
            </div>

            <h1 class="font-display text-7xl sm:text-9xl font-bold tracking-tighter text-stone-850 select-none mb-2 relative">
                <span class="gold-text-sweep">404</span>
            </h1>

            <h2 class="font-display text-2xl sm:text-3xl font-semibold text-white tracking-tight mb-4 uppercase">
                Página Não Encontrada no Ecossistema
            </h2>

            <p class="text-stone-400 text-sm sm:text-base font-light max-w-xl mx-auto leading-relaxed mb-10">
                O endereço que você tentou acessar foi movido, renomeado ou não faz parte de nossas publicações ativas. Explore nossos principais diretórios abaixo:
            </p>

            <!-- Action buttons -->
            <div class="flex flex-wrap items-center justify-center gap-4">
                <a href="index.html" class="relative group rounded-full p-[1.5px] overflow-hidden hover:scale-[1.02] active:scale-[0.98] transition-all duration-300">
                    <span class="absolute inset-[-1000%] animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,rgba(214,188,140,0.8)_50%,transparent_100%)] opacity-80 group-hover:opacity-100 transition-opacity"></span>
                    <span class="relative flex items-center justify-center gap-2.5 h-full w-full bg-[#0c0a09] px-7 py-3.5 rounded-full transition-colors group-hover:bg-[#151311]">
                        <iconify-icon icon="solar:home-2-linear" class="text-[#d6bc8c] text-base"></iconify-icon>
                        <span class="font-medium text-xs text-white tracking-widest uppercase">Voltar ao Início</span>
                    </span>
                </a>

                <a href="autores.html" class="px-6 py-3.5 rounded-full bg-stone-900/60 hover:bg-stone-850 border border-stone-800 hover:border-[#d6bc8c]/40 text-stone-300 hover:text-white text-xs font-medium uppercase tracking-widest transition-all duration-300 flex items-center gap-2">
                    <iconify-icon icon="solar:users-group-rounded-linear" class="text-stone-400 text-sm"></iconify-icon>
                    <span>Ver Autores</span>
                </a>

                <a href="livros.html" class="px-6 py-3.5 rounded-full bg-stone-900/60 hover:bg-stone-850 border border-stone-800 hover:border-[#d6bc8c]/40 text-stone-300 hover:text-white text-xs font-medium uppercase tracking-widest transition-all duration-300 flex items-center gap-2">
                    <iconify-icon icon="solar:book-2-linear" class="text-stone-400 text-sm"></iconify-icon>
                    <span>Catálogo de Livros</span>
                </a>

                <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20vim%20do%20site%20da%20Elooo%20e%20quero%20saber%20como%20publicar%20o%20meu%20livro." target="_blank" rel="noopener noreferrer" class="px-6 py-3.5 rounded-full bg-[#25D366]/10 hover:bg-[#25D366]/20 border border-[#25D366]/30 text-[#25D366] text-xs font-medium uppercase tracking-widest transition-all duration-300 flex items-center gap-2">
                    <iconify-icon icon="ic:baseline-whatsapp" class="text-sm"></iconify-icon>
                    <span>Falar no WhatsApp</span>
                </a>
            </div>

        </div>
    </main>

    <!-- INCLUDE_FOOTER -->
</body>
</html>"""
    save_file('src/404.html', content)

# =========================================================================
# 2. FAQ PAGE (src/faq.html)
# =========================================================================
def generate_faq():
    faq_items = [
        {
            "cat": "editorial",
            "q": "Quanto tempo dura o processo de publicação de um livro na ELOOO?",
            "a": "O ciclo completo de produção editorial — desde a validação do conceito e estruturação do sumário até a diagramação de luxo, revisão ortográfica e impressão premium — leva em média de 60 a 90 dias. Cada fase é acompanhada em tempo real pelo autor através do nosso sistema proprietário SEAAS."
        },
        {
            "cat": "editorial",
            "q": "Preciso ter o manuscrito já escrito para iniciar o projeto?",
            "a": "Não. Mais de 70% dos nossos autores de elite iniciam com suas ideias, mentorias e experiências práticas. Nossa equipe editorial e o método exclusivo 'Da Ideia ao Manuscrito' conduzem você por sessões de alinhamento, estrutura capitular e redação assistida para materializar sua obra com máxima sofisticação."
        },
        {
            "cat": "distribuicao",
            "q": "Como funciona a distribuição internacional de livros?",
            "a": "A ELOOO International Group opera com sede matriz no Brasil (Joinville/SC) e polos parceiros de distribuição na Europa (Cascais/Portugal e Madrid/Espanha). Nossos livros contam com tiragens impressas de luxo, distribuição direta para eventos, feiras e pontos estratégicos, além de entrega digital global integrada."
        },
        {
            "cat": "distribuicao",
            "q": "Quais são as opções de formatos disponibilizados para os leitores?",
            "a": "Além do exemplar físico capa dura de colecionador, a ELOOO disponibiliza a Plataforma Multientrega do Leitor, que entrega a obra em múltiplos formatos complementares: Livro Versão Digital/PDF diagramado, Resumos executivos, Tarefas práticas de implementação (MAPs), Mapas Mentais (MindMaps), Áudios e Aulas em vídeo com acesso imediato."
        },
        {
            "cat": "modalidades",
            "q": "Qual a diferença entre publicação individual, coautoria e institucional?",
            "a": "O Livro Individual é uma obra solo voltada à consolidação definitiva da sua autoridade pessoal e metodologia própria. A Coautoria reúne especialistas selecionados em capítulos complementares sob um tema de alto impacto. Já a edição Institucional/Corporativa documenta a trajetória, cultura e conquistas de grandes empresas e organizações."
        },
        {
            "cat": "tecnologia",
            "q": "O que é o SEAAS (Sistema Empresarial Autônomo-Assistido)?",
            "a": "O SEAAS é a tecnologia exclusiva desenvolvida pela ELOOO para gerenciar o ecossistema autoral. Ele reúne o pipeline de projetos em tempo real, ranking da elite autoral com gamificação, portal de membros com transações em Moeda ELOOO, e a universidade corporativa para capacitação de autores."
        },
        {
            "cat": "comunidade",
            "q": "O que é o ELOOO Club e como funciona a Moeda ELOOO?",
            "a": "O ELOOO Club é uma comunidade fechada de alto nível para os autores da editora. Nele, os membros trocam serviços, realizam networking de negócios, participam de conselhos consultivos privados e utilizam a Moeda ELOOO para transações de permuta rastreável dentro da rede."
        },
        {
            "cat": "direitos",
            "q": "Quem mantém a propriedade intelectual e direitos autorais do livro?",
            "a": "O autor mantém 100% dos direitos autorais e patrimoniais da sua criação intelectual. A ELOOO atua como editora parceira na produção, chancela institucional, registro de ISBN/Ficha Catalográfica e distribuição."
        },
        {
            "cat": "atendimento",
            "q": "Como faço para submeter meu projeto ou agendar uma reunião?",
            "a": "Você pode preencher nosso formulário na página de Contato ou falar diretamente com o nosso Concierge Executivo via WhatsApp pelo número +55 (47) 98866-0791. Nosso comitê editorial realiza a análise prévia do seu perfil em até 48 horas úteis."
        }
    ]

    faq_accordion_html = ""
    for i, item in enumerate(faq_items):
        faq_accordion_html += f"""
                <!-- FAQ Item {i+1} -->
                <div class="faq-card glass-card p-6 md:p-8 cursor-pointer group" data-category="{item['cat']}" onclick="toggleFaq({i})">
                    <div class="flex items-start justify-between gap-4">
                        <div class="flex items-start gap-4">
                            <span class="text-[#d6bc8c] font-mono text-xs mt-1 shrink-0">0{i+1 if i < 9 else i+1}</span>
                            <h3 class="font-display text-base md:text-lg font-medium text-white group-hover:text-[#d6bc8c] transition-colors leading-snug">
                                {item['q']}
                            </h3>
                        </div>
                        <div class="w-8 h-8 rounded-full border border-stone-800 flex items-center justify-center shrink-0 text-stone-400 group-hover:text-white group-hover:border-[#d6bc8c]/40 transition-all">
                            <iconify-icon id="faq-icon-{i}" icon="solar:alt-arrow-down-linear" class="text-base transition-transform duration-300"></iconify-icon>
                        </div>
                    </div>
                    <div id="faq-ans-{i}" class="hidden pt-4 mt-4 border-t border-stone-800/60 pl-8">
                        <p class="text-stone-300 text-xs md:text-sm font-light leading-relaxed">
                            {item['a']}
                        </p>
                    </div>
                </div>"""

    content = f"""<!DOCTYPE html>
<html class="scroll-smooth" lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>FAQ - Perguntas Frequentes | ELOOO International Group</title>
    <meta name="description" content="Tire suas dúvidas sobre o processo editorial, distribuição internacional, direitos autorais e tecnologia SEAAS da ELOOO Editora.">
    <meta property="og:title" content="FAQ - Perguntas Frequentes | ELOOO International Group">
    <meta property="og:description" content="Tire todas as suas dúvidas sobre publicação, mentoria e distribuição na ELOOO.">
    <meta property="og:image" content="static/images/og-share.png">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        display: ['Space Grotesk', 'sans-serif'],
                    }},
                    colors: {{
                        stone: {{
                            850: '#211f1d',
                            900: '#1c1917',
                            950: '#0c0a09',
                        }}
                    }},
                    backgroundImage: {{
                        'noise': "url(\\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\\")",
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            background-color: #0c0a09;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }}
        .gold-text-sweep {{
            background: linear-gradient(90deg, #d6bc8c 0%, #f6e3c5 25%, #d6bc8c 50%, #f6e3c5 75%, #d6bc8c 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: goldSweep 6s linear infinite;
        }}
        @keyframes goldSweep {{
            0% {{ background-position: 0% center; }}
            100% {{ background-position: -200% center; }}
        }}
        .glass-card {{
            background: rgba(28, 25, 23, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(16px);
            border-radius: 20px;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .glass-card:hover {{
            border-color: rgba(214, 188, 140, 0.3);
            background: rgba(28, 25, 23, 0.7);
        }}
    </style>
</head>
<body class="relative min-h-screen flex flex-col justify-between">
    <div class="fixed inset-0 w-full h-full bg-noise opacity-[0.02] pointer-events-none z-50"></div>

    <!-- INCLUDE_NAVBAR -->

    <main class="relative z-10 flex-grow pt-36 pb-24 px-6 md:px-24">
        <div class="max-w-[1100px] mx-auto">
            
            <!-- Page Header -->
            <div class="text-center mb-16">
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-stone-900/80 border border-stone-800 text-[#d6bc8c] text-[10px] font-mono uppercase tracking-[0.25em] mb-4">
                    <iconify-icon icon="solar:question-circle-linear" class="text-sm"></iconify-icon>
                    <span>Central de Respostas</span>
                </div>
                <h1 class="font-display text-3xl sm:text-5xl font-medium tracking-tight text-white uppercase mb-4">
                    Perguntas <span class="gold-text-sweep font-semibold">Frequentes</span>
                </h1>
                <p class="text-stone-400 text-xs sm:text-sm font-light max-w-2xl mx-auto leading-relaxed">
                    Tudo o que você precisa saber sobre a publicação, metodologia, direitos autorais, distribuição internacional e o ecossistema ELOOO.
                </p>
                
                <!-- Live Search Bar -->
                <div class="max-w-xl mx-auto mt-8 relative">
                    <input type="text" id="faqSearch" placeholder="Digite uma palavra-chave (ex: distribuição, prazos, royalties, SEAAS)..." class="w-full bg-stone-900/70 border border-stone-800 focus:border-[#d6bc8c]/50 rounded-full py-3.5 pl-12 pr-6 text-xs text-white placeholder-stone-500 outline-none transition-all" oninput="filterFaq()">
                    <iconify-icon icon="solar:magnifer-linear" class="absolute left-4 top-1/2 -translate-y-1/2 text-stone-500 text-lg"></iconify-icon>
                </div>
            </div>

            <!-- FAQ List -->
            <div class="space-y-4" id="faqList">
                {faq_accordion_html}
            </div>

            <!-- Still have questions banner -->
            <div class="mt-16 p-8 rounded-3xl bg-gradient-to-r from-stone-900/80 via-stone-850/60 to-stone-900/80 border border-[#d6bc8c]/25 text-center flex flex-col items-center justify-center">
                <h3 class="font-display text-xl font-medium text-white mb-2">Ainda tem dúvidas específicas sobre a sua obra?</h3>
                <p class="text-stone-400 text-xs max-w-lg mb-6 leading-relaxed">Nossa equipe de especialistas editoriais está à disposição para analisar seu projeto e orientar a melhor trilha de publicação.</p>
                <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20vim%20do%20site%20da%20Elooo%20e%20quero%20saber%20como%20publicar%20o%20meu%20livro." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2.5 px-8 py-3.5 rounded-full bg-[#25D366] hover:bg-[#20ba5a] text-white text-xs font-semibold uppercase tracking-widest transition-all shadow-lg hover:shadow-[#25D366]/20">
                    <iconify-icon icon="ic:baseline-whatsapp" class="text-lg"></iconify-icon>
                    <span>Falar com o Concierge no WhatsApp</span>
                </a>
            </div>

        </div>
    </main>

    <!-- INCLUDE_FOOTER -->

    <script>
        function toggleFaq(index) {{
            const ans = document.getElementById('faq-ans-' + index);
            const icon = document.getElementById('faq-icon-' + index);
            if (!ans || !icon) return;

            const isHidden = ans.classList.contains('hidden');
            if (isHidden) {{
                ans.classList.remove('hidden');
                icon.style.transform = 'rotate(180deg)';
            }} else {{
                ans.classList.add('hidden');
                icon.style.transform = 'rotate(0deg)';
            }}
        }}

        function filterFaq() {{
            const query = document.getElementById('faqSearch').value.toLowerCase();
            const cards = document.querySelectorAll('.faq-card');
            cards.forEach(card => {{
                const text = card.innerText.toLowerCase();
                if (text.includes(query)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>"""
    save_file('src/faq.html', content)

# =========================================================================
# 3. PRIVACY POLICY (src/privacidade.html)
# =========================================================================
def generate_privacidade():
    content = """<!DOCTYPE html>
<html class="scroll-smooth" lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>Política de Privacidade | ELOOO International Group</title>
    <meta name="description" content="Conheça a Política de Privacidade da ELOOO International Group, em plena conformidade com a LGPD (Brasil) e GDPR (União Europeia).">
    <meta property="og:title" content="Política de Privacidade | ELOOO International Group">
    <meta property="og:description" content="Compromisso de proteção de dados e privacidade em conformidade com LGPD e GDPR.">
    <meta property="og:image" content="static/images/og-share.png">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        display: ['Space Grotesk', 'sans-serif'],
                    },
                    colors: {
                        stone: {
                            850: '#211f1d',
                            900: '#1c1917',
                            950: '#0c0a09',
                        }
                    },
                    backgroundImage: {
                        'noise': "url(\\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\\")",
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #0c0a09;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        .gold-text-sweep {
            background: linear-gradient(90deg, #d6bc8c 0%, #f6e3c5 25%, #d6bc8c 50%, #f6e3c5 75%, #d6bc8c 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: goldSweep 6s linear infinite;
        }
        @keyframes goldSweep {
            0% { background-position: 0% center; }
            100% { background-position: -200% center; }
        }
    </style>
</head>
<body class="relative min-h-screen flex flex-col justify-between">
    <div class="fixed inset-0 w-full h-full bg-noise opacity-[0.02] pointer-events-none z-50"></div>

    <!-- INCLUDE_NAVBAR -->

    <main class="relative z-10 flex-grow pt-36 pb-24 px-6 md:px-24">
        <div class="max-w-4xl mx-auto">
            
            <!-- Header -->
            <div class="mb-12 border-b border-stone-800/80 pb-8">
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-stone-900/80 border border-stone-800 text-[#d6bc8c] text-[10px] font-mono uppercase tracking-[0.25em] mb-4">
                    <iconify-icon icon="solar:shield-check-bold-duotone" class="text-sm"></iconify-icon>
                    <span>Segurança & Governança de Dados</span>
                </div>
                <h1 class="font-display text-3xl sm:text-5xl font-medium tracking-tight text-white uppercase mb-3">
                    Política de <span class="gold-text-sweep font-semibold">Privacidade</span>
                </h1>
                <p class="text-stone-500 text-xs font-mono tracking-wider">Última atualização: Agosto de 2026 · Conformidade LGPD (BR) e GDPR (UE)</p>
            </div>

            <!-- Content Body -->
            <div class="space-y-8 text-stone-300 text-xs md:text-sm font-light leading-relaxed">
                
                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">01.</span> Introdução e Princípios
                    </h2>
                    <p>A <strong>ELOOO International Group</strong> (com sede matriz em Joinville/SC, Brasil, e representações parceiras em Cascais/Portugal e Madrid/Espanha) valoriza a confidencialidade e a segurança dos dados pessoais de seus autores, clientes, leitores e visitantes. Esta Política de Privacidade estabelece como coletamos, utilizamos, armazenamos e protegemos suas informações, respeitando integralmente a <strong>Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018 - LGPD)</strong> e o <strong>Regulamento Geral sobre a Proteção de Dados (Regulamento UE 2016/679 - GDPR)</strong>.</p>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">02.</span> Dados Pessoais Coletados
                    </h2>
                    <p class="mb-2">Coletamos apenas os dados estritamente necessários para a prestação dos nossos serviços editoriais de alta performance:</p>
                    <ul class="list-disc list-inside space-y-1.5 text-stone-400 pl-2">
                        <li><strong>Dados de Identificação:</strong> Nome completo, e-mail corporativo, número de telefone/WhatsApp, profissão, empresa e biografia executiva.</li>
                        <li><strong>Dados de Projetos e Originais:</strong> Sinopses, rascunhos, manuscritos, sumários e arquivos submetidos para avaliação do comitê editorial.</li>
                        <li><strong>Dados de Navegação:</strong> Endereço IP, tipo de navegador, páginas acessadas e dados anônimos de interação recolhidos via cookies de desempenho.</li>
                    </ul>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">03.</span> Finalidade e Bases Legais do Tratamento
                    </h2>
                    <p class="mb-2">Seus dados são tratados com base nas seguintes hipóteses legais:</p>
                    <ul class="list-disc list-inside space-y-1.5 text-stone-400 pl-2">
                        <li><strong>Execução de Contrato:</strong> Para produzir, diagramar, registrar ISBN, imprimir e distribuir obras literárias sob demanda.</li>
                        <li><strong>Consentimento:</strong> Para envio de comunicados institucionais, convites para encontros da Elite Autoral e novidades de catálogo.</li>
                        <li><strong>Legítimo Interesse:</strong> Para aprimoramento contínuo das funcionalidades do sistema proprietário SEAAS e segurança cibernética da plataforma.</li>
                    </ul>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">04.</span> Transferência Internacional de Dados
                    </h2>
                    <p>Devido à nossa operação transfronteiriça entre o Brasil e a Europa (Portugal e Espanha), seus dados podem ser processados em servidores seguros localizados em múltiplos territórios. Adotamos cláusulas contratuais padrão e padrões rigorosos de criptografia ponta a ponta (AES-256 e TLS 1.3) para garantir que o nível de proteção exigido pela LGPD e GDPR seja mantido em todas as jurisdições.</p>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">05.</span> Direitos do Titular
                    </h2>
                    <p class="mb-2">Você tem o direito de solicitar a qualquer momento:</p>
                    <ul class="list-disc list-inside space-y-1.5 text-stone-400 pl-2">
                        <li>Confirmação da existência de tratamento e acesso aos dados.</li>
                        <li>Correção de dados incompletos, inexatos ou desatualizados.</li>
                        <li>Anonimização, bloqueio ou eliminação de dados desnecessários.</li>
                        <li>Portabilidade dos dados a outro fornecedor de serviço editorial.</li>
                        <li>Revogação do consentimento previamente concedido.</li>
                    </ul>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">06.</span> Canal do Encarregado de Dados (DPO)
                    </h2>
                    <p>Para exercer quaisquer dos seus direitos ou esclarecer dúvidas sobre a privacidade dos seus dados, entre em contato diretamente com o nosso Encarregado pelo Tratamento de Dados Pessoais (DPO):</p>
                    <div class="mt-4 p-4 rounded-xl bg-stone-950/70 border border-stone-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                        <div>
                            <p class="font-mono text-xs text-white font-medium">Encarregado DPO · ELOOO International Group</p>
                            <p class="text-stone-400 text-xs mt-0.5">E-mail: <a href="mailto:privacidade@elooo.com" class="text-[#d6bc8c] hover:underline">privacidade@elooo.com</a></p>
                        </div>
                        <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20gostaria%20de%20falar%20sobre%20privacidade%20e%20prote%C3%A7%C3%A3o%20de%20dados." target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-full bg-stone-900 hover:bg-stone-800 border border-[#d6bc8c]/40 text-[#d6bc8c] text-[11px] font-mono uppercase tracking-wider transition-colors">
                            Atendimento DPO
                        </a>
                    </div>
                </section>

            </div>

        </div>
    </main>

    <!-- INCLUDE_FOOTER -->
</body>
</html>"""
    save_file('src/privacidade.html', content)

# =========================================================================
# 4. TERMS OF USE (src/termos.html)
# =========================================================================
def generate_termos():
    content = """<!DOCTYPE html>
<html class="scroll-smooth" lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>Termos de Uso | ELOOO International Group</title>
    <meta name="description" content="Termos de Uso e Condições Gerais da ELOOO International Group para autores, clientes e usuários da plataforma.">
    <meta property="og:title" content="Termos de Uso | ELOOO International Group">
    <meta property="og:description" content="Condições gerais e diretrizes de propriedade intelectual da ELOOO.">
    <meta property="og:image" content="static/images/og-share.png">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        display: ['Space Grotesk', 'sans-serif'],
                    },
                    colors: {
                        stone: {
                            850: '#211f1d',
                            900: '#1c1917',
                            950: '#0c0a09',
                        }
                    },
                    backgroundImage: {
                        'noise': "url(\\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\\")",
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #0c0a09;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        .gold-text-sweep {
            background: linear-gradient(90deg, #d6bc8c 0%, #f6e3c5 25%, #d6bc8c 50%, #f6e3c5 75%, #d6bc8c 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: goldSweep 6s linear infinite;
        }
        @keyframes goldSweep {
            0% { background-position: 0% center; }
            100% { background-position: -200% center; }
        }
    </style>
</head>
<body class="relative min-h-screen flex flex-col justify-between">
    <div class="fixed inset-0 w-full h-full bg-noise opacity-[0.02] pointer-events-none z-50"></div>

    <!-- INCLUDE_NAVBAR -->

    <main class="relative z-10 flex-grow pt-36 pb-24 px-6 md:px-24">
        <div class="max-w-4xl mx-auto">
            
            <!-- Header -->
            <div class="mb-12 border-b border-stone-800/80 pb-8">
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-stone-900/80 border border-stone-800 text-[#d6bc8c] text-[10px] font-mono uppercase tracking-[0.25em] mb-4">
                    <iconify-icon icon="solar:document-text-bold-duotone" class="text-sm"></iconify-icon>
                    <span>Regulamento Institucional</span>
                </div>
                <h1 class="font-display text-3xl sm:text-5xl font-medium tracking-tight text-white uppercase mb-3">
                    Termos de <span class="gold-text-sweep font-semibold">Uso</span>
                </h1>
                <p class="text-stone-500 text-xs font-mono tracking-wider">Vigência: 2026 · ELOOO International Group</p>
            </div>

            <!-- Content Body -->
            <div class="space-y-8 text-stone-300 text-xs md:text-sm font-light leading-relaxed">
                
                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">01.</span> Aceitação dos Termos
                    </h2>
                    <p>Ao navegar pelo site, solicitar serviços editoriais ou acessar o ecossistema digital da <strong>ELOOO International Group</strong>, o usuário declara concordar integralmente com estes Termos de Uso. Caso não concorde com qualquer disposição aqui expressa, solicitamos a interrupção imediata da utilização dos nossos serviços e plataformas.</p>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">02.</span> Propriedade Intelectual e Direitos das Obras
                    </h2>
                    <p class="mb-2">A integridade dos direitos autorais é um dos pilares inegociáveis da ELOOO:</p>
                    <ul class="list-disc list-inside space-y-1.5 text-stone-400 pl-2">
                        <li><strong>Obras dos Autores:</strong> O autor contratante preserva a totalidade dos direitos autorais patrimoniais e morais de seu conteúdo intelectual original, nos termos da Lei de Direitos Autorais (Lei nº 9.610/1998) e Convenções Internacionais de Berna.</li>
                        <li><strong>Marcas e Ativos ELOOO:</strong> O logotipo, o método ATL System, a identidade visual do SEAAS, materiais de treinamento, layouts e códigos do ecossistema são de propriedade exclusiva da ELOOO International Group, sendo estritamente proibida sua reprodução sem anuência prévia e expressa.</li>
                    </ul>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">03.</span> Submissão e Avaliação de Originais
                    </h2>
                    <p>O envio de propostas, sinopses ou originais através dos canais de contato da editora implica na autorização para que o nosso comitê editorial examine o material exclusivamente para fins de avaliação de viabilidade editorial e enquadramento nas trilhas de publicação. A ELOOO compromete-se a manter total sigilo sobre o material recebido.</p>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">04.</span> Uso do Sistema SEAAS e Plataforma do Leitor
                    </h2>
                    <p>O acesso ao SEAAS (Sistema Empresarial Autônomo-Assistido), à Plataforma Multientrega do Leitor e à Universidade Corporativa é restrito a autores e leitores devidamente credenciados. É vedado o compartilhamento de credenciais de acesso, cópia não autorizada de módulos ou qualquer tentativa de engenharia reversa das ferramentas proprietárias.</p>
                </section>

                <section class="p-6 rounded-2xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-base md:text-lg font-semibold text-white mb-3 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">05.</span> Legislação Aplicável e Foro
                    </h2>
                    <p>Estes Termos são regidos e interpretados pelas leis da República Federativa do Brasil. Para dirimir eventuais controvérsias decorrentes deste instrumento, fica eleito o Foro da Comarca de <strong>Joinville / Santa Catarina</strong>, com renúncia a qualquer outro, por mais privilegiado que seja, observadas as disposições subsidiárias para relações contratuais celebradas na União Europeia (Portugal e Espanha).</p>
                </section>

            </div>

        </div>
    </main>

    <!-- INCLUDE_FOOTER -->
</body>
</html>"""
    save_file('src/termos.html', content)

# =========================================================================
# 5. VISUAL SITEMAP PAGE (src/mapa-do-site.html)
# =========================================================================
def generate_mapa_do_site():
    # Build authors link list
    authors_links = ""
    for a in authors_data:
        authors_links += f"""
                        <li>
                            <a href="autores/{a['slug']}.html" class="text-stone-400 hover:text-[#d6bc8c] transition-colors flex items-center justify-between text-xs py-1 group">
                                <span class="group-hover:translate-x-1 transition-transform">{a['name']}</span>
                                <span class="text-[10px] font-mono text-stone-600 group-hover:text-stone-400">{a['book']}</span>
                            </a>
                        </li>"""

    content = f"""<!DOCTYPE html>
<html class="scroll-smooth" lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>Mapa do Site | ELOOO International Group</title>
    <meta name="description" content="Índice completo de navegação e páginas do ecossistema editorial ELOOO International Group.">
    <meta property="og:title" content="Mapa do Site | ELOOO International Group">
    <meta property="og:description" content="Acesse todas as páginas, perfis dos 31 autores e catálogo completo da ELOOO.">
    <meta property="og:image" content="static/images/og-share.png">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        display: ['Space Grotesk', 'sans-serif'],
                    }},
                    colors: {{
                        stone: {{
                            850: '#211f1d',
                            900: '#1c1917',
                            950: '#0c0a09',
                        }}
                    }},
                    backgroundImage: {{
                        'noise': "url(\\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\\")",
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            background-color: #0c0a09;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }}
        .gold-text-sweep {{
            background: linear-gradient(90deg, #d6bc8c 0%, #f6e3c5 25%, #d6bc8c 50%, #f6e3c5 75%, #d6bc8c 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: goldSweep 6s linear infinite;
        }}
        @keyframes goldSweep {{
            0% {{ background-position: 0% center; }}
            100% {{ background-position: -200% center; }}
        }}
        .glass-panel {{
            background: rgba(28, 25, 23, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(16px);
            border-radius: 24px;
            padding: 28px;
            transition: all 0.4s ease;
        }}
        .glass-panel:hover {{
            border-color: rgba(214, 188, 140, 0.3);
            background: rgba(28, 25, 23, 0.65);
        }}
    </style>
</head>
<body class="relative min-h-screen flex flex-col justify-between">
    <div class="fixed inset-0 w-full h-full bg-noise opacity-[0.02] pointer-events-none z-50"></div>

    <!-- INCLUDE_NAVBAR -->

    <main class="relative z-10 flex-grow pt-36 pb-24 px-6 md:px-24">
        <div class="max-w-[1280px] mx-auto">
            
            <!-- Page Header -->
            <div class="text-center mb-16">
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-stone-900/80 border border-stone-800 text-[#d6bc8c] text-[10px] font-mono uppercase tracking-[0.25em] mb-4">
                    <iconify-icon icon="solar:sitemap-bold-duotone" class="text-sm"></iconify-icon>
                    <span>Índice Estruturado</span>
                </div>
                <h1 class="font-display text-3xl sm:text-5xl font-medium tracking-tight text-white uppercase mb-4">
                    Mapa do <span class="gold-text-sweep font-semibold">Site</span>
                </h1>
                <p class="text-stone-400 text-xs sm:text-sm font-light max-w-2xl mx-auto leading-relaxed">
                    Diretório integral de páginas, perfis dos 31 autores, livros publicados, metodologias e centrais institucionais.
                </p>
            </div>

            <!-- Grid of Sections -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Col 1: Institucional & Metodologia -->
                <div class="space-y-8">
                    <div class="glass-panel">
                        <div class="flex items-center gap-3 mb-5 border-b border-stone-800 pb-3">
                            <div class="w-1 h-5 rounded-full bg-[#d6bc8c]"></div>
                            <h2 class="font-display text-base font-semibold text-white tracking-wide uppercase">Institucional</h2>
                        </div>
                        <ul class="space-y-2.5">
                            <li><a href="index.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Página Inicial (Home)</a></li>
                            <li><a href="quem-somos.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Quem Somos & Trajetória</a></li>
                            <li><a href="trilhas.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Trilhas Editoriais & Métodos</a></li>
                            <li><a href="galeria.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Galeria de Lançamentos</a></li>
                            <li><a href="contato.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Contato & Concierge</a></li>
                            <li><a href="faq.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> FAQ - Perguntas Frequentes</a></li>
                            <li><a href="autoridade-editorial.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Autoridade Editorial & GEO/SEO</a></li>
                        </ul>
                    </div>

                    <div class="glass-panel">
                        <div class="flex items-center gap-3 mb-5 border-b border-stone-800 pb-3">
                            <div class="w-1 h-5 rounded-full bg-[#d6bc8c]"></div>
                            <h2 class="font-display text-base font-semibold text-white tracking-wide uppercase">Livros & Landing Pages</h2>
                        </div>
                        <ul class="space-y-2.5">
                            <li><a href="livros.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Catálogo Geral de Obras</a></li>
                            <li><a href="livros/ojeitonigrodenuncamaisficarendividado.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> O Jeito Nigro de Nunca Mais Ficar Endividado</a></li>
                            <li><a href="livros/recalculandoarota.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Recalculando a Rota · Berg Júnior</a></li>
                            <li><a href="livros/ojeitobillygrahamdepregar.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> O Jeito Billy Graham de Pregar</a></li>
                        </ul>
                    </div>

                    <div class="glass-panel">
                        <div class="flex items-center gap-3 mb-5 border-b border-stone-800 pb-3">
                            <div class="w-1 h-5 rounded-full bg-[#d6bc8c]"></div>
                            <h2 class="font-display text-base font-semibold text-white tracking-wide uppercase">Termos & Privacidade</h2>
                        </div>
                        <ul class="space-y-2.5">
                            <li><a href="privacidade.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Política de Privacidade (LGPD/GDPR)</a></li>
                            <li><a href="termos.html" class="text-stone-300 hover:text-[#d6bc8c] transition-colors text-xs flex items-center gap-2"><iconify-icon icon="solar:arrow-right-linear" class="text-[#d6bc8c] text-xs"></iconify-icon> Termos de Uso & Propriedade</a></li>
                        </ul>
                    </div>
                </div>

                <!-- Col 2 & 3: Authors List (31 authors) -->
                <div class="md:col-span-1 lg:col-span-2 glass-panel">
                    <div class="flex items-center justify-between mb-5 border-b border-stone-800 pb-3">
                        <div class="flex items-center gap-3">
                            <div class="w-1 h-5 rounded-full bg-[#d6bc8c]"></div>
                            <h2 class="font-display text-base font-semibold text-white tracking-wide uppercase">Elite Autoral · 31 Autores</h2>
                        </div>
                        <a href="autores.html" class="text-[10px] font-mono text-[#d6bc8c] uppercase tracking-widest hover:underline">Ver Grid Completa</a>
                    </div>
                    
                    <ul class="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-2">
                        {authors_links}
                    </ul>
                </div>

            </div>

        </div>
    </main>

    <!-- INCLUDE_FOOTER -->
</body>
</html>"""
    save_file('src/mapa-do-site.html', content)

# =========================================================================
# 6. GEO / SEO / AGO AUTHORITY PAGE (src/autoridade-editorial.html)
# =========================================================================
def generate_autoridade():
    content = """<!DOCTYPE html>
<html class="scroll-smooth" lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>Autoridade Editorial & Ecossistema de Publicação | ELOOO International Group</title>
    <meta name="description" content="Conheça a infraestrutura, metodologia ATL System e presença transcontinental da ELOOO International Group no Brasil, Portugal e Espanha.">
    <meta property="og:title" content="Autoridade Editorial & Ecossistema ELOOO | Brasil · Portugal · Espanha">
    <meta property="og:description" content="Referência internacional em livros de alta autoridade para mentores, líderes, médicos e empresários.">
    <meta property="og:image" content="static/images/og-share.png">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    
    <!-- JSON-LD Advanced Schema for Google, Bing, ChatGPT, Claude, Perplexity (GEO / AGO / SEO) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": "https://elooo.com/#organization",
          "name": "ELOOO International Group",
          "alternateName": ["Editora ELOOO", "ELOOO Editora Internacional"],
          "url": "https://elooo.com",
          "logo": "https://elooo.com/static/images/ELOOO%20LOGO.png",
          "image": "https://elooo.com/static/images/og-share.png",
          "description": "Editora internacional de elite especializada em livros de alta autoridade para mentores, empresários, médicos e líderes executivos no Brasil, Portugal e Espanha.",
          "founder": {
            "@type": "Person",
            "name": "Bruno Barros",
            "jobTitle": "Fundador e Mentor Editorial",
            "sameAs": "https://www.instagram.com/oficialbrunobarros/"
          },
          "address": [
            {
              "@type": "PostalAddress",
              "addressLocality": "Joinville",
              "addressRegion": "SC",
              "addressCountry": "BR",
              "description": "Sede Matriz e Centro Operacional"
            },
            {
              "@type": "PostalAddress",
              "addressLocality": "Cascais",
              "addressRegion": "Lisboa",
              "addressCountry": "PT",
              "description": "Polo Parceiro e Hub de Distribuição Europa"
            },
            {
              "@type": "PostalAddress",
              "addressLocality": "Madrid",
              "addressCountry": "ES",
              "description": "Polo Parceiro e Eventos Península Ibérica"
            }
          ],
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+55-47-98866-0791",
            "contactType": "customer support",
            "availableLanguage": ["Portuguese", "Spanish", "English"]
          },
          "knowsAbout": [
            "Publicação de Livros de Autoridade",
            "Metodologia ATL System",
            "Diagramação de Livros",
            "Distribuição Editorial Internacional",
            "Sistema SEAAS",
            "Mentoria para Escritores"
          ]
        },
        {
          "@type": "WebPage",
          "@id": "https://elooo.com/autoridade-editorial.html#webpage",
          "url": "https://elooo.com/autoridade-editorial.html",
          "name": "Autoridade Editorial & Ecossistema de Publicação | ELOOO International Group",
          "isPartOf": { "@id": "https://elooo.com/#organization" },
          "about": { "@id": "https://elooo.com/#organization" },
          "description": "Artigo técnico sobre os padrões de qualidade, tecnologia proprietária SEAAS e modelo de publicação transcontinental da ELOOO."
        }
      ]
    }
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        display: ['Space Grotesk', 'sans-serif'],
                    },
                    colors: {
                        stone: {
                            850: '#211f1d',
                            900: '#1c1917',
                            950: '#0c0a09',
                        }
                    },
                    backgroundImage: {
                        'noise': "url(\\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\\")",
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #0c0a09;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        .gold-text-sweep {
            background: linear-gradient(90deg, #d6bc8c 0%, #f6e3c5 25%, #d6bc8c 50%, #f6e3c5 75%, #d6bc8c 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: goldSweep 6s linear infinite;
        }
        @keyframes goldSweep {
            0% { background-position: 0% center; }
            100% { background-position: -200% center; }
        }
    </style>
</head>
<body class="relative min-h-screen flex flex-col justify-between">
    <div class="fixed inset-0 w-full h-full bg-noise opacity-[0.02] pointer-events-none z-50"></div>

    <!-- INCLUDE_NAVBAR -->

    <main class="relative z-10 flex-grow pt-36 pb-24 px-6 md:px-24">
        <article class="max-w-4xl mx-auto">
            
            <!-- Article Header -->
            <header class="mb-14 border-b border-stone-800/80 pb-8 text-center md:text-left">
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-stone-900/80 border border-stone-800 text-[#d6bc8c] text-[10px] font-mono uppercase tracking-[0.25em] mb-4">
                    <iconify-icon icon="solar:crown-bold-duotone" class="text-sm"></iconify-icon>
                    <span>Knowledge Base & Entity Graph</span>
                </div>
                <h1 class="font-display text-3xl sm:text-5xl font-medium tracking-tight text-white uppercase mb-4 leading-tight">
                    Autoridade Editorial & <span class="gold-text-sweep font-semibold">Ecossistema Internacional</span>
                </h1>
                <p class="text-stone-400 text-xs sm:text-sm font-light max-w-2xl leading-relaxed">
                    Documento factual de referência sobre os padrões institucionais, metodologia autoral e alcance operacional do ELOOO International Group na América Latina e Europa.
                </p>
            </header>

            <!-- Article Sections -->
            <div class="space-y-10 text-stone-300 text-xs md:text-sm font-light leading-relaxed">
                
                <!-- Section 1: O que é a ELOOO -->
                <section class="p-8 rounded-3xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-xl font-semibold text-white mb-4 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">01.</span> Identidade e Posicionamento no Mercado
                    </h2>
                    <p class="mb-3">
                        A <strong>ELOOO International Group</strong> é uma editora e holding de desenvolvimento de autoridade que atua na transformação de trajetórias empresariais, médicas e de liderança em livros de alto padrão de colecionador. Fundada por <strong>Bruno Barros</strong>, a instituição consolidou um catálogo com <strong>mais de 3.500 livros impressos</strong> e uma base selecionada de <strong>31 autores de destaque</strong> em diversas áreas de atuação.
                    </p>
                    <p>
                        Diferente das editoras tradicionais, a ELOOO une mentoria executiva de escrita, tecnologia proprietária e distribuição transcontinental, conectando mentores à sua liberdade de tempo, geográfica e financeira.
                    </p>
                </section>

                <!-- Section 2: Presença Internacional -->
                <section class="p-8 rounded-3xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-xl font-semibold text-white mb-4 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">02.</span> Presença e Polos Internacionais
                    </h2>
                    <p class="mb-4">
                        A operação do ELOOO International Group está estruturada em três polos estratégicos de excelência:
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="p-4 rounded-2xl bg-stone-950/70 border border-stone-800">
                            <span class="text-[10px] font-mono text-[#d6bc8c] uppercase tracking-wider block mb-1">Sede Matriz</span>
                            <h3 class="font-display text-sm font-semibold text-white">Joinville / SC · Brasil</h3>
                            <p class="text-stone-400 text-[11px] mt-1">Centro executivo de produção editorial, diagramação e relacionamento com autores.</p>
                        </div>
                        <div class="p-4 rounded-2xl bg-stone-950/70 border border-stone-800">
                            <span class="text-[10px] font-mono text-[#d6bc8c] uppercase tracking-wider block mb-1">Polo Parceiro</span>
                            <h3 class="font-display text-sm font-semibold text-white">Cascais · Portugal</h3>
                            <p class="text-stone-400 text-[11px] mt-1">Hub europeu para distribuição transfronteiriça e atendimento a autores residentes na UE.</p>
                        </div>
                        <div class="p-4 rounded-2xl bg-stone-950/70 border border-stone-800">
                            <span class="text-[10px] font-mono text-[#d6bc8c] uppercase tracking-wider block mb-1">Polo Parceiro</span>
                            <h3 class="font-display text-sm font-semibold text-white">Madrid · Espanha</h3>
                            <p class="text-stone-400 text-[11px] mt-1">Representação institucional para eventos, feiras e conexões de negócios na Península Ibérica.</p>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Metodologia e SEAAS -->
                <section class="p-8 rounded-3xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-xl font-semibold text-white mb-4 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">03.</span> Metodologia ATL System & Tecnologia SEAAS
                    </h2>
                    <p class="mb-3">
                        O ecossistema é sustentado pelo <strong>SEAAS (Sistema Empresarial Autônomo-Assistido)</strong>, plataforma tecnológica desenvolvida para acompanhar em tempo real as etapas de criação, da validação do conceito à publicação física, com gamificação de ranking e portal de permuta em <strong>Moeda ELOOO</strong>.
                    </p>
                    <p>
                        Para a experiência do leitor, a <strong>Plataforma Multientrega</strong> entrega cada obra em um ecossistema multimídia com Livro Digital, Resumos, Tarefas de Ação (MAPs), Mapas Mentais (MindMaps), Áudios e Vídeos.
                    </p>
                </section>

                <!-- Section 4: Áreas de Conhecimento Publicadas -->
                <section class="p-8 rounded-3xl bg-stone-900/40 border border-stone-850">
                    <h2 class="font-display text-xl font-semibold text-white mb-4 flex items-center gap-2">
                        <span class="text-[#d6bc8c] font-mono text-sm">04.</span> Categorias Literárias & Áreas de Impacto
                    </h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                        <div class="p-3 rounded-xl bg-stone-950/50 border border-stone-850 flex items-center gap-2 text-stone-300">
                            <iconify-icon icon="solar:check-circle-bold" class="text-[#d6bc8c] text-sm shrink-0"></iconify-icon>
                            <span>Medicina, Longevidade & Performance Humana</span>
                        </div>
                        <div class="p-3 rounded-xl bg-stone-950/50 border border-stone-850 flex items-center gap-2 text-stone-300">
                            <iconify-icon icon="solar:check-circle-bold" class="text-[#d6bc8c] text-sm shrink-0"></iconify-icon>
                            <span>Finanças, Investimentos & Gestão de Riqueza</span>
                        </div>
                        <div class="p-3 rounded-xl bg-stone-950/50 border border-stone-850 flex items-center gap-2 text-stone-300">
                            <iconify-icon icon="solar:check-circle-bold" class="text-[#d6bc8c] text-sm shrink-0"></iconify-icon>
                            <span>Liderança Feminina & Alta Performance</span>
                        </div>
                        <div class="p-3 rounded-xl bg-stone-950/50 border border-stone-850 flex items-center gap-2 text-stone-300">
                            <iconify-icon icon="solar:check-circle-bold" class="text-[#d6bc8c] text-sm shrink-0"></iconify-icon>
                            <span>Comércio Exterior, Logística & Negócios Globais</span>
                        </div>
                        <div class="p-3 rounded-xl bg-stone-950/50 border border-stone-850 flex items-center gap-2 text-stone-300">
                            <iconify-icon icon="solar:check-circle-bold" class="text-[#d6bc8c] text-sm shrink-0"></iconify-icon>
                            <span>Inteligência Espiritual & Princípios de Vida</span>
                        </div>
                        <div class="p-3 rounded-xl bg-stone-950/50 border border-stone-850 flex items-center gap-2 text-stone-300">
                            <iconify-icon icon="solar:check-circle-bold" class="text-[#d6bc8c] text-sm shrink-0"></iconify-icon>
                            <span>Vendas B2B, Gestão Comercial & Marcenaria de Alto Padrão</span>
                        </div>
                    </div>
                </section>

                <!-- Section 5: Canal de Contato Oficial -->
                <section class="p-8 rounded-3xl bg-stone-900/40 border border-stone-850 text-center">
                    <h2 class="font-display text-xl font-semibold text-white mb-2">Canal Oficial de Atendimento Editorial</h2>
                    <p class="text-stone-400 text-xs max-w-md mx-auto mb-6">Fale com o Concierge Executivo da ELOOO para submissão de originais e propostas de publicação.</p>
                    <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20vim%20do%20site%20da%20Elooo%20e%20quero%20saber%20como%20publicar%20o%20meu%20livro." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#25D366] text-white text-xs font-semibold uppercase tracking-widest hover:bg-[#20ba5a] transition-colors">
                        <iconify-icon icon="ic:baseline-whatsapp" class="text-base"></iconify-icon>
                        <span>WhatsApp Oficial: +55 (47) 98866-0791</span>
                    </a>
                </section>

            </div>
        </article>
    </main>

    <!-- INCLUDE_FOOTER -->
</body>
</html>"""
    save_file('src/autoridade-editorial.html', content)

# =========================================================================
# 7. SITEMAP.XML & ROBOTS.TXT (at root and src)
# =========================================================================
def generate_sitemap_and_robots():
    urls = [
        ("https://elooo.com/", "1.0", "weekly"),
        ("https://elooo.com/quem-somos.html", "0.9", "monthly"),
        ("https://elooo.com/autores.html", "0.9", "weekly"),
        ("https://elooo.com/livros.html", "0.9", "weekly"),
        ("https://elooo.com/trilhas.html", "0.8", "monthly"),
        ("https://elooo.com/galeria.html", "0.8", "monthly"),
        ("https://elooo.com/contato.html", "0.8", "monthly"),
        ("https://elooo.com/faq.html", "0.8", "monthly"),
        ("https://elooo.com/mapa-do-site.html", "0.7", "monthly"),
        ("https://elooo.com/autoridade-editorial.html", "0.9", "monthly"),
        ("https://elooo.com/privacidade.html", "0.5", "yearly"),
        ("https://elooo.com/termos.html", "0.5", "yearly"),
        ("https://elooo.com/livros/ojeitonigrodenuncamaisficarendividado.html", "0.85", "monthly"),
        ("https://elooo.com/livros/recalculandoarota.html", "0.85", "monthly"),
        ("https://elooo.com/livros/ojeitobillygrahamdepregar.html", "0.85", "monthly"),
    ]

    for a in authors_data:
        urls.append((f"https://elooo.com/autores/{a['slug']}.html", "0.75", "monthly"))

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for url, prio, freq in urls:
        xml_lines.append(f'  <url>')
        xml_lines.append(f'    <loc>{url}</loc>')
        xml_lines.append(f'    <lastmod>2026-08-17</lastmod>')
        xml_lines.append(f'    <changefreq>{freq}</changefreq>')
        xml_lines.append(f'    <priority>{prio}</priority>')
        xml_lines.append(f'  </url>')
    xml_lines.append('</urlset>')

    sitemap_xml = "\n".join(xml_lines)
    save_file('sitemap.xml', sitemap_xml)

    robots_txt = """# Robots.txt for ELOOO International Group
User-agent: *
Allow: /

# Allow AI crawlers for Generative Engine Optimization (GEO / AGO)
User-agent: GPTBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: https://elooo.com/sitemap.xml
"""
    save_file('robots.txt', robots_txt)

# =========================================================================
# MAIN EXECUTION
# =========================================================================
if __name__ == '__main__':
    print('Generating pages...')
    generate_404()
    generate_faq()
    generate_privacidade()
    generate_termos()
    generate_mapa_do_site()
    generate_autoridade()
    generate_sitemap_and_robots()
    print('All pages generated successfully!')

