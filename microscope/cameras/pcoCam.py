import logging
import queue
import time

import numpy as np

import microscope
import microscope.abc
import pco
import ctypes as C
import numpy as np
import os



class pcoPandaCamera(
    microscope.abc.FloatingDeviceMixin, microscope.abc.Camera,
    ):    
    def __init__(self, index=0, **kwargs):
        super().__init__(index=index, **kwargs)
        self.myCam = pco.Camera()
        self.initialize()
        #will need to init those two later after the first capture
        self.imageBuffer = None
        self.imageMetaData = None
        

    @microscope.abc.keep_acquiring
    def set_exposure_time(self, value: float) -> None:
        #may need to convert the value to exponential notation
        self.myCam.exposure_time = value

    def get_exposure_time(self) -> float:
        """Return the current exposure time in seconds."""
        return self.myCam.exposure_time

    #Not sure what to do here
    def get_cycle_time(self) -> float:
        """Return the cycle time in seconds."""
        """ 
        This does not seem to be a parameter bound to the camera itself, more to the 
        system as a whole. Usually in cycles we also have stage movements for multi-axis
        imagery. This is different from delay time: which represents the amount of time between
        captures
        """
        
        """
        Pass for now
        """
        pass

    #may need to import pco.sdk if this doesn't work
    def _get_sensor_shape(self) -> typing.Tuple[int, int]:
        """Return a tuple of `(width, height)` indicating shape in pixels."""
        #Consult pco.camera maybe 
        cam_desc = self.myCam.sdk.get_camera_description()
        width = cam_desc["max. horizontal resolution standard"]
        height = cam_desc["max. vertical resolution standard"]
        return (width, height)
    
    def _get_binning(self) -> microscope.Binning:
        """Return the current binning."""
        h, v = self.myCam.configuration['binning']
        
        # must type cast to microscope.Binning
        return microscope.Binning(h, v)
        
    
    def _set_binning(self, binning: microscope.Binning):
        """Set binning along both axes.  Return `True` if successful."""
        #break down the arg for type casting
        h, v = binning 
        self.myCam.configuration['binning'] = (h, v)
        if (self._get_binning == binning):
            return True
        else:
            return False
        
    
    def _get_roi(self) -> microscope.ROI:
        left, top, width, height = self.myCam.configuration['roi']
        return microscope.ROI(left, top, width, height)
    
    def _set_roi(self, roi: microscope.ROI):
        """Set the ROI on the hardware.  Return `True` if successful."""
        self.myCam.configuration['roi'] = roi
        
        if (self._get_roi == roi):
            return True
        else:
            return False
    
    # Method is depracated for trigger type and trigger mode
    def get_trigger_type(self):
        """Return the current trigger mode.

        One of
            TRIGGER_AFTER,
            TRIGGER_BEFORE or
            TRIGGER_DURATION (bulb exposure.)
        """
        pass
    
    def abort(self) -> None:
        """Stop acquisition as soon as possible."""
        if self.myCam.is_recording:
            self.myCam.stop()
            self._acquiring = False
        
    
    def _fetch_data(self) -> None:
        """Poll for data and return it, with minimal processing.

        If the device uses buffering in software, this function should
        copy the data from the buffer, release or recycle the buffer,
        then return a reference to the copy.  Otherwise, if the SDK
        returns a data object that will not be written to again, this
        function can just return a reference to the object.  If no
        data is available, return `None`.

        """
        
        image, metadata = self.myCam.image()
        """
        So the pco library comes with two ways to fetch the image(s) respectively called
        image() and images(). image() will only consider the most recent image while images()
        will return the buffer of images as an array of images and an array of metadata. Length
        for that array will be equal the the number specified in number_of_images when calling 
        cam.record(number_of_images=x, mode='sequence'). We may want to consider using images
        when working on single-site experiment and multi-site experiment.
        """
        
        return image
    
    @keep_acquiring
    def update_settings(self, settings, init: bool = False) -> None:
        """Update settings, toggling acquisition if necessary."""
        super().update_settings(settings, init)
        
    def get_id(self) -> str:
        """Return a unique hardware identifier such as a serial number."""
        return self.myCam.camera_serial
    
    #TODO: implement
    @property
    def trigger_mode(self) -> microscope.TriggerMode:
        raise NotImplementedError()

    #TODO: implement
    @property
    def trigger_type(self) -> microscope.TriggerType:
        raise NotImplementedError()

    #TODO: implement
    def set_trigger(
        self, ttype: microscope.TriggerType, tmode: microscope.TriggerMode
    ) -> None:
        """Set device for a specific trigger.
        """
        raise NotImplementedError()

    def _do_trigger(self) -> None:
        """Actual trigger of the device.

        Classes implementing this interface should implement this
        method instead of `trigger`.

        """
        #At the moment I do not see any reason to use other modes
        #Maybe we can consider taking multiple images
        self.myCam.record(number_of_images=1, mode='sequence')
        #raise NotImplementedError()
        
    
    def _do_shutdown(self) -> None:
        """Private method - actual shutdown of the device.

        Users should be calling :meth:`shutdown` and not this method.
        Concrete implementations should implement this method instead
        of `shutdown`.

        From manual:
        
        def __exit__(self, exc_type, exc_value, exc_traceback):    
            
        Closes the activated camera and releases the blocked ressources.
        Do not call this explicitly, this function is called automatically when a camera object is destroyed.
        Either directly cam.close() or by the with statement.
        
        def close(self):
        
        Closes the activated camera and releases the blocked ressources. 
        This function must be called before the application is terminated. Otherwise, the resources remain occupied.
        This function is called automatically if the camera object was released by the with statement. 
        An explicit call to close() is no longer necessary.
        
        """        
        self.myCam.close()
    
    def initialize(self) -> None:
        """Initialize the device.

        If devices have this method (not required, and many don't),
        then they should call it as part of the initialisation, i.e.,
        they should call it on their `__init__` method.

        From manual:
        
        def __init__(self, interface=None):
        
        Opens and initializes the camera. 
        Do not call this explicitly, this function is called automatically when a camera object is created. 
        Either directly cam = pco.Camera() or by the with statement.
        """
        #We create the object in init and then call initialize to set default configuration
        #pco.Camera().configurations are stored in a dictionary
        
        self.myCam.default_configuration()
        

