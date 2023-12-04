import os
import sys
import pathlib
import requests

from string import Template
from pathlib import Path

try:
    requests
except ImportError:
    print('requests not installed, please run `pip3 install requests` first')
    sys.exit()


try:
    from pybtex.database.input import bibtex
except ImportError:
    print('pybtex not installed, please run `pip3 install pybtex` first')
    sys.exit()
    
try:
    from unidecode import unidecode
except ImportError:
    print('pybtex not installed, please run `pip3 install pybtex` first')
    sys.exit()

# parse bibtex
parser = bibtex.Parser()
bib_data = parser.parse_file('bibliography.bib')

J_ABBREV = {
    'bioRxiv': 'bioRxiv',
    'arXiv': 'arXiv',
    'Bioinformatics': 'Bioinformatics',
    'PLoS Computational Biology': 'PLoS Comput. Biol.',
    'PLoS One': 'PLoS One',
    'Cell Systems': 'Cell Syst.',
    'Briefings in Bioinformatics': 'Brief. Bioinform.',
    'Nucleic Acids Research': 'Nucleic Acids Res.',
    'npj Systems Biology and Applications': 'npj Syst. Biol. Appl.',
    'Molecular Systems Biology': 'Mol. Syst. Biol.',
    'Cell Reports': 'Cell Rep.'
}

MAPPINGS = {
    'TITLE': 'title',
    'YEAR': 'year',
    'MONTH': 'month',
    'DAY': 'day',
    'JOURNAL': 'journal',
    'DOI': 'doi',
    'ABSTRACT': 'abstract',
    'VOLUME': 'volume',
    'PAGES': 'pages',
    'ISSUE': 'number',
}

CODE_LINKS = {
    '2016-01-25-kazeroonian-moment-generation': 'https://github.com/CERENADevelopers/CERENA',
    '2016-07-22-frohlich-moment-estimation': 'https://doi.org/10.1371/journal.pcbi.1005030.s002',
    '2017-01-23-frohlich-adjoint-sensitivity': 'https://doi.org/10.1371/journal.pcbi.1005331.s002',
    '2016-12-27-frohlich-event-sensitivity': '',
    '2017-10-23-stapor-pesto-estimation': 'https://github.com/ICB-DCM/PESTO/',
    '2017-11-30-ligon-genssi-identifiability': 'https://github.com/genssi-developer/GenSSI',
    '2018-05-23-loos-hierarchical-heterogeneity': 'https://github.com/ICB-DCM/ODEMM',
    '2018-06-27-stapor-hessian-sensi': 'https://github.com/AMICI-dev/AMICI',
    '2018-08-23-villaverde-benchmarking-sensitivities': 'https://zenodo.org/record/1304034#.Y2k3Zi-B2-Z',
    '2018-12-10-frohlich-multiexperiment-nlme': 'https://github.com/ICB-DCM/MEMOIR',
    '2018-12-26-frohlich-pancancer-drug': 'https://zenodo.org/record/1472794#.Y2k3Ny-B2-Z',
    '2019-07-26-schmiester-relative-scaling': 'https://github.com/ICB-DCM/CS_Signalling_ERBB_RAS_AKT',
    '2020-11-18-gerosa-erk-pulses': 'https://github.com/labsyspharm/marm1-supplement',
    '2021-01-26-schmiester-petab-problem': 'https://github.com/PEtab-dev/PEtab',
    '2021-04-02-frohlich-amici-simulation': 'https://github.com/AMICI-dev/AMICI',
    '2021-10-09-villaverde-calibration-protocol': 'https://github.com/ICB-DCM/model_calibration_protocol',
    '2021-12-28-schmucker-drug-combinations': 'https://github.com/Sandholm-Lab/treatment-opt-pancancer',
    '2022-05-07-shaikh-biosimulators-platform': 'https://github.com/biosimulators/Biosimulators',
    '2022-07-13-frohlich-fides-optimizer': 'https://github.com/fides-dev/fides-benchmark',
    '2023-01-03-lakrisenko-adjoint-steadystate': '',
    '2023-01-26-frohlich-allosteric-rewiring': 'https://github.com/labsyspharm/marm2-supplement',
    '2023-03-13-chen-erk-senescence': 'https://github.com/clemenshug/erk_senescence',
    '2023-11-23-schalte-pypesto': 'https://github.com/ICB-DCM/pyPESTO',
}

