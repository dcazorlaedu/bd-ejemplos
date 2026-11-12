#!/usr/bin/env python3
"""Build the public exercise index and one GitHub/Pages page per exercise."""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT.parent
DATA = json.loads((ROOT / "ejercicios.json").read_text(encoding="utf-8"))
UNIDADES = DATA["unidad"]
EJERCICIOS = DATA["ejercicios"]
CE_ESPERADOS = {
    "RA1": set("abcdefghij"),
    "RA6": set("abcdefgh"),
    "RA2": set("abcdefgh"),
    "RA3": set("abcdefgh"),
    "RA4": set("abcdefgh"),
    "RA5": set("abcdefghij"),
    "RA7": set("abcde"),
}


def esc(value):
    return html.escape(str(value), quote=True)


def validar():
    if len(EJERCICIOS) != 20:
        raise ValueError(f"Se esperaban 20 ejercicios; hay {len(EJERCICIOS)}")
    ids = [exercise["id"] for exercise in EJERCICIOS]
    wanted = [
        f"{number:02d}_ejercicio_UT{exercise['ut']}"
        for number, exercise in enumerate(EJERCICIOS, 1)
    ]
    if ids != wanted:
        raise ValueError("Los ejercicios deben estar numerados de forma consecutiva y nombrados por UT")
    for ut in range(1, 8):
        levels = [e["dificultad"] for e in EJERCICIOS if e["ut"] == ut]
        if not levels or levels != sorted(levels):
            raise ValueError(f"La UT{ut} no tiene ejercicios o no están ordenados por dificultad")
    for ut, info in UNIDADES.items():
        ra = info["ra"]
        covered = {ce for exercise in EJERCICIOS if exercise["ut"] == int(ut) for ce in exercise["ce"]}
        if covered != CE_ESPERADOS[ra]:
            raise ValueError(f"Cobertura incompleta de {ra}: faltan {sorted(CE_ESPERADOS[ra] - covered)}")


def header(title, page_prefix, active=""):
    links = "".join(
        f'<a href="{page_prefix}ut{n}/">UT{n}</a>' for n in range(1, 8)
    )
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · Bases de Datos</title>
<link rel="icon" href="{page_prefix}assets/favicon.svg">
<link rel="stylesheet" href="{page_prefix}assets/site.css"></head><body>
<header class="top"><div class="in"><a class="logo" href="{page_prefix}">&lt;/&gt; Bases de Datos</a>
<nav>{links}<a href="{page_prefix}ejercicios/" class="{active}">Ejercicios</a><a href="{page_prefix}lab/">Laboratorio SQL</a></nav></div></header>"""


def render_listing():
    page = header("Batería de ejercicios", "../", "on")
    page += """<div class="hero"><div class="in"><div class="badge">Bases de Datos · 1.º DAW</div>
<h1>20 ejercicios por UT</h1><p>Una secuencia progresiva: empieza por los fundamentos y avanza hasta tareas integradas. Cada unidad trabaja el RA asociado y cubre todos sus criterios de evaluación.</p>
<p><a class="btn" href="#lista">Ver ejercicios</a> <a class="btn sec" href="../">Volver a Bases de Datos</a></p></div></div>
<main><div class="tip"><strong>Cómo usar la batería.</strong> Los ejercicios están ordenados por unidad y, dentro de cada UT, por dificultad creciente. Las consignas no incluyen soluciones. Usa datos inventados; no publiques contraseñas ni datos personales reales. Las prácticas SQL están pensadas para una base de pruebas MySQL 8.4 y UT7 para MongoDB.</div>
<div class="row"><label for="unidad"><strong>Filtrar por unidad</strong><select id="unidad"><option value="">Todas las unidades</option>"""
    for ut, info in UNIDADES.items():
        count = sum(e["ut"] == int(ut) for e in EJERCICIOS)
        page += f'<option value="{ut}">UT{ut} · {esc(info["ra"])} · {count} ejercicios</option>'
    page += """</select></label><div><strong>Progreso:</strong> del ejercicio 01 al 20, sin saltos.</div></div>
<h2 id="lista">Ejercicios</h2><div class="grid" id="ejercicios">"""
    for exercise in EJERCICIOS:
        info = UNIDADES[str(exercise["ut"])]
        ce_list = ", ".join(f"{ce})" for ce in exercise["ce"])
        page += f"""<a class="card ejercicio" data-ut="{exercise['ut']}" href="{esc(exercise['id'])}/">
<div class="ra">{esc(exercise['id'])} · UT{exercise['ut']} · {esc(info['ra'])} · Nivel {exercise['dificultad']}</div>
<h3>{esc(exercise['titulo'])}</h3><p>{esc(exercise['contexto'])}</p>
<p><strong>CE trabajados:</strong> {esc(ce_list)}</p></a>"""
    page += """</div><h2>Cobertura curricular</h2><p>La colección completa cubre los siete RA y todos sus CE, según las unidades de trabajo de Bases de Datos.</p><div class="cols">"""
    for ut, info in UNIDADES.items():
        ce_set = sorted({ce for exercise in EJERCICIOS if exercise["ut"] == int(ut) for ce in exercise["ce"]})
        page += f"""<div class="tip"><strong>UT{ut} · {esc(info['ra'])}</strong><br>{esc(info['nombre'])}
