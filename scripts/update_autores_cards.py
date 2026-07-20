import os

# Author data with names, books, flags, and custom biographies
authors_data = [
    {
        "slug": "tatiana-fonseca",
        "name": "Tatiana Fonseca",
        "book": "Permaneça - O Caminho para a Plenitude",
        "flag": "circle-flags:br",
        "bio": "Mentora de desenvolvimento pessoal, ajuda mulheres a alcançarem a plenitude espiritual e inteligência emocional em suas jornadas."
    },
    {
        "slug": "kenje-kambara",
        "name": "Kenje Kambara",
        "book": "Os Segredos do Lojista B2B & Mercado Automotivo",
        "flag": "circle-flags:br",
        "bio": "Especialista em escala comercial e negócios B2B/B2C, mentorando lojistas e empresários do setor automotivo."
    },
    {
        "slug": "berenice-duarte-borba",
        "name": "Berenice Duarte Borba",
        "book": "De Ateu ao Encontro com Deus Pai",
        "flag": "circle-flags:br",
        "bio": "Escritora e mentora espiritual, dedica sua vida a guiar pessoas no caminho do autoconhecimento e conexão com a fé."
    },
    {
        "slug": "murilo-melocra",
        "name": "Dr. Murilo Melocra",
        "book": "A Receita da Liberdade",
        "flag": "circle-flags:br",
        "bio": "Médico de alta performance e fundador da ELOOO. Especialista em gestão patrimonial, investimentos e liberdade profissional."
    },
    {
        "slug": "vanessa-rodrigues",
        "name": "Dra. Vanessa Rodrigues",
        "book": "Emagreça Saudável e Feliz",
        "flag": "circle-flags:br",
        "bio": "Médica integrativa especialista em emagrecimento saudável, promovendo reprogramação metabólica e bem-estar."
    },
    {
        "slug": "berg-junior",
        "name": "Berg Junior",
        "book": "Recalculando a Rota",
        "flag": "circle-flags:br",
        "bio": "Estrategista de negócios e mentor de carreira, focado em ajudar profissionais a recalcularem suas rotas rumo ao sucesso."
    },
    {
        "slug": "carine-aparecida",
        "name": "Carine Aparecida",
        "book": "Além da Beleza",
        "flag": "circle-flags:br",
        "bio": "Especialista em estética de alta autoridade e desenvolvimento pessoal, revelando a beleza que transcende o espelho."
    },
    {
        "slug": "franklyn-fuck",
        "name": "Franklyn Fuck",
        "book": "O Maná do Vendedor",
        "flag": "circle-flags:br",
        "bio": "Treinador de vendas e mentor de times comerciais, especialista em negociação de alto impacto e fechamento de contratos."
    },
    {
        "slug": "fernando-merlos",
        "name": "Dr. Fernando Merlos",
        "book": "Alma Médica",
        "flag": "circle-flags:br",
        "bio": "Médico humanista, mentor e palestrante focado na essência da medicina e no resgate da Alma Médica."
    },
    {
        "slug": "dimas-neto",
        "name": "Dimas Neto",
        "book": "A Arte da Persistência",
        "flag": "circle-flags:br",
        "bio": "Empresário e palestrante motivacional, ensina os segredos da persistência e superação de limites no empreendedorismo."
    },
    {
        "slug": "anildo-silva",
        "name": "Anildo Silva",
        "book": "A Missão do Fundador",
        "flag": "circle-flags:br",
        "bio": "Fundador de grandes marcas, mentor de liderança executiva especializado em governança corporativa e sucessão."
    },
    {
        "slug": "savio-cardoso",
        "name": "Dr. Sávio Cardoso",
        "book": "O Código da Vitalidade Masculina",
        "flag": "circle-flags:pt",
        "bio": "Médico andrologista e mentor em saúde masculina na Europa, focado em alta performance, longevidade e vigor biológico."
    },
    {
        "slug": "hewandro-entringer",
        "name": "Hewandro Entringer",
        "book": "Os Códigos do Networking",
        "flag": "circle-flags:br",
        "bio": "Especialista em parcerias estratégicas e networking de elite, mentorando profissionais a construírem conexões milionárias."
    },
    {
        "slug": "claudio-dutra",
        "name": "Cláudio Dutra",
        "book": "Profissional Inquestionável",
        "flag": "circle-flags:br",
        "bio": "Consultor de alta performance e mentor de executivos, especialista no desenvolvimento de profissionais inquestionáveis."
    },
    {
        "slug": "marcio-lira",
        "name": "Márcio Lira",
        "book": "Liderança Inquestionável",
        "flag": "circle-flags:br",
        "bio": "Mentor de líderes e empresários, especializado em desenvolvimento de equipes e posicionamento profissional inquestionável."
    },
    {
        "slug": "diego-arcas",
        "name": "Diego Arcas",
        "book": "Despertando os Propósitos de Deus",
        "flag": "circle-flags:br",
        "bio": "Teólogo, mentor espiritual e palestrante especializado em guiar pessoas no despertar do propósito divino de vida."
    },
    {
        "slug": "rafael-cavalcanti",
        "name": "Rafael Cavalcanti",
        "book": "Os Códigos da Lucratividade",
        "flag": "circle-flags:br",
        "bio": "Estrategista financeiro e mentor de negócios, focado em escala de lucros e otimização de fluxo de caixa."
    },
    {
        "slug": "gabriela-mendes",
        "name": "Dra. Gabriela Mendes",
        "book": "Segredos da Saúde Integrativa",
        "flag": "circle-flags:br",
        "bio": "Especialista em saúde integrativa e longevidade saudável, mentoreando profissionais a alcançarem alta performance física."
    },
    {
        "slug": "herick-pereira",
        "name": "Herick Pereira",
        "book": "O Código do Campeão",
        "flag": "circle-flags:br",
        "bio": "Atleta profissional e mentor esportivo, especialista no desenvolvimento de mentalidade vencedora e foco absoluto."
    },
    {
        "slug": "gustavo-da-silva",
        "name": "Dr. Gustavo da Silva",
        "book": "Segredos da Ortopedia Esportiva",
        "flag": "circle-flags:br",
        "bio": "Médico especialista em medicina esportiva e ortopedia, focado em reabilitação de alta performance e performance física."
    },
    {
        "slug": "douglas-vacilotto",
        "name": "Douglas Vacilotto",
        "book": "Rompendo Fronteiras",
        "flag": "circle-flags:es",
        "bio": "Empresário com atuação internacional, mentor de internacionalização de negócios e atração de capital na Europa."
    },
    {
        "slug": "edson-fabiano",
        "name": "Edson Fabiano",
        "book": "Shammah - O Deus que Ouve",
        "flag": "circle-flags:br",
        "bio": "Pastor, escritor e mentor espiritual focado em liderança eclesiástica, cura emocional e maturidade cristã."
    }
]

