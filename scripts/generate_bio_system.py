# -*- coding: utf-8 -*-
import os

def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'Created: {path} ({len(content)} bytes)')

# ----------------------------------------------------
# 1. LANDING PAGE (src/bio/index.html & src/bio.html)
# ----------------------------------------------------
LANDING_HTML = """<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>ELOOO VITRINE PREMIUM | Vitrine de Alto Padrão + IA que Atende e Vende 24h por Dia</title>
    <meta name="description" content="As redes sociais são lojas. Tenha uma Vitrine Premium impecável e uma IA que atende seus clientes e vende 24h por dia. Construída pela equipe ELOOO em 24h."/>
    
    <!-- Open Graph / Meta -->
    <meta property="og:title" content="ELOOO VITRINE PREMIUM | Vitrine de Alto Padrão + IA Vendedora 24h"/>
    <meta property="og:description" content="Seu Instagram é a sua loja. Criamos sua Vitrine Premium e treinamos sua IA que atende e vende no automático. No ar em 24h."/>
    <meta property="og:image" content="static/images/og-share.png"/>
    <meta property="og:type" content="website"/>
    <meta name="theme-color" content="#EAEAE5"/>

    <!-- High-Performance Font Loading: Preconnect & display=swap (Grade A Speed) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
    
    <!-- Iconify -->
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>

    <!-- Tailwind CSS Engine -->
    <script src="https://cdn.tailwindcss.com"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        display: ['Space Grotesk', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        stone: {
                            50: '#fafaf9',
                            100: '#f5f5f4',
                            200: '#e7e5e4',
                            300: '#d6d3d1',
                            400: '#a8a29e',
                            500: '#78716c',
                            600: '#57534e',
                            700: '#44403c',
                            800: '#292524',
                            900: '#1c1917',
                            950: '#0c0a09',
                        },
                        gold: {
                            100: '#fdf6e7',
                            200: '#faeac7',
                            300: '#f5dc9e',
                            400: '#e5be63',
                            500: '#d6bc8c',
                            600: '#b89445',
                            700: '#8c6e26',
                        }
                    },
                    backgroundImage: {
                        'noise': "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\")",
                    }
                }
            }
        }
    </script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #EAEAE5;
            color: #1C1917;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        .font-display {
            font-family: 'Space Grotesk', sans-serif;
        }

        /* FLOATING PILL NAVBAR */
        .glass-nav {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(28, 25, 23, 0.1);
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.08), 0 2px 6px rgba(0, 0, 0, 0.02);
        }

        /* FLASHLIGHT HOVER CARD */
        .flashlight-card {
            position: relative;
            background: #FFFFFF;
            border: 1px solid rgba(28, 25, 23, 0.08);
            border-radius: 24px;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .flashlight-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(500px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(214, 188, 140, 0.3), transparent 60%);
            z-index: 1;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s ease;
            border-radius: inherit;
        }
        .flashlight-card:hover {
            transform: translateY(-3px);
            border-color: #d6bc8c;
            box-shadow: 0 20px 40px -15px rgba(28, 25, 23, 0.1), 0 0 25px rgba(214, 188, 140, 0.25);
        }
        .flashlight-card:hover::before {
            opacity: 1;
        }

        /* ABSOLUTELY GOLD SUPER-PREMIUM BUTTON */
        @keyframes goldGleam {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes goldShimmerSweep {
            0% { transform: translateX(-150%) skewX(-20deg); }
            100% { transform: translateX(250%) skewX(-20deg); }
        }

        .btn-gold-luxury {
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: linear-gradient(135deg, #d6bc8c 0%, #faeac7 25%, #c5a870 50%, #f5dc9e 75%, #d6bc8c 100%);
            background-size: 250% 250%;
            animation: goldGleam 4s ease infinite;
            color: #12100e !important;
            font-weight: 800;
            border-radius: 9999px;
            border: 1.5px solid #faeac7;
            box-shadow: 0 10px 25px -5px rgba(214, 188, 140, 0.65), 0 0 15px rgba(214, 188, 140, 0.4);
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            cursor: pointer;
            text-decoration: none;
            text-shadow: 0 1px 1px rgba(255, 255, 255, 0.5);
        }

        .btn-gold-luxury::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 60%;
            height: 100%;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.65) 50%, transparent 100%);
            transform: translateX(-150%) skewX(-20deg);
            animation: goldShimmerSweep 3.5s infinite;
            pointer-events: none;
        }

        .btn-gold-luxury:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 15px 35px -5px rgba(214, 188, 140, 0.9), 0 0 25px rgba(250, 234, 199, 0.7);
            border-color: #ffffff;
            color: #000000 !important;
        }

        /* LUXURY GOLD GRADIENT SECTIONS */
        .section-gold-luxury {
            background: linear-gradient(145deg, #1c1917 0%, #29241b 50%, #171512 100%);
            color: #ffffff;
            border-top: 1px solid rgba(214, 188, 140, 0.35);
            border-bottom: 1px solid rgba(214, 188, 140, 0.35);
        }

        .section-gold-warm {
            background: linear-gradient(160deg, #FDF9F0 0%, #F5ECDB 100%);
            border-top: 1px solid rgba(214, 188, 140, 0.4);
            border-bottom: 1px solid rgba(214, 188, 140, 0.4);
        }

        /* SMARTPHONE FRAME 3D (PREMIUM MOCKUP WITH DYNAMIC ISLAND) */
        .phone-mockup-wrapper {
            position: relative;
            border-radius: 46px;
            padding: 8px;
            background: linear-gradient(145deg, #2b2825, #141311);
            box-shadow: 0 30px 70px -15px rgba(28, 25, 23, 0.35), 0 0 30px rgba(214, 188, 140, 0.2);
            border: 2px solid rgba(214, 188, 140, 0.5);
        }
    </style>
</head>
<body class="antialiased selection:bg-stone-900 selection:text-white">

    <!-- FLOATING TOP NAVBAR -->
    <div class="fixed top-3 sm:top-4 inset-x-3 sm:inset-x-6 z-50 flex justify-center pointer-events-none">
        <nav class="pointer-events-auto flex items-center justify-between gap-4 pl-4 pr-3 sm:pl-6 sm:pr-3 py-2.5 rounded-full w-full max-w-4xl glass-nav relative">
            <!-- Brand Logo & Product Name Always Linked -->
            <a class="inline-flex items-center flex-none group cursor-pointer" href="index.html">
                <img src="static/images/ELOOO LOGO.png" alt="ELOOO VITRINE PREMIUM" class="h-9 sm:h-11 object-contain transition-transform group-hover:scale-105" style="filter: brightness(0);"/>
                <span class="ml-3 text-[11.5px] font-mono font-bold uppercase tracking-[0.2em] text-stone-900 border-l border-stone-300 pl-3">
                    VITRINE PREMIUM
                </span>
            </a>

            <!-- Right Action: Hamburger + Gold CTA -->
            <div class="flex items-center gap-2.5 flex-none">
                <a href="cadastrar.html" class="btn-gold-luxury px-5 py-2.5 text-[11px] sm:text-xs font-mono font-bold uppercase tracking-widest">
                    <span>Quero Minha Vitrine</span>
                    <iconify-icon icon="solar:arrow-right-linear" class="text-sm"></iconify-icon>
                </a>

                <!-- Hamburger Button (Desktop & Mobile) -->
                <button id="menu-hamburger-btn" type="button" class="w-10 h-10 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-900 flex items-center justify-center text-xl transition-all cursor-pointer shadow-sm border border-stone-200" aria-label="Abrir Menu">
                    <iconify-icon icon="solar:hamburger-menu-linear"></iconify-icon>
                </button>
            </div>
        </nav>
    </div>

    <!-- LUXURY DRAWER (OPENS VIA HAMBURGER) -->
    <div id="luxury-drawer" class="fixed inset-0 bg-stone-950/70 backdrop-blur-md z-50 opacity-0 pointer-events-none transition-all duration-300 flex justify-end">
        <div id="luxury-drawer-content" class="w-full max-w-sm bg-white h-full shadow-2xl p-6 sm:p-8 flex flex-col justify-between transform translate-x-full transition-transform duration-300 overflow-y-auto">
            <div>
                <!-- Drawer Header -->
                <div class="flex items-center justify-between border-b border-stone-200 pb-4 mb-6">
                    <div class="flex items-center gap-2">
                        <img src="static/images/ELOOO LOGO.png" alt="ELOOO VITRINE PREMIUM" class="h-8 object-contain" style="filter: brightness(0);"/>
                        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-stone-900">VITRINE PREMIUM</span>
                    </div>
                    <button id="luxury-drawer-close" class="w-8 h-8 rounded-full bg-stone-100 text-stone-800 flex items-center justify-center text-lg hover:bg-stone-200 transition-colors">
                        <iconify-icon icon="solar:close-circle-linear"></iconify-icon>
                    </button>
                </div>

                <!-- Navigation Links -->
                <nav class="space-y-2 font-sans font-bold text-xs uppercase tracking-wider text-stone-700">
                    <a href="#entregaveis" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Os 2 Entregáveis</a>
                    <a href="#problema" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Sua Rede é uma Loja</a>
                    <a href="#como" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Nós Fazemos Tudo em 24h</a>
                    <a href="#demo" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">IA que Atende e Vende</a>
                    <a href="#agenda" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Agenda Integrada (Plano Elite)</a>
                    <a href="#planos" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Planos & Valores</a>
                    <a href="brunobarros.html" target="_blank" class="drawer-link block px-4 py-3 rounded-2xl bg-stone-900 text-white font-bold flex items-center justify-between border border-[#d6bc8c]">
                        <span>Vitrine Modelo Bruno Barros</span>
                        <iconify-icon icon="solar:arrow-right-up-linear"></iconify-icon>
                    </a>
                </nav>
            </div>

            <!-- Drawer Bottom Actions -->
            <div class="pt-6 border-t border-stone-200 space-y-2.5">
                <a href="entrar.html" class="block w-full py-3 rounded-full text-center text-xs font-bold text-stone-800 bg-stone-100 hover:bg-stone-200 transition-colors uppercase tracking-wider">
                    Fazer Login
                </a>
                <a href="cadastrar.html" class="btn-gold-luxury w-full py-3.5 text-xs font-mono font-bold uppercase tracking-widest text-center">
                    Contratar Vitrine em 24h →
                </a>
            </div>
        </div>
    </div>

    <!-- MAIN CONTENT -->
    <main class="relative z-10">

        <!-- HERO SECTION -->
        <section class="relative pt-28 pb-10 sm:pt-32 sm:pb-12 overflow-hidden">
            <div class="max-w-4xl mx-auto px-5 text-center relative z-10">
                
                <!-- Main Headline -->
                <h1 class="text-3xl sm:text-5xl lg:text-[54px] font-bold font-display tracking-tight text-stone-900 leading-[1.1] mb-3">
                    Sua Vitrine Premium com Inteligência Artificial que Atende e Vende 24h por dia.
                </h1>

                <!-- Subtitle -->
                <p class="text-sm sm:text-base text-stone-600 max-w-2xl mx-auto mb-6 leading-relaxed">
                    As redes sociais são lojas. Nós construímos a sua <strong class="text-stone-950 font-semibold">Vitrine Premium de Alto Padrão</strong> e treinamos a sua <strong class="text-stone-950 font-semibold">IA Vendedora que atende e fecha vendas 24h por dia</strong>. Tudo 100% configurado e no ar em até 24 horas.
                </p>

                <!-- Hero Action Buttons -->
                <div class="flex flex-col sm:flex-row items-center justify-center gap-3 mb-8">
                    <a href="cadastrar.html" class="btn-gold-luxury w-full sm:w-auto px-8 py-4 text-xs sm:text-sm font-mono font-bold uppercase tracking-widest shadow-xl">
                        <span>Quero Minha Vitrine Pronta em 24h</span>
                        <iconify-icon icon="solar:arrow-right-linear" class="text-base"></iconify-icon>
                    </a>
                    
                    <a href="brunobarros.html" target="_blank" class="w-full sm:w-auto px-7 py-4 rounded-full bg-white text-stone-900 border-2 border-[#d6bc8c] hover:border-[#b89445] text-xs sm:text-sm font-mono font-bold uppercase tracking-wider transition-all flex items-center justify-center gap-2 shadow-sm">
                        <span>Ver Vitrine de Bruno Barros</span>
                        <iconify-icon icon="solar:arrow-right-up-linear" class="text-base text-[#b89445]"></iconify-icon>
                    </a>
                </div>

                <!-- SMARTPHONE MOCKUP (PREMIUM WITH DYNAMIC ISLAND & LIVE BRUNO BARROS VITRINE) -->
                <div class="flex justify-center mb-10">
                    <div class="w-full max-w-[310px] phone-mockup-wrapper relative">
                        <!-- Dynamic Island -->
                        <div class="absolute top-3 left-1/2 -translate-x-1/2 w-24 h-4 bg-black rounded-full z-20 flex items-center justify-end pr-2">
                            <div class="w-2 h-2 rounded-full bg-[#222]"></div>
                        </div>
                        
                        <!-- Interactive Screen Loading Bruno Barros Live Vitrine -->
                        <div class="relative rounded-[38px] overflow-hidden h-[540px] bg-stone-950">
                            <iframe src="brunobarros.html" title="Vitrine Bruno Barros Ao Vivo - premium.elooo.com.br/brunobarros" class="w-full h-full border-0"></iframe>
                            <a href="brunobarros.html" target="_blank" class="absolute inset-x-0 bottom-0 py-3 bg-gradient-to-t from-black/95 via-black/70 to-transparent backdrop-blur-sm text-center text-xs font-mono font-bold uppercase tracking-widest text-[#f6e3c5] hover:text-white transition-colors">
                                Abrir vitrine oficial completa →
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Credibility Stats (10 Anos / 1.1 Bi / 10.000 Alunos) -->
                <div class="pt-6 border-t border-stone-300 max-w-3xl mx-auto">
                    <div class="grid grid-cols-3 gap-3 sm:gap-5">
                        <div class="flashlight-card p-3 sm:p-4 text-center">
                            <div class="text-xl sm:text-3xl font-extrabold font-display text-stone-950 tracking-tight">
                                <span class="counter" data-target="10">10</span> Anos
                            </div>
                            <div class="mt-0.5 text-[9px] sm:text-[11px] font-mono font-semibold uppercase tracking-wider text-stone-500">
                                de atuação
                            </div>
                        </div>

                        <div class="flashlight-card p-3 sm:p-4 text-center">
                            <div class="text-xl sm:text-3xl font-extrabold font-display text-stone-950 tracking-tight">
                                +1.1 Bi
                            </div>
                            <div class="mt-0.5 text-[9px] sm:text-[11px] font-mono font-semibold uppercase tracking-wider text-stone-500">
                                gerados para clientes
                            </div>
                        </div>

                        <div class="flashlight-card p-3 sm:p-4 text-center">
                            <div class="text-xl sm:text-3xl font-extrabold font-display text-stone-950 tracking-tight">
                                +<span class="counter" data-target="10000">10.000</span>
                            </div>
                            <div class="mt-0.5 text-[9px] sm:text-[11px] font-mono font-semibold uppercase tracking-wider text-stone-500">
                                alunos & mentorados
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- OS 2 ENTREGÁVEIS PRINCIPAIS (VITRINE PREMIUM + IA QUE ATENDE E VENDE) -->
        <section class="py-12 sm:py-16 px-5 section-gold-warm border-t border-b border-stone-300" id="entregaveis">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-10">
                    <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#8c6e26] block mb-1">
                        A COMBINAÇÃO PERFEITA DE CONVERSÃO
                    </span>
                    <h2 class="text-2xl sm:text-4xl font-bold font-display text-stone-950 leading-tight">
                        Dois entregáveis essenciais para sua presença de elite.
                    </h2>
                    <p class="text-xs sm:text-sm mt-1.5 max-w-xl mx-auto text-stone-600">
                        Sua rede social é a sua loja física no digital. Ela precisa de uma vitrine impecável e de uma vendedora de alto nível disponível 24 horas por dia.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
                    <!-- Entregável 01: Vitrine Premium -->
                    <div class="flashlight-card p-7 sm:p-8 bg-white border border-[#d6bc8c]/60 shadow-lg flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between mb-4">
                                <div class="w-12 h-12 rounded-2xl bg-[#d6bc8c]/20 text-[#8c6e26] flex items-center justify-center text-2xl">
                                    <iconify-icon icon="solar:shop-2-bold"></iconify-icon>
                                </div>
                                <span class="text-[10.5px] font-mono font-bold uppercase tracking-wider px-3 py-1 rounded-full bg-stone-100 text-stone-700">
                                    ENTREGÁVEL 01
                                </span>
                            </div>

                            <h3 class="text-2xl font-bold font-display text-stone-950 mb-2">
                                VITRINE PREMIUM
                            </h3>
                            <p class="text-xs sm:text-sm text-stone-600 leading-relaxed mb-6">
                                Uma vitrine de altíssimo padrão visual onde seus livros, mentorias, consultas e serviços ganham autoridade imediata. Seus seguidores entram na sua loja e enxergam valor instantâneo.
                            </p>

                            <ul class="space-y-2 text-xs font-medium text-stone-700">
                                <li class="flex items-center gap-2 text-stone-900">
                                    <span class="text-[#8c6e26] font-bold">✦</span>
                                    <span>Design de alto padrão editorial internacional</span>
                                </li>
                                <li class="flex items-center gap-2 text-stone-900">
                                    <span class="text-[#8c6e26] font-bold">✦</span>
                                    <span>Carrossel estilo Netflix de produtos & serviços</span>
                                </li>
                                <li class="flex items-center gap-2 text-stone-900">
                                    <span class="text-[#8c6e26] font-bold">✦</span>
                                    <span>Zero poluição de links desorganizados</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <!-- Entregável 02: IA Que Atende e Vende -->
                    <div class="flashlight-card p-7 sm:p-8 bg-[#12110e] text-white border-2 border-[#d6bc8c] shadow-2xl flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between mb-4">
                                <div class="w-12 h-12 rounded-2xl bg-[#d6bc8c]/25 text-[#d6bc8c] flex items-center justify-center text-2xl">
                                    <iconify-icon icon="solar:chat-round-dots-bold"></iconify-icon>
                                </div>
                                <span class="text-[10.5px] font-mono font-bold uppercase tracking-wider px-3 py-1 rounded-full bg-[#d6bc8c]/20 text-[#f6e3c5]">
                                    ENTREGÁVEL 02
                                </span>
                            </div>

                            <h3 class="text-2xl font-bold font-display text-white mb-2">
                                IA QUE ATENDE E VENDE
                            </h3>
                            <p class="text-xs sm:text-sm text-stone-300 leading-relaxed mb-6">
                                Sua consultora e vendedora de elite que nunca descansa. A IA recebe cada visitante, faz perguntas estratégicas para entender o momento dele e recomenda a solução exata com compra direta.
                            </p>

                            <ul class="space-y-2 text-xs font-medium text-stone-200">
                                <li class="flex items-center gap-2">
                                    <span class="text-[#d6bc8c] font-bold">✦</span>
                                    <span>Atendimento e qualificação ativa 24 horas por dia</span>
                                </li>
                                <li class="flex items-center gap-2">
                                    <span class="text-[#d6bc8c] font-bold">✦</span>
                                    <span>Treinada com as regras e produtos do seu negócio</span>
                                </li>
                                <li class="flex items-center gap-2">
                                    <span class="text-[#d6bc8c] font-bold">✦</span>
                                    <span>Conduz o cliente até a decisão de compra</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Section Action CTA Button -->
                <div class="mt-10 text-center">
                    <a href="cadastrar.html" class="btn-gold-luxury px-9 py-4 text-xs sm:text-sm font-mono font-bold uppercase tracking-widest shadow-xl">
                        <span>Quero Minha Vitrine Premium + IA 24h →</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- O PROBLEMA (Sua Rede é uma Loja) -->
        <section class="py-12 sm:py-16 px-5 bg-white" id="problema">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-8">
                    <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                        Você deixaria sua loja sem vitrine e sem vendedor?
                    </h2>
                    <p class="text-xs sm:text-sm mt-1.5 max-w-lg mx-auto text-stone-600">
                        A maioria dos profissionais coloca uma lista confusa de botões na bio e perde mais de 80% das vendas. Nós transformamos seu perfil em uma loja irresistível.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
                    <!-- Antes Card -->
                    <div class="flashlight-card p-6 sm:p-7 bg-stone-50 border border-stone-200">
                        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-stone-500 block mb-3">
                            ✕ Como a maioria faz hoje
                        </span>
                        <h3 class="text-lg font-bold font-display mb-3 text-stone-950">Vinte links empilhados e cliente perdido.</h3>
                        <ul class="space-y-2 text-xs sm:text-sm text-stone-600">
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>O seguidor clica no link e não sabe para onde olhar</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Ninguém atende ou tira as dúvidas dele na hora</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>A pessoa fecha a página e você perde o cliente para sempre</span>
                            </li>
                        </ul>
                    </div>

                    <!-- Depois Card -->
                    <div class="flashlight-card p-6 sm:p-7 bg-[#141311] text-white border border-[#d6bc8c]/50 shadow-lg">
                        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-[#d6bc8c] block mb-3">
                            ✓ Com ELOOO VITRINE PREMIUM
                        </span>
                        <h3 class="text-lg font-bold font-display mb-3 text-[#f6e3c5]">Vitrine impecável + IA Vendedora 24h.</h3>
                        <ul class="space-y-2 text-xs sm:text-sm text-stone-200">
                            <li class="flex items-start gap-2">
                                <span class="text-[#d6bc8c] font-bold">✓</span>
                                <span>Vitrine de alto padrão que valoriza seus produtos</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-[#d6bc8c] font-bold">✓</span>
                                <span>IA que atende o cliente, qualifica e fecha a venda</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-[#d6bc8c] font-bold">✓</span>
                                <span>Configuração 100% feita por nossa equipe em 24h</span>
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Section Action CTA Button -->
                <div class="mt-8 text-center">
                    <a href="cadastrar.html" class="btn-gold-luxury px-8 py-3.5 text-xs font-mono font-bold uppercase tracking-widest">
                        <span>Quero a equipe ELOOO montando minha vitrine →</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- COMO FUNCIONA (4 Passos do Done-For-You em 24h) -->
        <section class="py-12 sm:py-16 px-5 section-gold-warm" id="como">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-8">
                    <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                        Como funciona a entrega da sua Vitrine em 24 horas.
                    </h2>
                    <p class="text-xs sm:text-sm mt-1 text-stone-600 font-medium">
                        Zero esforço técnico para você. Toda a execução profissional é por nossa conta.
                    </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
                    <!-- Passo 1 -->
                    <div class="flashlight-card p-5 bg-white">
                        <div class="text-xl font-display font-bold text-[#b89445] mb-2">01</div>
                        <h3 class="text-sm font-bold font-display text-stone-950 mb-1">Você envia os dados</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            Você nos passa suas fotos, produtos, livros, serviços e links de venda em 2 minutos.
                        </p>
                    </div>

                    <!-- Passo 2 -->
                    <div class="flashlight-card p-5 bg-white">
                        <div class="text-xl font-display font-bold text-[#b89445] mb-2">02</div>
                        <h3 class="text-sm font-bold font-display text-stone-950 mb-1">Nós criamos tudo</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            Nossa equipe monta sua Vitrine Premium e treina sua IA Vendedora com precisão.
                        </p>
                    </div>

                    <!-- Passo 3 -->
                    <div class="flashlight-card p-5 bg-stone-900 text-white border-[#d6bc8c]/60">
                        <div class="text-xl font-display font-bold text-[#d6bc8c] mb-2">03</div>
                        <h3 class="text-sm font-bold font-display text-white mb-1">No ar em 24h</h3>
                        <p class="text-xs text-stone-300 leading-relaxed">
                            Em até 24 horas sua Vitrine Oficial está pronta para receber visitas.
                        </p>
                    </div>

                    <!-- Passo 4 -->
                    <div class="flashlight-card p-5 bg-white">
                        <div class="text-xl font-display font-bold text-[#b89445] mb-2">04</div>
                        <h3 class="text-sm font-bold font-display text-stone-950 mb-1">A IA vende 24h</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            Seus visitantes são atendidos e tomam decisões de compra dia e noite no automático.
                        </p>
                    </div>
                </div>

                <!-- Section Action CTA Button -->
                <div class="mt-8 text-center">
                    <a href="cadastrar.html" class="btn-gold-luxury px-8 py-3.5 text-xs font-mono font-bold uppercase tracking-widest">
                        <span>Iniciar Minha Vitrine Premium em 24h →</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- DEMO INTERATIVA (IA QUE ATENDE E VENDE) -->
        <section class="py-12 sm:py-16 px-5 bg-white border-t border-b border-stone-300" id="demo">
            <div class="max-w-4xl mx-auto">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10 items-start">
                    <div>
                        <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                            Experimente a IA que atende e vende no automático.
                        </h2>
                        <p class="text-xs sm:text-sm mt-3 text-stone-600 leading-relaxed">
                            Veja como sua IA Vendedora atua com cada seguidor. Ela qualifica a dor de cada pessoa e indica exatamente o seu produto ou mentoria que vai resolver o problema dela.
                        </p>

                        <div class="mt-6">
                            <a href="cadastrar.html" class="btn-gold-luxury px-8 py-3.5 text-xs font-mono font-bold uppercase tracking-widest">
                                <span>Quero Minha IA Vendedora Treinada →</span>
                            </a>
                        </div>
                    </div>

                    <!-- Interactive Concierge Widget -->
                    <div class="flashlight-card p-5 sm:p-6" id="concierge-widget">
                        <!-- Step 1 -->
                        <div id="quiz-step-1" class="quiz-step">
                            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-[#b89445] mb-1">Passo 1 de 3</p>
                            <h3 class="text-base font-bold font-display text-stone-950 mb-3">Como você está no seu negócio hoje?</h3>
                            <div class="space-y-2">
                                <button onclick="nextQuizStep(1, 'Estou começando')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Estou começando agora</span>
                                    <span class="text-stone-400 group-hover:text-[#d6bc8c]">→</span>
                                </button>
                                <button onclick="nextQuizStep(1, 'Vendo sem previsibilidade')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Vendo, mas sem consistência</span>
                                    <span class="text-stone-400 group-hover:text-[#d6bc8c]">→</span>
                                </button>
                                <button onclick="nextQuizStep(1, 'Quero escala')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Já faturo alto, quero escala</span>
                                    <span class="text-stone-400 group-hover:text-[#d6bc8c]">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 2 -->
                        <div id="quiz-step-2" class="quiz-step hidden">
                            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-[#b89445] mb-1">Passo 2 de 3</p>
                            <h3 class="text-base font-bold font-display text-stone-950 mb-3">Qual seu objetivo principal agora?</h3>
                            <div class="space-y-2">
                                <button onclick="nextQuizStep(2, 'Atrair clientes qualificados')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Atrair clientes de alto valor</span>
                                    <span class="text-stone-400 group-hover:text-[#d6bc8c]">→</span>
                                </button>
                                <button onclick="nextQuizStep(2, 'Automatizar 24h')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Automatizar vendas 24h</span>
                                    <span class="text-stone-400 group-hover:text-[#d6bc8c]">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 3 -->
                        <div id="quiz-step-3" class="quiz-step hidden">
                            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-[#b89445] mb-1">Passo 3 de 3</p>
                            <h3 class="text-base font-bold font-display text-stone-950 mb-3">Qual sua faixa de faturamento mensal?</h3>
                            <div class="space-y-2">
                                <button onclick="finishQuiz('Até 10k')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Até R$ 10.000 / mês</span>
                                    <span class="text-stone-400 group-hover:text-[#d6bc8c]">→</span>
                                </button>
                                <button onclick="finishQuiz('Acima de 10k')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Mais de R$ 10.000 / mês</span>
                                    <span class="text-stone-400 group-hover:text-[#d6bc8c]">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Result -->
                        <div id="quiz-result" class="quiz-step hidden text-center py-2">
                            <div class="w-10 h-10 rounded-full bg-amber-100 text-stone-900 flex items-center justify-center mx-auto mb-2 text-xl border border-amber-300">
                                <iconify-icon icon="solar:check-circle-bold" class="text-amber-700"></iconify-icon>
                            </div>
                            <h4 class="text-base font-bold font-display text-stone-950">Plano Recomendado: ELOOO VITRINE Pró (R$ 147/mês)</h4>
                            <p class="text-xs text-stone-600 mt-1 mb-4">
                                Vitrine Premium + IA que Atende e Vende implementada e treinada por nossa equipe em até 24 horas.
                            </p>
                            <a href="cadastrar.html?plan=pro" class="btn-gold-luxury w-full py-4 text-xs font-mono font-bold uppercase tracking-widest text-center shadow-lg">
                                Contratar Plano Pró (Entrega 24h) →
                            </a>
                            <button onclick="resetQuiz()" class="mt-2.5 text-[11px] text-stone-500 hover:text-stone-950 underline">
                                Refazer teste
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- AGENDA INTEGRADA (EXCLUSIVO PLANO ELITE 497 - CONFIGURADO POR NÓS) -->
        <section class="py-12 sm:py-16 px-5 section-gold-luxury" id="agenda">
            <div class="max-w-4xl mx-auto">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10 items-center">
                    <div>
                        <!-- Exclusive Elite Badge -->
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#d6bc8c]/20 border border-[#d6bc8c]/40 text-[#f6e3c5] text-[10.5px] font-mono font-bold uppercase tracking-wider mb-3">
                            <iconify-icon icon="solar:crown-line-duotone" class="text-[#d6bc8c]"></iconify-icon>
                            <span>EXCLUSIVO DO PLANO ELITE (R$ 497/mês)</span>
                        </div>

                        <h2 class="text-2xl sm:text-3xl font-bold font-display text-white leading-tight">
                            Nós configuramos sua agenda completa.
                        </h2>
                        <p class="text-xs sm:text-sm mt-3 text-stone-300 leading-relaxed font-light">
                            No <strong class="text-[#d6bc8c] font-semibold">Plano Elite</strong>, além da Vitrine Premium e da IA Vendedora, nossa equipe cadastra seus horários disponíveis e valores. O cliente escolhe a data e marca a consulta direto na sua vitrine.
                        </p>

                        <div class="mt-6">
                            <a href="cadastrar.html?plan=elite" class="btn-gold-luxury px-8 py-4 text-xs font-mono font-bold uppercase tracking-widest">
                                <span>Contratar Plano Elite (Setup 24h) →</span>
                            </a>
                        </div>
                    </div>

                    <!-- Clean Calendar Preview -->
                    <div class="flashlight-card p-5 max-w-sm mx-auto w-full bg-[#141311] text-white border border-[#d6bc8c]/40">
                        <div class="flex items-center justify-between mb-3 pb-2.5 border-b border-white/10">
                            <span class="text-xs font-bold font-display text-white uppercase tracking-wider">Junho 2026</span>
                            <span class="text-[10px] font-mono text-[#d6bc8c] bg-[#d6bc8c]/10 px-2 py-0.5 rounded">Plano Elite</span>
                        </div>

                        <div class="grid grid-cols-7 gap-1 text-center text-[10px] font-mono font-bold text-stone-500 mb-2">
                            <div>D</div><div>S</div><div>T</div><div>Q</div><div>Q</div><div>S</div><div>S</div>
                        </div>

                        <div class="grid grid-cols-7 gap-1 text-center text-xs font-medium">
                            <div class="py-1 text-stone-600">31</div>
                            <button class="py-1 rounded bg-white/5 hover:bg-white/10">1</button>
                            <button class="py-1 rounded bg-white/5 hover:bg-white/10">2</button>
                            <div class="py-1 text-stone-600 line-through">3</div>
                            <button class="py-1 rounded bg-white/5 hover:bg-white/10">4</button>
                            <button class="py-1 rounded bg-white/5 hover:bg-white/10">5</button>
                            <div class="py-1 text-stone-600">6</div>
                            <div class="py-1 text-stone-600">7</div>
                            <button class="py-1 rounded bg-white/5 hover:bg-white/10">8</button>
                            <div class="py-1 text-stone-600 line-through">9</div>
                            <button class="py-1 rounded bg-[#d6bc8c] text-black font-bold">10</button>
                            <button class="py-1 rounded bg-white/5 hover:bg-white/10">11</button>
                            <button class="py-1 rounded bg-white/5 hover:bg-white/10">12</button>
                            <div class="py-1 text-stone-600">13</div>
                        </div>

                        <div class="mt-3.5 pt-2.5 border-t border-white/10">
                            <p class="text-[10px] font-mono font-bold text-[#d6bc8c] mb-1.5">Horários Disponíveis (10 de Junho)</p>
                            <div class="grid grid-cols-3 gap-1.5 text-xs font-semibold">
                                <button class="py-1 rounded bg-white/5 text-stone-300">09:00</button>
                                <button class="py-1 rounded bg-[#d6bc8c] text-black font-bold">10:30</button>
                                <button class="py-1 rounded bg-white/5 text-stone-300">14:00</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- PLANOS & PREÇOS (BASIC 127 / PRÓ 147 / ELITE 497) -->
        <section class="py-12 sm:py-20 px-5 bg-white" id="planos">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-10">
                    <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#8c6e26] block mb-1">
                        IMPLEMENTAÇÃO 100% FEITA PELA NOSSA EQUIPE EM 24 HORAS
                    </span>
                    <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                        Escolha seu plano. Sua Vitrine no ar em 24h.
                    </h2>
                    <p class="text-xs sm:text-sm mt-1 text-stone-600">
                        Você fornece os dados e nós configuramos tudo. Sem esforço técnico e com 7 dias de garantia incondicional.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-5 max-w-4xl mx-auto items-stretch">
                    
                    <!-- Basic 127 -->
                    <div class="flashlight-card p-6 sm:p-7 flex flex-col justify-between border border-stone-200">
                        <div>
                            <span class="text-[10.5px] font-mono uppercase font-bold text-stone-400">Vitrine Premium Básica</span>
                            <h3 class="text-xl font-bold font-display text-stone-950 mt-0.5">Basic</h3>
                            <p class="text-xs text-stone-500 mt-0.5 mb-4">Sua vitrine montada por nós.</p>
                            
                            <div class="mb-4">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-extrabold font-display text-stone-950">R$ 127</span>
                                    <span class="text-xs text-stone-500 font-medium">/mês</span>
                                </div>
                                <p class="text-[10.5px] text-[#8c6e26] font-mono font-bold mt-1">✦ Entrega completa em até 24h</p>
                            </div>

                            <ul class="space-y-2 mb-6 text-xs text-stone-700">
                                <li class="flex items-center gap-2 font-semibold text-stone-900">✓ Nós montamos sua Vitrine Premium</li>
                                <li class="flex items-center gap-2">✓ Cadastro de produtos & serviços</li>
                                <li class="flex items-center gap-2">✓ Direcionamento para link de vendas</li>
                                <li class="flex items-center gap-2">✓ Zero trabalho técnico para você</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=basic" class="btn-gold-luxury w-full py-3.5 text-xs font-mono font-bold uppercase tracking-widest text-center shadow-md">
                            Contratar Basic (24h) →
                        </a>
                    </div>

                    <!-- Pro 147 (MAIS VENDIDO - VITRINE + IA QUE ATENDE E VENDE) -->
                    <div class="flashlight-card p-6 sm:p-7 flex flex-col justify-between bg-[#11100E] text-white relative shadow-2xl scale-[1.02] border-2 border-[#d6bc8c]">
                        
                        <div>
                            <!-- MAIS VENDIDO BADGE -->
                            <div class="mb-3">
                                <div class="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full text-[10.5px] font-mono font-bold uppercase tracking-wider bg-gradient-to-r from-[#d6bc8c] via-[#faeac7] to-[#d6bc8c] text-stone-950 shadow-md">
                                    <iconify-icon icon="solar:star-bold" class="text-stone-950"></iconify-icon>
                                    <span>MAIS VENDIDO</span>
                                </div>
                            </div>

                            <span class="text-[10.5px] font-mono uppercase font-bold text-[#d6bc8c]">Vitrine + IA Vendedora 24h</span>
                            <h3 class="text-2xl font-bold font-display text-white mt-0.5">Pró</h3>
                            <p class="text-xs text-stone-400 mt-0.5 mb-4">Vitrine Premium + IA treinada por especialistas.</p>
                            
                            <div class="mb-4">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-4xl font-extrabold font-display text-white">R$ 147</span>
                                    <span class="text-xs text-stone-400 font-medium">/mês</span>
                                </div>
                                <p class="text-[10.5px] text-[#f6e3c5] font-mono font-bold mt-1">✦ Entrega completa em até 24h</p>
                            </div>

                            <ul class="space-y-2 mb-6 text-xs text-stone-200">
                                <li class="flex items-center gap-2 font-bold text-[#d6bc8c]">✓ Tudo do Plano Basic</li>
                                <li class="flex items-center gap-2 font-semibold text-white">✓ IA que Atende e Vende 24h/dia</li>
                                <li class="flex items-center gap-2">✓ Qualificação automática de seguidores</li>
                                <li class="flex items-center gap-2">✓ Métricas e relatórios de conversão</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=pro" class="btn-gold-luxury w-full py-4 text-xs sm:text-sm font-mono font-bold uppercase tracking-widest text-center shadow-xl">
                            Contratar Plano Pró (24h) →
                        </a>
                    </div>

                    <!-- Elite 497 (VITRINE + IA + AGENDA INTEGRADA) -->
                    <div class="flashlight-card p-6 sm:p-7 flex flex-col justify-between border border-stone-200">
                        <div>
                            <span class="text-[10.5px] font-mono uppercase font-bold text-[#b89445]">Setup Executivo Total</span>
                            <h3 class="text-xl font-bold font-display text-stone-950 mt-0.5">Elite</h3>
                            <p class="text-xs text-stone-500 mt-0.5 mb-4">Vitrine + IA Vendedora + Agenda Marcada.</p>
                            
                            <div class="mb-4">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-extrabold font-display text-stone-950">R$ 497</span>
                                    <span class="text-xs text-stone-500 font-medium">/mês</span>
                                </div>
                                <p class="text-[10.5px] text-[#8c6e26] font-mono font-bold mt-1">✦ Entrega completa em até 24h</p>
                            </div>

                            <ul class="space-y-2 mb-6 text-xs text-stone-700">
                                <li class="flex items-center gap-2 font-semibold text-stone-900">✓ Tudo do Plano Pró</li>
                                <li class="flex items-center gap-2 font-bold text-[#8c6e26]">✓ Nós configuramos sua Agenda Integrada</li>
                                <li class="flex items-center gap-2">✓ IA Vendedora com regras estendidas</li>
                                <li class="flex items-center gap-2">✓ Suporte prioritário via WhatsApp</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=elite" class="btn-gold-luxury w-full py-3.5 text-xs font-mono font-bold uppercase tracking-widest text-center shadow-md">
                            Contratar Elite (24h) →
                        </a>
                    </div>

                </div>

                <!-- Garantia 7 Dias -->
                <div class="max-w-4xl mx-auto mt-8 text-center">
                    <p class="text-xs text-stone-600 font-medium flex items-center justify-center gap-2">
                        <iconify-icon icon="solar:shield-check-bold" class="text-stone-800 text-base"></iconify-icon>
                        <span>Garantia incondicional de 7 dias — receba sua vitrine pronta e se não amar, devolvemos 100% do valor.</span>
                    </p>
                </div>
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer class="py-8 px-6 text-center text-xs text-stone-500 bg-white border-t border-stone-300">
        <p>© 2026 <strong class="text-stone-900">ELOOO VITRINE PREMIUM</strong> · Ecossistema <strong class="text-stone-900">ELOOO International Group</strong>.</p>
        <div class="flex items-center justify-center gap-6 mt-2.5 font-mono">
            <a class="hover:text-stone-900 transition-colors" href="termos.html">Termos</a>
            <a class="hover:text-stone-900 transition-colors" href="privacidade.html">Privacidade</a>
            <a href="https://wa.me/5547988660791" target="_blank" rel="noopener noreferrer" class="hover:text-stone-900 transition-colors">WhatsApp Suporte</a>
            <a href="mailto:contato@elooo.com.br" class="hover:text-stone-900 transition-colors">contato@elooo.com.br</a>
        </div>
    </footer>

    <!-- LIGHTWEIGHT SCRIPT (GRADE A SPEED) -->
    <script>
        // Flashlight mouse tracking on cards
        document.querySelectorAll('.flashlight-card').forEach(card => {
            card.addEventListener('mousemove', e => {
                const rect = card.getBoundingClientRect();
                card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
                card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
            });
        });

        // Luxury Drawer Toggle
        const drawer = document.getElementById('luxury-drawer');
        const drawerContent = document.getElementById('luxury-drawer-content');
        const openBtn = document.getElementById('menu-hamburger-btn');
        const closeBtn = document.getElementById('luxury-drawer-close');
        const drawerLinks = document.querySelectorAll('.drawer-link');

        function openDrawer() {
            drawer.classList.remove('opacity-0', 'pointer-events-none');
            drawerContent.classList.remove('translate-x-full');
        }

        function closeDrawer() {
            drawer.classList.add('opacity-0', 'pointer-events-none');
            drawerContent.classList.add('translate-x-full');
        }

        if (openBtn) openBtn.addEventListener('click', openDrawer);
        if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
        drawer.addEventListener('click', (e) => {
            if (e.target === drawer) closeDrawer();
        });
        drawerLinks.forEach(l => l.addEventListener('click', closeDrawer));

        // Counter Animation
        document.addEventListener('DOMContentLoaded', () => {
            const counters = document.querySelectorAll('.counter');
            counters.forEach(counter => {
                const target = +counter.getAttribute('data-target');
                let count = 0;
                const speed = target / 25;
                const update = () => {
                    count += speed;
                    if (count < target) {
                        counter.innerText = Math.ceil(count);
                        setTimeout(update, 35);
                    } else {
                        counter.innerText = target.toLocaleString('pt-BR');
                    }
                };
                update();
            });
        });

        // Quiz Logic
        let quizAnswers = {};

        function nextQuizStep(currentStep, answer) {
            quizAnswers['step' + currentStep] = answer;
            document.getElementById('quiz-step-' + currentStep).classList.add('hidden');
            const next = currentStep + 1;
            const nextEl = document.getElementById('quiz-step-' + next);
            if (nextEl) nextEl.classList.remove('hidden');
        }

        function finishQuiz(answer) {
            quizAnswers['step3'] = answer;
            document.getElementById('quiz-step-3').classList.add('hidden');
            document.getElementById('quiz-result').classList.remove('hidden');
        }

        function resetQuiz() {
            quizAnswers = {};
            document.getElementById('quiz-result').classList.add('hidden');
            document.getElementById('quiz-step-1').classList.remove('hidden');
            document.getElementById('quiz-step-2').classList.add('hidden');
            document.getElementById('quiz-step-3').classList.add('hidden');
        }
    </script>
</body>
</html>
"""