<br><small>Criterios cubiertos: {esc(', '.join(ce + ')' for ce in ce_set))}</small><br>
<a href="?ut={ut}">Ver ejercicios de la UT{ut}</a></div>"""
    page += """</div><h2>Material de prácticas</h2><p><a href="material/tiendatech_mysql.sql">Esquema y datos ficticios de TiendaTech para MySQL 8.4</a> ·
<a href="material/tiendatech_mongo.js">Datos de ejemplo para MongoDB</a>. Ejecuta siempre el material en una base de pruebas.</p>
</main><footer>Material didáctico · 2026-27 · Ejercicios sin solucionarios públicos; datos ficticios.</footer>
<script>const unidad=document.getElementById('unidad'),params=new URLSearchParams(location.search);unidad.value=params.get('ut')||'';
function filtrar(){document.querySelectorAll('.ejercicio').forEach(e=>e.hidden=!!unidad.value&&e.dataset.ut!==unidad.value)}
unidad.addEventListener('change',()=>{filtrar();const q=unidad.value?('?ut='+unidad.value):location.pathname;history.replaceState(null,'',q)});
filtrar();</script></body></html>"""
    return page


def render_exercise(exercise):
    ut = exercise["ut"]
    info = UNIDADES[str(ut)]
    max_level = max(e["dificultad"] for e in EJERCICIOS if e["ut"] == ut)
    prefix = "../../"
    page = header(exercise["titulo"], prefix)
    ce_labels = ", ".join(f"{ce})" for ce in exercise["ce"])
    page += f"""<div class="hero"><div class="in"><div class="badge">{esc(exercise['id'])} · UT{ut} · {esc(info['ra'])}</div>
<h1>{esc(exercise['titulo'])}</h1><p>Nivel {exercise['dificultad']} de {max_level} · {esc(info['nombre'])}</p></div></div>
<main><div class="crumb"><a href="../">Batería de ejercicios</a> › <a href="{prefix}ut{ut}/">UT{ut}</a> › {esc(exercise['id'])}</div>
<div class="tip"><strong>Resultado de aprendizaje:</strong> {esc(info['ra'])}. {esc(info['descripcion_ra'])}<br>
<strong>Criterios trabajados:</strong> {esc(ce_labels)}</div>
<h2>Situación</h2><p>{esc(exercise['contexto'])}</p><h2>Enunciado</h2><ol>"""
    page += "".join(f"<li>{esc(task)}</li>" for task in exercise["tareas"])
    page += f"""</ol><h2>Entrega</h2><p>{esc(exercise['entrega'])}</p>"""
    if ut in (3, 4, 5, 6):
        page += f"""<h2>Material y herramientas</h2><p><a href="../material/tiendatech_mysql.sql">Descargar esquema y datos ficticios de TiendaTech (MySQL 8.4)</a>.
Trabaja en una base de datos de pruebas, no en una instancia compartida. También puedes abrir el <a href="../../lab/">laboratorio SQL del sitio</a> para las consultas compatibles con SQLite.</p>"""
    elif ut == 7:
        page += """<h2>Material y herramientas</h2><p><a href="../material/tiendatech_mongo.js">Descargar guion de datos ficticios para MongoDB</a>. Ejecútalo solo en una base de pruebas.</p>"""
    page += f"""<div class="tip"><strong>Auto-revisión:</strong> comprueba que la entrega resuelve todos los apartados, que puedes repetir las operaciones en un entorno limpio y que explicas las decisiones de diseño. <a href="?">Volver al índice</a>.</div>
</main><footer>Material didáctico · 2026-27 · Datos ficticios · Sin soluciones públicas.</footer></body></html>"""
    return page


def render_markdown(exercise):
    info = UNIDADES[str(exercise["ut"])]
    ce_labels = ", ".join(f"{ce})" for ce in exercise["ce"])
    tasks = "\n".join(f"{n}. {task}" for n, task in enumerate(exercise["tareas"], 1))
    text = f"""# {exercise['id']} · {exercise['titulo']}

**UT{exercise['ut']} · {info['ra']} · Nivel {exercise['dificultad']}**
{info['nombre']}

**Resultado de aprendizaje:** {info['descripcion_ra']}
**Criterios trabajados:** {ce_labels}

## Situación

{exercise['contexto']}

## Enunciado

{tasks}

## Entrega

{exercise['entrega']}

## Material

"""
    if exercise["ut"] in (3, 4, 5, 6):
        text += "Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4."
    elif exercise["ut"] == 7:
        text += "Datos ficticios: [`../material/tiendatech_mongo.js`](../material/tiendatech_mongo.js). Usa una base de datos MongoDB de pruebas."
    else:
        text += "Utiliza únicamente datos inventados y documenta tus supuestos."
    text += "\n\n[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/" + exercise["id"] + "/)\n"
    return text


def main():
    validar()
    ROOT.mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(render_listing(), encoding="utf-8")
    for exercise in EJERCICIOS:
        folder = ROOT / exercise["id"]
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(render_exercise(exercise), encoding="utf-8")
        (folder / "README.md").write_text(render_markdown(exercise), encoding="utf-8")
    print(f"Generados {len(EJERCICIOS)} ejercicios en 7 UT.")


if __name__ == "__main__":
    main()
