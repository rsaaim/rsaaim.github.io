#!/usr/bin/env python3
"""Generates the static pages for rsaaim.github.io.

Edit the content in this file, then run:  python3 tools/build.py
Output: index.html and projects/*.html at the repo root.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = "rsaaim@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/rayhaansaaim/"
FONTS = ("https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700"
         "&family=Share+Tech+Mono&family=Inter:wght@400;500;600&display=swap")


def head(title, desc, base):
    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="https://rsaaim.github.io/assets/img/hero/01_hero-holding-rear-suspension.jpg">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<script>try{{var t=localStorage.getItem('theme');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="{base}css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="{base}index.html"><span class="brand-mark" aria-hidden="true">RS</span><span class="brand-name">R.SAAIM</span></a>
  <nav class="nav" aria-label="Main">
    <a href="{base}index.html#experience">EXPERIENCE</a>
    <a href="{base}index.html#projects">PROJECTS</a>
    <a href="{base}index.html#about">ABOUT</a>
    <a class="btn-resume" href="{base}resume.pdf">RESUME</a>
    <button class="theme-toggle" type="button" aria-label="Switch to dark mode">DARK</button>
  </nav>
</header>
<main id="main">
"""


def foot(base):
    return f"""</main>
<footer class="site-footer"><span>© 2026 RAYHAAN SAAIM</span><span>BUILT IN SOMERVILLE, MA</span></footer>
<script src="{base}js/site.js"></script>
</body>
</html>
"""


def img(base, path):
    return f"{base}assets/img/{path}"


