# Edit this file to change your website, then run:  python build.py
# Add an entry = copy a { ... } block and change the text. Remove an entry = delete its block.
# Keys: title, meta (one line under the title), text (paragraph), tags (small chips),
#       status (small badge), link (makes the title a link). All keys except title are optional.

PROFILE = {
    "name": "Sunil Yadav",
    "role": "Space physics researcher",
    "lede": "I am a doctoral researcher in space physics at the University of Turku. I study how shock waves near the Sun are built at kinetic scales, using data from Parker Solar Probe and Solar Orbiter.",
    "affiliation": "Space Research Laboratory, Department of Physics and Astronomy, University of Turku, Finland",
    "email": "sunil.s.yadav@utu.fi",
    "photo": "photo.jpg",  # image file in this folder, embedded into the About page by build.py; "" hides it
    # (label, url) pairs shown on the Contact page. Add or remove lines freely.
    "links": [
        ("ORCID 0009-0003-9858-5720", "https://orcid.org/0009-0003-9858-5720"),
        # ("GitHub", "https://github.com/your-username"),
    ],
}

# Short intro line under the title of each inner page.
INTRO = {
    "research": "My doctoral work and the projects that came before it.",
    "publications": "Papers and conference contributions.",
    "contact": "The best way to reach me is by email.",
}

# Paragraphs on the About page.
BIO = [
    "I joined the Space Research Laboratory at the University of Turku in January 2026, after an integrated BS-MS in Physical Sciences at IISER Berhampur, India. My earlier projects covered solar magnetic fields, sunspots, flares and coronal mass ejections; my doctoral work turns to shock waves near the Sun.",
]

EDUCATION = [
    {"title": "PhD, Physics", "meta": "University of Turku · January 2026 to December 2028 (expected)"},
    {"title": "Integrated BS-MS, Physical Sciences", "meta": "IISER Berhampur, India · 2020 to 2025 · CPI 8.5/10"},
]

SKILLS = ["Python", "SunPy", "LaTeX", "MATLAB (introductory)", "Linux", "JHelioviewer", "Autoplot", "Astrometrica"]
LANGUAGES = "Hindi, English, Awadhi"
SERVICE = "Volunteer organizer, first Exoplanet Workshop in India (IIT Kanpur, April 2025) and the IMBROGLIO event of the IISER Berhampur Physics Club."

TRAINING = [
    {"title": "7th Aditya-L1 Support Cell Workshop", "meta": "ARIES, Nainital · May 2024. Group project: replicated part of De Moortel et al. (2014) on Alfvénic turbulence in coronal loops, using uCoMP data."},
    {"title": "4th Aditya-L1 Support Cell Workshop", "meta": "ARIES, Nainital · June to July 2023. Group project: tracked five CMEs with JHelioviewer, using the CDAW catalogue and LASCO C2 and C3 to measure velocity and acceleration."},
    {"title": "ISWI Space Weather School, Nepal", "meta": "Nepal Physical Society · September 2024"},
    {"title": "National Workshop on CME Kinematics", "meta": "Centurion University · August 2022"},
    {"title": "Sagan Exoplanet Summer Workshop", "meta": "NASA Exoplanet Science Institute · July 2022"},
    {"title": "IIA Summer School", "meta": "Indian Institute of Astrophysics · July 2022"},
    {"title": "Sokendai Asia Winter School", "meta": "Graduate University for Advanced Studies · February 2022"},
    {"title": "Emerging Trends in Gravitation and Cosmology", "meta": "Presidency University, Kolkata · December 2021"},
]

RESEARCH = [
    {
        "title": "Kinetic structure of near-Sun shock waves",
        "status": "Current",
        "meta": "PhD, University of Turku · since January 2026",
        "text": "My doctoral work characterizes the kinetic structure of shocks close to the Sun from observations, combining Parker Solar Probe and Solar Orbiter data. It is supported by a doctoral research grant on interplanetary shock waves from the Space Research Laboratory (2026).",
        "tags": ["Parker Solar Probe", "Solar Orbiter", "Shock waves"],
    },
    {
        "title": "Large- and small-scale solar magnetic fields and X-ray flux",
        "meta": "MS thesis · May 2024 to April 2025 · Dr. Gopal Hazra, IIT Kanpur",
        "text": "I related the Sun's large- and small-scale photospheric magnetic fields to its soft X-ray flux. I separated the scales with a spherical harmonic decomposition (lmax = 5, 10, 20) and an adaptive threshold on SHARP active regions, then computed Pearson correlations with the X-ray flux.",
        "tags": ["HMI", "MDI", "GOES/XRS", "TIMED/SEE", "SORCE/XPS"],
    },
    {
        "title": "Penumbral spots in the RGO Sunspots Database",
        "meta": "December 2023 to February 2024 · Dr. Theodosios Chatzistergos, Max Planck Institute for Solar System Research",
        "text": "I wrote code that extracts penumbral spots from the database and compares spots with no umbra to spots with umbra: area and number of groups over time and per cycle, 1875 to 2013.",
        "tags": ["RGO database", "Sunspots"],
    },
    {
        "title": "Small-scale transients in the solar atmosphere",
        "meta": "May to July 2023 · Dr. Girjesh R. Gupta, Udaipur Solar Observatory, PRL",
        "text": "I fitted a power law to the frequency distribution of flare peaks in Chandrayaan-2 XSM time series and did a case study of the 5-minute oscillation in GONG data.",
        "tags": ["Chandrayaan-2 XSM", "GONG", "Power law"],
    },
    {
        "title": "Earlier reading projects",
        "meta": "Special relativity with Prof. Kinjalk Lochan, IISER Mohali (2022) · Coronal holes and the solar wind with Dr. Saurabh Das, IIT Indore (2022)",
    },
]

PUBLICATIONS = [
    {
        "title": "Submitted paper, The Astrophysical Journal Letters",
        "status": "Under review",
        "meta": "Led by Dr. Immanuel Jebaraj",
        "text": "I contributed to the data analysis behind this paper. Add the title, authors and a link here once it is accepted.",
    },
    {
        "title": "Poster from my MS thesis work",
        "status": "Poster",
        "meta": "Solar Cycle Variability 2024 · ARIES, Nainital · 14 to 18 October 2024",
        "text": "Presented by my supervisor.",
    },
]
