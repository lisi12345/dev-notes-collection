import subprocess
import sys
from PyQt5 import QtWidgets, QtCore


# Step 1: Create a worker class
class GetStdout(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    append = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.keep_reading = False

    def start(self):
        self.keep_reading = True
        self.run()

    def stop(self):
        self.keep_reading = False
        self.finished.emit()

    def run(self):
        """Long-running task."""
        process = subprocess.Popen(
            'candump can0',
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            encoding='utf-8',
            errors='replace'
        )

        while self.keep_reading:
            realtime_output = process.stdout.readline()

            if realtime_output == '' and process.poll() is not None:
                continue

            if realtime_output:
                self.append.emit(realtime_output.strip())
                # print(realtime_output.strip(), flush=True)


class LogTextBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text_box = QtWidgets.QPlainTextEdit()
        self.text_box.setReadOnly(True)

        self.button = QtWidgets.QPushButton("Start")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.clicked_btn)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button)
        vlayout.addWidget(self.text_box)

        self.thread = QtCore.QThread()
        self.worker = GetStdout()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.start)
        self.worker.finished.connect(self.thread.quit)
        self.worker.append.connect(self.add_line)

    def clicked_btn(self):
        if self.button.isChecked():
            self.button.setText('Stop')
            self.thread.start()
        else:
            self.button.setText('Start')
            self.worker.stop()

    def add_line(self, line: str):
        self.text_box.appendPlainText(line)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = LogTextBox()
    a.show()
    a.raise_()
    sys.exit(app.exec_())
