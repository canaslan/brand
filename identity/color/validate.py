"""Validate token references and intended contrast pairs. Python 3, no dependencies."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'colors.tokens.json').read_text())

def flatten(obj, prefix=''):
    result = {}
    for key, value in obj.items():
        path = prefix + key
        if '$value' in value:
            assert set(value) >= {'$value', '$type', '$description'}, path
            assert value['$type'] == 'color', path
            assert not any(not k.startswith('$') for k in value), path
            result[path] = value['$value']
        else:
            result.update(flatten(value, path + '.'))
    return result

def resolve(name, tokens, seen=()):
    assert name not in seen, f'Alias cycle: {seen} -> {name}'
    value = tokens[name]
    if value.startswith('{') and value.endswith('}'):
        return resolve(value[1:-1], tokens, seen + (name,))
    assert value.startswith('#') and len(value) in (7, 9), (name, value)
    int(value[1:], 16)
    return value

def luminance(value):
    assert len(value) == 7, 'Contrast checks require opaque colors'
    channels = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(linear, (.2126, .7152, .0722)))

def contrast(a, b):
    x, y = sorted([luminance(a), luminance(b)])
    return (y + .05) / (x + .05)

results = []
for theme in data['$themes']:
    tokens = {}
    for name in data['$metadata']['tokenSetOrder']:
        if theme['selectedTokenSets'].get(name) == 'enabled':
            tokens.update(flatten(data[name]))
    resolved = {name: resolve(name, tokens) for name in tokens}
    def check(fg, bg, minimum):
        a, b = resolved['color.' + fg], resolved['color.' + bg]
        ratio = contrast(a, b)
        results.append({'theme': theme['name'], 'foreground': fg, 'background': bg,
                        'foregroundHex': a, 'backgroundHex': b, 'ratio': round(ratio, 4),
                        'minimum': minimum, 'pass': ratio >= minimum})
    for surface in ['surface.default', 'surface.subtle']:
        for fg in ['text.primary', 'text.secondary', 'text.tertiary', 'text.accent',
                   'link.active', 'link.hovered', 'link.visited']:
            check(fg, surface, 4.5)
        for fg in ['border.control', 'border.focus', 'icon.accent', 'icon.grey']:
            check(fg, surface, 3)
    for state in ['active', 'hovered', 'pressed']:
        fg = 'button.foreground.' + ('pressed' if state == 'pressed' else 'default')
        check(fg, 'button.' + state, 4.5)
    check('text.on-accent', 'surface.accent', 4.5)
    for status in ['success', 'warning', 'error', 'info']:
        for surface in ['surface.default', 'surface.subtle', 'status.' + status + '.background']:
            for role, minimum in [('text', 4.5), ('icon', 3), ('border', 3), ('default', 4.5)]:
                check('status.' + status + '.' + role, surface, minimum)

assert set(flatten(data['Color/Light'])) == set(flatten(data['Color/Dark'])), 'Theme parity failed'
report = {'method': 'WCAG 2 relative luminance, opaque sRGB; compare unrounded ratios.',
          'scope': 'Declared default/subtle, status, and button pairs only; not a full UI accessibility audit.',
          'checks': len(results), 'failures': sum(not r['pass'] for r in results), 'results': results}
(ROOT / 'contrast-report.json').write_text(json.dumps(report, indent=2) + '\n')
print(f"{report['checks']} contrast checks; {report['failures']} failures. All aliases resolve; themes match.")
for row in results:
    if not row['pass']:
        print(row)
raise SystemExit(1 if report['failures'] else 0)
