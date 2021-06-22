import sys
import threading
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
        self.ui.input_url.setEnabled(False)
        self.ui.progressBar.setValue(0)
        url = self.ui.input_url.text()
        t = threading.Thread(target=self.download, args=(url,))
        t.start()

    def download(self, url):
        self.ui.status.setText(f'Downloading {url}')
        self.yt = YouTube(
            url, on_progress_callback=self.yt_progress
        ).streams.get_highest_resolution()
        self.yt.download()
        self.ui.status.setText(f'{url} done!')
        self.ui.input_url.setEnabled(True)

    def yt_progress(self, stream, _, remain):
        complete = stream.filesize - remain
        val = complete / stream.filesize * 100
        self.ui.progressBar.setValue(val)

app = wg.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
