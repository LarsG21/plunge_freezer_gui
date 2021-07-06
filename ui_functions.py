

## ==> GUI FILE
from main import *

class UIFunctions(QMainWindow):

    def update_labels(self,temp_chamber,temp_cryo, humid):

        self.ui.temp_lable_2.setText(str(temp_chamber)+"°C")
        self.ui.temp_lable_bottom_4.setText(str(temp_cryo)+"°C")
        if humid >= 0 and humid <=100:
            self.ui.humid_lable_2.setText(str(humid)+"%")
        else:
            self.ui.humid_lable_2.setText("Error in senor reading")

    def send_start_command(self):
        temp_chamber = self.ui.temp_control_2.value()
        temp_cryo = self.ui.temp_control_botttom_4.value()
        humid = self.ui.humid_control_2.value()
        blotting_force = self.ui.blotting_force_control_2.value()
        blotting_time = self.ui.blotting_time_control_2.value()
        blotting_nr = self.ui.blotting_number_control_2.value()

        #Send data to uc
        print(temp_chamber,temp_cryo, humid, blotting_force, blotting_time, blotting_nr)

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
                self.ui.button_page_home.setText('          Home')
                self.ui.button_page_plots.setText('          Plots')
                self.ui.button_page_Data.setText('          Data')
            else:
                widthExtended = standard
                self.ui.button_page_home.setText('    ')
                self.ui.button_page_plots.setText('    ')
                self.ui.button_page_Data.setText('    ')

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

