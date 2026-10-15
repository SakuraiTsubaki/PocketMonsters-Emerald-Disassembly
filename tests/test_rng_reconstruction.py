import csv,hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
ADDR={'emerald-jp-rev0':0x0806F050,'emerald-en-rev0':0x0806F5CC,'emerald-de-rev0':0x0806F5CC,'emerald-fr-rev0':0x0806F5C8,'emerald-it-rev0':0x0806F5CC,'emerald-es-rev0':0x0806F5C8}
class Tests(unittest.TestCase):
 def test_all_releases(self):
  rows={r['id']:r for r in csv.DictReader((ROOT/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(ADDR))
  for release,address in ADDR.items():
   m=json.loads((ROOT/f'analysis/{release}-rng.json').read_text());self.assertEqual(m['target']['sha256'],rows[release]['sha256']);self.assertEqual((m['variant'],m['functions']['Random']['address']),('emerald',f'0x{address:08X}'));self.assertEqual(m['functions']['SeedRng']['rom_offset']-m['functions']['Random']['rom_offset'],44);self.assertEqual((m['functions']['Random']['code_sha256'],m['functions']['SeedRng']['code_sha256']),('7a127cd9fb3c422f84c3834409ec9e04057ef5680c16b22fb68dd9e9a9fee63e','a15ae683e626610da45d5a377c6d80212c0757411d25d272c3ebf48533b11c0a'));self.assertEqual(set(m['globals']),{'gRngValue','sRandCount','sUnknown'})
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/rng-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
