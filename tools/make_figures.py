# -*- coding: utf-8 -*-
"""Dibuja las figuras del grafo de dependencias en los dos idiomas.

    python3 tools/make_figures.py

Escribe es/grafo_*.svg y en/*_graph.svg. Estilo: figura de publicacion.
Draws the dependency-graph figures in both languages; run from the repo root.
"""
import math, io, os

TINTA, GRIS, SUAVE = "#111827", "#6b7280", "#9ca3af"
RELLENO, REJILLA, BORDE = "#f3f4f6", "#eef2f6", "#d1d5db"
MONO  = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SERIF = "Georgia,'Times New Roman',serif"

ES = {
    "dir": "es", "f1": "grafo_estructura.svg", "f2": "grafo_etapas.svg",
    "fig": "Figura", "t1": "Dependencias entre los archivos de la plantilla.",
    "t2": "Archivos que escribe cada etapa del flujo.",
    "pie1": "Trazo grueso: el recorrido del trabajo. Trazo fino: quién referencia a quién.",
    "pie2": "Trazo continuo: lo que la etapa crea. Discontinuo: un campo que actualiza de paso.",
    "centro": ["INSTRUCCIONES", "PROYECTO"],
    "nodos": ["/CLAUDE.md", "AGENTS.md", "/GEMINI.md", "README.md", "PROCESOS_ACTIVOS.md",
              "OFERTAS_APLICADAS.md", "OFERTAS.md", "PLATAFORMAS.md", "PERFIL_CANDIDATO.md"],
    "ley": ["INSTRUCCIONES_PROYECTO.md — la autoridad; el resto la referencia",
            "AGENTS.md — las reglas que lee el agente al empezar",
            "archivos de estado: los escribe el agente mientras trabaja",
            "tuyos: tus datos y tu guía",
            "punteros de una línea, en la raíz del repo, a AGENTS.md"],
    "etapas": ["Elegir dónde\nbuscar", "Preparar\nperfiles", "Buscar\nofertas", "Generar\nCVs", "Aplicar"],
    "arch": ["PLATAFORMAS.md", "OFERTAS.md", "OFERTAS_APLICADAS.md", "CVs_OFERTAS/", "PROCESOS_ACTIVOS.md"],
}
EN = {
    "dir": "en", "f1": "structure_graph.svg", "f2": "stages_graph.svg",
    "fig": "Figure", "t1": "Dependencies between the template's files.",
    "t2": "Files written by each stage of the flow.",
    "pie1": "Thick stroke: the path the work takes. Thin stroke: who references whom.",
    "pie2": "Solid: what the stage creates. Dashed: a field it updates along the way.",
    "centro": ["PROJECT", "INSTRUCTIONS"],
    "nodos": ["/CLAUDE.md", "AGENTS.md", "/GEMINI.md", "README.md", "ACTIVE_PROCESSES.md",
              "JOBS_APPLIED.md", "JOBS.md", "PLATFORMS.md", "CANDIDATE_PROFILE.md"],
    "ley": ["PROJECT_INSTRUCTIONS.md — the authority; everything else references it",
            "AGENTS.md — the rules the agent reads when it starts",
            "state files: the agent writes them as it works",
            "yours: your data and your guide",
            "one-line pointers, at the repo root, to AGENTS.md"],
    "etapas": ["Choose where\nto search", "Prepare\nprofiles", "Search\njobs", "Generate\nCVs", "Apply"],
    "arch": ["PLATFORMS.md", "JOBS.md", "JOBS_APPLIED.md", "CVs_JOBS/", "ACTIVE_PROCESSES.md"],
}

def cabecera(w, h, fig, num, titulo):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{titulo}">
<defs>
  <pattern id="rej" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M24,0 L0,0 0,24" fill="none" stroke="{REJILLA}" stroke-width="1"/>
  </pattern>
  <marker id="p" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0.5 L7.5,4 L0,7.5 z" fill="{GRIS}"/></marker>
  <marker id="pn" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7.5" markerHeight="7.5" orient="auto-start-reverse">
    <path d="M0,0.5 L7.5,4 L0,7.5 z" fill="{TINTA}"/></marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect width="{w}" height="{h}" fill="url(#rej)"/>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" fill="none" stroke="{BORDE}" stroke-width="1"/>