# ----------------------------------------------------
# 2. ENTRAR (src/bio/entrar.html)
# ----------------------------------------------------
ENTRAR_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>Entrar — ELOOO VITRINE PREMIUM</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; }
        .font-display { font-family: 'Space Grotesk', sans-serif; }
        
        @keyframes goldGleam {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes goldShimmerSweep {
            0% { transform: translateX(-150%) skewX(-20deg); }
            100% { transform: translateX(250%) skewX(-20deg); }
        }
        .btn-gold-luxury {
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #d6bc8c 0%, #faeac7 25%, #c5a870 50%, #f5dc9e 75%, #d6bc8c 100%);
            background-size: 250% 250%;
            animation: goldGleam 4s ease infinite;
            color: #12100e !important;
            font-weight: 800;
            border-radius: 9999px;
            border: 1.5px solid #faeac7;
            box-shadow: 0 10px 25px -5px rgba(214, 188, 140, 0.65), 0 0 15px rgba(214, 188, 140, 0.4);
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            cursor: pointer;
            text-decoration: none;
        }
        .btn-gold-luxury::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 60%;
            height: 100%;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.65) 50%, transparent 100%);
            transform: translateX(-150%) skewX(-20deg);
            animation: goldShimmerSweep 3.5s infinite;
            pointer-events: none;
        }
        .btn-gold-luxury:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 15px 35px -5px rgba(214, 188, 140, 0.9);
            border-color: #ffffff;
            color: #000000 !important;
        }
    </style>
