from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets


class StepSizeWidget(QtWidgets.QWidget):
    valueChanged = QtCore.Signal(int)

    def __init__(self, value=1):
        super(StepSizeWidget, self).__init__()

        # Step Size Spin Box
        self.step_size_spin_box = QtWidgets.QSpinBox()
        self.step_size_spin_box.setRange(-1000, 1000)
        self.set_value(value)
        self.step_size_spin_box.setToolTip("Video Step Size")
        self.step_size_spin_box.setStatusTip(self.step_size_spin_box.toolTip())
        self.step_size_spin_box.setAlignment(QtCore.Qt.AlignCenter)

        # Predict Button
        self.predict_button = QtWidgets.QPushButton("Pred")

        # Connect valueChanged signal of QSpinBox to self.valueChanged
        self.step_size_spin_box.valueChanged.connect(self.emit_value_changed)

        # Layout
        layout = QtWidgets.QVBoxLayout()  # Vertical layout
        layout.addWidget(self.step_size_spin_box)
        layout.addWidget(self.predict_button)  # Predict button below spin box
        self.setLayout(layout)
        # Set the width of the prediction button to match the width of the spin box
        self.predict_button.setFixedWidth(
            self.step_size_spin_box.sizeHint().width())

    def set_value(self, value):
        self.step_size_spin_box.setValue(value)

    def emit_value_changed(self, value):
        self.valueChanged.emit(value)

    def minimumSizeHint(self):
        height = super(StepSizeWidget, self).minimumSizeHint().height()
        fm = QtGui.QFontMetrics(self.font())
        width = fm.width(str(self.step_size_spin_box.maximum()))
        return QtCore.QSize(width, height)