ACCENTS = {
    r'\"o': r'ö',
    r'\"u': r'ü',
    r'\"a': r'ä',
    r'\"i': r'i',
    r'\"O': r'Ö',
    r'\"U': r'Ü',
    r'\"A': r'Ä',
    r'\`a': r'à',
    r"\'a": r'á',
    r'\`e': r'è',
    r"\'e": r'é',
    r'\`o': r'ò',
    r"\'o": r'ó',
    r'\`u': r'ù',
    r'\'u': r'ú',
    r'\L': r'Ł',
    r'\v{s}': r'š',
    r'\c{s}': r'ş',
    r'\ss': r'ß',
}

PAPER_PDF_PATH = '/pdfs/papers/'

# cleanup
for p in Path(__file__).parent.glob('*.md'):
    print(f'removing {p}')
    p.unlink()

def sanitize(name: str) -> str:
    for s, t in ACCENTS.items():
        name = name.replace(f'{{{s}}}', t)
        name = name.replace(f'{s}', t)
    if "\\" in name or "{{" in name or "}}" in name:
        print(
            f'name {name} contains an accents that could not be sanitized, '
            'please add the respective accent to the ACCENTS variable in '
            'this script.'
        )
        sys.exit()
    return name

for pubkey, entry in bib_data.entries.items():
    print(f'processing {pubkey}')

    template_data = dict()
    for key, field in MAPPINGS.items():
        if field not in entry.fields and field not in [
            'number', 'pages', 'volume'
        ]:
            print(
                f'bibtext information about `{field}` not available, please '
                'fix the respective bibtex entry.'
            )
            sys.exit()
        template_data[key] = entry.fields.get(field, '')

    for key in ['ABSTRACT', 'TITLE']:
        if template_data[key].startswith('{'):
            template_data[key] = template_data[key][1:]
        if template_data[key].endswith('}'):
            template_data[key] = template_data[key][:-1]


    if template_data['JOURNAL'] not in J_ABBREV:
        print(
            f'{template_data["JOURNAL"]} does not have an abbreviation, either '
            'fix the journal name or add the abbreviation to the MAPPINGS '
            'variable in this script.'
        )
        sys.exit()
    template_data['JOURNAL_ABBREV'] = J_ABBREV[template_data['JOURNAL']]

    # parse authors
    authors = entry.persons['author']

    template_data['FIRSTAUTH'] = ' '.join(
        sanitize(name) for name in entry.persons['author'][0].last_names
    )
    firstauth = template_data['FIRSTAUTH'].lower()

    template_data['AUTHORS'] = ', '.join(
        ' '.join((
            ' '.join(sanitize(name) for name in author.last_names),
            ''.join(sanitize(name)[0].upper()
                    for name in author.first_names + author.middle_names)
        ))
        for author in entry.persons['author']
    )

    template_data['PREPRINT'] = template_data['JOURNAL'] in [
        'bioRxiv', 'arXiv', 'medRxiv'
    ]

    pubid = Template(f'$YEAR-$MONTH-$DAY-{firstauth}-{pubkey}').safe_substitute(
        template_data
    )
    pubid = unidecode(pubid)
    if pubid not in CODE_LINKS:
        print(
            f'Code link is missing for {pubid}. Please add link to the '
            'CODE_LINKS variable in this script. If there is no associated '
            'code, add `` as link.'
        )
        sys.exit()
    template_data['CODE'] = CODE_LINKS.get(pubid, '')


    # write post using template data
    template_file = 'post.md.template'
    target_file = pubid + '.md'
    pdf_file = os.path.splitext(target_file)[0] + '.pdf'
    pdf_file_path = (
        Path('.') / '..' / '..' / 'pdfs' / 'papers' / pdf_file
    ).resolve()
    if not pdf_file_path.exists():
        if 'eprint' not in entry.fields:
            print(
                f'Did not find associated pdf {pdf_file_path}, and did not find an '
                '`epub` entry in the bibtex entry. Please either download the '
                f'pdf and place it in `{PAPER_PDF_PATH}` or add an epub field.'
            )
            sys.exit()
        template_data['PDFLINK'] = entry.fields["eprint"]
        template_data['PDF'] = ''
    else:
        template_data['PDF'] = PAPER_PDF_PATH + pdf_file
        template_data['PDFLINK'] = ''

    with open(template_file) as filein:
        src = Template(filein.read())
    result = src.safe_substitute(template_data)
    with open(target_file, 'w') as fileout:
        fileout.write(result)