# ---------------------------------------------------------------- homepage
def index():
    b = ""
    xp = [
        dict(href="projects/fikst-robotics.html", nda=True, org="FIKST PRODUCT DEVELOPMENT · WILMINGTON, MA",
             dates="SEP 2025 — PRESENT", cur=True, title="Mechanical Engineer I",
             text="Production parts for an industrial and warehouse robotics client: a molded silicone ingress seal, a drop-in nylon harness tray, and chassis changes backed by bolted-joint and tolerance-stack analysis."),
        dict(href="projects/fikst-2024.html", img="fikst-2024/06_bumper-compression-test.jpg", alt="Rubber bumper compression test on a Mark-10 force stand",
             org="FIKST PRODUCT DEVELOPMENT · WILMINGTON, MA", dates="JUN — AUG 2024", title="Mechanical Engineering Intern",
             text="Medical device work: an injection-molded wear pad, quarter-turn nut tool sets, bumper and valve test rigs, and a blood heat-exchanger study for upper management."),
        dict(href="projects/lincoln.html", img="lincoln/01_rayhaan-at-lincoln.jpg", alt="Rayhaan at Lincoln Electric",
             org="LINCOLN ELECTRIC · CLEVELAND, OH", dates="JUN — AUG 2023", title="Engineering Intern · Machine R&amp;D",
             text="Built a welding concept machine from two engine-drive platforms: brushless motor swap, idle-control logic and wiring, and a portability kit. Presented to upper management."),
    ]
    xp_html = ""
    for x in xp:
        left = ('<div class="xp-nda"><span class="tag">[ UNDER NDA ]</span><span class="bar" style="width:80%"></span>'
                '<span class="bar" style="width:60%"></span><span>CLIENT DETAILS WITHHELD</span></div>') if x.get("nda") \
            else f'<img src="{img(b, x["img"])}" alt="{x["alt"]}" loading="lazy">'
        dates = f'<span class="acc">{x["dates"]}</span>' if x.get("cur") else f'<span>{x["dates"]}</span>'
        xp_html += f"""
      <a class="xp chamfer reveal" href="{x['href']}"><div class="xp-inner chamfer">{left}
        <div class="xp-body"><div class="meta"><span>{x['org']}</span>{dates}</div>
          <h3>{x['title']}</h3><p>{x['text']}</p><span class="more">READ MORE &gt;&gt;</span></div></div></a>"""

    cards = [
        ("projects/fsae-suspension.html", "fsae-suspension/02_suspension-on-test-rig.jpg", "Rear suspension mounted on the camber test rig",
         "[ STUDENT TEAM ] 2024–25", "FSAE Rear Suspension", "−1.25° static camber, never positive through travel. Hub and upright machined in-house.", ""),
        ("projects/fea.html", "fsae-fea/05_von-mises-stress-mount.jpg", "Von Mises stress plot of the suspension mounting tab",
         "[ STUDENT TEAM ] 2024", "Mount FEA Optimization", "25-step parametric sweep in MATLAB + Abaqus. 7.3% lighter at a safety factor of 2.", ""),
        ("projects/ej255.html", "ej255/05_heads-before-after-cleaning.jpg", "EJ255 cylinder heads before and after cleaning",
         "[ PERSONAL ] 2024–25", "EJ255 Engine Rebuild", "Junkyard turbo boxer: teardown, new bearings and rings, lapped valves, honed bores.", ""),
        ("projects/crimson-motorsports.html", "formula-sae-team/01_team-at-competition.jpg", "Crimson Motorsports members at an FSAE competition",
         "[ LEADERSHIP ] 2024–25", "Founding Crimson Motorsports", "Started Harvard's first FSAE team from zero members and handed off an elected board.", ""),
    ]
    cards_html = "".join(f"""
      <a class="card reveal" href="{h}"><img src="{img(b, i)}" alt="{a}" loading="lazy"{c}>
        <div class="card-body"><span class="tag-line">{t}</span><h3>{n}</h3><p>{d}</p></div></a>""" for h, i, a, t, n, d, c in cards)

    skills = ["SOLIDWORKS", "GD&amp;T Y14.5", "TOLERANCE STACKS", "BOLTED JOINTS", "MOLDING / CASTING DFM",
              "ABAQUS FEA", "MATLAB", "CNC / LATHE / MILL", "TIG WELDING"]
    chips = "".join(f'<span class="chip">{s}</span>' for s in skills)

    body = f"""
  <section class="wrap hero" id="top">
    <div class="hero-copy">
      <p class="eyebrow">// MECHANICAL ENGINEERING PORTFOLIO</p>
      <h1>Rayhaan<br>Saaim</h1>
      <div class="readout"><span class="k">ROLE</span><span>MECHANICAL ENGINEER I</span><span class="k">LOCATION</span><span>BOSTON, MA</span></div>
      <p class="lede">I design production hardware for industrial and warehouse robots at Fikst Product Development. At Harvard I founded the Formula SAE team, built its rear suspension, and led integration on a liquid rocket engine test stand.</p>
      <p class="status">OPEN TO EV · AUTO · AERO ROLES — BOSTON / CALIFORNIA</p>
    </div>
    <figure class="bracket-frame"><span class="br-b" aria-hidden="true"></span>
      <img src="{img(b, 'hero/01_hero-holding-rear-suspension.jpg')}" alt="Rayhaan holding the FSAE rear suspension he designed and built">
      <figcaption class="img-caption"><span>IMG_01 // FSAE REAR SUSPENSION</span><span class="acc">2024–25</span></figcaption>
    </figure>
  </section>

  <section class="wrap" aria-labelledby="skills-h"><div class="skills"><h2 id="skills-h">SKILLS</h2>{chips}</div></section>

  <section class="wrap section" id="experience">
    <div class="section-head"><span class="num">01</span><h2>Experience</h2><span class="rule" aria-hidden="true"></span></div>
    <div class="xp-list">{xp_html}
    </div>
  </section>

  <section class="wrap section" id="projects">
    <div class="section-head"><span class="num">02</span><h2>Projects</h2><span class="rule" aria-hidden="true"></span></div>
    <div class="cards" style="grid-template-columns: repeat(auto-fit, minmax(min(100%, 290px), 1fr))">{cards_html}
    </div>
    <p class="meta" style="margin-top:20px; justify-content:flex-start; gap:24px"><span>ALSO:</span><a href="projects/raynmaker.html">THE RAYNMAKER ROBOT (2022) &gt;&gt;</a></p>
  </section>

  <section class="wrap about" id="about">
    <div style="display:flex; flex-direction:column; gap:14px">
      <div class="section-head" style="margin:0"><span class="num">03</span><h2>About</h2></div>
      <p>Harvard BS Mechanical Engineering, 2025. Integration lead for a 500 lbf LOX/ethanol rocket engine test stand with the Harvard Rocket Propulsion Group. I like the whole loop: CAD, analysis, machining or welding the part myself, then testing it.</p>
    </div>
    <div class="contact-box" id="contact">
      <span class="h">&gt; CONTACT</span>
      <a href="mailto:{EMAIL}">EMAIL ........ {EMAIL}</a>
      <a href="{LINKEDIN}">LINKEDIN ..... /in/rayhaansaaim</a>
      <a href="resume.pdf">RESUME ....... download PDF</a>
    </div>
  </section>
"""
    return head("Rayhaan Saaim — Mechanical Engineer",
                "Mechanical engineering portfolio of Rayhaan Saaim: production robotics hardware, FSAE suspension, FEA, and engine rebuilds.", b) + body + foot(b)


