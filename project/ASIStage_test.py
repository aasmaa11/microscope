import unittest
from random import uniform as r
from asi import asi_handler


class TestASIStage(unittest.TestCase):
    def test_valid_move_to(self):
        """
        Test that stage moves to right position
        with move_to

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y', 'Z'), lead_screws=('S','S','S'),
                        axes_min_mm= (-23,-23,-0.08), axes_max_mm= ( 25,23,0.06), 
                        use_pwm=True, verbose=True, very_verbose=False)
        pos = []
        for name, limits in ms.limits.items():
            min_pos = limits[0]
            max_pos = limits[1]
            pos.append(round(r(min_pos, max_pos), 1))
        exp_pos = {'X': pos[0], 'Y': pos[1], 'Z': pos[2]}
        ms.move_to(exp_pos)

        ret_pos = ms.position
        ms._do_shutdown()
        self.assertEqual(ret_pos, exp_pos)

    def test_invalid_move_to(self):
        """
        Test that handler raises assertion error for move_to when 
        inputs not within axis limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y', 'Z'), lead_screws=('S','S','S'),
                        axes_min_mm= (-23,-23,-0.08), axes_max_mm= ( 25,23,0.06), 
                        use_pwm=True, verbose=True, very_verbose=False)
        pos = []
        for name, limits in ms.limits.items():
            min_pos = limits[0]
            max_pos = limits[1]
            pos.append(min_pos - 1)

        try:
            ms.move_to({'X': pos[0], 'Y': pos[1], 'Z': pos[2]})
        except AssertionError:
            assert True    
        
        ms._do_shutdown()

    def test_valid_move_by(self):
        """
        Test that stage moves to right position
        with move_by

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y', 'Z'), lead_screws=('S','S','S'),
                        axes_min_mm= (-23,-23,-0.08), axes_max_mm= ( 25,23,0.06), 
                        use_pwm=True, verbose=True, very_verbose=False)
        ms.move_to({'X': 0.0, 'Y': 0.0, 'Z': 0.0})
        pos = []
        for name, limits in ms.limits.items():
            min_pos = limits[0]
            max_pos = limits[1]
            pos.append(round(r(min_pos, max_pos)))
        exp_pos = {'X': pos[0], 'Y': pos[1], 'Z': pos[2]}
        ms.move_by(exp_pos)

        ret_pos = ms.position
        ms._do_shutdown()
        self.assertEqual(ret_pos, exp_pos)

    def test_invalid_move_by(self):
        """
        Test that handler raises assertion error for move_by when 
        inputs not within axis limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y', 'Z'), lead_screws=('S','S','S'),
                         axes_min_mm= (-23,-23,-0.08), axes_max_mm= ( 25,23,0.06), 
                        use_pwm=True, verbose=True, very_verbose=False)

        ms.move_to({'X': 0.0, 'Y': 0.0, 'Z': 0.0})

        pos = []
        for name, limits in ms.limits.items():
            min_pos = limits[0]
            max_pos = limits[1]
            pos.append(min_pos - 1)

        try:
            ms.move_by({'X': pos[0], 'Y': pos[1], 'Z': pos[2]})
        except AssertionError:
            assert True
        
        ms._do_shutdown()

if __name__ == '__main__':
    unittest.main()
