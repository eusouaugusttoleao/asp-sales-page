#!/usr/bin/env python3
"""
Consolida as 13 seções v3.4 dos previews em um único index-v3.4-final.html
Estratégia:
- Pega a estrutura base (head + nav + escassez + ticker + js) do preview 01-hero
- Para cada preview, extrai apenas o CSS section-specific + o HTML <section>
- Monta o arquivo final em ordem
"""
import re
from pathlib import Path

REPO = Path("/Users/franklinaugustto/Desktop/asp-sales-page")
PREVIEWS = REPO / "previews"
OUT = REPO / "index-v3.4-final.html"

SECTIONS = [
    "01-hero",
    "02-algema",
    "2.5-nao-e-pra",
    "03-agitacao",
    "04-historia",
    "05-oferta",
    "06-pedras",
    "07-vozes",
    "08-cases",
    "09-demo",
    "10-bonus",
    "11-faq",
    "12-urgencia",
]


def read_preview(slug):
    return (PREVIEWS / f"secao-{slug}" / "index.html").read_text()


def extract_style(html):
    """Pega o conteúdo entre <style> e </style>."""
    m = re.search(r"<style>\s*(.*?)\s*</style>", html, re.S)
    return m.group(1) if m else ""


def extract_section(html):
    """Pega o <section ...>...</section> principal (primeiro)."""
    m = re.search(r"(<section[^>]+>.*?</section>)", html, re.S)
    return m.group(1) if m else ""


def strip_preview_banner_css(css):
    """Remove a regra .preview-banner do CSS (não vai pra produção)."""
    return re.sub(r"\.preview-banner\s*\{[^}]*\}\s*", "", css, flags=re.S)


def main():
    # Lê todos os previews
    previews = {slug: read_preview(slug) for slug in SECTIONS}

    # CSS de cada preview, com preview-banner stripped
    all_css = []
    for slug in SECTIONS:
        css = extract_style(previews[slug])
        css = strip_preview_banner_css(css)
        all_css.append(f"\n/* ============================================================\n   SEÇÃO {slug.upper()}\n   ============================================================ */\n{css}\n")

    merged_css = "\n".join(all_css)

    # Sections HTML em ordem
    section_blocks = []
    for slug in SECTIONS:
        sec = extract_section(previews[slug])
        section_blocks.append(f"\n<!-- ========== SEÇÃO {slug.upper()} ========== -->\n{sec}\n")

    sections_html = "\n".join(section_blocks)

    # Pega nav e escassez do preview 01 (são iguais nos demais)
    nav_m = re.search(r"(<nav class=\"nav\">.*?</nav>)", previews["01-hero"], re.S)
    nav_html = nav_m.group(1) if nav_m else ""

    escassez_m = re.search(r"(<!-- ESCASSEZ.*?-->\s*<div class=\"escassez-bar\">.*?</div>\s*</div>\s*</div>)", previews["01-hero"], re.S)
    # Fallback simpler match
    if not escassez_m:
        escassez_m = re.search(r"(<div class=\"escassez-bar\">.*?</div>\s*</div>\s*</div>)", previews["01-hero"], re.S)
    escassez_html = escassez_m.group(1) if escassez_m else ""

    # Ticker: pega do preview 12-urgencia (clima de fechamento, mas qualquer um funciona)
    ticker_m = re.search(r"(<div class=\"rocha-rail\">.*?</div>\s*</div>)", previews["12-urgencia"], re.S)
    ticker_html = ticker_m.group(1) if ticker_m else ""

    # Script da contagem de vagas (pega do 01-hero)
    script_m = re.search(r"(<script>.*?</script>)", previews["01-hero"], re.S)
    script_html = script_m.group(1) if script_m else ""

    # Monta o documento final
    final = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ative Seu Poder · ASP® · Augustto Leão</title>
<meta name="description" content="Em 3 meses você sai da névoa para a clareza: ativa o que está travado e multiplica seus resultados em 3 a 10 vezes em performance, posicionamento e dinheiro.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
<style>
{merged_css}
</style>
</head>
<body>

{nav_html}

{escassez_html}

<main>
{sections_html}
</main>

{ticker_html}

{script_html}

</body>
</html>
"""

    OUT.write_text(final)
    lines = final.count("\n")
    size_kb = len(final) / 1024
    print(f"✅ Gerado: {OUT}")
    print(f"   {lines:,} linhas · {size_kb:.1f} KB")
    print(f"   {len(SECTIONS)} seções consolidadas")


if __name__ == "__main__":
    main()
