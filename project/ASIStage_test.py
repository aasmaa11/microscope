import unittest
from random import uniform as r
from asi import asi_handler.py


class TestASIStage(unittest.TestCase):
    def test_valid_move_to(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        for a in range(3):
            min_pos = ms.min_position_um[a] / 10
            max_pos = ms.max_position_um[a] / 10
            pos.append(r(min_pos, max_pos))
        exp_pos = {'x': pos[0], 'y': pos[1], 'z': pos[2]}
        ms.move_to(exp_pos)

        ret_pos = ms.position
        ms._do_shutdown()
        self.assertEqual(ret_pos, exp_pos)

    def test_invalid_move_to(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        for a in range(3):
            min_pos = ms.min_position_um[a] / 10
            max_pos = ms.max_position_um[a] / 10
            pos.append(min_pos - 1)
        self.assertRaises(AssertionError, ms.move_to({'x': pos[0], 'y': pos[1], 'z': pos[2]}))        
        
        ms._do_shutdown()

    def test_valid_move_by(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)
        ms.move_to({'x': 0, 'y': 0})

        for a in range(3):
            min_pos = ms.min_position_um[a] / 10
            max_pos = ms.max_position_um[a] / 10
            pos.append(r(min_pos, max_pos))
        exp_pos = {'x': pos[0], 'y': pos[1], 'z': pos[2]}
        ms.move_by(exp_pos)

        ret_pos = ms.position
        ms._do_shutdown()
        self.assertEqual(ret_pos, exp_pos)

    def test_invalid_move_by(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)
        ms.move_to({'x': 0, 'y': 0})

        for a in range(3):
            min_pos = ms.min_position_um[a] / 10
            max_pos = ms.max_position_um[a] / 10
            pos.append(min_pos - 1)
        self.assertRaises(AssertionError, ms.move_by({'x': pos[0], 'y': pos[1], 'z': pos[2]}))        
        
        ms._do_shutdown()

if __name__ == '__main__':
    unittest.main()