</head>
<body class="antialiased min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-md bg-white p-8 sm:p-10 rounded-3xl border border-stone-300 shadow-xl">
        <a href="index.html" class="inline-flex items-center gap-2 mb-6">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO VITRINE PREMIUM" class="h-10 object-contain" style="filter: brightness(0);"/>
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-stone-900">VITRINE PREMIUM</span>
        </a>

        <h1 class="text-2xl font-bold font-display text-stone-950">Acessar sua conta</h1>
        <p class="text-xs text-stone-500 mt-1 mb-6">
            Ainda não tem sua vitrine pronta? <a href="cadastrar.html" class="font-bold underline text-stone-900">Contratar em 24h</a>
        </p>

        <form class="space-y-4" onsubmit="event.preventDefault(); alert('Login efetuado com sucesso! Redirecionando...');">
            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1.5">E-mail</label>
                <input type="email" required placeholder="seu@email.com" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <div>
                <div class="flex justify-between mb-1.5">
                    <label class="text-xs font-bold text-stone-700">Senha</label>
                    <a href="#esqueci" onclick="alert('Instruções enviadas para seu e-mail!')" class="text-xs text-stone-500 hover:underline">Esqueci a senha</a>
                </div>
                <input type="password" required placeholder="••••••••" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <button type="submit" class="btn-gold-luxury w-full py-4 text-xs font-mono font-bold uppercase tracking-widest text-center mt-2 shadow-lg">
                Entrar no Painel →
            </button>
        </form>

        <div class="mt-6 text-center">
            <a href="index.html" class="text-xs text-stone-500 hover:text-stone-950 underline">← Voltar à página inicial</a>
        </div>
    </div>
