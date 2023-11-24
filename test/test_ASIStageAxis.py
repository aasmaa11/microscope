import unittest
from random import uniform as r
from asi import asi_handler


class TestASIStageAxis(unittest.TestCase):
    def test_valid_acceleration_x(self):
        """
        Test that it can change the acceleration
        of the x-axis
        Precision: integer
        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_acc = round(r(axes['X'].min_acceleration_ms, axes['X'].max_acceleration_ms))
        axes['X']._set_acceleration(valid_acc)

        ret_acc = axes['X']._get_acceleration()
        ms._do_shutdown()
        self.assertEqual(ret_acc, valid_acc)

    def test_invalid_acceleration_x(self):
        """
        Test that it raises an assertion error when
        the acceleration of the x-axis is not within the limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        try:
            axes['X']._set_acceleration(axes['X'].max_acceleration_ms + 1)
        except AssertionError:
            assert True   
        ms._do_shutdown()

    def test_valid_acceleration_y(self):
        """
        Test that it can change the acceleration
        of the y-axis
        Precision: integer
        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_acc = round(r(axes['Y'].min_acceleration_ms, axes['Y'].max_acceleration_ms))
        axes['Y']._set_acceleration(valid_acc)

        ret_acc = axes['Y']._get_acceleration()
        ms._do_shutdown()
        self.assertEqual(ret_acc, valid_acc)

    def test_invalid_acceleration_y(self):
        """
        Test that it raises an assertion error when
        the acceleration of the y-axis is not within the limits
        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        try:
            axes['Y']._set_acceleration(axes['Y'].max_acceleration_ms + 1)
        except AssertionError:
            assert True               
        ms._do_shutdown()

    def test_valid_velocity_x(self):
        """
        Test that it can change the velocity
        of the x-axis
        Precision: 6 decimal places
        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        min_vel = 1
        # generate a random acceleration within the range of valid accelerations
        valid_vel = round(r(min_vel, axes['X'].max_velocity_mmps), 6)
        axes['X']._set_velocity(valid_vel)

        ret_vel = axes['X']._get_velocity()
        ms._do_shutdown()
        self.assertEqual(ret_vel, (valid_vel))

    def test_invalid_velocity_x(self):
        """
        Test that it raises an assertion error when
        the velocity of the x-axis is not within the limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))
        axes = ms.axes  
        try:
            axes['X']._set_velocity(axes['X'].max_velocity_mmps + 1)
        except AssertionError:
            assert True  
          
        ms._do_shutdown()
        
    def test_valid_velocity_y(self):
        """
        Test that it can change the velocity
        of the y-axis
        Precision: 6 decimal places

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        min_vel = 1
        # generate a random acceleration within the range of valid accelerations
        valid_vel = round(r(min_vel, axes['Y'].max_velocity_mmps), 6)
        axes['Y']._set_velocity(valid_vel)

        ret_vel = axes['Y']._get_velocity()
        ms._do_shutdown()
        self.assertEqual(ret_vel, (valid_vel))

    def test_invalid_velocity_y(self):
        """
        Test that it raises an assertion error when
        the velocity of the y-axis is not within the limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        try:
            axes['Y']._set_velocity(axes['Y'].max_velocity_mmps + 1)
        except AssertionError:
            assert True    
        ms._do_shutdown()

    def test_valid_settle_time_x(self):
        """
        Test that it can change the settle time
        of the x-axis
        Precision: integer

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_stl = round(r(0, axes['X'].max_settle_time_ms))
        axes['X']._set_settle_time(valid_stl)

        ret_stl = axes['X']._get_settle_time()
        ms._do_shutdown()
        self.assertEqual(ret_stl, (valid_stl))

    def test_invalid_settle_time_x(self):
        """
        Test that it raises an assertion error when
        the settle time of the x-axis is not within the limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        try:
            axes['X']._set_settle_time(axes['X'].max_settle_time_ms + 1)
        except AssertionError:
            assert True     
        ms._do_shutdown()

    def test_valid_settle_time_y(self):
        """
        Test that it can change the settle time
        of the y-axis
        Precision: integer

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        # generate a random acceleration within the range of valid accelerations
        valid_stl = round(r(0, axes['Y'].max_settle_time_ms))
        axes['Y']._set_settle_time(valid_stl)

        ret_stl = axes['Y']._get_settle_time()
        ms._do_shutdown()
        self.assertEqual(ret_stl, (valid_stl))

    def test_invalid_settle_time_y(self):
        """
        Test that it raises an assertion error when
        the settle time of the y-axis is not within the limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        try:
            axes['Y']._set_settle_time(axes['Y'].max_settle_time_ms + 1)
        except AssertionError:
            assert True      
        ms._do_shutdown()

    def test_valid_precision_x(self):
        """
        Test that it can change the precision
        of the x-axis
        Precision: integer

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes

        valid_pre = round(r(axes['X'].min_precision_um, axes['X'].max_precision_um))
        axes['X']._set_precision(valid_pre)

        ret_pre = axes['X']._get_precision()
        ms._do_shutdown()
        self.assertEqual(ret_pre, valid_pre)

    def test_invalid_precision_x(self):
        """
        Test that it raises an assertion error when
        the precision of the x-axis is not within the limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        try:
            axes['X']._set_precision(axes['X'].min_precision_um - 1)
        except AssertionError:
            assert True
        ms._do_shutdown()

    def test_valid_precision_y(self):
        """
        Test that it can change the precision
        of the y-axis
        Precision: integer

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes

        valid_pre = round(r(axes['Y'].min_precision_um, axes['Y'].max_precision_um))
        axes['Y']._set_precision(valid_pre)

        ret_pre = axes['Y']._get_precision()
        ms._do_shutdown()
        self.assertEqual(ret_pre, valid_pre)

    def test_invalid_precision_y(self):
        """
        Test that it raises an assertion error when
        the precision of the y-axis is not within the limits

        """
        ms = asi_handler.ASIStage(which_port='COM3', axes=('X', 'Y'), lead_screws=('F','F'),
                        axes_min_mm=(-50,-25), axes_max_mm=( 50, 25))

        axes = ms.axes
        try:
            axes['Y']._set_precision(axes['Y'].min_precision_um - 1)
        except AssertionError:
            assert True     
        ms._do_shutdown()

if __name__ == '__main__':
    unittest.main()