# Read src/autores.html
with open('src/autores.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject gold text shadow effect to the stylesheet
old_style_end = "    </style>"
gold_hover_style = """        /* Gold name hover glow and color */
        .flashlight-card:hover h3 {
            color: #d6bc8c !important;
            text-shadow: 0 0 10px rgba(214, 188, 140, 0.6), 0 0 2px rgba(214, 188, 140, 0.8);
        }
    </style>"""

if gold_hover_style not in content:
    content = content.replace(old_style_end, gold_hover_style)

# 2. Find grid container block and replace the whole cards listing
grid_start_marker = '<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 relative z-20 -mt-16 sm:-mt-28 md:-mt-36 lg:-mt-52 pb-20">'
grid_end_marker = '            </div>\n        </div>\n    </section>'

start_idx = content.find(grid_start_marker)
end_idx = content.find(grid_end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Error: Could not locate grid container in src/autores.html!")
    exit(1)

# Generate cards HTML
cards_html = grid_start_marker + "\n"

for author in authors_data:
    # Use fallback file extension .png matching local image assets
    img_path = f"static/images/{author['slug']}.png"
    if author['slug'] == 'murilo-melocra':
        img_path = "static/images/FOTO MURILO.jpeg"
        
    cards_html += f"""            <!-- Author Card: {author['name']} -->
            <div class="flashlight-card group p-[1.5px] relative overflow-hidden rounded-[32px] transition-all duration-500 bg-stone-900/40">
                <!-- Rotating light border sweep -->
                <span class="absolute inset-[-1000%] animate-[spin_4s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,rgba(214,188,140,0.8)_50%,transparent_100%)] opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></span>
                
                <!-- Inner Container (Holds flashlight and content) -->
                <div class="flashlight-card-inner relative z-10 w-full h-full bg-[#0c0a09]/95 backdrop-blur-md rounded-[31px] p-6 flex flex-col justify-between" onmousemove="updateFlashlight(event, this)">
                    <div class="z-10">
                        <!-- Photo Container -->
                        <div class="w-full aspect-[3/4] rounded-2xl overflow-hidden mb-4 bg-stone-850 border border-stone-800/80">
                            <img src="{img_path}" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700" alt="{author['name']}" onerror="this.src='static/images/FOTO MURILO.jpeg'; this.style.filter='grayscale(1) brightness(0.6)';">
                        </div>
                        
                        <!-- Name & Flag & Instagram (Centered & Elevated) -->
                        <div class="flex items-center justify-center gap-1.5 mb-1">
                            <h3 class="font-display text-[15px] sm:text-base font-semibold text-white tracking-wide transition-colors duration-500 whitespace-nowrap">
                                {author['name']}
                            </h3>
                            <a href="https://www.instagram.com/" target="_blank" class="text-stone-400 hover:text-[#d6bc8c] transition-colors flex items-center shrink-0" title="Instagram de {author['name']}">
                                <iconify-icon icon="ri:instagram-line" class="text-sm"></iconify-icon>
                            </a>
                            <iconify-icon icon="{author['flag']}" class="text-sm shrink-0 shadow-[0_2px_4px_rgba(0,0,0,0.4)] rounded-full"></iconify-icon>
                        </div>
                        
                        <!-- Book Title (Gold & Centered) -->
                        <p class="font-sans text-xs text-[#d6bc8c] font-medium mt-1 leading-snug text-center">{author['book']}</p>
                        
                        <!-- Small Biography (Centered) -->
                        <p class="font-sans text-[11px] text-stone-400 font-light mt-2 leading-relaxed line-clamp-3 min-h-[50px] text-center">{author['bio']}</p>
                    </div>
                    
                    <div class="z-10 mt-4 pt-4 border-t border-stone-800/60 flex items-center justify-between">
                        <span class="text-[10px] font-mono uppercase tracking-widest text-stone-500 group-hover:text-stone-300 transition-colors">Acessar Perfil</span>
                        <a href="autores/{author['slug']}.html" class="w-8 h-8 rounded-full border border-stone-800 flex items-center justify-center bg-stone-950 text-stone-400 group-hover:bg-[#d6bc8c] group-hover:text-stone-950 group-hover:border-[#d6bc8c] transition-all duration-300 relative z-20">
                            <iconify-icon icon="solar:arrow-right-linear" class="text-sm"></iconify-icon>
                        </a>
                    </div>
                </div>
            </div>\n"""

# Reconstruct file content
new_content = content[:start_idx] + cards_html + content[end_idx:]

with open('src/autores.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Procedural cards updated in src/autores.html.")
