import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1]
E={'emerald-jp-rev0':('0x0806F094','0x0806F0A4','0x03005AE4'),'emerald-en-rev0':('0x0806F610','0x0806F620','0x03005D84'),'emerald-de-rev0':('0x0806F610','0x0806F620','0x03005D84'),'emerald-fr-rev0':('0x0806F60C','0x0806F61C','0x03005D84'),'emerald-it-rev0':('0x0806F610','0x0806F620','0x03005D84'),'emerald-es-rev0':('0x0806F60C','0x0806F61C','0x03005D84')}
class T(unittest.TestCase):
 def test_all_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E))
  for k,(seed,random,state) in E.items():
   m=json.loads((R/f'analysis/{k}-rng2.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual(m['globals'],{'gRng2Value':state});self.assertEqual(m['functions']['SeedRng2']['address'],seed);self.assertEqual(m['functions']['Random2']['address'],random);self.assertEqual(m['functions']['Random2']['rom_offset']-m['functions']['SeedRng2']['rom_offset'],16);self.assertEqual(m['functions']['SeedRng2']['code_sha256'],'77dddf4b6256d28fe54fe4fa7c41a15d549d1d3e086013e03c7919823fda7edb');self.assertEqual(m['functions']['Random2']['code_sha256'],'72526af8af03e60317e6ac115ece4a9415af188772c5432ec1c145e0acaf09fb');self.assertTrue(m['algorithm']['independent_from_primary']);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((R/'manifests/rng2-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
