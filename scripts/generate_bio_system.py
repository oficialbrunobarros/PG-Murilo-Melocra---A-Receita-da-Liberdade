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
    <meta name="description" content="Pare de perder vendas com links confusos. O ELOOO BIO PREMIUM qualifica seus visitantes com Inteligência Artificial, agenda consultas e recomenda o produto certo."/>
    
    <!-- Open Graph / Meta -->
    <meta property="og:title" content="ELOOO BIO PREMIUM | O Link na Bio que Vende"/>
    <meta property="og:description" content="Página de link na bio de alta conversão. Concierge de IA, vitrine inteligente, agendamento e métricas de vendas."/>
    <meta property="og:image" content="static/images/og-share.png"/>
    <meta property="og:type" content="website"/>
    <meta name="theme-color" content="#EAEAE5"/>

    <!-- Exact Fonts from ELOOO Website: Space Grotesk + Inter + JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
    
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
                        surface: '#EAEAE5',
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

        /* FLOATING NAVBAR */
        .glass-nav {
            background: rgba(255, 255, 255, 0.85);
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
            border-radius: 28px;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .flashlight-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(500px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(214, 188, 140, 0.25), transparent 60%);
            z-index: 1;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .flashlight-card:hover {
            transform: translateY(-4px);
            border-color: #d6bc8c;
            box-shadow: 0 20px 40px -15px rgba(28, 25, 23, 0.1), 0 0 25px rgba(214, 188, 140, 0.2);
        }
        .flashlight-card:hover::before {
            opacity: 1;
        }

        /* MOVING GOLD BORDER BUTTON (EXACT ELOOO STANDARD) */
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
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }
        .btn-gold-spin:hover {
            transform: scale(1.02);
            box-shadow: 0 10px 25px -5px rgba(214, 188, 140, 0.4);
        }
        .btn-gold-spin span.spin-border {
            position: absolute;
            inset: -1000%;
            background: conic-gradient(from 90deg at 50% 50%, transparent 0%, rgba(214, 188, 140, 0.9) 50%, transparent 100%);
            animation: spin 3s linear infinite;
        }

        /* GOLD ACTIVE TAB / SELECTOR */
        .gold-tab {
            background: #1C1917;
            color: #FFFFFF;
            border: 1px solid #d6bc8c;
            box-shadow: 0 0 15px rgba(214, 188, 140, 0.25);
        }

        /* IPHONE FRAME 3D STYLING */
        .phone-mockup-wrapper {
            position: relative;
            border-radius: 48px;
            padding: 10px;
            background: linear-gradient(145deg, #2b2825, #141311);
            box-shadow: 0 35px 80px -15px rgba(28, 25, 23, 0.35), 0 0 35px rgba(214, 188, 140, 0.15);
            border: 2px solid rgba(214, 188, 140, 0.4);
        }
    </style>
</head>
<body class="antialiased selection:bg-stone-900 selection:text-white">

    <!-- FLOATING TOP NAVBAR -->
    <div class="fixed top-3 sm:top-5 inset-x-3 sm:inset-x-6 z-50 flex justify-center pointer-events-none">
        <nav class="pointer-events-auto flex items-center justify-between gap-4 pl-4 pr-3 sm:pl-6 sm:pr-4 py-3 rounded-full w-full max-w-5xl glass-nav relative">
            <!-- Brand Logo (Enlarged and Crisp) -->
            <a class="inline-flex items-center flex-none group" href="index.html">
                <img src="static/images/ELOOO LOGO.png" alt="ELOOO BIO PREMIUM" class="h-9 sm:h-11 md:h-12 object-contain transition-transform group-hover:scale-105" style="filter: brightness(0);"/>
                <span class="ml-3 hidden sm:inline-block text-[11px] font-mono font-bold uppercase tracking-[0.2em] text-stone-600 border-l border-stone-300 pl-3">
                    BIO PREMIUM
                </span>
            </a>

            <!-- Desktop Nav Links -->
            <div class="hidden md:flex items-center gap-7 text-[12px] font-sans font-semibold uppercase tracking-[0.14em] text-stone-700">
                <a href="#problema" class="hover:text-stone-950 transition-colors">Por que</a>
                <a href="#como" class="hover:text-stone-950 transition-colors">Como funciona</a>
                <a href="#demo" class="hover:text-stone-950 transition-colors">Concierge IA</a>
                <a href="#agenda" class="hover:text-stone-950 transition-colors">Agenda</a>
                <a href="#planos" class="hover:text-stone-950 transition-colors">Planos</a>
                <a href="brunobarros.html" target="_blank" class="text-stone-950 font-bold hover:text-amber-800 transition-colors flex items-center gap-1">
                    <span>Bio Demo</span>
                    <iconify-icon icon="solar:arrow-right-up-linear" class="text-xs"></iconify-icon>
                </a>
            </div>

            <!-- Action Buttons + Mobile Hamburger -->
            <div class="flex items-center gap-3 flex-none">
                <a class="hidden sm:inline-block px-3.5 py-2 text-[12px] font-sans font-bold uppercase tracking-wider text-stone-700 hover:text-stone-950 transition-colors" href="entrar.html">
                    Entrar
                </a>
                
                <!-- Moving Gold Border CTA -->
                <a href="cadastrar.html" class="btn-gold-spin">
                    <span class="spin-border"></span>
                    <span class="relative flex items-center justify-center gap-1.5 px-5 sm:px-6 py-2.5 rounded-full bg-[#0a0a0a] text-white text-[11px] sm:text-[12px] font-bold uppercase tracking-widest hover:bg-[#151515] transition-colors">
                        <span>Começar</span>
                        <iconify-icon icon="solar:arrow-right-linear" class="text-sm text-amber-300"></iconify-icon>
                    </span>
                </a>

                <!-- Hamburger Button (Mobile) -->
                <button id="mobile-hamburger-btn" type="button" class="md:hidden w-10 h-10 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-900 flex items-center justify-center text-xl transition-all cursor-pointer" aria-label="Abrir Menu">
                    <iconify-icon icon="solar:hamburger-menu-linear"></iconify-icon>
                </button>
            </div>
        </nav>
    </div>

    <!-- MOBILE MENU OVERLAY / DRAWER -->
    <div id="mobile-drawer" class="fixed inset-0 bg-stone-950/70 backdrop-blur-md z-50 opacity-0 pointer-events-none transition-all duration-300 flex justify-end">
        <div id="mobile-drawer-content" class="w-full max-w-xs bg-white h-full shadow-2xl p-6 flex flex-col justify-between transform translate-x-full transition-transform duration-300">
            <div>
                <!-- Drawer Header -->
                <div class="flex items-center justify-between border-b border-stone-200 pb-4 mb-6">
                    <img src="static/images/ELOOO LOGO.png" alt="ELOOO BIO" class="h-8 object-contain" style="filter: brightness(0);"/>
                    <button id="mobile-drawer-close" class="w-8 h-8 rounded-full bg-stone-100 text-stone-800 flex items-center justify-center text-lg">
                        <iconify-icon icon="solar:close-circle-linear"></iconify-icon>
                    </button>
                </div>

                <!-- Drawer Links -->
                <nav class="space-y-3 font-sans font-bold text-xs uppercase tracking-wider text-stone-700">
                    <a href="#problema" class="mobile-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Por que</a>
                    <a href="#como" class="mobile-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Como funciona</a>
                    <a href="#demo" class="mobile-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Concierge com IA</a>
                    <a href="#agenda" class="mobile-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Agenda Integrada</a>
                    <a href="#planos" class="mobile-link block px-4 py-3 rounded-2xl hover:bg-stone-100 hover:text-stone-950 transition-colors">Planos & Preços</a>
                    <a href="brunobarros.html" target="_blank" class="mobile-link block px-4 py-3 rounded-2xl bg-stone-900 text-white font-bold flex items-center justify-between border border-[#d6bc8c]">
                        <span>Bio Bruno Barros</span>
                        <iconify-icon icon="solar:arrow-right-up-linear"></iconify-icon>
                    </a>
                </nav>
            </div>

            <!-- Drawer Bottom Actions -->
            <div class="pt-6 border-t border-stone-200 space-y-2.5">
                <a href="entrar.html" class="block w-full py-3 rounded-full text-center text-xs font-bold text-stone-800 bg-stone-100 hover:bg-stone-200 transition-colors uppercase tracking-wider">
                    Fazer Login
                </a>
                <a href="cadastrar.html" class="block w-full py-3.5 rounded-full text-center text-xs font-bold text-white bg-stone-950 shadow-md uppercase tracking-wider">
                    Criar Conta Agora
                </a>
            </div>
        </div>
    </div>

    <!-- MAIN CONTENT -->
    <main class="relative z-10">

        <!-- HERO SECTION (High-Impact Headline + Moving Border CTAs + SMARTPHONE MOCKUP RIGHT BELOW) -->
        <section class="relative pt-32 pb-14 sm:pt-40 sm:pb-16 overflow-hidden">
            <div class="max-w-5xl mx-auto px-5 sm:px-6 text-center relative z-10">
                
                <!-- Main Headline in Clean Space Grotesk -->
                <h1 class="text-3xl sm:text-5xl lg:text-6xl font-bold font-display tracking-tight text-stone-900 leading-[1.12] mb-5">
                    O link na bio que entende seu cliente e conduz a venda.
                </h1>

                <!-- Subtitle -->
                <p class="text-base sm:text-lg text-stone-600 max-w-2xl mx-auto mb-8 leading-relaxed font-normal">
                    Pare de empilhar vinte botões confusos. O <strong class="text-stone-950 font-semibold">ELOOO BIO PREMIUM</strong> faz 3 perguntas estratégicas, qualifica o momento da pessoa e recomenda a solução exata com botão de compra direto.
                </p>

                <!-- Hero Action Buttons -->
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
                    <a href="cadastrar.html" class="btn-gold-spin w-full sm:w-auto shadow-xl">
                        <span class="spin-border"></span>
                        <span class="relative flex items-center justify-center gap-2 px-8 py-4 rounded-full bg-[#0a0a0a] text-white text-xs sm:text-sm font-bold uppercase tracking-widest hover:bg-[#151515] transition-colors">
                            <span>Quero vender no automático</span>
                            <iconify-icon icon="solar:arrow-right-linear" class="text-base text-amber-300"></iconify-icon>
                        </span>
                    </a>
                    
                    <a href="brunobarros.html" target="_blank" class="w-full sm:w-auto px-7 py-4 rounded-full bg-white text-stone-900 border border-stone-300 hover:border-[#d6bc8c] hover:bg-stone-50 text-xs sm:text-sm font-bold uppercase tracking-wider transition-all flex items-center justify-center gap-2 shadow-sm">
                        <span>Ver Bio de Bruno Barros</span>
                        <iconify-icon icon="solar:arrow-right-up-linear" class="text-base text-stone-600"></iconify-icon>
                    </a>
                </div>

                <!-- SMARTPHONE MOCKUP (RIGHT BELOW TITLE AND CTAS) -->
                <div class="flex justify-center mb-14">
                    <div class="w-full max-w-[330px] phone-mockup-wrapper relative">
                        <!-- Dynamic Island -->
                        <div class="absolute top-4 left-1/2 -translate-x-1/2 w-28 h-5 bg-black rounded-full z-20 flex items-center justify-end pr-2.5">
                            <div class="w-2.5 h-2.5 rounded-full bg-[#222]"></div>
                        </div>
                        
                        <!-- Interactive Screen -->
                        <div class="relative rounded-[40px] overflow-hidden h-[580px] bg-stone-950">
                            <iframe src="brunobarros.html" title="Bio Bruno Barros Ao Vivo" class="w-full h-full border-0"></iframe>
                            <a href="brunobarros.html" target="_blank" class="absolute inset-x-0 bottom-0 py-3.5 bg-gradient-to-t from-black/90 via-black/60 to-transparent backdrop-blur-sm text-center text-xs font-mono font-bold uppercase tracking-widest text-[#f6e3c5] hover:text-white transition-colors">
                                Abrir bio oficial completa →
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Credibility & Stats Ribbon -->
                <div class="pt-8 border-t border-stone-300 max-w-4xl mx-auto">
                    <p class="text-[11px] font-mono font-bold uppercase tracking-[0.25em] text-stone-500 mb-6">
                        Desenvolvido por ELOOO International Group
                    </p>
                    
                    <div class="grid grid-cols-3 gap-3 sm:gap-6">
                        <div class="flashlight-card p-4 sm:p-5 text-center">
                            <div class="text-2xl sm:text-4xl font-extrabold font-display text-stone-950 tracking-tight">
                                <span class="counter" data-target="18">18</span> MI
                            </div>
                            <div class="mt-1 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider text-stone-500">
                                faturamento gerado
                            </div>
                        </div>

                        <div class="flashlight-card p-4 sm:p-5 text-center">
                            <div class="text-2xl sm:text-4xl font-extrabold font-display text-stone-950 tracking-tight">
                                +<span class="counter" data-target="45">45</span> MI
                            </div>
                            <div class="mt-1 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider text-stone-500">
                                impactos gerados
                            </div>
                        </div>

                        <div class="flashlight-card p-4 sm:p-5 text-center">
                            <div class="text-2xl sm:text-4xl font-extrabold font-display text-stone-950 tracking-tight">
                                +<span class="counter" data-target="3800">3.800</span>
                            </div>
                            <div class="mt-1 text-[10px] sm:text-xs font-mono font-semibold uppercase tracking-wider text-stone-500">
                                clientes & autores
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- O PROBLEMA (Antes vs Depois) -->
        <section class="py-14 sm:py-20 px-5 sm:px-6 bg-white border-t border-b border-stone-300" id="problema">
            <div class="max-w-5xl mx-auto">
                <div class="text-center mb-12">
                    <h2 class="text-2xl sm:text-4xl font-bold font-display text-stone-950 leading-tight">
                        Mostrar tudo é o mesmo que não mostrar nada.
                    </h2>
                    <p class="text-sm sm:text-base mt-2.5 max-w-xl mx-auto text-stone-600">
                        Quanto mais opções você empilha no link, mais o cliente se perde. O ELOOO BIO PREMIUM inverte isso: ele <strong class="text-stone-950 font-semibold">conduz</strong> a decisão.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-7">
                    <!-- Antes Card -->
                    <div class="flashlight-card p-7 sm:p-9 bg-stone-50 border border-stone-200">
                        <span class="text-xs font-mono font-bold uppercase tracking-wider text-stone-500 block mb-4">
                            ✕ Como a maioria faz hoje
                        </span>
                        <h3 class="text-xl font-bold font-display mb-4 text-stone-950">Você joga tudo no link e torce.</h3>
                        <ul class="space-y-3 text-sm text-stone-600">
                            <li class="flex items-start gap-2.5">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Dez ou vinte opções competindo pela atenção ao mesmo tempo</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>O visitante não sabe o que é adequado para o momento dele</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Sem qualificação, você perde tempo com curiosos no WhatsApp</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Mais de 80% abandonam a página sem tomar nenhuma ação</span>
                            </li>
                        </ul>
                    </div>

                    <!-- Depois Card (ELOOO BIO) -->
                    <div class="flashlight-card p-7 sm:p-9 bg-[#141311] text-white border border-[#d6bc8c]/40 shadow-xl">
                        <span class="text-xs font-mono font-bold uppercase tracking-wider text-amber-300 block mb-4">
                            ✓ Com ELOOO BIO PREMIUM
                        </span>
                        <h3 class="text-xl font-bold font-display mb-4 text-[#f6e3c5]">O sistema entende o momento e conduz.</h3>
                        <ul class="space-y-3 text-sm text-stone-200">
                            <li class="flex items-start gap-2.5">
                                <span class="text-emerald-400 font-bold">✓</span>
                                <span>O visitante responde 3 perguntas rápidas e dinâmicas</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <span class="text-emerald-400 font-bold">✓</span>
                                <span>A IA cruza o objetivo, nível e momento do cliente</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <span class="text-emerald-400 font-bold">✓</span>
                                <span>Mostra 1 recomendação exata com explicação e botão de compra</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <span class="text-emerald-400 font-bold">✓</span>
                                <span>Sua conversão aumenta e as vendas acontecem 24h por dia</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- COMO FUNCIONA (4 Passos com Flashlight Cards) -->
        <section class="py-14 sm:py-20 px-5 sm:px-6" id="como">
            <div class="max-w-5xl mx-auto">
                <div class="text-center mb-12">
                    <h2 class="text-2xl sm:text-4xl font-bold font-display text-stone-950 leading-tight">
                        Quatro passos. Uma máquina de conversão.
                    </h2>
                    <p class="text-sm mt-2 text-stone-600 font-medium">
                        Simples de configurar. Extremamente poderoso para vender.
                    </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
                    <!-- Passo 1 -->
                    <div class="flashlight-card p-6">
                        <div class="text-2xl font-display font-bold text-[#d6bc8c] mb-3">01</div>
                        <h3 class="text-base font-bold font-display text-stone-950 mb-1.5">Você cadastra</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            Produtos, livros, mentorias e serviços. Cada um com preço, momento e dor que resolve.
                        </p>
                    </div>

                    <!-- Passo 2 -->
                    <div class="flashlight-card p-6">
                        <div class="text-2xl font-display font-bold text-[#d6bc8c] mb-3">02</div>
                        <h3 class="text-base font-bold font-display text-stone-950 mb-1.5">O cliente responde</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            3 a 5 perguntas rápidas e intuitivas na bio. Sem formulários longos ou chatos.
                        </p>
                    </div>

                    <!-- Passo 3 -->
                    <div class="flashlight-card p-6 bg-stone-900 text-white border-[#d6bc8c]/50">
                        <div class="text-2xl font-display font-bold text-amber-300 mb-3">03</div>
                        <h3 class="text-base font-bold font-display text-white mb-1.5">A IA recomenda</h3>
                        <p class="text-xs text-stone-300 leading-relaxed">
                            O sistema cruza as respostas em tempo real e entrega a melhor opção com motivo claro.
                        </p>
                    </div>

                    <!-- Passo 4 -->
                    <div class="flashlight-card p-6">
                        <div class="text-2xl font-display font-bold text-[#d6bc8c] mb-3">04</div>
                        <h3 class="text-base font-bold font-display text-stone-950 mb-1.5">Você converte</h3>
                        <p class="text-xs text-stone-600 leading-relaxed">
                            O cliente fecha a compra ou agenda direto com você com alto nível de decisão.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- DEMO INTERATIVA (Concierge IA em Tempo Real) -->
        <section class="py-14 sm:py-20 px-5 sm:px-6 bg-white border-t border-b border-stone-300" id="demo">
            <div class="max-w-5xl mx-auto">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-14 items-start">
                    <div>
                        <h2 class="text-2xl sm:text-4xl font-bold font-display text-stone-950 leading-tight">
                            Diagnostica, qualifica e recomenda em segundos.
                        </h2>
                        <p class="text-sm sm:text-base mt-4 text-stone-600 leading-relaxed">
                            Experimente ao lado como o Concierge de IA funciona na prática. Ele entende a resposta de cada visitante e entrega a solução exata com argumento de valor.
                        </p>

                        <div class="mt-8">
                            <a href="cadastrar.html" class="btn-gold-spin">
                                <span class="spin-border"></span>
                                <span class="relative flex items-center justify-center gap-2 px-7 py-3.5 rounded-full bg-[#0a0a0a] text-white text-xs font-bold uppercase tracking-widest">
                                    <span>Montar meu concierge agora</span>
                                    <iconify-icon icon="solar:arrow-right-linear" class="text-amber-300"></iconify-icon>
                                </span>
                            </a>
                        </div>
                    </div>

                    <!-- Interactive Concierge Widget -->
                    <div class="flashlight-card p-6 sm:p-8" id="concierge-widget">
                        <!-- Step 1 -->
                        <div id="quiz-step-1" class="quiz-step">
                            <p class="text-xs font-mono font-bold uppercase tracking-wider text-[#d6bc8c] mb-1">Passo 1 de 3</p>
                            <h3 class="text-lg font-bold font-display text-stone-950 mb-4">Como você está no seu negócio hoje?</h3>
                            <div class="space-y-2.5">
                                <button onclick="nextQuizStep(1, 'Estou começando')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Estou começando agora</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(1, 'Vendo sem previsibilidade')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Vendo, mas sem consistência</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(1, 'Tenho estrutura desorganizada')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Tenho demanda, mas falta organização</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(1, 'Quero escala')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Já faturei alto, quero escala e autoridade</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 2 -->
                        <div id="quiz-step-2" class="quiz-step hidden">
                            <p class="text-xs font-mono font-bold uppercase tracking-wider text-[#d6bc8c] mb-1">Passo 2 de 3</p>
                            <h3 class="text-lg font-bold font-display text-stone-950 mb-4">Qual seu objetivo principal agora?</h3>
                            <div class="space-y-2.5">
                                <button onclick="nextQuizStep(2, 'Atrair clientes qualificados')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Atrair clientes qualificados</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(2, 'Aumentar ticket')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Aumentar o valor das minhas vendas</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(2, 'Automatizar 24h')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Automatizar vendas 24h sem esforço manual</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="nextQuizStep(2, 'Publicar livro')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Publicar livro e lançar mentoria</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 3 -->
                        <div id="quiz-step-3" class="quiz-step hidden">
                            <p class="text-xs font-mono font-bold uppercase tracking-wider text-[#d6bc8c] mb-1">Passo 3 de 3</p>
                            <h3 class="text-lg font-bold font-display text-stone-950 mb-4">Qual sua faixa de faturamento mensal?</h3>
                            <div class="space-y-2.5">
                                <button onclick="finishQuiz('Até 10k')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Até R$ 10.000 / mês</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="finishQuiz('De 10k a 50k')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>De R$ 10.000 a R$ 50.000 / mês</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                                <button onclick="finishQuiz('Acima de 50k')" class="w-full text-left px-4 py-3 rounded-2xl text-sm font-medium bg-stone-50 hover:bg-stone-900 hover:text-white border border-stone-200 transition-all flex items-center justify-between group">
                                    <span>Mais de R$ 50.000 / mês</span>
                                    <span class="text-stone-400 group-hover:text-amber-300">→</span>
                                </button>
                            </div>
                        </div>

                        <!-- Result -->
                        <div id="quiz-result" class="quiz-step hidden text-center py-2">
                            <div class="w-12 h-12 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center mx-auto mb-3 text-2xl">
                                <iconify-icon icon="solar:check-circle-bold"></iconify-icon>
                            </div>
                            <h4 class="text-xl font-bold font-display text-stone-950">Plano Recomendado: ELOOO BIO Pro</h4>
                            <p class="text-xs text-stone-600 mt-1 mb-5">
                                A IA identificou que seu maior gargalo é a automação e triagem de leads qualificados antes de atender.
                            </p>
                            <a href="cadastrar.html?plan=pro" class="btn-gold-spin w-full">
                                <span class="spin-border"></span>
                                <span class="relative block w-full py-3.5 rounded-full bg-[#0a0a0a] text-white text-xs font-bold uppercase tracking-widest text-center">
                                    Ativar Plano Pro →
                                </span>
                            </a>
                            <button onclick="resetQuiz()" class="mt-3 text-xs text-stone-500 hover:text-stone-950 underline">
                                Refazer teste
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- AGENDA INTEGRADA -->
        <section class="py-14 sm:py-20 px-5 sm:px-6" id="agenda">
            <div class="max-w-5xl mx-auto">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-14 items-center">
                    <div>
                        <h2 class="text-2xl sm:text-4xl font-bold font-display text-stone-950 leading-tight">
                            Da recomendação ao horário marcado.
                        </h2>
                        <p class="text-sm sm:text-base mt-4 text-stone-600 leading-relaxed">
                            O cliente seleciona o dia, o horário e o tipo de atendimento direto na sua bio. Sem ida e volta de mensagens. Confirmação instantânea no seu WhatsApp.
                        </p>

                        <div class="mt-7">
                            <a href="cadastrar.html" class="btn-gold-spin">
                                <span class="spin-border"></span>
                                <span class="relative flex items-center justify-center gap-2 px-7 py-3.5 rounded-full bg-[#0a0a0a] text-white text-xs font-bold uppercase tracking-widest">
                                    <span>Ativar minha agenda</span>
                                    <iconify-icon icon="solar:arrow-right-linear" class="text-amber-300"></iconify-icon>
                                </span>
                            </a>
                        </div>
                    </div>

                    <!-- Clean Calendar Preview -->
                    <div class="flashlight-card p-6 max-w-sm mx-auto w-full">
                        <div class="flex items-center justify-between mb-4 pb-3 border-b border-stone-200">
                            <span class="text-xs font-bold font-display text-stone-950 uppercase tracking-wider">Junho 2026</span>
                            <div class="flex gap-1">
                                <button class="w-6 h-6 rounded bg-stone-100 text-stone-700 text-xs">‹</button>
                                <button class="w-6 h-6 rounded bg-stone-100 text-stone-700 text-xs">›</button>
                            </div>
                        </div>

                        <div class="grid grid-cols-7 gap-1 text-center text-[10px] font-mono font-bold text-stone-400 mb-2">
                            <div>D</div><div>S</div><div>T</div><div>Q</div><div>Q</div><div>S</div><div>S</div>
                        </div>

                        <div class="grid grid-cols-7 gap-1 text-center text-xs font-medium">
                            <div class="py-1.5 text-stone-300">31</div>
                            <button class="py-1.5 rounded-lg bg-stone-50 hover:bg-stone-200">1</button>
                            <button class="py-1.5 rounded-lg bg-stone-50 hover:bg-stone-200">2</button>
                            <div class="py-1.5 text-stone-300 line-through">3</div>
                            <button class="py-1.5 rounded-lg bg-stone-50 hover:bg-stone-200">4</button>
                            <button class="py-1.5 rounded-lg bg-stone-50 hover:bg-stone-200">5</button>
                            <div class="py-1.5 text-stone-300">6</div>
                            <div class="py-1.5 text-stone-300">7</div>
                            <button class="py-1.5 rounded-lg bg-stone-50 hover:bg-stone-200">8</button>
                            <div class="py-1.5 text-stone-300 line-through">9</div>
                            <button class="py-1.5 rounded-lg bg-stone-950 text-white font-bold border border-[#d6bc8c]">10</button>
                            <button class="py-1.5 rounded-lg bg-stone-50 hover:bg-stone-200">11</button>
                            <button class="py-1.5 rounded-lg bg-stone-50 hover:bg-stone-200">12</button>
                            <div class="py-1.5 text-stone-300">13</div>
                        </div>

                        <div class="mt-4 pt-3 border-t border-stone-200">
                            <p class="text-[11px] font-mono font-bold text-stone-600 mb-2">Horários Disponíveis (10 de Junho)</p>
                            <div class="grid grid-cols-3 gap-1.5 text-xs font-semibold">
                                <button class="py-1.5 rounded-lg bg-stone-100 hover:bg-stone-950 hover:text-white transition-colors">09:00</button>
                                <button class="py-1.5 rounded-lg bg-stone-950 text-white font-bold border border-[#d6bc8c]">10:30</button>
                                <button class="py-1.5 rounded-lg bg-stone-100 hover:bg-stone-950 hover:text-white transition-colors">14:00</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- PLANOS & PREÇOS -->
        <section class="py-14 sm:py-24 px-5 sm:px-6 bg-white border-t border-b border-stone-300" id="planos">
            <div class="max-w-5xl mx-auto">
                <div class="text-center mb-12">
                    <h2 class="text-2xl sm:text-4xl font-bold font-display text-stone-950 leading-tight">
                        Planos desenhados para o seu momento.
                    </h2>
                    <p class="text-sm sm:text-base mt-2 text-stone-600">
                        Comece simples e suba de plano conforme vende mais.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto items-stretch">
                    
                    <!-- Starter -->
                    <div class="flashlight-card p-7 flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-bold font-display text-stone-950">Starter</h3>
                            <p class="text-xs text-stone-500 mt-1 mb-5">Sua presença pronta pra vender.</p>
                            
                            <div class="mb-5">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-extrabold font-display text-stone-950">R$ 97</span>
                                    <span class="text-xs text-stone-500 font-medium">/mês</span>
                                </div>
                                <p class="text-[11px] font-mono text-stone-400 mt-0.5">R$ 81/mês no plano anual</p>
                            </div>

                            <ul class="space-y-2.5 mb-7 text-xs text-stone-700">
                                <li class="flex items-center gap-2">✓ Bio profissional + vitrine de produtos</li>
                                <li class="flex items-center gap-2">✓ Captura de contato no WhatsApp</li>
                                <li class="flex items-center gap-2">✓ Setup guiado em 2 minutos</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=starter" class="block w-full py-3 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-900 font-bold text-center text-xs uppercase tracking-wider transition-colors">
                            Começar com Starter
                        </a>
                    </div>

                    <!-- Pro (Destaque Dark com Borda Giratória Gold) -->
                    <div class="flashlight-card p-7 flex flex-col justify-between bg-[#11100E] text-white relative shadow-2xl scale-[1.03] border-2 border-[#d6bc8c]">
                        <span class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full text-[10px] font-mono font-bold uppercase tracking-wider bg-[#d6bc8c] text-stone-950 shadow-md">
                            ★ Mais Escolhido
                        </span>

                        <div>
                            <h3 class="text-2xl font-bold font-display text-white mt-1">Pro</h3>
                            <p class="text-xs text-stone-400 mt-1 mb-5">A IA que qualifica e vende por você 24h.</p>
                            
                            <div class="mb-5">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-4xl font-extrabold font-display text-white">R$ 147</span>
                                    <span class="text-xs text-stone-400 font-medium">/mês</span>
                                </div>
                                <p class="text-[11px] font-mono text-amber-200/80 mt-0.5">R$ 123/mês no plano anual</p>
                            </div>

                            <ul class="space-y-3 mb-7 text-xs text-stone-200">
                                <li class="flex items-center gap-2 font-bold text-amber-300">✓ Tudo do Starter</li>
                                <li class="flex items-center gap-2 font-semibold text-white">✓ Concierge com IA inteligente</li>
                                <li class="flex items-center gap-2">✓ CRM de leads + roteamento para WhatsApp</li>
                                <li class="flex items-center gap-2">✓ Métricas e analytics de conversão</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=pro" class="btn-gold-spin w-full">
                            <span class="spin-border"></span>
                            <span class="relative block w-full py-3.5 rounded-full bg-[#1c1917] text-white font-bold text-xs uppercase tracking-widest text-center">
                                Começar com Pro →
                            </span>
                        </a>
                    </div>

                    <!-- Elite -->
                    <div class="flashlight-card p-7 flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-bold font-display text-stone-950">Elite</h3>
                            <p class="text-xs text-stone-500 mt-1 mb-5">Seu negócio rodando no automático.</p>
                            
                            <div class="mb-5">
                                <div class="flex items-baseline gap-1">
                                    <span class="text-3xl font-extrabold font-display text-stone-950">R$ 197</span>
                                    <span class="text-xs text-stone-500 font-medium">/mês</span>
                                </div>
                                <p class="text-[11px] font-mono text-stone-400 mt-0.5">R$ 164/mês no plano anual</p>
                            </div>

                            <ul class="space-y-2.5 mb-7 text-xs text-stone-700">
                                <li class="flex items-center gap-2 font-semibold">✓ Tudo do Pro</li>
                                <li class="flex items-center gap-2 font-semibold">✓ Agendamento sincronizado</li>
                                <li class="flex items-center gap-2">✓ IA com limites ampliados</li>
                                <li class="flex items-center gap-2">✓ Suporte prioritário no WhatsApp</li>
                            </ul>
                        </div>

                        <a href="cadastrar.html?plan=elite" class="block w-full py-3 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-900 font-bold text-center text-xs uppercase tracking-wider transition-colors">
                            Começar com Elite
                        </a>
                    </div>

                </div>

                <!-- Garantia 7 Dias -->
                <div class="max-w-4xl mx-auto mt-10 text-center">
                    <p class="text-xs text-stone-600 font-medium flex items-center justify-center gap-2">
                        <iconify-icon icon="solar:shield-check-bold" class="text-emerald-600 text-base"></iconify-icon>
                        <span>Garantia incondicional de 7 dias — não gostou, devolvemos 100% do valor.</span>
                    </p>
                </div>
            </div>
        </section>

        <!-- CTA FINAL (Obsidian Dark with Gold Moving Border) -->
        <section class="py-16 sm:py-20 px-6 text-center bg-[#0a0a0a] text-white">
            <div class="max-w-2xl mx-auto">
                <img src="static/images/ELOOO LOGO.png" alt="ELOOO BIO PREMIUM" class="h-12 object-contain mx-auto mb-5 filter brightness-0 invert"/>
                <h2 class="text-3xl sm:text-5xl font-bold font-display mb-3">Sua bio pronta em 2 minutos.</h2>
                <p class="text-stone-400 text-sm sm:text-base mb-8">
                    Crie sua conta agora e comece a conduzir decisões de compra.
                </p>
                <a href="cadastrar.html" class="btn-gold-spin scale-105">
                    <span class="spin-border"></span>
                    <span class="relative flex items-center justify-center gap-2 px-9 py-4 rounded-full bg-[#141311] text-[#f6e3c5] text-xs sm:text-sm font-bold uppercase tracking-widest">
                        <span>Criar conta e começar →</span>
                    </span>
                </a>
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer class="py-10 px-6 text-center text-xs text-stone-500 bg-white border-t border-stone-300">
        <p>© 2026 ELOOO BIO PREMIUM · Ecossistema <strong class="text-stone-900">ELOOO International Group</strong>.</p>
        <div class="flex items-center justify-center gap-6 mt-3 font-mono">
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

        // Mobile Drawer Toggle
        const drawer = document.getElementById('mobile-drawer');
        const drawerContent = document.getElementById('mobile-drawer-content');
        const openBtn = document.getElementById('mobile-hamburger-btn');
        const closeBtn = document.getElementById('mobile-drawer-close');
        const mobileLinks = document.querySelectorAll('.mobile-link');

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
        mobileLinks.forEach(l => l.addEventListener('click', closeDrawer));

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

        <!-- Plan Selector Bar -->
        <div class="mb-5 p-1 rounded-2xl bg-stone-100 grid grid-cols-3 gap-1 text-xs font-bold text-center">
            <button type="button" onclick="selectPlan('starter')" id="btn-starter" class="py-2 rounded-xl transition-colors text-stone-600">Starter</button>
            <button type="button" onclick="selectPlan('pro')" id="btn-pro" class="py-2 rounded-xl bg-stone-950 text-white shadow-sm transition-colors">Pro</button>
            <button type="button" onclick="selectPlan('elite')" id="btn-elite" class="py-2 rounded-xl transition-colors text-stone-600">Elite</button>
        </div>

        <form class="space-y-3.5" onsubmit="event.preventDefault(); window.location.href='https://wa.me/5547988660791?text=Ol%C3%A1%2C%20acabei%20de%20me%20cadastrar%20no%20ELOOO%20BIO%20PREMIUM%20e%20quero%20ativar%20minha%20conta.';">
            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Nome Completo</label>
                <input type="text" required placeholder="Seu nome" class="w-full px-4 py-3 rounded-xl text-sm bg-stone-50 border border-stone-300 focus:border-stone-900 outline-none transition-colors"/>
            </div>

            <div>
                <label class="block text-xs font-bold text-stone-700 mb-1">Usuário da sua Bio</label>
                <div class="flex items-center rounded-xl bg-stone-50 border border-stone-300 focus-within:border-stone-900 overflow-hidden">
                    <span class="px-3 text-xs text-stone-400">bio.elooo.com.br/</span>
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
                <p>Os leads e clientes capturados pela sua bio pertencem 100% a você.</p>
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
    print("Generating ELOOO BIO PREMIUM pages with Space Grotesk typography, moving gold borders, flashlight cards and elevated smartphone mockup...")
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
