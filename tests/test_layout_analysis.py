from __future__ import annotations
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class LayoutAnalysisTests(unittest.TestCase):
 def test_origin_layout_is_complete_and_conservative(self):
  r=json.loads((ROOT/"analysis"/"emerald-jp-rev0-layout.json").read_text(encoding="utf-8"));self.assertEqual(r["sha256"],"33f5610b9186b4add09fef68895deb00f552b997b3d133b5a961e5123506343c");self.assertEqual(r["region_count"],16);self.assertEqual([x["region"] for x in r["regions"] if x["classification"]=="padding"],[10]);self.assertTrue(all(x["rom_pointer_words"]>=x["thumb_pointer_words"] for x in r["regions"]))
 def test_manifest_hashes_output(self):
  m=json.loads((ROOT/"analysis"/"emerald-jp-rev0-layout-manifest.json").read_text(encoding="utf-8"));o=m["outputs"][0];self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()
