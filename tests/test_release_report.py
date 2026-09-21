from __future__ import annotations
import csv,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ReleaseReportTests(unittest.TestCase):
 def test_release_evidence_is_synchronized(self):
  p={x["id"]:x for x in json.loads((ROOT/"project.json").read_text(encoding="utf-8"))["releases"]};report=json.loads((ROOT/"analysis"/"emerald-release-header-report.json").read_text(encoding="utf-8"));r={x["id"]:x for x in report["releases"]}
  with (ROOT/"research"/"releases.csv").open(newline="",encoding="utf-8") as s:c={x["id"]:x for x in csv.DictReader(s)}
  self.assertEqual(set(p),set(r));self.assertEqual(set(p),set(c));self.assertEqual((report["observed_files"],report["unique_identities"]),(3,2))
  for i,x in p.items():self.assertEqual(x["status"],"candidate");self.assertEqual(x["sha256"],r[i]["sha256"]);self.assertEqual(x["sha256"],c[i]["sha256"]);self.assertTrue(all(r[i]["validation"].values()))
 def test_language_codes_and_duplicate_are_preserved(self):
  rs=json.loads((ROOT/"analysis"/"emerald-release-header-report.json").read_text(encoding="utf-8"))["releases"];self.assertEqual({x["header"]["game_code"] for x in rs},{"BPEJ","BPEE"});en=next(x for x in rs if x["id"]=="emerald-en-rev0");self.assertEqual(len(en["observed_filenames"]),2)
if __name__=="__main__":unittest.main()
