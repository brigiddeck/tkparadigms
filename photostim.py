'''
Create a paradigm for calibrating the amount of water delivered.

TO DO:
- Add laser outputs
- Do both at the same time (include a menu selector)

'''

import sys
from PySide import QtCore 
from PySide import QtGui 
from taskontrol.settings import rigsettings
from taskontrol.core import dispatcher
from taskontrol.core import statematrix
from taskontrol.core import savedata
from taskontrol.core import paramgui
from taskontrol.core import messenger
from taskontrol.core import arraycontainer
from taskontrol.plugins import manualcontrol

class PhotoStim(QtGui.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None, dummy=False):
        super(PhotoStim, self).__init__(parent)

        self.name = 'photostim'

        # -- Read settings --
        if dummy:
            smServerType = 'dummy'
        else:
            smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Module for saving data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR)

        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Add parameters --
        self.params = paramgui.Container()

        self.params['timeStimLeft'] = paramgui.NumericParam('Time stim left',value=1,
                                                            units='s',group='Stimulation times')
        self.params['timeDelayPostLeft'] = paramgui.NumericParam('Delay post left',value=4,
                                                            units='s',group='Stimulation times')
        self.params['timeStimRight'] = paramgui.NumericParam('Time stim right',value=1,
                                                            units='s',group='Stimulation times')
        self.params['timeDelayPostRight'] = paramgui.NumericParam('Delay post right',value=4,
                                                            units='s',group='Stimulation times')
        self.params['timeStimBoth'] = paramgui.NumericParam('Time stim both',value=1,
                                                            units='s',group='Stimulation times')
        self.params['timeDelayPostBoth'] = paramgui.NumericParam('Delay post both',value=4,
                                                            units='s',group='Stimulation times')
        stimTimes = self.params.layout_group('Stimulation times')

        # -- Create dispatcher --
        self.dispatcherModel = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)
        self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)
 
        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcherModel.statemachine)

        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QHBoxLayout()
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()
        layoutCol3 = QtGui.QVBoxLayout()

        layoutCol1.addWidget(self.saveData)
        #layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(self.dispatcherView)

        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()

        layoutCol3.addWidget(stimTimes)
        layoutCol3.addStretch()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables storing results --
        self.results = arraycontainer.Container()

        # -- Connect signals from dispatcher --
        self.dispatcherModel.prepareNextTrial.connect(self.prepare_next_trial)
        self.dispatcherModel.timerTic.connect(self._timer_tic)

        # -- Connect messenger --
        self.messagebar = messenger.Messenger()
        self.messagebar.timedMessage.connect(self._show_message)
        self.messagebar.collect('Created window')

        # -- Connect signals to messenger
        self.saveData.logMessage.connect(self.messagebar.collect)
        self.dispatcherModel.logMessage.connect(self.messagebar.collect)

        # -- Connect other signals --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        # -- Center in screen --
        paramgui.center_in_screen(self)

        # -- Prepare first trial --
        # - No need to prepare here. Dispatcher sends a signal when pressing Start -
        #self.prepare_next_trial(0)
        

    def _show_message(self,msg):
        self.statusBar().showMessage(str(msg))
        print msg

    def _timer_tic(self,etime,lastEvents):
        pass

    def save_to_file(self):
        pass

    def prepare_next_trial(self, nextTrial):
        print '============ Prearing trial {0} ==========='.format(self.dispatcherModel.currentTrial)
        self.sm.reset_transitions()

        #valveTimeR = self.params['timeWaterValveR'].get_value()
        #valveTimeR = self.params['timeWaterValveR'].get_value()

        self.sm.add_state(name='startTrial', statetimer=0,
                          transitions={'Tup':'stimLeft'})
        self.sm.add_state(name='stimLeft',
                          statetimer=self.params['timeStimLeft'].get_value(),
                          transitions={'Tup':'delayPostLeft'},
                          outputsOn={'leftLED'})
        self.sm.add_state(name='delayPostLeft',
                          statetimer=self.params['timeDelayPostLeft'].get_value(),
                          transitions={'Tup':'stimRight'},
                          outputsOff={'leftLED'})
        self.sm.add_state(name='stimRight',
                          statetimer=self.params['timeStimRight'].get_value(),
                          transitions={'Tup':'delayPostRight'},
                          outputsOn={'rightLED'})
        self.sm.add_state(name='delayPostRight',
                          statetimer=self.params['timeDelayPostRight'].get_value(),
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff={'rightLED'})

        #print self.sm ### DEBUG
        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
        self.dispatcherModel.die()
        event.accept()

if __name__ == "__main__":
    (app,paradigm) = paramgui.create_app(PhotoStim)
