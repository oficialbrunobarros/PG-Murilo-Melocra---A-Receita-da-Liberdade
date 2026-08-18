# INFRA · Mapa de domínios (LEIA ANTES DE MEXER NO vercel.json)

> Dois agentes trabalham neste repo (Antigravity = páginas · Claude Code = infra/app).
> Antes de qualquer mudança: `git pull`. No `vercel.json`, mexa só no que é seu.

## O mapa

| Host | Serve | Projeto Vercel |
|---|---|---|
| elooo.com.br | institucional (HOJE: WordPress externo via Cloudflare) | — (futuro: gateway `index.html` deste repo) |
| editora.elooo.com.br | `/editora` (editora + autores + livros) | eloooeditora (este repo) |
| bio.elooo.com.br | LP da Bio Premium (`/bio/index`) + **slugs de usuário via proxy** | pg-murilo-melocra (este repo) |
| content.elooo.com.br | `/content` (LP da ferramenta — criar `content.html`) | pg-murilo-melocra (este repo) |
| academy.elooo.com.br | `/academy` (vitrine — criar `academy.html`) | pg-murilo-melocra (este repo) |
| app.elooo.com.br | o SEAAS/app (repo elooo-system) | elooo-system |

## Regras que NÃO podem ser removidas do vercel.json

1. **Proxies do host bio** (as páginas dos usuários vêm do app):
   - `/api/midia` → `https://app.elooo.com.br/api/midia`
   - `/:slug([a-z0-9][a-z0-9-]{1,58}[a-z0-9])` → `https://app.elooo.com.br/api/midia?bio=1&slug=:slug`
   Elas ficam ANTES do fallback `/:path*`. Qualquer path de 3+ caracteres no host
   bio que não seja página da LP vira bio de usuário.
2. **Redirects de raiz por host** (arquivo estático vence rewrite; raiz dinâmica
   exige redirect): `/`→`/inicio` (bio), `/`→`/editora`, `/`→`/content`, `/`→`/academy`.
3. **`cleanUrls: true`**: destino de rewrite NUNCA termina em `.html`
   (o arquivo fica oculto e dá 404). Use o path limpo (`/bio/entrar`).
4. **Headers de segurança** no topo (HSTS/nosniff/XFO/referrer/permissions).
   Não adicionar CSP aqui: os slugs de usuário passam pelo proxy e já recebem
   a CSP do app — uma segunda CSP viraria interseção e quebraria embeds.

## Para novas LPs

Criar `content.html` / `academy.html` na raiz (o redirect da raiz do host já
aponta para lá). Assets em `/static/`. Nomes de página na raiz do host bio são
alcançáveis pelos usuários? Não — slugs reservados no app: `premium, api,
admin, app, www, bio, elooo-oficial` + os paths da LP (`inicio, entrar,
cadastrar, termos, privacidade, demo`) resolvem primeiro pelas rewrites da LP.
