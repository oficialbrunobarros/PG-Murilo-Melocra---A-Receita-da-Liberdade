import os

# Author data with names, books, flags, and custom biographies
authors_data = [
    # Row 1
    {
        "slug": "tatiana-fonseca",
        "name": "Tatiana Fonseca",
        "book": "Permaneça - O Caminho para a Plenitude",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/tatiana.vfonseca/",
        "bio": "Escritora, mentora e palestrante. Transforma experiências, aprendizados e princípios em mensagens que incentivam pessoas a reconhecerem seu valor, desenvolverem seu potencial e construírem uma vida com mais propósito."
    },
    {
        "slug": "savio-cardoso",
        "name": "Dr. Sávio Cardoso",
        "book": "O Código da Vitalidade Masculina",
        "flag": "circle-flags:pt",
        "instagram": "https://www.instagram.com/drsaviocardoso/",
        "bio": "Médico com atuação no Brasil e em Portugal nas áreas de longevidade, performance e reposição hormonal. Direciona seu trabalho a quem busca envelhecer com saúde, vigor, disposição e qualidade de vida."
    }, # Position 2 (Portugal)
    {
        "slug": "kenje-kambara",
        "name": "Kenje Kambara",
        "book": "Os Segredos do Lojista B2B & Mercado Automotivo",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/kenjekambara/",
        "bio": "Empresário e fundador da ZS Autos, especializada em veículos premium em Recife. Com vasta experiência no setor de compra e venda, compartilha conhecimentos para negócios mais seguros no mercado automotivo."
    },
    {
        "slug": "berenice-duarte-borba",
        "name": "Berenice Duarte",
        "book": "De Ateu ao Encontro com Deus Pai",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/bereniceduartte/",
        "bio": "Pastora, empresária e diretora da Cia Florestal, de soluções ambientais. Sua trajetória une fé, liderança e sustentabilidade, compartilhando ensinamentos sobre propósito, crescimento e serviço."
    },
    # Row 2
    {
        "slug": "sergio-canico",
        "name": "Dr. Sérgio Caniço",
        "book": "O Poder de Um Sorriso",
        "flag": "circle-flags:pt",
        "instagram": "https://www.instagram.com/drsergiocanico/",
        "bio": "Médico-dentista e diretor clínico da Clínica Caniço em Braga, Portugal, com atuação também em Genebra. Especialista em implantologia e estética avançada, resgata a saúde e a beleza do sorriso."
    }, # Position 5 (Portugal)
    {
        "slug": "murilo-melocra",
        "name": "Dr. Murilo Melocra",
        "book": "A Receita da Liberdade",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/murilomelocra/",
        "bio": "Médico, investidor e fundador da ELOOO. Ensina profissionais da saúde a investirem em Bitcoin e construírem patrimônio sólido, gerando segurança e liberdade financeira além dos plantões."
    },
    {
        "slug": "vanessa-rodrigues",
        "name": "Dra. Vanessa Rodrigues",
        "book": "Emagreça Saudável e Feliz",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/dravanessarodriguess/",
        "bio": "Médica especialista no cuidado da saúde feminina. Seu trabalho une acompanhamento médico, mudança de hábitos e uma visão integral da mulher, considerando saúde, qualidade de vida, identidade e propósito."
    },
    {
        "slug": "berg-junior",
        "name": "Berg Júnior",
        "book": "Recalculando a Rota",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/bergjunior6/",
        "bio": "Empresário e fundador da Quarteiro, do setor de alimentação. Sua trajetória é marcada pelo empreendedorismo, liderança e fé, compartilhando aprendizados de quem constrói negócios sobre valores fortes."
    },
    # Row 3
    {
        "slug": "carine-aparecida",
        "name": "Carine Aparecida",
        "book": "Além da Beleza",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/carineaparecida/",
        "bio": "Empresária, especialista em visagismo e fundadora da Confidera em Joinville. Ajuda mulheres a valorizarem sua beleza individual, respeitando suas características físicas, identidade e essência."
    },
    {
        "slug": "franklyn-fuck",
        "name": "Franklyn Rafael Fuck",
        "book": "O Maná do Vendedor",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/franklynfuck/",
        "bio": "Empresário e franqueado da Impacto Prime, rede de serviços automotivos. Sua trajetória reúne liderança, fé e superação, compartilhando lições de quem decidiu romper limites."
    },
    {
        "slug": "fernando-merlos",
        "name": "Dr. Fernando Merlos",
        "book": "Alma Médica",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/merlos.fernando/",
        "bio": "Médico especialista em comunicação na saúde. Ajuda profissionais a desenvolverem habilidades para conduzir conversas difíceis, comunicar decisões com clareza e humanizar o atendimento."
    },
    {
        "slug": "douglas-vacilotto",
        "name": "Douglas Vacilotto",
        "book": "Rompendo Fronteiras",
        "flag": "circle-flags:es",
        "instagram": "https://www.instagram.com/vacilo77o/",
        "bio": "Empresário em Madrid no ramo de móveis de luxo e mentor de desenvolvimento. Incentiva homens a romperem padrões limitantes, desenvolverem disciplina e assumirem responsabilidades."
    }, # Position 12 (Spain)
    # Row 4+
    {
        "slug": "dimas-neto",
        "name": "Dimas Neto",
        "book": "A Arte da Persistência",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/dimais.neto/",
        "bio": "Empresário e fundador da Dimas Móveis Sob Medida, de marcenaria fina de alto padrão. Compartilha desafios, decisões and aprendizados na construção de uma empresa focada em excelência e confiança."
    },
    {
        "slug": "anildo-silva",
        "name": "Anildo Silva",
        "book": "A Missão do Fundador",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/anildosilvabr/",
        "bio": "Empresário, mentor, palestrante e fundador do Itália Cucina Tradizionale. Ajuda empreendedores a organizarem suas operações, aumentarem a lucratividade e reduzirem a dependência do proprietário no dia a dia."
    },
    {
        "slug": "hewandro-entringer",
        "name": "Hewandro Entringer",
        "book": "Os Códigos do Networking",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/hewandroentringer/",
        "bio": "Empresário, especialista em vendas e fundador do Empreendegol. Ajuda empreendedores a ampliarem suas conexões estratégicas e transformarem networking em grandes oportunidades comerciais."
    },
    {
        "slug": "claudio-dutra",
        "name": "Claudio Dutra",
        "book": "Profissional Inquestionável",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/claudiodutra.partner/",
        "bio": "Empresário e fundador da Partner PSE e da CredPartner. Atua com soluções corporativas e comerciais no mercado imobiliário, com vasta experiência em liderança, crédito e vendas."
    },
    {
        "slug": "marcio-lira",
        "name": "Marcio Lira",
        "book": "Liderança Inquestionável",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/eusoumarciolira/",
        "bio": "Empresário, diretor de operações e sócio da Partner PSE. Focado no desenvolvimento de negócios e processos comerciais, capacita líderes e equipes a evoluírem de forma contínua e responsável."
    },
    {
        "slug": "diego-arcas",
        "name": "Diego Arcas",
        "book": "Despertando os Propósitos de Deus",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/diego.arcas/",
        "bio": "Administrador, empresário, jogador de poker e fundador da In Festa Buffet Kids em Joinville. Utiliza estratégia, disciplina e controle emocional como fundamentos para tomada de decisões nos negócios."
    },
    {
        "slug": "rafael-cavalcanti",
        "name": "Rafael Cavalcanti",
        "book": "Os Códigos da Lucratividade",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/rafael.cavalcanti1/",
        "bio": "Empresário e fundador da VITA 24h, rede de hospitais veterinários. Atua com medicina veterinária integrada a tecnologia, processos eficientes, automação e gestão humanizada."
    },
    {
        "slug": "gabriela-mendes",
        "name": "Dra. Gabriela Mendes",
        "book": "Segredos da Saúde Integrativa",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/gabrielamendes.oficial/",
        "bio": "Médica-veterinária, empresária e sócia da VITA 24h. Cofundou e gerencia a estrutura hospitalar voltada ao cuidado animal, unindo conhecimento técnico, sensibilidade e liderança."
    },
    {
        "slug": "herick-pereira",
        "name": "Herick Pereira",
        "book": "O Código do Campeão",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/herickpereirafutsal/",
        "bio": "Treinador, campeão mundial de futsal e mentor de alta performance. Utiliza disciplina, mentalidade e responsabilidade para formar campeões tanto nas quadras quanto na vida."
    },
    {
        "slug": "gustavo-da-silva",
        "name": "Dr. Gustavo Silva",
        "book": "Segredos da Ortopedia Esportiva",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/drgustavo.silva/",
        "bio": "Médico com atuação na área de saúde mental. Aborda de forma humana e acessível temas como ansiedade, depressão, pânico e insônia, orientando sobre a importância do cuidado profissional."
    },
    {
        "slug": "edson-fabiano",
        "name": "Edson Fabiano",
        "book": "Shammah - O Deus que Ouve",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/fabinho01/",
        "bio": "Cristão, empresário e especialista em tecnologia. Aplica inovação prática para aprimorar processos e, como escritor, compartilha reflexões de fé e revelações sobre a Palavra de Deus."
    },
    {
        "slug": "manoel-alvino",
        "name": "Manoel Alvino",
        "book": "Odonto Business",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/manoelalvino/",
        "bio": "Empresário, gestor e fundador da Rede Ortoestética. Especialista em gestão e lucratividade na odontologia, ajuda profissionais a transformarem clínicas em negócios organizados e rentáveis."
    },
    {
        "slug": "romulo-costa",
        "name": "Rômulo Costa",
        "book": "Comercial de Alta Performance",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/costarom/",
        "bio": "Especialista em vendas e fundador da R&G Soluções Comerciais. Com vasta experiência em representação comercial, ajuda empresas a estruturarem processos e reverterem relações em resultados."
    },
    {
        "slug": "gislaine-costa",
        "name": "Gislaine da Costa",
        "book": "Comercial de Alta Performance",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/gislainecpc/",
        "bio": "Empresária e sócia da R&G Soluções Comerciais. Especialista em vendas e gestão comercial, atua no aprimoramento de processos comerciais, liderança de equipes e relações de confiança."
    },
    {
        "slug": "bruno-barros",
        "name": "Bruno Barros",
        "book": "VIDANOVA & Autoralidade",
        "flag": "circle-flags:br",
        "instagram": "https://www.instagram.com/oficialbrunobarros/",
        "bio": "Escritor, palestrante, mentor e fundador da Elooo Editora. Autor de VIDANOVA e Autoralidade e criador do ATL System, orienta líderes a transformarem suas trajetórias em livros e autoridade."
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
                            <img src="{img_path}" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700" alt="{author['name']}" onerror="this.src='static/images/avatar_placeholder.png'; this.style.filter='grayscale(1) brightness(0.6)';">
                        </div>
                        
                        <!-- Name & Flag & Instagram (Centered & Elevated) -->
                        <div class="flex items-center justify-center gap-1.5 mb-1">
                            <h3 class="font-display text-[15px] sm:text-base font-semibold text-white tracking-wide transition-colors duration-500 whitespace-nowrap">
                                {author['name']}
                            </h3>
                            <a href="{author['instagram']}" target="_blank" class="text-stone-400 hover:text-[#d6bc8c] transition-colors flex items-center shrink-0" title="Instagram de {author['name']}">
                                <iconify-icon icon="ri:instagram-line" class="text-sm"></iconify-icon>
                            </a>
                            <iconify-icon icon="{author['flag']}" class="text-sm shrink-0 shadow-[0_2px_4px_rgba(0,0,0,0.4)] rounded-full"></iconify-icon>
                        </div>
                        
                        <!-- Book Title (Gold & Centered) -->
                        <p class="font-sans text-xs text-[#d6bc8c] font-medium mt-1 leading-snug text-center">{author['book']}</p>
                        
                        <!-- Small Biography (Centered) -->
                        <p class="font-sans text-[11px] text-stone-400 font-light mt-2 leading-relaxed text-center">{author['bio']}</p>
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
