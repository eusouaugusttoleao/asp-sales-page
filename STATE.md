# ASP Sales Page · STATE
**Última atualização:** 2026-05-27 (rodada 2 · 15h50)
**Arquivo de trabalho:** `~/Desktop/asp-sales-page/index-v3.4-final.html`
**Backup com depoimentos:** `index-v3.4-COM-DEPOIMENTOS-backup-2026-05-27.html`

---

## 🟢 Rodada 2 · 27/05 15h50 · 11 ajustes aplicados

1. **Hero** · imagem aumentada · `grid: 1fr 1.05fr` + `align-items: stretch` + `.hero-right height:100%`
2. **Nav-cta GARANTIR VAGA** · fonte verde escura `#062b12` + `font-weight: 800`
3. **Algemas SVG** · subidas · `.algema-grid align: flex-start` + `.algema-visual position: sticky top:90px` + padding-top
4. **Frase "meio milhão"** · reescrita: "Foi mais um milhão ao longo de 10 anos, em cursos, mentorias e treinamentos, eventos e imersões..."
5. **ATO 2 enquadramento** · `aspect-ratio: 4/5` + `object-position: center 25%` (preserva rostos)
6. **ATO 3 título** · prefixado "Em 2019 todos que ajudei..."
7. **ATO 3 aside** · completado "E encontra quem acredita em você."
8. **ATO 4 enquadramento** · idem ATO 2 (CSS comum `.ato-photos img`)
9. **ATO 5 aumentado** · grid `repeat(2, 1fr)` + `aspect-ratio: 4/5` + 5ª foto wide span 2
10. **Endorse Emerson** · quote real ("Augustto é um monstro...") + role-note ("De vendedor de perfume, a CMO de Multinacional.")
11. **REMOVIDOS temporariamente** (preservados no backup): 3 vídeos prioritários + 6 depoimentos antes/depois + megatype "ELES ATIVARAM"

---

## 🟢 Rodada 1 · 27/05 manhã · Imagens reais inseridas (24 de 32)
- ATO 1 · 4/4 fotos reais
- ATO 2 · 5/4 fotos (ganhou 5ª "Hospital público" em formato wide) · narrativa 03+04 atualizada (destaque nacional · coordenador nacional)
- ATO 3 · 4/4 fotos reais
- ATO 4 · 4/4 fotos · narrativa 02+03 atualizada (despedida da indústria · Itália reconstrução pessoal)
- ATO 5 · 5 fotos (sem palestra que não chegou · caribe trocado por salto de paraquedas em Dubai)
- DEPOIMENTOS · endorse-emerson + case-01-kaue reais · cases 02-09 ainda em SVG placeholder

CSS aditivo: `.ato-photos img` (4:3 cover · radius 10 · saturate 0.9) + `.ato-photos img.wide` (span 2 · 16:9) pra foto 05 do ATO 2.

---

## 🟡 PRÓXIMA AÇÃO · 8 cases pendentes
- case-02-bruno · case-03-tony · case-04-aline-joel · case-05-luis-felipe · case-06-lucas-passos · case-07-marcelo · case-08-nata · case-09-andre
- Quando chegarem: substituir `.svg` por `.jpg` nos `<img>` correspondentes.

---

## 📦 Histórico anterior · aguardando 32 imagens do Franklin

Estrutura de pastas criada em `~/Desktop/asp-sales-page/assets/`:

```
atos/
├── ato-1/   ← 01.jpg · 02.jpg · 03.jpg · 04.jpg   (20 anos · 1º DP)
├── ato-2/   ← 01.jpg · 02.jpg · 03.jpg · 04.jpg   (filha · promessa de pai)
├── ato-3/   ← 01.jpg · 02.jpg · 03.jpg · 04.jpg   (traição · CMO)
└── ato-4/   ← 01.jpg · 02.jpg · 03.jpg · 04.jpg   (burnout · gênese método)

ato5/   ← substitui SVGs existentes
├── ato5-dubai.jpg
├── ato5-caribe.jpg
├── ato5-harley.jpg
├── ato5-palestra.jpg
├── ato5-familia.jpg
└── ato5-palco.jpg

cases/   ← substitui SVGs existentes
├── endorse-emerson.jpg          (Emerson Ventura · Presidente Luci Luci)
├── case-01-kaue.jpg             (Kauê Petry · Tier S · 16:9)
├── case-02-bruno.jpg            (Bruno Criativo · Tier S · 16:9)
├── case-03-tony.jpg             (Tony Burses · Tier S · 16:9)
├── case-04-aline-joel.jpg       (Aline e Joel Daleprane · 4:3)
├── case-05-luis-felipe.jpg      (Luis Felipe · posto · 4:3)
├── case-06-lucas-passos.jpg     (Lucas Passos · 4:3)
├── case-07-marcelo.jpg          (Marcelo Brick · 4:3)
├── case-08-nata.jpg             (Natã Kesller · 4:3)
└── case-09-andre.jpg            (André Antunes · 4:3)
```

### Quando Franklin disser "imagens estão lá":
1. Rodar `ls -la` em cada pasta pra detectar o que chegou
2. Substituir os `<div class="slot">foto 0X</div>` em atos 1-4 por `<img src="assets/atos/ato-X/0Y.jpg">` (manter o CSS .ato-photos atual)
3. Trocar extensões `.svg` por `.jpg` nas tags `<img>` de ato5/ e cases/
4. Reabrir página pra conferir

---

## 📋 Estado dos arquivos no projeto

- `index-v3.4-final.html` · página principal (em uso · ~7400 linhas)
- `index.html` · v3.3 antiga (não mexer)
- `build-v3.4-final.py` · script de build (referência)
- `previews/` · seções individuais (referência)
- `assets/` · imagens (estrutura nova criada hoje)
- `STATE.md` · este arquivo

---

## 🎨 Especificações de imagem

- **Atos 1-4:** JPG · 4:3 · ~1200×900
- **Ato 5:** JPG · 4:3 · ~1200×900 · substitui SVG
- **Endorse Emerson:** JPG · 1:1 ou 4:5 · 800×800 mínimo
- **Cases vídeo (01-03):** JPG · 16:9 · 1280×720
- **Cases depoimento (04-09):** JPG · 4:3 · 1000×750

---

## 🚀 Comandos rápidos

```bash
# Abrir página
open ~/Desktop/asp-sales-page/index-v3.4-final.html

# Listar imagens chegadas
ls -la ~/Desktop/asp-sales-page/assets/atos/ato-1/
ls -la ~/Desktop/asp-sales-page/assets/atos/ato-2/
ls -la ~/Desktop/asp-sales-page/assets/atos/ato-3/
ls -la ~/Desktop/asp-sales-page/assets/atos/ato-4/
ls -la ~/Desktop/asp-sales-page/assets/ato5/
ls -la ~/Desktop/asp-sales-page/assets/cases/
```
