import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from client import MultimodalChartDataPointExtractor

class CoreTests(unittest.TestCase):
    def setUp(self):self.c=MultimodalChartDataPointExtractor()

    def test_fit_quality(self):
        self.assertAlmostEqual(self.c.calibrate_axis_scale([{'coord':0,'val':0},{'coord':1,'val':1},{'coord':2,'val':4}])['r_squared'],12/13)
        self.assertEqual(self.c.calibrate_axis_scale([{'coord':1,'val':0},{'coord':1,'val':2}])['status'],'ERROR')
    def test_conversions(self):
        cal=self.c.calibrate_axis_scale([{'coord':500,'val':0},{'coord':100,'val':200}])
        self.assertEqual(self.c.extract_bar_chart_series([{'label':'A','y_top':300,'y_base':500}],cal)[0]['extracted_value'],100)
        self.assertEqual(self.c.extract_scatter_points([{'x':2,'y':300}],{'slope':3,'intercept':1},cal)[0]['x'],7)
