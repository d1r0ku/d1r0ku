from html import escape
from itertools import groupby

ART_FILE, OUT_FILE = "art.txt", "dark_mode.svg"
W, H = 1040, 530
ART_X, ART_Y, ART_FONT, ART_STEP = 15, 22, 7, 9
TEXT_X, WIDTH = 460, 56

COLORS = {"@": "#a3ad7f", "%": "#7f925e", "#": "#c7c5b5", "*": "#dac584",
          "+": "#8fa092", "=": "#4d6459", "-": "#2f4640", ":": "#3d5a52"}

art = [l.rstrip("\n") for l in open(ART_FILE, encoding="utf-8")]

def art_svg():
    out = []
    for i, line in enumerate(art):
        y = ART_Y + i * ART_STEP
        runs = "".join(
            f'<tspan fill="{COLORS.get(c, "#4d6459")}">{escape("".join(g))}</tspan>'
            for c, g in groupby(line))
        out.append(f'<tspan x="{ART_X}" y="{y}">{runs}</tspan>')
    return "\n".join(out)

def row(key, value):
    dots = "." * max(2, WIDTH - len(key) - len(value) - 4)
    return (f'<tspan class="c">. </tspan><tspan class="k">{escape(key)}</tspan>:'
            f'<tspan class="c"> {dots} </tspan><tspan class="v">{escape(value)}</tspan>')

def title(name):
    return f'<tspan class="t">{escape(name)}</tspan> <tspan class="c">{"-" * (WIDTH - len(name) - 1)}</tspan>'

blocks = [
    [title("soku@home"), row("Name", "Soku"), row("Role", "Systems engineering student"),
     row("Location", "Colombia"), row("Status", "Learning / building / dreaming")],
    [title("~/toolbox"), row("Languages", "Python, Java, JavaScript, SQL"),
     row("Web", "HTML, CSS, Flask"), row("Tools", "PostgreSQL, Git, GitHub")],
    [title("~/interests"), row("Exploring", "Software, Databases, Networks"),
     row("Offline", "Gaming, Writing, Aviation"), row("Aesthetic", "Dreamcore with a quiet cyber touch")],
]

lines, y = [], 30
for b in blocks:
    for l in b:
        lines.append(f'<tspan x="{TEXT_X}" y="{y}">{l}</tspan>')
        y += 20
    y += 20
lines.append(f'<tspan x="{TEXT_X}" y="{y}" class="l">&gt; there is still a light on._</tspan>')

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}px" height="{H}px" font-family="Consolas, 'Liberation Mono', Menlo, monospace" font-size="16px">
<style>
.k {{fill:#a6b58d}} .v {{fill:#d4d9cb}} .c {{fill:#5f7a70}} .t {{fill:#eee9d8}} .l {{fill:#dac584}}
text, tspan {{white-space: pre}}
</style>
<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101b25"/><stop offset="1" stop-color="#203632"/></linearGradient></defs>
<rect width="{W}px" height="{H}px" fill="url(#bg)" rx="15"/>
<text font-size="{ART_FONT}px" aria-hidden="true">
{art_svg()}
</text>
<text fill="#c9d1d9">
{chr(10).join(lines)}
</text>
</svg>"""
open(OUT_FILE, "w", encoding="utf-8").write(svg)
print("listo:", OUT_FILE)