import os

# Author data mapped from screenshots
authors = [
    {
        "slug": "tatiana-fonseca",
        "name": "Tatiana Fonseca",
        "title_br": "Tatiana<br>Fonseca",
        "book": "Permaneça - O Caminho para a Plenitude",
        "category": "DIAMOND",
        "points": "1.656"
    },
    {
        "slug": "kenje-kambara",
        "name": "Kenje Kambara",
        "title_br": "Kenje<br>Kambara",
        "book": "Os Segredos do Lojista Fora da Curva (B2B) & Os Segredos do Mercado Automotivo (B2C)",
        "category": "VIP",
        "points": "1.028"
    },
    {
        "slug": "berenice-duarte-borba",
        "name": "Berenice Duarte Borba",
        "title_br": "Berenice<br>Duarte Borba",
        "book": "De Ateu ao Encontro com Deus Pai",
        "category": "PRIME",
        "points": "978"
    },
    {
        "slug": "vanessa-rodrigues",
        "name": "Dra. Vanessa Rodrigues",
        "title_br": "Dra. Vanessa<br>Rodrigues",
        "book": "Emagreça Saudável e Feliz",
        "category": "PRIME",
        "points": "880"
    },
    {
        "slug": "berg-junior",
        "name": "Berg Junior",
        "title_br": "Berg<br>Junior",
        "book": "Recalculando a Rota",
        "category": "VIP",
        "points": "640"
    },
    {
        "slug": "carine-aparecida",
        "name": "Carine Aparecida",
        "title_br": "Carine<br>Aparecida",
        "book": "Além da Beleza",
        "category": "VIP",
        "points": "538"
    },
    {
        "slug": "franklyn-fuck",
        "name": "Franklyn Fuck",
        "title_br": "Franklyn<br>Fuck",
        "book": "O Maná do Vendedor",
        "category": "VIP",
        "points": "534"
    },
    {
        "slug": "fernando-merlos",
        "name": "Dr. Fernando Merlos",
        "title_br": "Dr. Fernando<br>Merlos",
        "book": "Alma Médica",
        "category": "VIP",
        "points": "526"
    },
    {
        "slug": "dimas-neto",
        "name": "Dimas Neto",
        "title_br": "Dimas<br>Neto",
        "book": "A Arte da Persistência",
        "category": "VIP",
        "points": "514"
    },
    {
        "slug": "anildo-silva",
        "name": "Anildo Silva",
        "title_br": "Anildo<br>Silva",
        "book": "A Missão do Fundador",
        "category": "VIP",
        "points": "412"
    },
    {
        "slug": "savio-cardoso",
        "name": "Dr. Sávio Cardoso",
        "title_br": "Dr. Sávio<br>Cardoso",
        "book": "O Código da Vitalidade Masculina",
        "category": "VIP",
        "points": "412"
    },
    {
        "slug": "hewandro-entringer",
        "name": "Hewandro Entringer",
        "title_br": "Hewandro<br>Entringer",
        "book": "Os Códigos do Networking",
        "category": "VIP",
        "points": "412"
    },
    {
        "slug": "claudio-dutra",
        "name": "Cláudio Dutra",
        "title_br": "Cláudio<br>Dutra",
        "book": "Profissional Inquestionável",
        "category": "VIP",
        "points": "408"
    },
    {
        "slug": "marcio-lira",
        "name": "Márcio Lira",
        "title_br": "Márcio<br>Lira",
        "book": "Profissional Inquestionável",
        "category": "VIP",
        "points": "408"
    },
    {
        "slug": "diego-arcas",
        "name": "Diego Arcas",
        "title_br": "Diego<br>Arcas",
        "book": "Despertando os Propósitos de Deus",
        "category": "VIP",
        "points": "408"
    },
    {
        "slug": "rafael-cavalcanti",
        "name": "Rafael Cavalcanti",
        "title_br": "Rafael<br>Cavalcanti",
        "book": "Os Códigos da Lucratividade",
        "category": "VIP",
        "points": "408"
    },
    {
        "slug": "gabriela-mendes",
        "name": "Dra. Gabriela Mendes",
        "title_br": "Dra. Gabriela<br>Mendes",
        "book": "Título a definir",
        "category": "VIP",
        "points": "408"
    },
    {
        "slug": "herick-pereira",
        "name": "Herick Pereira",
        "title_br": "Herick<br>Pereira",
        "book": "O Código do Campeão",
        "category": "VIP",
        "points": "408"
    },
    {
        "slug": "gustavo-da-silva",
        "name": "Dr. Gustavo da Silva",
        "title_br": "Dr. Gustavo<br>da Silva",
        "book": "Título a definir",
        "category": "VIP",
        "points": "408"
    },
    {
        "slug": "douglas-vacilotto",
        "name": "Douglas Vacilotto",
        "title_br": "Douglas<br>Vacilotto",
        "book": "Rompendo Fronteiras",
        "category": "VIP",
        "points": "318"
    },
    {
        "slug": "edson-fabiano",
        "name": "Edson Fabiano",
        "title_br": "Edson<br>Fabiano",
        "book": "Shammah - O Deus que Ouve",
        "category": "VIP",
        "points": "310"
    }
]

template_path = "src/autores/template-autor.html"

def generate():
    if not os.path.exists(template_path):
        print(f"Error: Template {template_path} not found!")
        return

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    os.makedirs('src/autores', exist_ok=True)

    for author in authors:
        dest_path = f"src/autores/{author['slug']}.html"
        
        # Replace template placeholders
        content = template_content
        content = content.replace("Nome do Autor | ELOOO International Group", f"{author['name']} | ELOOO International Group")
        content = content.replace("Nome do<br>\n                    Autor", author['title_br'])
        content = content.replace("static/assets/video_frames_murilo", f"static/assets/video_frames_{author['slug']}")
        content = content.replace("Uma frase de impacto marcante sobre o propósito e a <span class=\"font-medium text-stone-200\">transformação principal</span> gerada pelo autor.", f"Autor do livro <span class=\"font-medium text-stone-200\">{author['book']}</span>. Mentor e palestrante oficial do ELOOO International Group.")
        
        # Write file
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Generated: {dest_path}")

if __name__ == "__main__":
    generate()