</body>
</html>
"""

# ----------------------------------------------------
# 3. CADASTRAR (src/bio/cadastrar.html)
# ----------------------------------------------------
CADASTRAR_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>Contratar Vitrine Premium — ELOOO (No Ar em 24h)</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; }
        .font-display { font-family: 'Space Grotesk', sans-serif; }
        
        @keyframes goldGleam {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes goldShimmerSweep {
            0% { transform: translateX(-150%) skewX(-20deg); }
            100% { transform: translateX(250%) skewX(-20deg); }
        }
        .btn-gold-luxury {
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #d6bc8c 0%, #faeac7 25%, #c5a870 50%, #f5dc9e 75%, #d6bc8c 100%);
            background-size: 250% 250%;
            animation: goldGleam 4s ease infinite;
            color: #12100e !important;
            font-weight: 800;
            border-radius: 9999px;
            border: 1.5px solid #faeac7;
            box-shadow: 0 10px 25px -5px rgba(214, 188, 140, 0.65), 0 0 15px rgba(214, 188, 140, 0.4);
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            cursor: pointer;
            text-decoration: none;
        }
        .btn-gold-luxury::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 60%;
            height: 100%;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.65) 50%, transparent 100%);
            transform: translateX(-150%) skewX(-20deg);
            animation: goldShimmerSweep 3.5s infinite;
            pointer-events: none;
        }
        .btn-gold-luxury:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 15px 35px -5px rgba(214, 188, 140, 0.9);
            border-color: #ffffff;
            color: #000000 !important;
        }
    </style>
</head>
<body class="antialiased min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-md bg-white p-8 sm:p-10 rounded-3xl border border-stone-300 shadow-xl">
        <a href="index.html" class="inline-flex items-center gap-2 mb-4">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO VITRINE PREMIUM" class="h-10 object-contain" style="filter: brightness(0);"/>
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-stone-900">VITRINE PREMIUM</span>
        </a>

        <div class="mb-4">
            <h1 class="text-2xl font-bold font-display text-stone-950 mt-1">Sua Vitrine + IA em 24h</h1>
            <p class="text-xs text-stone-500 mt-1">
                Após assinar, nossa equipe entrará em contato para receber seus dados e colocar sua Vitrine Premium no ar.
            </p>
        </div>

        <!-- Plan Selector Bar (Basic 127 / Pro 147 / Elite 497) -->
        <div class="mb-5 p-1 rounded-2xl bg-stone-100 grid grid-cols-3 gap-1 text-xs font-bold text-center">
            <button type="button" onclick="selectPlan('basic')" id="btn-basic" class="py-2.5 rounded-xl transition-all text-stone-600">Basic R$127</button>
            <button type="button" onclick="selectPlan('pro')" id="btn-pro" class="py-2.5 rounded-xl bg-gradient-to-r from-[#d6bc8c] via-[#faeac7] to-[#d6bc8c] text-stone-950 shadow-md border border-[#c5a870] font-bold transition-all">Pró R$147</button>
            <button type="button" onclick="selectPlan('elite')" id="btn-elite" class="py-2.5 rounded-xl transition-all text-stone-600">Elite R$497</button>
        </div>

        <form class="space-y-3.5" onsubmit="event.preventDefault(); window.location.href='https://wa.me/5547988660791?text=Ol%C3%A1%2C%20acabei%20de%20assinar%20o%20ELOOO%20VITRINE%20PREMIUM%20e%20quero%20enviar%20minhas%20informa%C3%A7%C3%B5es%20para%20colocar%20minha%20vitrine%20no%20ar%20em%2024h.';">
            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Nome Completo</label>
                <input type="text" required placeholder="Seu nome completo" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Usuário desejado na sua Vitrine</label>
                <div class="flex items-center rounded-xl bg-stone-50 border border-stone-300 focus-within:border-stone-900 overflow-hidden">
                    <span class="px-3 text-xs text-stone-400 font-mono">premium.elooo.com.br/</span>
                    <input type="text" required placeholder="seunome" class="w-full py-3 pr-4 text-sm bg-transparent outline-none"/>
                </div>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Seu WhatsApp</label>
                <input type="tel" required placeholder="(DDD) 99999-9999" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">E-mail de Contato</label>
                <input type="email" required placeholder="seu@email.com" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <button type="submit" class="btn-gold-luxury w-full py-4 text-xs sm:text-sm font-mono font-bold uppercase tracking-widest text-center mt-2 shadow-xl">
                Contratar e Iniciar Implementação (24h) →
            </button>
        </form>

        <div class="mt-6 text-center">
            <a href="index.html" class="text-xs text-stone-400 hover:text-stone-900 underline">← Voltar à página inicial</a>
        </div>
    </div>

    <script>
        function selectPlan(plan) {
            const btns = {
                basic: document.getElementById('btn-basic'),
                pro: document.getElementById('btn-pro'),
                elite: document.getElementById('btn-elite')
            };
            for (let k in btns) {
                btns[k].className = 'py-2.5 rounded-xl transition-all text-stone-600 font-medium';
            }
            if (btns[plan]) {
                btns[plan].className = 'py-2.5 rounded-xl bg-gradient-to-r from-[#d6bc8c] via-[#faeac7] to-[#d6bc8c] text-stone-950 shadow-md border border-[#c5a870] font-bold transition-all';
            }
        }
        const urlParams = new URLSearchParams(window.location.search);
        let planParam = urlParams.get('plan');
        if (planParam === 'starter') planParam = 'basic';
        if (planParam && ['basic', 'pro', 'elite'].includes(planParam)) {
            selectPlan(planParam);
        }
    </script>
</body>
</html>
"""

