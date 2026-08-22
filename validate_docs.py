from pathlib import Path
import re

root = Path('/home/ubuntu/skills/ccss-5-0')
required = [
    'SKILL.md', 'README.md',
    'references/command-protocol.md', 'references/mission-protocol.md',
    'references/quality-security.md', 'references/federation-adapters.md',
    'references/progressive-disclosure.md',
    'templates/mission.md', 'templates/decision.md', 'templates/research.md',
    'templates/evidence.md', 'templates/architecture.md', 'templates/workflow.md',
    'templates/artifact.md', 'templates/review.md', 'templates/redteam.md',
    'templates/checkpoint.md', 'templates/capability.md',
]
missing = [p for p in required if not (root / p).is_file()]
assert not missing, f'missing required files: {missing}'

for path in root.rglob('*.md'):
    text = path.read_text()
    for target in re.findall(r'`((?:references|templates|examples)/[^`]+\.md)`', text):
        if '*' in target:
            continue
        assert (root / target).is_file(), f'{path}: broken reference {target}'

for path in (root / 'templates').glob('*.md'):
    text = path.read_text()
    assert 'Purpose' in text and 'When to use' in text, f'{path}: missing purpose/use guidance'
    assert 'Copy-ready template' in text, f'{path}: missing copy-ready section'
    assert 'example' in text.lower(), f'{path}: missing example'

skill = (root / 'SKILL.md').read_text()
assert len(skill.splitlines()) < 500
assert 'unavailable' in skill and 'verification' in skill.lower()
print(f'validated {len(required)} required files, {len(list((root / "templates").glob("*.md")))} templates, and {len(list(root.rglob("*.md")))} Markdown files')