# ---------------------------------------------------------------- project pages
def gallery(base, items, wide=False):
    figs = ""
    for path, cap, *opt in items:
        cls = ' class="contain"' if opt and opt[0] == "contain" else ""
        src = img(base, path)
        figs += f'<figure><a href="{src}"><img src="{src}" alt="{escape(cap)}" loading="lazy"{cls}></a><figcaption>{escape(cap)}</figcaption></figure>'
    return f'<div class="gallery{" wide" if wide else ""}">{figs}</div>'


def specs(pairs):
    return '<div class="specs">' + "".join(f'<div><p class="k">{k}</p><p class="v">{v}</p></div>' for k, v in pairs) + "</div>"


def project(slug, title, eyebrow, lede, spec_pairs, body, nxt):
    b = "../"
    nxt_html = f'<div class="next-proj"><a href="../index.html#projects">&lt;&lt; ALL PROJECTS</a><a href="{nxt[0]}">{nxt[1]} &gt;&gt;</a></div>'
    html = head(f"{title} — Rayhaan Saaim", lede, b) + f"""
  <div class="wrap crumb"><a href="../index.html">HOME</a> / <a href="../index.html#projects">PROJECTS</a> / {escape(title.upper())}</div>
  <section class="wrap proj-hero">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{escape(title)}</h1>
    <p class="lede">{lede}</p>
    {specs(spec_pairs)}
  </section>
  <article class="wrap" style="padding-bottom:24px">
{body(b)}
    {nxt_html}
  </article>
"""
    return slug, html + foot(b)