<text x="34" y="46" fill="{TINTA}" font-family="{SERIF}" font-size="15" font-weight="700">{fig} {num}</text>
<text x="34" y="68" fill="{TINTA}" font-family="{SERIF}" font-size="14" font-style="italic">{titulo}</text>
'''

def vertice(x, y, r, relleno="#ffffff", guion=None, ancho=1.6, doble=False):
    d = f' stroke-dasharray="{guion}"' if guion else ""
    s = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{relleno}" stroke="{TINTA}" stroke-width="{ancho}"{d}/>\n'
    if doble:
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r-5}" fill="none" stroke="{TINTA}" stroke-width="1"/>\n'
    return s

def etiqueta(x, y, r, texto, ang, size=11):
    c, s_ = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    if c > 0.35:    tx, ty, anc = x + r + 9, y + 4, "start"
    elif c < -0.35: tx, ty, anc = x - r - 9, y + 4, "end"
    else:
        tx, anc = x, "middle"
        ty = y - r - 10 if s_ > 0 else y + r + 17
    return (f'<text x="{tx:.1f}" y="{ty:.1f}" fill="{TINTA}" font-family="{MONO}" '
            f'font-size="{size}" text-anchor="{anc}">{texto}</text>\n')

def arista(p1, r1, p2, r2, ancho=1, color=None, guion=None, flecha="p", doble=False):
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2-x1, y2-y1
    d = math.hypot(dx, dy) or 1
    ux, uy = dx/d, dy/d
    color = color or GRIS
    g = f' stroke-dasharray="{guion}"' if guion else ""
    ini = f' marker-start="url(#{flecha})"' if doble else ""
    return (f'<line x1="{x1+ux*(r1+2):.1f}" y1="{y1+uy*(r1+2):.1f}" x2="{x2-ux*(r2+6):.1f}" '
            f'y2="{y2-uy*(r2+6):.1f}" stroke="{color}" stroke-width="{ancho}"{g} '
            f'marker-end="url(#{flecha})"{ini}/>\n')

def figura1(L):
    W, H = 920, 770
    CX, CY, R, RV = 460, 350, 214, 24
    tipos = ["puntero", "reglas", "puntero", "tuyo", "estado", "estado", "estado", "estado", "tuyo"]
    pos, ang, tipo = {}, {}, {}
    for i, n in enumerate(L["nodos"]):
        a = 90 - i*(360/9)
        ang[n], tipo[n] = a, tipos[i]
        pos[n] = (CX + R*math.cos(math.radians(a)), CY - R*math.sin(math.radians(a)))
    svg = cabecera(W, H, L["fig"], 1, L["t1"])
    svg += f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{BORDE}" stroke-width="1" stroke-dasharray="3 5"/>\n'
    for n in pos:
        if tipo[n] != "puntero":
            svg += arista((CX, CY), 46, pos[n], RV, ancho=1, color=SUAVE, doble=True)
    for n in (L["nodos"][0], L["nodos"][2]):
        svg += arista(pos[n], RV-7, pos[L["nodos"][1]], RV, ancho=1.2, guion="4 3")
    flujo = [L["nodos"][8], L["nodos"][7], L["nodos"][6], L["nodos"][5], L["nodos"][4]]
    for a, b in zip(flujo, flujo[1:]):
        svg += arista(pos[a], RV, pos[b], RV, ancho=2.2, color=TINTA, flecha="pn")
    svg += vertice(CX, CY, 46, doble=True, ancho=2)
    for i, t in enumerate(L["centro"]):
        svg += (f'<text x="{CX}" y="{CY-3+i*12}" fill="{TINTA}" font-family="{MONO}" font-size="9.5" '
                f'text-anchor="middle" font-weight="700">{t}</text>\n')
    for n, (x, y) in pos.items():
        t = tipo[n]
        if t == "estado":    svg += vertice(x, y, RV, relleno=RELLENO)
        elif t == "tuyo":    svg += vertice(x, y, RV, guion="5 3")
        elif t == "puntero": svg += vertice(x, y, RV-7, ancho=1.1, guion="2 3")
        else:                svg += vertice(x, y, RV, ancho=2.4)
        svg += etiqueta(x, y, RV if t != "puntero" else RV-7, n, ang[n])
    svg += f'<line x1="34" y1="620" x2="{W-34}" y2="620" stroke="{BORDE}" stroke-width="1"/>\n'
    for i, t in enumerate(L["ley"]):
        y = 646 + i*18
        if i == 0:
            svg += vertice(43, y-4, 8, ancho=1.8)
            svg += f'<circle cx="43" cy="{y-4}" r="4" fill="none" stroke="{TINTA}" stroke-width="1"/>\n'
        elif i == 1: svg += vertice(43, y-4, 8, ancho=2.4)
        elif i == 2: svg += vertice(43, y-4, 8, relleno=RELLENO)
        elif i == 3: svg += vertice(43, y-4, 8, guion="5 3")
        else:        svg += vertice(43, y-4, 6, ancho=1.1, guion="2 3")
        svg += f'<text x="60" y="{y}" fill="{GRIS}" font-family="{MONO}" font-size="10">{t}</text>\n'
    svg += (f'<text x="34" y="{H-26}" fill="{GRIS}" font-family="{SERIF}" font-size="12.5" '
            f'font-style="italic">{L["pie1"]}</text>\n')
    return svg + "</svg>\n"

def figura2(L):
    W, H = 920, 560
    EY, ER, AR = 175, 24, 24
    ex = [90 + i*185 for i in range(5)]
    PLAT, JOBS, APLI, CVS, PROC = L["arch"]
    arch = {PLAT: (250, 400), JOBS: (470, 400), APLI: (700, 400), CVS: (585, 300), PROC: (838, 300)}
    svg = cabecera(W, H, L["fig"], 2, L["t2"])
    svg += f'<line x1="60" y1="{EY}" x2="{W-40}" y2="{EY}" stroke="{BORDE}" stroke-width="1"/>\n'
    E = lambda i: (ex[i], EY)
    for i, (a, b, ancho, guion, col, fl) in enumerate([
            (0, PLAT, 1.8, None, TINTA, "pn"), (1, PLAT, 1.8, None, TINTA, "pn"),
            (2, JOBS, 1.8, None, TINTA, "pn"), (2, PLAT, 1, "4 4", GRIS, "p"),
            (3, CVS, 1.8, None, TINTA, "pn"), (3, JOBS, 1, "4 4", GRIS, "p"),
            (4, APLI, 1.8, None, TINTA, "pn"), (4, PROC, 1, "4 4", GRIS, "p")]):
        svg += arista(E(a), ER, arch[b], AR, ancho=ancho, guion=guion, color=col, flecha=fl)
    svg += arista(arch[JOBS], AR, arch[APLI], AR, ancho=1.4)
    for i, lab in enumerate(L["etapas"]):
        x = ex[i]
        svg += f'<line x1="{x}" y1="{EY-6}" x2="{x}" y2="{EY+6}" stroke="{BORDE}" stroke-width="1"/>\n'
        if i < 4: svg += arista((x, EY), ER, (ex[i+1], EY), ER, ancho=1, color=SUAVE)
        svg += vertice(x, EY, ER, ancho=2)
        svg += (f'<text x="{x}" y="{EY+5}" fill="{TINTA}" font-family="{MONO}" font-size="14" '
                f'text-anchor="middle" font-weight="700">{i+1}</text>\n')
        for j, linea in enumerate(lab.split("\n")):
            svg += (f'<text x="{x}" y="{EY-ER-24+j*13}" fill="{GRIS}" font-family="{MONO}" '
                    f'font-size="10.5" text-anchor="middle">{linea}</text>\n')
    for n, (x, y) in arch.items():
        svg += vertice(x, y, AR, relleno=RELLENO)
        svg += (f'<text x="{x}" y="{y+AR+16}" fill="{TINTA}" font-family="{MONO}" font-size="10.5" '
                f'text-anchor="middle">{n}</text>\n')
    svg += f'<line x1="34" y1="{H-62}" x2="{W-34}" y2="{H-62}" stroke="{BORDE}" stroke-width="1"/>\n'
    svg += (f'<text x="34" y="{H-40}" fill="{GRIS}" font-family="{SERIF}" font-size="12.5" '
            f'font-style="italic">{L["pie2"]}</text>\n')
    return svg + "</svg>\n"

for L in (ES, EN):
    os.makedirs(L["dir"], exist_ok=True)
    io.open(os.path.join(L["dir"], L["f1"]), "w", encoding="utf-8").write(figura1(L))
    io.open(os.path.join(L["dir"], L["f2"]), "w", encoding="utf-8").write(figura2(L))
    print("escrito", L["dir"])