# ----------------------------------------------------
# 4. TERMOS (src/bio/termos.html)
# ----------------------------------------------------
TERMOS_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>Termos de Uso — ELOOO VITRINE PREMIUM</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; } .font-display { font-family: 'Space Grotesk', sans-serif; }</style>
</head>
<body class="antialiased min-h-screen">
    <header class="border-b border-stone-300 px-6 py-4 flex items-center justify-between bg-white">
        <a class="flex items-center gap-2" href="index.html">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO VITRINE PREMIUM" class="h-8 object-contain" style="filter: brightness(0);"/>
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-stone-900">VITRINE PREMIUM</span>
        </a>
        <a class="text-xs text-stone-500 hover:text-stone-950 underline" href="index.html">← Voltar</a>
    </header>

    <main class="max-w-2xl mx-auto px-6 py-12">
        <h1 class="text-2xl font-bold font-display text-stone-950 mb-1">Termos de Uso & Entrega em 24h</h1>
        <p class="text-xs text-stone-500 mb-6 font-mono">Última atualização: 18 de agosto de 2026</p>

        <div class="space-y-6 text-sm text-stone-700 leading-relaxed bg-white p-8 rounded-3xl border border-stone-300 shadow-sm">
            <section>
                <h2 class="font-bold font-display text-stone-950 mb-1">1. Serviço de Implementação</h2>
                <p>O serviço do ELOOO VITRINE PREMIUM inclui a implementação técnica completa da sua Vitrine Premium e o treinamento da sua IA Vendedora por nossa equipe especializada em até 24 horas úteis após o envio das informações.</p>
            </section>
            <section>
                <h2 class="font-bold font-display text-stone-950 mb-1">2. Garantia de 7 Dias</h2>
                <p>Todos os planos contam com garantia incondicional de reembolso total em até 7 dias a contar da ativação.</p>
            </section>
            <section>
                <h2 class="font-bold font-display text-stone-950 mb-1">3. Suporte</h2>
                <p>WhatsApp: <a href="https://wa.me/5547988660791" class="underline font-semibold">+55 (47) 98866-0791</a> · E-mail: contato@elooo.com.br</p>
            </section>
        </div>
    </main>
