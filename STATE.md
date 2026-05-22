# ASP Sales Page · STATE
**Última atualização:** 2026-05-19
**Arquivo de trabalho:** `~/Desktop/asp-sales-page/index-v3.4-final.html`

---

## 🟢 Onde paramos

Auditoria completa de imagens concluída. Página `index-v3.4-final.html` está estável com:
- Reorganização da seção O MECANISMO (tabela subiu · pedras inline · grid removido · encerramento ao final · footer visual com 7 pedras 20%)
- Auditoria de preços fechada (A DECISÃO R$ 7.476 intermediário · BÔNUS REVELADOS R$ 11.967 · 3 mentorias reveladas no meio)
- Tese lockup banner adicionado antes de O MECANISMO
- 11 correções da última rodada aplicadas (duplicata removida · ato 2 reescrito · vozes com hover silence · cases novo hook · Emerson PRESIDENTE · Practitioner 10 anos · oferta R$1.685/R$1.497)

---

## 🔴 PRÓXIMA AÇÃO · aguardando 32 imagens do Franklin

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
