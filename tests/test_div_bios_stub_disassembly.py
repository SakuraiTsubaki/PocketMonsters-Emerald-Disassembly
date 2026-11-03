import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/div-bios-stub-disassembly-summary.json").read_text());self.assertEqual(s["release_count"],6);self.assertEqual(s["function"],"Div")
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());f=e["function"];self.assertEqual(f["software_interrupt"],6);self.assertEqual(f["lz77_vram_relative_offset"],-4);self.assertEqual(f["quotient_register"],"r0");self.assertEqual(f["remainder_register"],"r1");self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/div-bios-stub-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
