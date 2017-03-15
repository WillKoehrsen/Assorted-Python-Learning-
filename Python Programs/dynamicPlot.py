import joystick as jk
import numpy as np
import time

class test(jk.Joystick, y_data):
    # initialize the infinite loop and callit decorators so they can auto-
    # register methods they decorate
    _infinite_loop = jk.deco_infinite_loop()
    _callit = jk.deco_callit()

    @_callit('before', 'init')
    def _init_data(self, *args, **kwargs):
        # Function automatically called at initialization, thanks to the
        # decorator
        self.xdata = np.array([])  # time x-axis
        self.ydata = np.array([y_data])  # fake data y-axis

    @_callit('after', 'init')
    def _build_frames(self, *args, **kwargs):
        # Function automatically called at initialization, thanks to the
        # decorator. It will be called after "_init_data" given that it is
        # declared after
        # create a graph frame
        self.mygraph = self.add_frame(
                   jk.Graph(name="test", size=(500, 500), pos=(50, 50),
                            fmt="go-", xnpts=15, freq_up=7, bgcol="y",
                            xylim=(0,10,0,1), xlabel='t', ylabel='random'))
        # create a text frame
        self.mytext = self.add_frame(
                      jk.Text(name="Y-overflow", size=(500, 250),
                              pos=(600, 50), freq_up=1))

    @_callit('before', 'start')
    def _set_t0(self):
        # initialize t0 at start-up
        self._t0 = time.time()

    @_infinite_loop(wait_time=0.2)
    def _get_data(self):
        # This method will automatically be called with simulation start
        # (t.start()), and looped every 0.2 in a separate thread as long as
        # the simulation runs (running == True)
        # It gets new data (fake random data) and pushes it to the frames.
        # concatenate data on the time x-axis
        new_x_data = time.time()
        self.xdata = jk.core.add_datapoint(self.xdata,
                                           new_x_data,
                                           xnptsmax=self.mygraph.xnptsmax)
        # concatenate data on the fake data y-axis
        '''
        new_y_data = np.random.random()*1.05
        # check overflow for the new data point
        if new_y_data > 1:
            # send warning to the text-frame
            self.mytext.add_text('Some data bumped into the ceiling: '
                                 '{:.3f}'.format(new_y_data))
        self.ydata = jk.core.add_datapoint(self.ydata,
                                           new_y_data,
                                           xnptsmax=self.mygraph.xnptsmax)
        '''
        
        # prepare the time axis
        t = np.round(self.xdata-self._t0, 1)
        # push new data to the graph
        self.mygraph.set_xydata(t, self.ydata)

    @_callit('before', 'exit')
    def exit_warning(self):
        # Just a warning, automatically called with the exit method, and
        # before the exiting actually takes place (closing frames, etc)
        print("You're about to exit, frames will disappear in 1 second")
        time.sleep(1)

t = test()
t.start()