</body>
</html>
"""

# ----------------------------------------------------
# 5. PRIVACIDADE (src/bio/privacidade.html)
# ----------------------------------------------------
PRIVACIDADE_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>Política de Privacidade — ELOOO VITRINE PREMIUM</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; } .font-display { font-family: 'Space Grotesk', sans-serif; }</style>
</head>
<body class="antialiased min-h-screen">
    <header class="border-b border-stone-300 px-6 py-4 flex items-center justify-between bg-white">
        <a class="flex items-center gap-2" href="index.html">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO VITRINE PREMIUM" class="h-8 object-contain" style="filter: brightness(0);"/>
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-stone-900">VITRINE PREMIUM</span>
        </a>
        <a class="text-xs text-stone-500 hover:text-stone-950 underline" href="index.html">← Voltar</a>
    </header>

    <main class="max-w-2xl mx-auto px-6 py-12">
        <h1 class="text-2xl font-bold font-display text-stone-950 mb-1">Política de Privacidade</h1>
        <p class="text-xs text-stone-500 mb-6 font-mono">Última atualização: 18 de agosto de 2026</p>

        <div class="space-y-6 text-sm text-stone-700 leading-relaxed bg-white p-8 rounded-3xl border border-stone-300 shadow-sm">
            <section>
                <h2 class="font-bold font-display text-stone-950 mb-1">1. Segurança dos Dados</h2>
                <p>Tratamos todos os dados coletados com respeito às normas da LGPD e com criptografia de ponta.</p>
            </section>
            <section>
                <h2 class="font-bold font-display text-stone-950 mb-1">2. Propriedade dos Contatos</h2>
                <p>Os contatos e clientes da sua vitrine pertencem 100% a você.</p>
            </section>
        </div>
    </main>
</body>
</html>
"""

