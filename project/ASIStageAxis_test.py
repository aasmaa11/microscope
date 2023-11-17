import unittest
from random import uniform as r
from asi import asi_handler.py


class TestASIStageAxis(unittest.TestCase):
    def test_valid_acceleration_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_acc = r(ms.min_acceleration_ms[0], ms.max_acceleration_ms[0])
        axes['X']._set_acceleration(valid_acc)

        ret_acc = axes['X']._get_acceleration()
        ms._do_shutdown()
        self.assertEqual(ret_acc, valid_acc)

    def test_invalid_acceleration_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        self.assertRaises(AssertionError, axes['X']._set_acceleration(ms.max_acceleration_ms[0] + 1))
        ms._do_shutdown()

    def test_valid_acceleration_y(self):
        """
        Test that it can change the acceleration
        of the y-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_acc = r(ms.min_acceleration_ms[1], ms.max_acceleration_ms[1])
        axes['Y']._set_acceleration(valid_acc)

        ret_acc = axes['Y']._get_acceleration()
        ms._do_shutdown()
        self.assertEqual(ret_acc, valid_acc)

    def test_invalid_acceleration_y(self):
        """
        Test that it can change the acceleration
        of the y-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        self.assertRaises(AssertionError, axes['Y']._set_acceleration(ms.max_acceleration_ms[1] + 1))        
        ms._do_shutdown()

    def test_valid_velocity_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        min_vel = 1
        # generate a random acceleration within the range of valid accelerations
        valid_vel = r(min_vel, ms.max_velocity_mmps[0])
        axes['X']._set_velocity(valid_vel)

        ret_vel = axes['X']._get_velocity()
        ms._do_shutdown()
        self.assertEqual(ret_vel, valid_vel)

    def test_invalid_velocity_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        self.assertRaises(AssertionError, axes['X']._set_velocity(ms.max_velocity_mmps[0] + 1))        
        ms._do_shutdown()
        
    def test_valid_velocity_y(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        min_vel = 1
        # generate a random acceleration within the range of valid accelerations
        valid_vel = r(min_vel, ms.max_velocity_mmps[1])
        axes['Y']._set_velocity(valid_vel)

        ret_vel = axes['Y']._get_velocity()
        ms._do_shutdown()
        self.assertEqual(ret_vel, valid_vel)

    def test_invalid_velocity_y(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes

        self.assertRaises(AssertionError, axes['Y']._set_velocity(ms.max_velocity_mmps[1] + 1))        
        ms._do_shutdown()

    def test_valid_settle_time_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_stl = r(0, ms.max_settle_time_ms[0])
        axes['X']._set_settle_time(valid_stl)

        ret_stl = axes['X']._get_settle_time()
        ms._do_shutdown()
        self.assertEqual(ret_stl, valid_stl)

    def test_invalid_settle_time_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        self.assertRaises(AssertionError, axes['X']._set_settle_time(ms.max_settle_time_ms[0] + 1))        
        ms._do_shutdown()

    def test_valid_settle_time_y(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_stl = r(0, ms.max_settle_time_ms[1])
        axes['Y']._set_settle_time(valid_stl)

        ret_stl = axes['Y']._get_settle_time()
        ms._do_shutdown()
        self.assertEqual(ret_stl, valid_stl)

    def test_invalid_settle_time_y(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes
        self.assertRaises(AssertionError, axes['Y']._set_settle_time(ms.max_settle_time_ms[1] + 1))        
        ms._do_shutdown()

    def test_valid_precision_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes

        valid_pre = r(ms.min_precision_um[0], ms.max_precision_um[0])
        axes['X']._set_precision(valid_pre)

        ret_pre = axes['X']._get_precision()
        ms._do_shutdown()
        self.assertEqual(ret_pre, valid_pre)

    def test_invalid_precision_x(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes

        self.assertRaises(AssertionError, axes['X']._set_precision(ms.min_precision_um[0] - 1))        
        ms._do_shutdown()

    def test_valid_precision_y(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes

        valid_pre = r(ms.min_precision_um[1], ms.max_precision_um[1])
        axes['Y']._set_precision(valid_pre)

        ret_pre = axes['Y']._get_precision()
        ms._do_shutdown()
        self.assertEqual(ret_pre, valid_pre)

    def test_invalid_precision_y(self):
        """
        Test that it can change the acceleration
        of the x-axis

        """
        ms = ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25), 
                        use_pwm=True, verbose=True, very_verbose=False)

        axes = ms.axes

        self.assertRaises(AssertionError, axes['Y']._set_precision(ms.min_precision_um[1] - 1))        
        ms._do_shutdown()

if __name__ == '__main__':
    unittest.main()