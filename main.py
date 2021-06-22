import sys
import PyQt5.QtGui as gui
import PyQt5.QtCore as core
import PyQt5.QtWidgets as wg

from pytube import YouTube
from ddownloader.main_ui import Ui_MainWindow


class MainWindow(wg.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_download.clicked.connect(self.btn_download_clicked)

    def btn_download_clicked(self):
        url = self.ui.input_url.text().strip()

        self.thread = core.QThread(self)
        self.worker = DownloadWorker(None, url)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.worker.status.connect(self.ui.status.setText)

        self.thread.start()

        self.ui.input_url.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.ui.input_url.setEnabled(True)
        )

    def reportProgress(self, val):
        print(f'Update progress {val}')
        self.ui.progressBar.setValue(val)

    def closeEvent(self, a0: gui.QCloseEvent):
        return super().closeEvent(a0)

class DownloadWorker(core.QObject):
    finished = core.pyqtSignal()
    progress = core.pyqtSignal(int)
    status = core.pyqtSignal(str)

    def __init__(self, parent, url):
        super().__init__(parent=parent)
        self.url = url

    def run(self):
        self.status.emit(f'Downloading {self.url}')
        self.yt = YouTube(
            self.url,
            on_progress_callback=self.progress_callback
        ).streams.get_highest_resolution()
        self.yt.download()
        self.progress.emit(1000)
        self.status.emit(f'Done: {self.yt.title}')
        self.finished.emit()

    def progress_callback(self, stream, _, remain):
        complete = stream.filesize - remain
        val = int(complete / stream.filesize * 1000)
        self.progress.emit(val)

def main():
    app = wg.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
