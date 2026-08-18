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
    <title>ELOOO BIO PREMIUM | O Link na Bio Inteligente que Conduz Decisões e Vende no Automático</title>
    <meta name="description" content="Pare de perder vendas com links confusos. O ELOOO BIO PREMIUM qualifica seus visitantes com Inteligência Artificial e recomenda o produto certo."/>
    
    <!-- Open Graph / Meta -->
    <meta property="og:title" content="ELOOO BIO PREMIUM | O Link na Bio que Vende"/>
    <meta property="og:description" content="Página de link na bio de alta conversão. Concierge de IA, vitrine inteligente e agendamento para o plano Elite."/>
    <meta property="og:image" content="static/images/og-share.png"/>
    <meta property="og:type" content="website"/>
    <meta name="theme-color" content="#EAEAE5"/>

    <!-- Exact Fonts from ELOOO Website: Space Grotesk + Inter + JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Iconify -->
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="static/css/linkcommerce_1.css"/>
    <link rel="stylesheet" href="static/css/linkcommerce_2.css"/>

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
        }

        .font-display {
            font-family: 'Space Grotesk', sans-serif;
        }

        /* FLOATING PILL NAVBAR - ULTRA MINIMALIST */
        .glass-nav {
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border: 1px solid rgba(28, 25, 23, 0.08);
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.06), 0 2px 6px rgba(0, 0, 0, 0.02);
        }

        /* FLASHLIGHT HOVER CARD (EXACT ELOOO STANDARD) */
        .flashlight-card {
            position: relative;
            background: #FFFFFF;
            border: 1px solid rgba(28, 25, 23, 0.08);
            border-radius: 24px;
            overflow: hidden;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
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
            transition: opacity 0.3s ease;
        }
        .flashlight-card:hover {
            transform: translateY(-3px);
            border-color: #d6bc8c;
            box-shadow: 0 20px 40px -15px rgba(28, 25, 23, 0.1), 0 0 25px rgba(214, 188, 140, 0.25);
        }
        .flashlight-card:hover::before {
            opacity: 1;
        }

        /* MOVING GOLD BORDER BUTTON (ELOOO GOLD SPIN) */
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        .btn-gold-spin {
            position: relative;
            display: inline-flex;
            overflow: hidden;
            border-radius: 9999px;
            padding: 1.5px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .btn-gold-spin:hover {
            transform: scale(1.02);
            box-shadow: 0 10px 25px -5px rgba(214, 188, 140, 0.45);
        }
        .btn-gold-spin span.spin-border {
            position: absolute;
            inset: -1000%;
            background: conic-gradient(from 90deg at 50% 50%, transparent 0%, rgba(214, 188, 140, 0.95) 50%, transparent 100%);
            animation: spin 3s linear infinite;
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

        /* SMARTPHONE FRAME 3D */
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

    <!-- FLOATING MINIMALIST TOP NAVBAR (DESKTOP & MOBILE HAMBURGER) -->
    <div class="fixed top-3 sm:top-4 inset-x-3 sm:inset-x-6 z-50 flex justify-center pointer-events-none">
        <nav class="pointer-events-auto flex items-center justify-between gap-4 pl-4 pr-3 sm:pl-6 sm:pr-3 py-2.5 rounded-full w-full max-w-4xl glass-nav relative">
            <!-- Brand Logo (Enlarged) -->
            <a class="inline-flex items-center flex-none group" href="index.html">
                <img src="static/images/ELOOO LOGO.png" alt="ELOOO BIO PREMIUM" class="h-9 sm:h-11 object-contain transition-transform group-hover:scale-105" style="filter: brightness(0);"/>
                <span class="ml-3 text-[11px] font-mono font-bold uppercase tracking-[0.2em] text-stone-600 border-l border-stone-300 pl-3">
                    BIO PREMIUM
                </span>
            </a>

            <!-- Right Action: Hamburger + Gold CTA (Sleek on Desktop & Mobile) -->
            <div class="flex items-center gap-2.5 flex-none">
                <a href="cadastrar.html" class="btn-gold-spin">
                    <span class="spin-border"></span>
                    <span class="relative flex items-center justify-center gap-1.5 px-5 py-2.5 rounded-full bg-[#0a0a0a] text-white text-[11px] sm:text-[12px] font-bold uppercase tracking-widest hover:bg-[#151515] transition-colors">
                        <span>Começar</span>
                        <iconify-icon icon="solar:arrow-right-linear" class="text-sm text-amber-300"></iconify-icon>
                    </span>
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
                    <img src="static/images/ELOOO LOGO.png" alt="ELOOO BIO" class="h-8 object-contain" style="filter: brightness(0);"/>
                    <button id="luxury-drawer-close" class="w-8 h-8 rounded-full bg-stone-100 text-stone-800 flex items-center justify-center text-lg hover:bg-stone-200 transition-colors">
                        <iconify-icon icon="solar:close-circle-linear"></iconify-icon>
                    </button>
                </div>

                <!-- Navigation Links -->
                <nav class="space-y-2 font-sans font-bold text-xs uppercase tracking-wider text-stone-700">
                    <a href="#problema" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Por que</a>
                    <a href="#como" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Como funciona</a>
                    <a href="#demo" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Concierge com IA</a>
                    <a href="#agenda" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Agenda (Plano Elite)</a>
                    <a href="#planos" class="drawer-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Planos & Preços</a>
                    <a href="brunobarros.html" target="_blank" class="drawer-link block px-4 py-3 rounded-2xl bg-stone-900 text-white font-bold flex items-center justify-between border border-[#d6bc8c]">
                        <span>Bio Oficial Bruno Barros</span>
                        <iconify-icon icon="solar:arrow-right-up-linear"></iconify-icon>
                    </a>
                </nav>
            </div>

            <!-- Drawer Bottom Actions -->
            <div class="pt-6 border-t border-stone-200 space-y-2.5">
                <a href="entrar.html" class="block w-full py-3 rounded-full text-center text-xs font-bold text-stone-800 bg-stone-100 hover:bg-stone-200 transition-colors uppercase tracking-wider">
                    Fazer Login
                </a>
                <a href="cadastrar.html" class="btn-gold-spin w-full">
                    <span class="spin-border"></span>
                    <span class="relative block w-full py-3.5 rounded-full bg-[#0a0a0a] text-white font-bold text-xs uppercase tracking-widest text-center">
                        Criar Conta Agora →
                    </span>
                </a>
            </div>
        </div>
    </div>

    <!-- MAIN CONTENT -->
    <main class="relative z-10">

        <!-- HERO SECTION (Tight, Direct & SMARTPHONE MOCKUP RIGHT BELOW) -->
        <section class="relative pt-24 pb-10 sm:pt-28 sm:pb-12 overflow-hidden">
            <div class="max-w-4xl mx-auto px-5 text-center relative z-10">
                
                <!-- Main Headline -->
                <h1 class="text-3xl sm:text-5xl lg:text-[54px] font-bold font-display tracking-tight text-stone-900 leading-[1.1] mb-3">
                    O link na bio que entende seu cliente e conduz a venda.
                </h1>

                <!-- Subtitle -->
                <p class="text-sm sm:text-base text-stone-600 max-w-xl mx-auto mb-6 leading-relaxed">
                    Pare de empilhar vinte botões confusos. O <strong class="text-stone-950 font-semibold">ELOOO BIO PREMIUM</strong> qualifica o momento do visitante e recomenda a solução exata com botão de compra direto.
                </p>

                <!-- Hero Action Buttons -->
                <div class="flex flex-col sm:flex-row items-center justify-center gap-3 mb-8">
                    <a href="cadastrar.html" class="btn-gold-spin w-full sm:w-auto shadow-xl">
                        <span class="spin-border"></span>
                        <span class="relative flex items-center justify-center gap-2 px-8 py-3.5 rounded-full bg-[#0a0a0a] text-white text-xs sm:text-sm font-bold uppercase tracking-widest hover:bg-[#151515] transition-colors">
                            <span>Quero vender no automático</span>
                            <iconify-icon icon="solar:arrow-right-linear" class="text-base text-amber-300"></iconify-icon>
                        </span>
                    </a>
                    
                    <a href="brunobarros.html" target="_blank" class="w-full sm:w-auto px-6 py-3.5 rounded-full bg-white text-stone-900 border border-stone-300 hover:border-[#d6bc8c] text-xs sm:text-sm font-bold uppercase tracking-wider transition-all flex items-center justify-center gap-2 shadow-sm">
                        <span>Ver Bio de Bruno Barros</span>
                        <iconify-icon icon="solar:arrow-right-up-linear" class="text-base text-stone-600"></iconify-icon>
                    </a>
                </div>

                <!-- SMARTPHONE MOCKUP (ELEVATED PROMINENTLY) -->
                <div class="flex justify-center mb-10">
                    <div class="w-full max-w-[310px] phone-mockup-wrapper relative">
                        <!-- Dynamic Island -->
                        <div class="absolute top-3 left-1/2 -translate-x-1/2 w-24 h-4 bg-black rounded-full z-20 flex items-center justify-end pr-2">
                            <div class="w-2 h-2 rounded-full bg-[#222]"></div>
                        </div>
                        
                        <!-- Interactive Screen -->
                        <div class="relative rounded-[38px] overflow-hidden h-[540px] bg-stone-950">
                            <iframe src="brunobarros.html" title="Bio Bruno Barros Ao Vivo" class="w-full h-full border-0"></iframe>
                            <a href="brunobarros.html" target="_blank" class="absolute inset-x-0 bottom-0 py-3 bg-gradient-to-t from-black/95 via-black/70 to-transparent backdrop-blur-sm text-center text-xs font-mono font-bold uppercase tracking-widest text-[#f6e3c5] hover:text-white transition-colors">
                                Abrir bio oficial completa →
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Updated Credibility Stats (10 Anos / 1.1 Bi / 10.000 Alunos) -->
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

        <!-- O PROBLEMA (Antes vs Depois) - WITH GOLD ACTION CTA -->
        <section class="py-12 sm:py-16 px-5 bg-white border-t border-b border-stone-300" id="problema">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-8">
                    <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                        Mostrar tudo é o mesmo que não mostrar nada.
                    </h2>
                    <p class="text-xs sm:text-sm mt-1.5 max-w-lg mx-auto text-stone-600">
                        Quanto mais opções empilhadas, mais o cliente trava. O ELOOO BIO PREMIUM <strong class="text-stone-950 font-semibold">conduz</strong> a decisão.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
                    <!-- Antes Card -->
                    <div class="flashlight-card p-6 sm:p-7 bg-stone-50 border border-stone-200">
                        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-stone-500 block mb-3">
                            ✕ Como a maioria faz hoje
                        </span>
                        <h3 class="text-lg font-bold font-display mb-3 text-stone-950">Vinte links confusos e sem direção.</h3>
                        <ul class="space-y-2 text-xs sm:text-sm text-stone-600">
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Opções competindo entre si ao mesmo tempo</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>O visitante não sabe o que faz sentido para ele</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Mais de 80% abandonam sem tomar decisão</span>
                            </li>
                        </ul>
                    </div>

                    <!-- Depois Card -->
                    <div class="flashlight-card p-6 sm:p-7 bg-[#141311] text-white border border-[#d6bc8c]/50 shadow-lg">
                        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-amber-300 block mb-3">
                            ✓ Com ELOOO BIO PREMIUM
                        </span>
                        <h3 class="text-lg font-bold font-display mb-3 text-[#f6e3c5]">Diagnóstico rápido e recomendação certa.</h3>
                        <ul class="space-y-2 text-xs sm:text-sm text-stone-200">
                            <li class="flex items-start gap-2">
                                <span class="text-emerald-400 font-bold">✓</span>
                                <span>3 perguntas rápidas qualificam o visitante</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-emerald-400 font-bold">✓</span>
                                <span>1 recomendação exata com botão de compra direto</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-emerald-400 font-bold">✓</span>
                                <span>Vendas no automático 24h por dia</span>
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Section Action CTA Button -->
                <div class="mt-8 text-center">
                    <a href="cadastrar.html" class="btn-gold-spin">
                        <span class="spin-border"></span>
                        <span class="relative flex items-center justify-center gap-2 px-7 py-3 rounded-full bg-[#0a0a0a] text-white text-xs font-bold uppercase tracking-widest">
                            <span>Quero conduzir minhas vendas →</span>
                        </span>
                    </a>
                </div>
            </div>
        </section>

        <!-- COMO FUNCIONA (4 Passos) - WITH GOLD LUXURY BACKGROUND & ACTION CTA -->
        <section class="py-12 sm:py-16 px-5 section-gold-warm" id="como">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-8">
                    <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                        Quatro passos. Uma máquina de conversão.
                    </h2>
                    <p class="text-xs sm:text-sm mt-1 text-stone-600 font-medium">
                        Simples de configurar. Extremamente poderoso para vender.
                    </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
                    <div class="flashlight-card p-5 bg-white">
                        <div class="text-xl font-display font-bold text-[#b89445] mb-2">01</div>
                        <h3 class="text-sm font-bold font-display text-stone-950 mb-1">Você cadastra</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            Produtos, livros e mentorias com faixas de preço e dor que resolve.
                        </p>
                    </div>

                    <div class="flashlight-card p-5 bg-white">
                        <div class="text-xl font-display font-bold text-[#b89445] mb-2">02</div>
                        <h3 class="text-sm font-bold font-display text-stone-950 mb-1">O cliente responde</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            3 perguntas rápidas e intuitivas direto na sua bio.
                        </p>
                    </div>

                    <div class="flashlight-card p-5 bg-stone-900 text-white border-[#d6bc8c]/60">
                        <div class="text-xl font-display font-bold text-amber-300 mb-2">03</div>
                        <h3 class="text-sm font-bold font-display text-white mb-1">A IA recomenda</h3>
                        <p class="text-xs text-stone-300 leading-relaxed">
                            A IA cruza as variáveis e entrega a melhor opção com motivo claro.
                        </p>
                    </div>

                    <div class="flashlight-card p-5 bg-white">
                        <div class="text-xl font-display font-bold text-[#b89445] mb-2">04</div>
                        <h3 class="text-sm font-bold font-display text-stone-950 mb-1">Você converte</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            O cliente toma a decisão e fecha a compra imediatamente.
                        </p>
                    </div>
                </div>

                <!-- Section Action CTA Button -->
                <div class="mt-8 text-center">
                    <a href="cadastrar.html" class="btn-gold-spin">
                        <span class="spin-border"></span>
                        <span class="relative flex items-center justify-center gap-2 px-7 py-3 rounded-full bg-[#0a0a0a] text-white text-xs font-bold uppercase tracking-widest">
                            <span>Criar minha bio agora →</span>
                        </span>
                    </a>
                </div>
            </div>
        </section>

        <!-- DEMO INTERATIVA (Concierge IA em Tempo Real) -->
        <section class="py-12 sm:py-16 px-5 bg-white border-t border-b border-stone-300" id="demo">
            <div class="max-w-4xl mx-auto">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10 items-start">
                    <div>
                        <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                            Diagnostica, qualifica e recomenda em segundos.
                        </h2>
                        <p class="text-xs sm:text-sm mt-3 text-stone-600 leading-relaxed">
                            Experimente como o Concierge de IA funciona na prática. Ele entende a resposta de cada visitante e entrega a solução exata com argumento de valor.
                        </p>

                        <div class="mt-6">
                            <a href="cadastrar.html" class="btn-gold-spin">
                                <span class="spin-border"></span>
                                <span class="relative flex items-center justify-center gap-2 px-6 py-3 rounded-full bg-[#0a0a0a] text-white text-xs font-bold uppercase tracking-widest">
                                    <span>Montar meu concierge agora →</span>
                                </span>
                            </a>
                        </div>
                    </div>

                    <!-- Interactive Concierge Widget -->
                    <div class="flashlight-card p-5 sm:p-6" id="concierge-widget">
                        <!-- Step 1 -->
                        <div id="quiz-step-1" class="quiz-step">
                            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-[#d6bc8c] mb-1">Passo 1 de 3</p>
                            <h3 class="text-base font-bold font-display text-stone-950 mb-3">Como você está no seu negócio hoje?</h3>
                            <div class="space-y-2">
                                <button onclick="nextQuizStep(1, 'Estou começando')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Estou começando agora</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(1, 'Vendo sem previsibilidade')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Vendo, mas sem consistência</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(1, 'Quero escala')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Já faturo alto, quero escala</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 2 -->
                        <div id="quiz-step-2" class="quiz-step hidden">
                            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-[#d6bc8c] mb-1">Passo 2 de 3</p>
                            <h3 class="text-base font-bold font-display text-stone-950 mb-3">Qual seu objetivo principal agora?</h3>
                            <div class="space-y-2">
                                <button onclick="nextQuizStep(2, 'Atrair clientes qualificados')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Atrair clientes de alto valor</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(2, 'Automatizar 24h')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Automatizar vendas 24h</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 3 -->
                        <div id="quiz-step-3" class="quiz-step hidden">
                            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-[#d6bc8c] mb-1">Passo 3 de 3</p>
                            <h3 class="text-base font-bold font-display text-stone-950 mb-3">Qual sua faixa de faturamento mensal?</h3>
                            <div class="space-y-2">
                                <button onclick="finishQuiz('Até 10k')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Até R$ 10.000 / mês</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="finishQuiz('Acima de 10k')" class="w-full text-left px-3.5 py-2.5 rounded-xl text-xs font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Mais de R$ 10.000 / mês</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Result -->
                        <div id="quiz-result" class="quiz-step hidden text-center py-2">
                            <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center mx-auto mb-2 text-xl">
                                <iconify-icon icon="solar:check-circle-bold"></iconify-icon>
                            </div>
                            <h4 class="text-base font-bold font-display text-stone-950">Plano Recomendado: ELOOO BIO Pro (R$ 147/mês)</h4>
                            <p class="text-xs text-stone-600 mt-1 mb-4">
                                A IA identificou que seu maior gargalo é a automação e qualificação de visitantes.
                            </p>
                            <a href="cadastrar.html?plan=pro" class="btn-gold-spin w-full">
                                <span class="spin-border"></span>
                                <span class="relative block w-full py-3 rounded-full bg-[#0a0a0a] text-white text-xs font-bold uppercase tracking-widest text-center">
                                    Ativar Plano Pro →
                                </span>
                            </a>
                            <button onclick="resetQuiz()" class="mt-2.5 text-[11px] text-stone-500 hover:text-stone-950 underline">
                                Refazer teste
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- AGENDA INTEGRADA - (CLARO QUE SÓ ESTÁ INCLUSA NO PLANO ELITE) - GOLD LUXURY SECTION -->
        <section class="py-12 sm:py-16 px-5 section-gold-luxury" id="agenda">
            <div class="max-w-4xl mx-auto">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10 items-center">
                    <div>
                        <!-- Exclusive Elite Badge -->
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-400/20 border border-amber-400/40 text-amber-300 text-[10.5px] font-mono font-bold uppercase tracking-wider mb-3">
                            <iconify-icon icon="solar:crown-line-duotone" class="text-amber-400"></iconify-icon>
                            <span>EXCLUSIVO DO PLANO ELITE (R$ 497/mês)</span>
                        </div>

                        <h2 class="text-2xl sm:text-3xl font-bold font-display text-white leading-tight">
                            Da qualificação ao horário marcado.
                        </h2>
                        <p class="text-xs sm:text-sm mt-3 text-stone-300 leading-relaxed font-light">
                            O recurso de agendamento integrado é exclusivo para assinantes do <strong class="text-amber-300 font-semibold">Plano Elite</strong>. O cliente escolhe dia e horário disponível e confirma a consulta direto na sua bio, sem atritos.
                        </p>

                        <div class="mt-6">
                            <a href="cadastrar.html?plan=elite" class="btn-gold-spin">
                                <span class="spin-border"></span>
                                <span class="relative flex items-center justify-center gap-2 px-7 py-3 rounded-full bg-[#121215] text-[#f6e3c5] text-xs font-bold uppercase tracking-widest">
                                    <span>Ativar Agenda no Plano Elite →</span>
                                </span>
                            </a>
                        </div>
                    </div>

                    <!-- Clean Calendar Preview -->
                    <div class="flashlight-card p-5 max-w-sm mx-auto w-full bg-[#141311] text-white border border-[#d6bc8c]/40">
                        <div class="flex items-center justify-between mb-3 pb-2.5 border-b border-white/10">
                            <span class="text-xs font-bold font-display text-white uppercase tracking-wider">Junho 2026</span>
                            <span class="text-[10px] font-mono text-amber-300 bg-amber-400/10 px-2 py-0.5 rounded">Plano Elite</span>
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

        <!-- PLANOS & PREÇOS (STARTER 127 / PRÓ 147 / ELITE 497) -->
        <section class="py-12 sm:py-20 px-5 bg-white" id="planos">
            <div class="max-w-4xl mx-auto">
                <div class="text-center mb-10">
                    <h2 class="text-2xl sm:text-3xl font-bold font-display text-stone-950 leading-tight">
                        Escolha seu plano e comece hoje.
                    </h2>
                    <p class="text-xs sm:text-sm mt-1 text-stone-600">
                        Investimento claro, sem contratos longos e com garantia incondicional de 7 dias.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-5 max-w-4xl mx-auto items-stretch">
                    
                    <!-- Starter 127 -->
                    <div class="flashlight-card p-6 flex flex-col justify-between border border-stone-200">
                        <div>
                            <h3 class="text-lg font-bold font-display text-stone-950">Starter</h3>
                            <p class="text-xs text-stone-500 mt-0.5 mb-4">Sua presença pronta pra vender.</p>
                            
                            <div class="mb-4">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-extrabold font-display text-stone-950">R$ 127</span>
                                    <span class="text-xs text-stone-500 font-medium">/mês</span>
                                </div>
                            </div>

                            <ul class="space-y-2 mb-6 text-xs text-stone-700">
                                <li class="flex items-center gap-2">✓ Bio profissional de alta velocidade</li>
                                <li class="flex items-center gap-2">✓ Vitrine inteligente de produtos & serviços</li>
                                <li class="flex items-center gap-2">✓ Direcionamento direto para link de vendas</li>
                                <li class="flex items-center gap-2">✓ Setup guiado em minutos</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=starter" class="block w-full py-2.5 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-900 font-bold text-center text-xs uppercase tracking-wider transition-colors">
                            Começar Starter
                        </a>
                    </div>

                    <!-- Pro 147 (MAIS ESCOLHIDO - DESTAQUE) -->
                    <div class="flashlight-card p-6 flex flex-col justify-between bg-[#11100E] text-white relative shadow-xl scale-[1.02] border-2 border-[#d6bc8c]">
                        <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase tracking-wider bg-[#d6bc8c] text-stone-950 shadow-md">
                            ★ Mais Escolhido
                        </span>

                        <div>
                            <h3 class="text-xl font-bold font-display text-white mt-1">Pró</h3>
                            <p class="text-xs text-stone-400 mt-0.5 mb-4">A IA que qualifica e vende 24h.</p>
                            
                            <div class="mb-4">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-4xl font-extrabold font-display text-white">R$ 147</span>
                                    <span class="text-xs text-stone-400 font-medium">/mês</span>
                                </div>
                            </div>

                            <ul class="space-y-2 mb-6 text-xs text-stone-200">
                                <li class="flex items-center gap-2 font-bold text-amber-300">✓ Tudo do Plano Starter</li>
                                <li class="flex items-center gap-2 font-semibold text-white">✓ Concierge com Inteligência Artificial</li>
                                <li class="flex items-center gap-2">✓ Qualificação automática de público</li>
                                <li class="flex items-center gap-2">✓ Métricas e analytics de conversão</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=pro" class="btn-gold-spin w-full">
                            <span class="spin-border"></span>
                            <span class="relative block w-full py-3 rounded-full bg-[#1c1917] text-white font-bold text-xs uppercase tracking-widest text-center">
                                Assinar Plano Pró →
                            </span>
                        </a>
                    </div>

                    <!-- Elite 497 (INCLUI AGENDA) -->
                    <div class="flashlight-card p-6 flex flex-col justify-between border border-stone-200">
                        <div>
                            <h3 class="text-lg font-bold font-display text-stone-950">Elite</h3>
                            <p class="text-xs text-stone-500 mt-0.5 mb-4">Para quem quer automação total.</p>
                            
                            <div class="mb-4">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-extrabold font-display text-stone-950">R$ 497</span>
                                    <span class="text-xs text-stone-500 font-medium">/mês</span>
                                </div>
                            </div>

                            <ul class="space-y-2 mb-6 text-xs text-stone-700">
                                <li class="flex items-center gap-2 font-semibold text-stone-900">✓ Tudo do Plano Pró</li>
                                <li class="flex items-center gap-2 font-bold text-amber-800">✓ Agendamento Integrado de Consultas</li>
                                <li class="flex items-center gap-2">✓ Concierge com IA estendida</li>
                                <li class="flex items-center gap-2">✓ Suporte prioritário via WhatsApp</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=elite" class="block w-full py-2.5 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-900 font-bold text-center text-xs uppercase tracking-wider transition-colors">
                            Começar Elite
                        </a>
                    </div>

                </div>

                <!-- Garantia 7 Dias -->
                <div class="max-w-4xl mx-auto mt-8 text-center">
                    <p class="text-xs text-stone-600 font-medium flex items-center justify-center gap-2">
                        <iconify-icon icon="solar:shield-check-bold" class="text-emerald-600 text-base"></iconify-icon>
                        <span>Garantia incondicional de 7 dias — não gostou, devolvemos 100% do seu dinheiro.</span>
                    </p>
                </div>
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer class="py-8 px-6 text-center text-xs text-stone-500 bg-white border-t border-stone-300">
        <p>© 2026 ELOOO BIO PREMIUM · Ecossistema <strong class="text-stone-900">ELOOO International Group</strong>.</p>
        <div class="flex items-center justify-center gap-6 mt-2.5 font-mono">
            <a class="hover:text-stone-900 transition-colors" href="termos.html">Termos</a>
            <a class="hover:text-stone-900 transition-colors" href="privacidade.html">Privacidade</a>
            <a href="https://wa.me/5547988660791" target="_blank" rel="noopener noreferrer" class="hover:text-emerald-600 transition-colors">WhatsApp Suporte</a>
            <a href="mailto:contato@elooo.com.br" class="hover:text-stone-900 transition-colors">contato@elooo.com.br</a>
        </div>
    </footer>

    <!-- INTERACTIVE SCRIPTS -->
    <script>
        // Flashlight mouse tracking on cards
        document.querySelectorAll('.flashlight-card').forEach(card => {
            card.addEventListener('mousemove', e => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                card.style.setProperty('--mouse-x', `${x}px`);
                card.style.setProperty('--mouse-y', `${y}px`);
            });
        });

        // Luxury Drawer Toggle (Works on Desktop & Mobile)
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
    <title>Entrar — ELOOO BIO PREMIUM</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; }
        .font-display { font-family: 'Space Grotesk', sans-serif; }
    </style>
</head>
<body class="antialiased min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-md bg-white p-8 sm:p-10 rounded-3xl border border-stone-300 shadow-xl">
        <a href="index.html" class="inline-block mb-6">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO BIO PREMIUM" class="h-10 object-contain" style="filter: brightness(0);"/>
        </a>

        <h1 class="text-2xl font-bold font-display text-stone-950">Entrar na sua conta</h1>
        <p class="text-xs text-stone-500 mt-1 mb-6">
            Não tem conta? <a href="cadastrar.html" class="font-bold underline text-stone-900">Criar conta</a>
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

            <button type="submit" class="w-full py-3.5 rounded-full bg-stone-950 text-white font-bold text-xs uppercase tracking-wider hover:bg-stone-800 transition-colors mt-2 shadow-md">
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
    <title>Criar Conta — ELOOO BIO PREMIUM</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; }
        .font-display { font-family: 'Space Grotesk', sans-serif; }
    </style>
</head>
<body class="antialiased min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-md bg-white p-8 sm:p-10 rounded-3xl border border-stone-300 shadow-xl">
        <a href="index.html" class="inline-block mb-6">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO BIO PREMIUM" class="h-10 object-contain" style="filter: brightness(0);"/>
        </a>

        <h1 class="text-2xl font-bold font-display text-stone-950">Criar sua conta</h1>
        <p class="text-xs text-stone-500 mt-1 mb-5">
            Já tem conta? <a href="entrar.html" class="font-bold underline text-stone-900">Fazer login</a>
        </p>

        <!-- Plan Selector Bar (Starter 127 / Pro 147 / Elite 497) -->
        <div class="mb-5 p-1 rounded-2xl bg-stone-100 grid grid-cols-3 gap-1 text-xs font-bold text-center">
            <button type="button" onclick="selectPlan('starter')" id="btn-starter" class="py-2 rounded-xl transition-colors text-stone-600">Starter R$127</button>
            <button type="button" onclick="selectPlan('pro')" id="btn-pro" class="py-2 rounded-xl bg-stone-950 text-white shadow-sm transition-colors">Pró R$147</button>
            <button type="button" onclick="selectPlan('elite')" id="btn-elite" class="py-2 rounded-xl transition-colors text-stone-600">Elite R$497</button>
        </div>

        <form class="space-y-3.5" onsubmit="event.preventDefault(); window.location.href='https://wa.me/5547988660791?text=Ol%C3%A1%2C%20acabei%20de%20me%20cadastrar%20no%20ELOOO%20BIO%20PREMIUM%20e%20quero%20ativar%20minha%20conta.';">
            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Nome Completo</label>
                <input type="text" required placeholder="Seu nome" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Usuário da sua Bio</label>
                <div class="flex items-center rounded-xl bg-stone-50 border border-stone-300 focus-within:border-stone-900 overflow-hidden">
                    <span class="px-3 text-xs text-stone-400 font-mono">bio.elooo.com.br/</span>
                    <input type="text" required placeholder="seunome" class="w-full py-3 pr-4 text-sm bg-transparent outline-none"/>
                </div>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">E-mail</label>
                <input type="email" required placeholder="seu@email.com" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Senha</label>
                <input type="password" required placeholder="••••••••" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <button type="submit" class="w-full py-3.5 rounded-full bg-stone-950 text-white font-bold text-xs uppercase tracking-wider hover:bg-stone-800 transition-colors mt-2 shadow-md">
                Criar Conta e Começar →
            </button>
        </form>

        <div class="mt-6 text-center">
            <a href="index.html" class="text-xs text-stone-400 hover:text-stone-900 underline">← Voltar à página inicial</a>
        </div>
    </div>

    <script>
        function selectPlan(plan) {
            const btns = {
                starter: document.getElementById('btn-starter'),
                pro: document.getElementById('btn-pro'),
                elite: document.getElementById('btn-elite')
            };
            for (let k in btns) {
                btns[k].className = 'py-2 rounded-xl transition-colors text-stone-600';
            }
            if (btns[plan]) {
                btns[plan].className = 'py-2 rounded-xl bg-stone-950 text-white shadow-sm transition-colors font-bold';
            }
        }
        const urlParams = new URLSearchParams(window.location.search);
        const planParam = urlParams.get('plan');
        if (planParam && ['starter', 'pro', 'elite'].includes(planParam)) {
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
    <title>Termos de Uso — ELOOO BIO PREMIUM</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; } .font-display { font-family: 'Space Grotesk', sans-serif; }</style>
</head>
<body class="antialiased min-h-screen">
    <header class="border-b border-stone-300 px-6 py-4 flex items-center justify-between bg-white">
        <a class="flex items-center gap-2" href="index.html">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO Logo" class="h-8 object-contain" style="filter: brightness(0);"/>
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-stone-600">BIO PREMIUM</span>
        </a>
        <a class="text-xs text-stone-500 hover:text-stone-950 underline" href="index.html">← Voltar</a>
    </header>

    <main class="max-w-2xl mx-auto px-6 py-12">
        <h1 class="text-2xl font-bold font-display text-stone-950 mb-1">Termos de Uso</h1>
        <p class="text-xs text-stone-500 mb-6 font-mono">Última atualização: 18 de agosto de 2026</p>

        <div class="space-y-6 text-sm text-stone-700 leading-relaxed bg-white p-8 rounded-3xl border border-stone-300 shadow-sm">
            <section>
                <h2 class="font-bold font-display text-stone-950 mb-1">1. Aceitação</h2>
                <p>Ao utilizar a plataforma ELOOO BIO PREMIUM da ELOOO International Group, você concorda com estes termos.</p>
            </section>
            <section>
                <h2 class="font-bold font-display text-stone-950 mb-1">2. Garantia de 7 Dias</h2>
                <p>Todos os planos contam com garantia incondicional de reembolso total em até 7 dias.</p>
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
    <title>Política de Privacidade — ELOOO BIO PREMIUM</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body { font-family: 'Inter', sans-serif; background: #EAEAE5; color: #1C1917; } .font-display { font-family: 'Space Grotesk', sans-serif; }</style>
</head>
<body class="antialiased min-h-screen">
    <header class="border-b border-stone-300 px-6 py-4 flex items-center justify-between bg-white">
        <a class="flex items-center gap-2" href="index.html">
            <img src="static/images/ELOOO LOGO.png" alt="ELOOO Logo" class="h-8 object-contain" style="filter: brightness(0);"/>
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-stone-600">BIO PREMIUM</span>
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
                <p>Os contatos e visitantes da sua bio pertencem 100% a você.</p>
            </section>
        </div>
    </main>
</body>
</html>
"""

# ----------------------------------------------------
# 6. BIO BRUNO BARROS (src/bio/brunobarros.html)
# ----------------------------------------------------
BRUNO_BARROS_BIO_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>Bruno Barros | Bio Oficial — ELOOO BIO PREMIUM</title>
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
            <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20Bruno!%20Vim%20pela%20sua%20bio%20e%20quero%20conversar." target="_blank" class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center text-stone-200 text-lg hover:bg-emerald-600 transition-colors">
                <iconify-icon icon="ic:baseline-whatsapp"></iconify-icon>
            </a>
            <a href="https://youtube.com" target="_blank" class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center text-stone-200 text-lg hover:bg-red-600 transition-colors">
                <iconify-icon icon="solar:play-circle-linear"></iconify-icon>
            </a>
        </div>

        <!-- Concierge IA Direct Action -->
        <a href="https://wa.me/5547988660791?text=Ol%C3%A1%2C%20Bruno!%20Quero%20fazer%20meu%20diagn%C3%B3stico%20editorial." target="_blank" class="bio-btn w-full p-4 rounded-2xl flex items-center gap-3.5 text-left shadow-lg border border-amber-400/40">
            <div class="w-11 h-11 rounded-xl bg-amber-400/20 text-amber-300 flex items-center justify-center text-xl flex-none">
                <iconify-icon icon="solar:bolt-circle-bold"></iconify-icon>
            </div>
            <div class="flex-1 min-w-0">
                <p class="font-bold text-sm text-white leading-tight">Diagnóstico Editorial Rápido</p>
                <p class="text-xs text-stone-400 mt-0.5">Descubra o próximo passo para o seu livro</p>
            </div>
            <div class="text-amber-300 text-sm">→</div>
        </a>

        <!-- Horizontal Netflix Carousel -->
        <div class="pt-2">
            <p class="text-[11px] font-mono font-bold uppercase tracking-wider text-stone-400 mb-2.5">
                PROJETOS & SOLUÇÕES
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
                Criado com ELOOO BIO PREMIUM
            </a>
        </div>

    </div>

</body>
</html>
"""

def generate_all():
    print("Generating refined ELOOO BIO PREMIUM pages with tighter spacing, gold CTA buttons in every section, new metrics, updated plans and minimal navbar...")
    save("src/bio/index.html", LANDING_HTML)
    save("src/bio/entrar.html", ENTRAR_HTML)
    save("src/bio/cadastrar.html", CADASTRAR_HTML)
    save("src/bio/termos.html", TERMOS_HTML)
    save("src/bio/privacidade.html", PRIVACIDADE_HTML)
    save("src/bio/brunobarros.html", BRUNO_BARROS_BIO_HTML)
    save("src/bio/leticia-vaz.html", BRUNO_BARROS_BIO_HTML)
    save("src/bio/demo.html", BRUNO_BARROS_BIO_HTML)
    save("src/bio.html", LANDING_HTML)
    print("All bio pages updated successfully!")

if __name__ == "__main__":
    generate_all()