# ----------------------------------------------------
# 6. VITRINE BRUNO BARROS (src/bio/brunobarros.html)
# ----------------------------------------------------
BRUNO_BARROS_BIO_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>Bruno Barros | Vitrine Premium Oficial</title>
    <meta name="description" content="Fundador da ELOOO International Group, escritor e mentor."/>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: #0E0D0C;
            color: #ffffff;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }
        .font-display { font-family: 'Space Grotesk', sans-serif; }

        .netflix-scroll {
            display: flex;
            gap: 12px;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scrollbar-width: none;
            -ms-overflow-style: none;
            padding-bottom: 8px;
        }
        .netflix-scroll::-webkit-scrollbar { display: none; }

        .bio-btn {
            background: rgba(26, 25, 23, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(16px);
            transition: all 0.2s ease;
        }
        .bio-btn:hover {
            transform: translateY(-1px);
            border-color: #d6bc8c;
            background: rgba(38, 36, 33, 0.95);
        }
    </style>
</head>
<body class="min-h-screen flex flex-col items-center py-8 px-4 relative">

    <div class="w-full max-w-[400px] space-y-4">
        
        <!-- Profile Header -->
        <div class="text-center flex flex-col items-center mb-4">
            <div class="w-24 h-24 rounded-full overflow-hidden border-2 border-[#d6bc8c] shadow-xl mb-3 bg-stone-900">
                <img src="static/images/bruno-barros.png" alt="Bruno Barros" class="w-full h-full object-cover object-top" onerror="this.src='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=300&auto=format&fit=crop';"/>
            </div>
            
            <h1 class="text-2xl font-bold font-display text-white tracking-tight">Bruno Barros</h1>
            <p class="text-xs text-stone-400 mt-0.5 max-w-xs leading-relaxed">
                Autor, Mentor & Fundador da ELOOO International Group
            </p>
        </div>

        <!-- Social Icons Row -->
        <div class="flex justify-center gap-3 py-1">
            <a href="https://instagram.com/oficialbrunobarros" target="_blank" class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center text-stone-200 text-lg hover:bg-stone-800 hover:text-amber-300 transition-colors">
                <iconify-icon icon="solar:camera-linear"></iconify-icon>
            </a>
            <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20Bruno!%20Vim%20pela%20sua%20vitrine%20e%20quero%20conversar." target="_blank" class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center text-stone-200 text-lg hover:bg-emerald-600 transition-colors">
                <iconify-icon icon="ic:baseline-whatsapp"></iconify-icon>
            </a>
            <a href="https://youtube.com" target="_blank" class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center text-stone-200 text-lg hover:bg-red-600 transition-colors">
                <iconify-icon icon="solar:play-circle-linear"></iconify-icon>
            </a>
        </div>

        <!-- IA Vendedora Direct Action -->
        <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20Bruno!%20Quero%20fazer%20meu%20diagn%C3%B3stico%20editorial." target="_blank" class="bio-btn w-full p-4 rounded-2xl flex items-center gap-3.5 text-left shadow-lg border border-amber-400/40">
            <div class="w-11 h-11 rounded-xl bg-amber-400/20 text-amber-300 flex items-center justify-center text-xl flex-none">
                <iconify-icon icon="solar:bolt-circle-bold"></iconify-icon>
            </div>
            <div class="flex-1 min-w-0">
                <p class="font-bold text-sm text-white leading-tight">Diagnóstico Editorial com IA</p>
                <p class="text-xs text-stone-400 mt-0.5">Descubra o próximo passo para o seu livro</p>
            </div>
            <div class="text-amber-300 text-sm">→</div>
        </a>

        <!-- Horizontal Netflix Carousel -->
        <div class="pt-2">
            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-stone-400 mb-2.5">
                VITRINE DE PROJETOS & LIVROS
            </p>

            <div class="netflix-scroll">
                <!-- Card 1: Livro -->
                <div class="w-[145px] flex-none rounded-2xl overflow-hidden bg-stone-900 border border-white/10 p-2.5 flex flex-col justify-between">
                    <div>
                        <div class="w-full aspect-[4/5] rounded-xl overflow-hidden mb-2 bg-stone-800">
                            <img src="static/images/recalculando-cover.png" onerror="this.src='static/images/bruno-barros.png';" class="w-full h-full object-cover"/>
                        </div>
                        <p class="text-xs font-bold font-display text-white leading-tight">VIDANOVA & AUTORALIDADE</p>
                        <p class="text-[10px] text-stone-400 mt-0.5">Livro Oficial</p>
                    </div>
                    <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20gostaria%20de%20adquirir%20o%20livro%20do%20Bruno%20Barros." target="_blank" class="block text-center mt-2.5 text-[9px] font-bold uppercase tracking-wider py-1.5 rounded-lg bg-white/10 hover:bg-[#d6bc8c] hover:text-black text-stone-200 transition-colors">
                        Adquirir
                    </a>
                </div>

                <!-- Card 2: Editora -->
                <div class="w-[145px] flex-none rounded-2xl overflow-hidden bg-stone-900 border border-white/10 p-2.5 flex flex-col justify-between">
                    <div>
                        <div class="w-full aspect-[4/5] rounded-xl overflow-hidden mb-2 bg-stone-800 flex items-center justify-center p-3">
                            <img src="static/images/ELOOO LOGO.png" class="w-full object-contain filter brightness-0 invert"/>
                        </div>
                        <p class="text-xs font-bold font-display text-white leading-tight">PUBLICAÇÃO EDITORIAL</p>
                        <p class="text-[10px] text-stone-400 mt-0.5">Editora Internacional</p>
                    </div>
                    <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20quero%20publicar%20meu%20livro." target="_blank" class="block text-center mt-2.5 text-[9px] font-bold uppercase tracking-wider py-1.5 rounded-lg bg-white/10 hover:bg-[#d6bc8c] hover:text-black text-stone-200 transition-colors">
                        Publicar Livro
                    </a>
                </div>

                <!-- Card 3: Mentoria -->
                <div class="w-[145px] flex-none rounded-2xl overflow-hidden bg-stone-900 border border-white/10 p-2.5 flex flex-col justify-between">
                    <div>
                        <div class="w-full aspect-[4/5] rounded-xl overflow-hidden mb-2 bg-stone-800 flex flex-col items-center justify-center p-2 text-center">
                            <iconify-icon icon="solar:crown-line-duotone" class="text-2xl text-amber-400 mb-1"></iconify-icon>
                            <span class="text-[10px] font-bold text-stone-300">MENTORIA</span>
                        </div>
                        <p class="text-xs font-bold font-display text-white leading-tight">MENTORIA VIP</p>
                        <p class="text-[10px] text-stone-400 mt-0.5">Individual</p>
                    </div>
                    <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20quero%20informa%C3%A7%C3%B5es%20da%20Mentoria." target="_blank" class="block text-center mt-2.5 text-[9px] font-bold uppercase tracking-wider py-1.5 rounded-lg bg-white/10 hover:bg-[#d6bc8c] hover:text-black text-stone-200 transition-colors">
                        Candidatura
                    </a>
                </div>
            </div>
        </div>

        <!-- Direct Publishing Button -->
        <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20Bruno!%20Quero%20publicar%20meu%20livro%20pela%20Elooo." target="_blank" class="bio-btn block w-full p-4 rounded-2xl flex items-center gap-3.5 text-left shadow-md">
            <div class="w-10 h-10 rounded-xl bg-stone-800 flex items-center justify-center text-amber-300 text-xl flex-none">
                <iconify-icon icon="solar:book-bookmark-bold"></iconify-icon>
            </div>
            <div class="flex-1 min-w-0">
                <p class="font-bold font-display text-sm text-white leading-tight">QUERO PUBLICAR MEU LIVRO</p>
                <p class="text-xs text-stone-400 mt-0.5">Editora ELOOO | Brasil, Cascais & Madrid</p>
            </div>
            <iconify-icon icon="solar:arrow-right-up-linear" class="text-stone-400 text-sm"></iconify-icon>
        </a>

        <!-- Footer -->
        <div class="pt-6 pb-2 text-center">
            <a href="index.html" class="text-[10px] font-mono font-bold text-stone-500 uppercase tracking-widest hover:text-white">
                Criado com ELOOO VITRINE PREMIUM
            </a>
        </div>

    </div>

</body>
</html>
"""

def generate_all():
    print("Generating ELOOO VITRINE PREMIUM pages with classic phone mockup and clean descriptions...")
    save("src/bio/index.html", LANDING_HTML)
    save("src/bio/entrar.html", ENTRAR_HTML)
    save("src/bio/cadastrar.html", CADASTRAR_HTML)
    save("src/bio/termos.html", TERMOS_HTML)
    save("src/bio/privacidade.html", PRIVACIDADE_HTML)
    save("src/bio/brunobarros.html", BRUNO_BARROS_BIO_HTML)
    save("src/bio/leticia-vaz.html", BRUNO_BARROS_BIO_HTML)
    save("src/bio/demo.html", BRUNO_BARROS_BIO_HTML)
    save("src/bio.html", LANDING_HTML)
    print("All pages generated successfully!")

if __name__ == "__main__":
    generate_all()