def pages():
    out = []

    out.append(project(
        "fsae-suspension", "FSAE Rear Suspension", "// SENIOR CAPSTONE · CRIMSON MOTORSPORTS · 2024–25",
        "I led the design, fabrication and testing of the rear suspension for Harvard's first Formula SAE car, a regulation-compliant system tuned for handling, durability and cost.",
        [("TYPE", "PUSHROD DOUBLE WISHBONE"), ("STATIC CAMBER", "−1.25°"), ("HUB", "7075 AL"), ("UPRIGHT", "6061 AL")],
        lambda b: f"""<div class="prose">
    <h2>Context</h2>
    <p>Harvard had never fielded a Formula SAE team. Seven seniors split the car into capstone projects (chassis, steering, powertrain, aero, and my rear suspension) so the club would start with real hardware instead of a blank sheet. The target was FSAE's internal-combustion class.</p>
    <h2>Architecture</h2>
    <p>I compared MacPherson strut, direct-acting double wishbone, pullrod and pushrod layouts and chose a <strong>double wishbone pushrod</strong> system. It moves the springs and dampers inboard for better aero and protection, adds adjustability through the rocker, and packages cleanly above the drivetrain.</p>
    </div>
    {gallery(b, [("fsae-suspension/08_cad-assembly-labeled.jpg", "Final CAD assembly, labeled", "contain"), ("fsae-suspension/14_cad-suspension-on-chassis.jpg", "Suspension on the chassis rear bulkhead", "contain"), ("fsae-suspension/09_cad-hub-upright-render.jpg", "Hub and upright render", "contain")])}
    <div class="prose">
    <h2>Geometry</h2>
    <p>The system is built around the Goodyear D2704 20.0x7.0-13 tire. Using SolidWorks sketches and a MATLAB four-bar linkage model, I tuned camber through bump, rebound and body roll:</p>
    <ul><li>Static camber of <strong>−1.25°</strong> for peak grip</li><li>Camber never goes positive anywhere in wheel travel</li><li>Wheel halves and offsets chosen to minimize scrub radius</li><li>Camber gain optimized against the control-arm pickup points and rear bulkhead geometry</li></ul>
    <p>Packaging kept moving the pickup points, so I re-ran the camber analysis against my spec each time and worked with the chassis engineer to lock the bulkhead for his torsional-stiffness FEA.</p>
    </div>
    {gallery(b, [("fsae-suspension/15_geometry-4-bar-sketch.jpg", "Four-bar linkage geometry sketch", "contain"), ("fsae-suspension/16_camber-diagrams.jpg", "Camber in bump and roll", "contain")], wide=True)}
    <div class="prose">
    <h2>Components &amp; machining</h2>
    <p><strong>Wheel hub:</strong> machined from 7075 aluminum on the manual lathe and mill, with some programmed features. Two ball bearings sit in a stacked configuration; the hub carries the inner races, the brake rotor (RCV floating rotor kit) and the CV axle's tripod mount, which the hub cap retains.</p>
    <p><strong>Upright:</strong> 6061 aluminum, waterjet-cut outline then finished on the manual mill. An interference fit plus a lip holds both bearing outer races, with mounts for the Wilwood PS1 caliper, both wishbones, the pushrod and the toe link.</p>
    <p><strong>Linkages:</strong> steel tubing notched, fixtured to prevent warping, and TIG-welded to rod-end inserts and bearing cups turned on the lathe.</p>
    </div>
    {gallery(b, [("fsae-suspension/10_cad-wheel-hub-labeled.jpg", "Wheel hub assembly", "contain"), ("fsae-suspension/12_cad-hub-exploded.jpg", "Hub stack, exploded", "contain"), ("fsae-suspension/11_cad-upright-labeled.jpg", "Upright mounting points", "contain"), ("fsae-suspension/21_lathe-turning-hub.jpg", "Turning the hub on the lathe"), ("fsae-suspension/19_machined-wheel-hub.jpg", "Finished 7075 wheel hub"), ("fsae-suspension/22_machined-upright.jpg", "Machined 6061 upright"), ("fsae-suspension/06_wishbone-weld-fixture.jpg", "Wishbone weld fixture"), ("fsae-suspension/07_tig-welding.jpg", "TIG welding the linkages"), ("fsae-suspension/26_finished-wishbones.jpg", "Finished wishbones")])}
    <div class="prose">
    <h2>Testing</h2>
    <p>I built a test rig whose mounts reproduce the chassis pickup points exactly, so I could measure camber through roll and compare it with the model, then checked wheel alignment on the car.</p>
    </div>
    {gallery(b, [("fsae-suspension/02_suspension-on-test-rig.jpg", "Assembly on the camber test rig"), ("fsae-suspension/29_dynamic-camber-test.jpg", "Measuring dynamic camber in roll"), ("fsae-suspension/05_fitting-wheel-to-chassis.jpg", "Fitting the wheel on the chassis"), ("fsae-suspension/01_rayhaan-with-chassis-and-suspension.jpg", "Final assembly on the chassis")])}""",
        ("fea.html", "NEXT: MOUNT FEA")))

    out.append(project(
        "fea", "Suspension Mount FEA Optimization", "// HARVARD ES128 · CRIMSON MOTORSPORTS · 2024",
        "I extended a from-scratch MATLAB finite element solver into a parametric tool that finds how thin the suspension mounting tabs can be before they yield, then cut 7.3% of their mass.",
        [("MASS REDUCTION", "7.3%"), ("SAFETY FACTOR", "2.0"), ("ELEMENTS", "~50,000"), ("SWEEP", "25 STEPS")],
        lambda b: f"""<div class="prose">
    <h2>The problem</h2>
    <p>The control arms attach to the chassis through ball joints bolted between pairs of welded steel tabs. The tabs have to survive race loads, but every gram on a student car counts. The question: how thin can they go while staying below yield with a safety factor of 2?</p>
    <h2>The tool</h2>
    <p>In ES128 (Computational Solid and Structural Mechanics) we built an FEA program in MATLAB that reads Abaqus input files, classifies the element types and solves each element. I built on it so the program takes a range of tab thicknesses and a step count, rebuilds and re-constrains the model for each thickness, solves it, and plots peak stress against thickness.</p>
    </div>
    {gallery(b, [("fsae-fea/01_real-suspension-mount.jpg", "The real mounting tabs on a car"), ("fsae-fea/02_abaqus-model.jpg", "Tube, tabs, bolt and nut merged into one part"), ("fsae-fea/03_tet-mesh.jpg", "Second-order tetrahedral mesh"), ("fsae-fea/04_boundary-conditions-load.jpg", "Fixed tube ends, load under the bolt")])}
    <div class="prose">
    <h2>Model</h2>
    <ul><li>Geometry: chassis tube section, left and right tabs, bolt and nut, merged into one part to avoid contact errors</li><li>Material: AISI 304 stainless (E = 190 GPa, yield 215 MPa)</li><li>Mesh: C3D10 second-order tets, about 50,000 elements</li><li>Load: 340 kg car × 3 g bump = 10,006 N, split over 16 mounts = 625 N per mount</li></ul>
    <h2>Result</h2>
    <p>The 3.175 mm baseline peaked around 100 MPa at the tab-to-tube joint. Sweeping from 3.175 mm down to 0.5 mm in 25 steps showed stress climbing sharply below 2.5 mm. At <strong>2.5 mm</strong> the peak was about 106 MPa, inside the safety factor of 2, for a <strong>7.3% lighter mount</strong>. Small on one car, but the same tool applies anywhere strength trades against weight or cost.</p>
    </div>
    {gallery(b, [("fsae-fea/05_von-mises-stress-mount.jpg", "Von Mises stress on the mount model"), ("fsae-fea/06_thin-tab-stress-past-yield.jpg", "Thin-tab case: stress climbs well past yield"), ("fsae-fea/07_max-stress-vs-thickness-plot.jpg", "Peak stress vs. tab thickness", "contain")])}""",
        ("ej255.html", "NEXT: EJ255 REBUILD")))

    out.append(project(
        "ej255", "EJ255 Engine Rebuild", "// PERSONAL PROJECT · 2024–25",
        "I pulled a turbocharged Subaru EJ255 from a junkyard 2005 Outback XT and rebuilt it on an engine stand, to go into a 2007 WRX later.",
        [("ENGINE", "EJ255 TURBO"), ("DONOR", "'05 OUTBACK XT"), ("BORES", "45° HONE"), ("STATUS", "READY TO INSTALL")],
        lambda b: f"""<div class="prose">
    <h2>Sourcing</h2>
    <p>My brother and I found the engine in a 2005 Outback 2.5 XT at a Buffalo junkyard. We pulled the drain plug first to check the oil for metal (a sign of a damaged block), then unbolted the accessories and hoses and pulled the engine.</p>
    <h2>Teardown</h2>
    <p>On the stand I removed the exhaust manifold, timing components, cam covers and camshafts, then the heads, compressing the valve springs to remove the valvetrain while tracking where every valve and spring came from. Then the pistons came out, the case was split, and the crank and rods were removed. Everything was labeled.</p>
    </div>
    {gallery(b, [("ej255/01_engine-on-stand.jpg", "On the engine stand"), ("ej255/02_long-block-teardown.jpg", "Long block during teardown"), ("ej255/04_valve-spring-compressor.jpg", "Valve spring compressor on the head"), ("ej255/05_heads-before-after-cleaning.jpg", "Heads before and after cleaning")])}
    <div class="prose">
    <h2>Prep</h2>
    <ul><li><strong>Valve lapping:</strong> lapping compound between each valve and its seat, rotated until the grinding sound went quiet, for a full seal</li><li><strong>Head flatness:</strong> checked with a machinist's level and feeler gauges; both heads were within Subaru spec</li><li><strong>Honing:</strong> deglazed the cylinders with a drill-driven three-stone hone to a 45° crosshatch for ring seating</li></ul>
    </div>
    {gallery(b, [("ej255/09_valve-lapping-compound.jpg", "Valve with lapping compound"), ("ej255/07_lapped-valves-seated.jpg", "Lapped valves seated"), ("ej255/12_honed-cylinder.jpg", "Honed cylinder wall")])}
    <div class="prose">
    <h2>Assembly</h2>
    <p><strong>Short block:</strong> new rod and main bearings, rods torqued to spec on the crank, four case O-rings, Permatex on the case halves, case bolted and torqued. Ring end gaps checked with feeler gauges, new rings fitted, pistons reinstalled.</p>
    <p><strong>Heads:</strong> new valve stem seals, valves and springs reinstalled with the spring compressor, retainers back in.</p>
    <p>The heads stay off the block for now so the engine is easier to move. New head gaskets go in at install.</p>
    </div>
    {gallery(b, [("ej255/11_crank-rods-new-bearings.jpg", "Crank, rods and new bearings"), ("ej255/14_assembled-short-block-and-heads.jpg", "Assembled short block with heads staged")])}""",
        ("crimson-motorsports.html", "NEXT: CRIMSON MOTORSPORTS")))

    out.append(project(
        "crimson-motorsports", "Founding Crimson Motorsports", "// HARVARD UNDERGRADUATE AUTOMOTIVE SOCIETY · 2024–25",
        "As president of the Harvard Undergraduate Automotive Society, I started Harvard's first Formula SAE team, tying five senior capstone projects to a new club with no members.",
        [("ROLE", "FOUNDER & PRESIDENT"), ("CAPSTONES", "5 INTEGRATED"), ("STARTED", "SEPT 2024"), ("NOW", "ADVISOR")],
        lambda b: f"""<div class="prose">
    <h2>Why capstones</h2>
    <p>FSAE teams are hard to start because nobody wants to join a team with nothing built. A year-long senior capstone guarantees real progress, so we pointed several at one car: my rear suspension, Edwin Dominguez's chassis, Jack Meyer's steering, Peter Fischer and Josh Gordon's powertrain, and Oliver Murcko and Steffan Jones's aero, building on a front suspension from an earlier capstone.</p>
    <h2>Building the club</h2>
    <p>The seniors had little time outside their capstones, and the team needed underclassmen to continue. I recruited at the activities fair and through the engineering mailing list, ran an onboarding go-kart project so new members could own a subsystem, and set up business development and a sponsorship package. After winter break the club pivoted fully to the car, with members leading the pedal box and brakes, electrical, seat and safety, and manufacturing.</p>
    <h2>Handoff</h2>
    <p>I put funds into designing and fabricating our own parts instead of buying assemblies (and banned team merch until we had something that looked like a car). I ran elections for the 2025–26 board, led visits to MIT's FSAE team and the FSAE Electric competition, and stay on as an advisor. The <a href="https://seas.harvard.edu/news/2025/07/zooming-future">Harvard SEAS article</a> covers the story.</p>
    </div>
    {gallery(b, [("formula-sae-team/01_team-at-competition.jpg", "At the FSAE Electric competition"), ("formula-sae-team/03_club-group-photo.jpg", "Club members"), ("formula-sae-team/04_club-work-session.jpg", "Weekly work session"), ("formula-sae-team/07_chassis-edwin.jpg", "Chassis capstone"), ("formula-sae-team/10_powertrain-capstone.jpg", "Powertrain capstone"), ("formula-sae-team/11_aero-capstone.jpg", "Aero capstone")])}""",
        ("fikst-robotics.html", "NEXT: FIKST ROBOTICS")))

    out.append(project(
        "fikst-robotics", "Robotics Production Parts", "// FIKST PRODUCT DEVELOPMENT · MECHANICAL ENGINEER I · 2025–PRESENT",
        "I design mechanical components for an industrial and warehouse robotics client and take them from concept through production release.",
        [("CLIENT", "INDUSTRIAL ROBOTICS"), ("PROCESSES", "INJECTION MOLDING"), ("ANALYSIS", "JOINTS · STACKS"), ("OUTPUT", "RELEASED DRAWINGS")],
        lambda b: """<div class="nda-panel"><span class="tag">[ UNDER NDA ]</span><span>Client name, product images and part geometry are withheld. This page describes the engineering problems and my approach in general terms.</span></div>
    <div class="prose">
    <h2>Liquid-ingress seal</h2>
    <p>Liquid reaching the robot's electronics caused shorts that required field replacements. I designed an <strong>injection-molded silicone</strong> seal to keep liquid out of the electronics.</p>
    <h2>Drop-in cable management</h2>
    <p>Technicians were routing and replacing cables one at a time. I designed an <strong>injection-molded nylon</strong> cable-management part with alignment features, so the full wiring harness drops in as one unit. It drastically cut the time spent routing and replacing cables.</p>
    <h2>Chassis changes</h2>
    <p>I modified the chassis to fit new hardware and make the robot easier to service, and validated the changes with <strong>bolted-joint</strong> and <strong>tolerance-stack</strong> analysis.</p>
    <h2>Getting it built</h2>
    <p>I create and release the engineering drawings, and work with suppliers on DFM and with the production line on design changes. Those changes reduced assembly issues and cycle time.</p>
    </div>""",
        ("fikst-2024.html", "NEXT: FIKST 2024 INTERNSHIP")))

    out.append(project(
        "fikst-2024", "Medical Device Design & Test", "// FIKST PRODUCT DEVELOPMENT · ME INTERN · SUMMER 2024",
        "A summer of design, prototyping and test work for medical-device clients: tooling, molded parts, and the rigs to prove them out.",
        [("TEST CYCLES", "10,000"), ("TOOL TYPES", "4 PROTOTYPED"), ("FORCE GAUGE", "MARK-10"), ("PROCESS", "INJECTION MOLDING")],
        lambda b: f"""<div class="prose">
    <h2>Through-bolt wear pad &amp; sealing tape</h2>
    <p>Prototyped three concepts, ran design selection, then designed an injection-molded wear pad and sealing tape for a through-bolted assembly. I iterated on fit, sealing and manufacturability, designed the threaded bosses to molding constraints, made the drawings, and worked with vendors on quoting and production.</p>
    </div>
    {gallery(b, [("fikst-2024/01_through-bolt-wear-pad-cad.jpg", "Wear pad in the through-bolt assembly", "contain"), ("fikst-2024/03_sealing-tape-cad.jpg", "Sealing tape", "contain"), ("fikst-2024/05_wear-pad-prototypes.jpg", "Wear pad prototypes")])}
    <div class="prose">
    <h2>Rubber bumper compression testing</h2>
    <p>The bumpers act as a cart's suspension. I ran spring-rate tests with a Mark-10 force gauge across fresh-out-of-box, high-temperature, high-temperature-and-humidity, and 10,000-cycle lifetime conditions (on a cycle fixture I helped build), then processed the data and presented it to the client to judge field viability.</p>
    </div>
    {gallery(b, [("fikst-2024/04_bumpers.jpg", "Bumper samples"), ("fikst-2024/06_bumper-compression-test.jpg", "Compression test on the Mark-10")])}
    <div class="prose">
    <h2>Quarter-turn nut tools</h2>
    <p>Designed modular tool prototypes for installing and removing quarter-turn nuts on bulkhead connections, gave four variants to technicians, iterated on their feedback, and delivered two final tool sets to the client.</p>
    <h2>Valve break &amp; leak test</h2>
    <p>Built a rig (angled mount and reservoir plate) that pairs a leak sensor with the Mark-10 to find the force that causes a critical leak in blood-reservoir ball valves, then tested several reservoirs and valves for the client.</p>
    </div>
    {gallery(b, [("fikst-2024/11_quarter-turn-tools.jpg", "Quarter-turn tool sets"), ("fikst-2024/10_quarter-turn-tool-section.jpg", "Tool section view", "contain"), ("fikst-2024/08_valve-test-fixture-cad.jpg", "Valve test fixture", "contain"), ("fikst-2024/09_valve-break-test.jpg", "Valve break test")])}
    <div class="prose">
    <h2>Blood heat-exchanger study</h2>
    <p>Concept project: chill 1 L of blood from room temperature to near freezing within 10 minutes. I set up a pressure-driven flow through tubing coiled in an ice bath, logged volumes and thermocouple temperatures every 15 seconds, and compared tube diameter, wall thickness, flow rate and agitation against a control using an efficiency metric. The results went to upper management and fed a custom model.</p>
    </div>
    {gallery(b, [("fikst-2024/13_heat-exchanger-test-setup.jpg", "Heat-exchanger test setup"), ("fikst-2024/14_heat-exchanger-ice-bath.jpg", "Ice-bath coil")])}""",
        ("lincoln.html", "NEXT: LINCOLN ELECTRIC")))

    out.append(project(
        "lincoln", "Welding Concept Machine", "// LINCOLN ELECTRIC · MACHINE R&D: COMMERCIAL ENGINE DRIVES · SUMMER 2023",
        "I turned a large commercial engine-drive welder into a simpler machine with the same power, using electronics from a smaller model.",
        [("MOTOR", "BRUSHLESS SWAP"), ("SWITCH", "5-POSITION"), ("EXTRA", "PORTABILITY KIT"), ("AUDIENCE", "UPPER MGMT")],
        lambda b: f"""<div class="nda-panel"><span class="tag">[ PARTIAL NDA ]</span><span>Identifying details and photos of the machine are withheld. The engineering is described below.</span></div>
    <div class="prose">
    <h2>What I did</h2>
    <ul><li>Swapped in a slightly smaller brushless motor (cheaper, less maintenance than brushed)</li><li>Swapped in the smaller machine's PCB and worked out how to adapt the engine and motor wiring to it</li><li>Drew the logic diagram for a five-position switch: starter, low idle, high idle, auto idle, off</li><li>Spliced wiring, installed relays, used a toroid for auto-idle sensing, and tested the machine</li><li>Designed and fabricated a portability kit prototype from parts already made in-house</li></ul>
    <p>I presented the working concept to upper management and at the Lincoln Electric Intern Showcase.</p>
    </div>
    {gallery(b, [("lincoln/01_rayhaan-at-lincoln.jpg", "At Lincoln Electric, Cleveland")])}""",
        ("raynmaker.html", "NEXT: THE RAYNMAKER")))

    out.append(project(
        "raynmaker", "The RaynMaker", "// HARVARD ES51 INTRO CAD · TEAM OF 3 · 2022",
        "A remote-control robot my team designed and built for a class-wide arena competition: push dog toys into nets within strict size limits.",
        [("DESIGN", "PLOW + SCOOP"), ("DRIVE", "REAR WHEEL"), ("GEARBOX", "SCREWDRIVER-SOURCED"), ("TEAM", "3")],
        lambda b: f"""<div class="prose">
    <h2>Approach</h2>
    <p>With limited time, materials and experience, we chose simplicity, reliability and mobility: a low-CG plow with rear-wheel drive, caster wheels for quick turns, and a servo-driven scoop. I helped size torque for climbing the ramp and pick wheels for traction. The gearbox came out of an electric screwdriver.</p>
    <p>We used laser cutting, milling, 3D printing and silicone molding. The robot was reliable and quick in seeding, and we left out storage to keep it nimble. Built with Jack Shea and Emma-Kate Price.</p>
    </div>
    {gallery(b, [("raynmaker/01_robot.jpg", "The RaynMaker")])}""",
        ("fsae-suspension.html", "BACK TO: FSAE SUSPENSION")))
    return out


def main():
    os.makedirs(os.path.join(ROOT, "projects"), exist_ok=True)
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(index())
    for slug, html in pages():
        with open(os.path.join(ROOT, "projects", slug + ".html"), "w") as f:
            f.write(html)
    print("built index + projects")


if __name__ == "__main__":
    main()
