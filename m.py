import subprocess
import pkg_resources
import sys

required = {'shodan', 'PySide2', 'asyncio'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import shodan
import ftplib
import asyncio
import json
import os
import time
import threading
import random
import socket
import traceback
#from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
#from PySide2.QtWidgets import *
#from PySide2.QtCore import QFile
#from PySide2 import *
import PySide2
from concurrent.futures import ThreadPoolExecutor, as_completed

from ui_mainwindow import Ui_MainWindow

class MainWindow:
    def __init__(self, parent=None):

        self.exit_event = threading.Event()
        self.cftpcon = {}
        self.config = self.loadConfig()
        app = PySide2.QtWidgets.QApplication(sys.argv)
        self.ex = Ui_MainWindow()
        w = PySide2.QtWidgets.QMainWindow()
        self.ex.setupUi(w)
        w.setWindowTitle("FTPKid | FTP Crawler Instrument")
        w.setWindowIcon(PySide2.QtGui.QIcon(os.getcwd() + "\\icon.png"))
        wi = w.frameGeometry().width()
        he = w.frameGeometry().height()
        w.setFixedSize(wi, he)
        #w.setWindowFlags(w.windowFlags() & PySide2.QtCore.Qt.WindowMaximizeButtonHint)
        w.setWindowFlags(PySide2.QtCore.Qt.WindowCloseButtonHint | PySide2.QtCore.Qt.WindowMinimizeButtonHint)
        self.ex.testButton.setVisible(False)
        
        self.cudir = ''
        self.dlist = {}
        self._stop = threading.Event()

        self.api = shodan.Shodan(self.config['token'])

        self.searchBusy = False
        self.progress = ''
        self.progressmax = ''
        #MAIN
        self.ex.tabWidget.setCurrentIndex(0)
        self.exit_action = PySide2.QtWidgets.QAction('Exit')
        self.exit_action.triggered.connect(self.closeEvent)
        app.aboutToQuit.connect(self.closeEvent)
        #self.ex.QUITButton.clicked.connect(self.saveSettings)
        #SEARCH TAB
        self.ex.testButton.clicked.connect(self.say_hello)
        self.ex.clearnButton.clicked.connect(self.clearHostList)
        self.ex.scanButton.clicked.connect(self.searchHosts)
        self.ex.cityLine.returnPressed.connect(self.searchHosts)
        self.ex.clonesButton.clicked.connect(self.removeClones)
        self.ex.qtHostList.itemDoubleClicked.connect(self.hostsItemClicked)
        self.ex.savehostsButton.clicked.connect(self.uiSaveHostList)
        self.ex.loadhostsButton.clicked.connect(self.uiLoadHostList)
        self.ex.openButton.clicked.connect(self.hostsItemButtonClicked)
        self.ex.validButton.clicked.connect(self.pingHosts)
        self.ex.removeButton.clicked.connect(self.removeItemButtonClicked)
        self.ex.qtHostList.model().rowsInserted.connect(self.countHosts)
        self.ex.qtHostList.model().rowsRemoved.connect(self.countHosts)
        #EXPLORE TAB
        self.ex.ipinputButton.clicked.connect(self.exploreFunction)
        self.ex.qtFileList.itemDoubleClicked.connect(self.exploreDirectory)
        self.ex.refreshButton.clicked.connect(self.refreshJob)
        self.ex.winscpButton.clicked.connect(self.openWinScp)
        self.ex.removesButton.clicked.connect(self.exploreRemoveItem)
        self.ex.favButton.clicked.connect(self.exploreFavItem)
        self.ex.selectInListButton.clicked.connect(self.exploreSelectInList)
        #CONFIG TAB
        self.ex.cfg_cancel.clicked.connect(self.visualConfig)
        self.ex.cfg_apply.clicked.connect(self.uiSaveSettings)
        #HOTKEYS
        #QtWidgets.QShortcut(QtGui.QKeySequence("right"), self.button, self.magic)
        PySide2.QtWidgets.QShortcut(PySide2.QtGui.QKeySequence("Ctrl+S"), w, self.hotkeytest)
        w.show()
        self.visualConfig()
        self.loadSettings()
        self.stopping = False

        if self.config['startup_load_searchlist'].lower() == "true":
            self.uiLoadHostList()

        sys.exit(app.exec_())
    def hotkeytest(self):
        print('?????????????????????????? ???????????????????? ????????????????...')
        self.stopping = True
    def stat(self, text="..."):
        try:
            self.ex.statusBar.showMessage(text)
        except Exception as e:
            print(f'???? ?????????????? ?????????????? ????????????: {e}')
    def hostsItemClicked(self, obj):
        if obj.column() == 0:
            self.ex.curhostLabel.setText('?????????????? ????????: ' + obj.text())
            self.ex.ipinputLine.setText(obj.text())
            self.exploreFunction()
            self.ex.tabWidget.setCurrentIndex(1)
    def removeItemButtonClicked(self):
        print(len(self.ex.qtHostList.selectedItems()))
        for row in self.ex.qtHostList.selectedItems():
            try:
                if row.column() == 0:
                    self.ex.qtHostList.removeRow(row.row())
            except:
                pass #???????? ??????????????????, ???? ???????????????? ???????????? ???? ?????????????? ?????????????? ?????? ???????????????? ????????????
    def hostsItemButtonClicked(self):
        if (len(self.ex.qtHostList.selectedItems())) == 1:
            if self.ex.qtHostList.selectedItems()[0].column() == 0:
                self.ex.curhostLabel.setText('?????????????? ????????: ' + self.ex.qtHostList.selectedItems()[0].text())
                self.exploreFunction(self.ex.qtHostList.selectedItems()[0].text())
                self.ex.tabWidget.setCurrentIndex(1)                
                self.stat('')
            else:
                self.stat('???? ?????????????? ???????????? ???? ???? ?????????????? IP-??????????????!')
        else:
            self.stat('?? ???? ???????? ?????????????? ?????????????????? ???????????? ????????????????????????, ???????? ???????????? ???? ??????????????.')
    def say_hello(self, tr=False):
        if tr==True:
            self.ex.qtHostList.addItems(['???? ????????????????'])
            self.stat('????????????????...')
            #maximum address list is ~50k
            for x in range(50000):
                self.stat(f'????????????????... ({x}) ({random.randint(1,10000)})')
                self.ex.qtHostList.addItems([f'?????????? ?????????? {x}'])
                time.sleep(1)

                if self.exit_event.is_set():break
            self.stat('????????????!')
            self.searchBusy = False
        else:
            if not self.searchBusy:
                self.searchBusy = True
                self.testr = threading.Thread(target=self.say_hello, args=(True,))
                self.testr.daemon = True
                self.testr.start()
            else:
                self.stat('?????????? ???????????? ?????? ????????. ???????????????????? ??????????.')
                self.exit_event.set()
    def countHosts(self):
        self.ex.hostcountLabel.setText(f"???????????????????? ????????????: {self.ex.qtHostList.rowCount()-1}")
        if 'true' in self.config['sort'].lower():
            if 'ascending' in self.config['sorting_order'].lower():
                self.ex.qtHostList.sortItems(int(self.config['sorting_by_column']), PySide2.QtCore.Qt.AscendingOrder)
            else:
                self.ex.qtHostList.sortItems(int(self.config['sorting_by_column']), PySide2.QtCore.Qt.DescendingOrder)
        self.ex.qtHostList.setHorizontalHeaderLabels(['IP-????????????','??????????????','??????????????????'])
        self.ex.qtHostList.horizontalHeader().setVisible(True)
    def removeClonesJob(self):
        c =0
        for i in range(self.ex.qtHostList.rowCount()):
            try:
                for ii in range(self.ex.qtHostList.rowCount()):
                    if self.ex.qtHostList.item(i, 0).text() in self.ex.qtHostList.item(ii, 0).text():
                        if not i == ii:
                            c+=1
                            self.ex.qtHostList.removeRow(i)
            except:
                continue
        self.FreezeControls(True)
        self.stat(f'?????????????? ????????????????????: {c}')
    def removeClones(self):
        self.stat(f'?????????????? ???????????? ???????????? ???? ????????????????????. ?????? ?????????? ???????????? ??????????, ????????????????????, ???????????? ???? ??????????????.')
        self.FreezeControls(False)
        self.cleanjob = threading.Thread(target=self.removeClonesJob)
        self.cleanjob.daemon = True
        self.cleanjob.start()
    def grabShodanJob(self, pages):
        pass
    def searchHostsJob(self, tr=False):
        if tr==True:
            self.stat('????????...')
            #self.FreezeControls(False)
            city = self.ex.cityLine.text()
            pages = self.ex.pagesLine.text()
            pages = int(pages)
            try:
                results = self.api.search(query=f"{self.config['query']} City:{city}", page=pages)
            except Exception as e:
                self.stat(f'?????????????????? ???????????? ?????? ?????????????? ???????????????? ???????????????????? ????????????: {e}')
                print('????????????????')
                print(e)
                if "the search request timed out" in e.args[0].lower():
                    self.searchBusy = False
                    self.FreezeControls(True)
                    print('?????????? ???? ????????????????')
                    self.stat('?????????? ???? ????????????????, ???????????????????? ?????????? ?????? ?????????????? ????????.')
                    return
                self.searchBusy = False
                self.FreezeControls(True)
                return
            i=0
            self.stat(f'???????????????? ???????????????? / {pages}')
            if pages < (1+int(results["total"])/100):
                if self.config['autoclean_searchlist'].lower() == "true":
                    self.clearHostList()
                for page in range(int(self.ex.pagesLineStart.text()), pages):
                    if not self.stopping:
                        self.stat(f'???????????????? ???????????????? {page} / {pages}')
                        print(f'???????????????? ???????????????? {page} / {pages}')
                        try:
                            presults = self.api.search(query=f"{self.config['query']} City:{city}", page=page)
                            for item in presults['matches']:
                                #self.ex.qtHostList.addItem(item['ip_str'])
                                self.ex.qtHostList.insertRow(i)
                                self.ex.qtHostList.setItem(i, 0, PySide2.QtWidgets.QTableWidgetItem(item['ip_str']))
                                self.ex.qtHostList.setItem(i, 2, PySide2.QtWidgets.QTableWidgetItem(item['org']))
                                self.ex.qtHostList.setItem(i, 1, PySide2.QtWidgets.QTableWidgetItem(f"{item['location']['country_code']}:{item['location']['city']}"))
                                i+=1
                        except Exception as e:
                            print(f'?????????????????? ???????????? ?????? ?????????????????? ???????????????? {page}!')
                            print(e)
                            if "the search request timed out" in e.args[0].lower():
                                print('?????????? ???? ????????????????')
                                self.stat('?????????? ???? ????????????????, ???????????????????? ?????????? ?????? ?????????????? ????????.')
                                self.searchBusy = False
                                self.FreezeControls(True)
                                return
                            continue
                    else:
                        print('?????????? ????????????????????.')
                        self.stopping = False
                        self.stat("?????????? ???????????? ?????? ???????????????????? ??????????????????????????.")
                        self.searchBusy = False
                        self.FreezeControls(True)
                        return
            else:
                if self.config['autoclean_searchlist'].lower() == "true":
                    self.clearHostList()
                print(1 + int(results["total"] / 100))
                for page in range(int(self.ex.pagesLineStart.text()), 1 + int(results["total"] / 100)):
                    if not self.stopping:
                        self.stat(f'???????????????? ???????????????? {page} / {(1 + int(results["total"] / 100))}')
                        print(f'???????????????? ???????????????? {page} / {(1 + int(results["total"] / 100))}')
                        try:
                            presults = self.api.search(query=f"{self.config['query']} City:{city}", page=page)
                            for item in presults['matches']:
                                #self.ex.qtHostList.addItem(item['ip_str'])
                                self.ex.qtHostList.insertRow(i)
                                self.ex.qtHostList.setItem(i, 0, PySide2.QtWidgets.QTableWidgetItem(item['ip_str']))
                                self.ex.qtHostList.setItem(i, 2, PySide2.QtWidgets.QTableWidgetItem(item['org']))
                                self.ex.qtHostList.setItem(i, 1, PySide2.QtWidgets.QTableWidgetItem(f"{item['location']['country_code']}:{item['location']['city']}"))
                                i+=1
                        except Exception as e:
                            print(f'?????????????????? ???????????? ?????? ?????????????????? ???????????????? {page}!')
                            print(e)
                            continue
                    else:
                        print('?????????? ????????????????????.')
                        self.stopping = False
                        self.stat("?????????? ???????????? ?????? ???????????????????? ??????????????????????????.")
                        self.searchBusy = False
                        self.FreezeControls(True)
                        return
                time.sleep(2)
            if len(results['matches'])<1:
                self.stat('')
            else:
                print(f'?????????? ???????????? ???????? ?????????????? ?? ????????????: {results["total"]}')
            self.stat(f'???????? ???????????????? {(1 + int(results["total"] / 100))} ?????????????? ???????????? ?? {results["total"]} ????????????')
            time.sleep(1)
            self.FreezeControls(True)
            self.searchBusy = False
        else:
            if not self.searchBusy:
                self.searchBusy = True
                self.testr = threading.Thread(target=self.searchHostsJob, args=(True,))
                self.testr.start()
            else:
                self.stat('?????????????? ???????????? ?????? ????????????????????, ???????????????????? ?????? ??????.')
                self.searchBusy = False
                self.FreezeControls(True)
                return
                #print('Buy.')
    def clearHostList(self):
        self.stat('?????????????? ????????????...')
        if 'true' in self.config['delete_favourites'].lower():
            self.ex.qtHostList.clear()
            self.ex.qtHostList.setHorizontalHeaderLabels(['IP-????????????','??????????????','??????????????????'])
            self.ex.qtHostList.setRowCount(1)
        else:
            protected = []
            for i in range(0, self.ex.qtHostList.rowCount()-1):
                if not self.ex.qtHostList.item(i,0) is None:
                    color = self.ex.qtHostList.item(i,0).backgroundColor()
                    colors = f'{color.red()}#{color.green()}#{color.blue()}'
                    if (not '255#255#255' in colors):
                        protected.append(f'{self.ex.qtHostList.item(i,0).text()};{self.ex.qtHostList.item(i,1).text()};{self.ex.qtHostList.item(i,2).text()}')
            self.ex.qtHostList.clear()
            self.ex.qtHostList.setHorizontalHeaderLabels(['IP-????????????','??????????????','??????????????????'])
            self.ex.qtHostList.setRowCount(1)
            o = 0
            for d in protected:
                dd=d.split(';')
                self.ex.qtHostList.insertRow(o)
                self.ex.qtHostList.setItem(o, 0, PySide2.QtWidgets.QTableWidgetItem(dd[0]))
                self.ex.qtHostList.setItem(o, 1, PySide2.QtWidgets.QTableWidgetItem(dd[1]))
                self.ex.qtHostList.setItem(o, 2, PySide2.QtWidgets.QTableWidgetItem(dd[2]))
                self.ex.qtHostList.item(o, 0).setBackgroundColor(PySide2.QtGui.QColor(255,250,205))
                o+=1
        self.stat('????????????!')
    def FreezeControls(self, state=False):
        # self.ex.qtHostList.setEnabled(state)
        # self.ex.validButton.setEnabled(state)
        # self.ex.clonesButton.setEnabled(state)
        # self.ex.clearnButton.setEnabled(state)
        # self.ex.scanButton.setEnabled(state)
        # self.ex.savehostsButton.setEnabled(state)
        # self.ex.loadhostsButton.setEnabled(state)
        # self.ex.openButton.setEnabled(state)
        self.ex.tabWidget.setEnabled(state)
    def searchHosts(self):
        self.FreezeControls(False)
        self.searchHostsJob()
    def isHostActive(self, ip, port):
        if not self.stopping:
            self.FreezeControls(False)
            self.progress += 1
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(int(self.config['host_timeout']))
            print(f'???????????????????????? ???????? {ip}... ({self.progress} / {self.progressmax})')
            self.stat(f'???????????????????????? ???????? {ip}... ({self.progress} / {self.progressmax})')
            try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                print(f'???????? {ip} ??????????')
                time.sleep(float(self.config['checker_delay']))
                return True
            except Exception as e:
                print(f'?????????????????? ???????????? ?????? ???????????????? {ip} - {e}')
                for i in range(self.ex.qtHostList.rowCount()):
                    try:
                        if self.ex.qtHostList.item(i, 0).text() == ip:
                            #print(i, 'aaa')
                            self.ex.qtHostList.removeRow(i)
                    except Exception as e:
                        print(e.with_traceback())
                #self.ex.qtHostList.removeRow()
                return False
            finally:
                s.close()
        else:
            return
    def checkHost(self, ip, port):
        isHostDead = True
        for i in range(int(self.config['host_check_retries'])):
            if self.isHostActive(ip, port):
                isHostDead = False
                break
            else:
                time.sleep(1)
        if isHostDead:
            print(f'???????? {ip} ??????????')
        return isHostDead
    def checkFolders(self, ip, port):
        if not self.stopping:
            port=int(port)
            thr=random.randint(0,2**24)
            self.FreezeControls(False)
            self.progress+=1
            self.stat(f'?????????????????? {ip} ???? ?????????????? ???????????? ?????????? ({self.progress} / {self.progressmax})')
            self.cftpcon[thr] = ftplib.FTP()
            files = []
            try:
                self.cftpcon[thr].connect(ip, port, timeout=10)
            except Exception as e:
                print(f'?????????????????????? ?? {ip} ???? ???????????????????? ??????????????: {e}')
                traceback.print_exc()
                print('------------')
                for row in range(self.ex.qtHostList.rowCount()):
                    if ip in self.ex.qtHostList.item(row, 0).text():
                        self.ex.qtHostList.removeRow(row)
                return False
            self.cftpcon[thr].encoding='utf-8'
            try:
                self.cftpcon[thr].sendcmd('OPTS UTF8 ON')
            except:
                print(f'?????? ???????????????? {ip} ????????????????????, ?????? ???? ???? ???????????????????????? UTF-8')
            try:
                self.cftpcon[thr].login('anonymous', 'anonymous')
            except Exception as e:
                print(f'?????? ???????????????? {ip} ???? ?????????????? ?? ???????? ????????????????????????')
                for row in range(self.ex.qtHostList.rowCount()):
                    if ip in self.ex.qtHostList.item(row, 0).text():
                        self.ex.qtHostList.removeRow(row)            
                return False
            try:
                files = self.cftpcon[thr].nlst()
            except Exception as e:
                print(f'???????? {ip} ???? ?????? ???????????????????? ?????????? ?? ??????????: {e}')
                traceback.print_exc()
                print('--------')
                for row in range(self.ex.qtHostList.rowCount()):
                    if ip in self.ex.qtHostList.item(row, 0).text():
                        self.ex.qtHostList.removeRow(row)
                return False
            try:
                files.remove('.');files.remove('..')
                #print(f'???????????? ???????????????? ???????????????? ?????????? {ip}')
            except Exception as e:
                # print(f'{e}')
                # traceback.print_exc()
                # print('------')
                pass
            if files == []:
                print(f'???????? {ip} ???????????????? ???????????? - ?? ??????????')
                for row in range(self.ex.qtHostList.rowCount()):
                    if ip in self.ex.qtHostList.item(row, 0).text():
                        self.ex.qtHostList.removeRow(row)
                return False
            else:
                #print(f'?? {ip} ??????????: {files}')
                for f in files:
                    try:
                        try:
                            self.cftpcon[thr].cwd(f)
                        except Exception as e:
                            if 'not a directory' in e.args[0].lower():
                                print(f'???????? {ip} ???????????????? - ???????? ??????????')
                            elif 'denied' in e.args[0].lower():
                                print(f'???????? {ip} ???????????????????????? ???????????????? ?? ????????????????????')
                            else:
                                print(f'?????? ?????????????? ?????????????? ???????????????????? {f} ???? ?????????? {ip} ???????????????? ????????????: {e}')
                                traceback.print_exc()
                                print('-------')
                                return
                        subfiles = self.cftpcon[thr].nlst()
                        try:
                            subfiles.remove('.');subfiles.remove('..')
                        except:pass
                        if not subfiles == []:
                            print(f'?? ???????????? ?????????? {ip} ???????? ??????????!')
                            break
                        else:
                            print(f'?? ???????????? ?????????? {ip} ???????????? ???? ???????????????????? - ?? ??????????.')
                            try:
                                for row in range(self.ex.qtHostList.rowCount()):
                                    if ip in self.ex.qtHostList.item(row, 0).text():
                                        self.ex.qtHostList.removeRow(row) 
                                        break                       
                            except Exception as e:
                                continue
                    except Exception as e:
                        print(e)
                        if 'not a directory' in e.args[0].lower():
                            print(f'???????? {ip} ???????????????? - ???????? ??????????')
                    self.cftpcon[thr].cwd('/')
        else:
            return
    def pingHostsJob(self):
        self.FreezeControls(False)
        if "true" in self.config['validator_ping_hosts'].lower():
            futures = []
            with ThreadPoolExecutor(max_workers=int(self.config['max_checking_threads'])) as executor:
            #with ThreadPoolExecutor(max_workers=int(self.config['max_checking_threads'])) as executor:
                try:
                    self.progress = 0
                    self.progressmax = str(self.ex.qtHostList.rowCount())
                    if self.ex.qtHostList.rowCount() > 0:
                        futures = [executor.submit(self.isHostActive, self.ex.qtHostList.item(i, 0).text(), '21') for i in range(0, self.ex.qtHostList.rowCount()-1)]
                except Exception as e:
                    print(e)
            if not self.stopping:
                print('?????????????? ???????????? ????????????????')
            else:
                print('?????????????? ???????????? ???????????????????? ??????????????????????????')
        if "true" in self.config['validator_check_folders'].lower():

            futures = []
            with ThreadPoolExecutor(max_workers=int(self.config['max_checking_threads'])) as executor:
                try:
                    self.progress = 0
                    self.progressmax = str(self.ex.qtHostList.rowCount())
                    if self.ex.qtHostList.rowCount() > 0:
                        futures = [executor.submit(self.checkFolders, self.ex.qtHostList.item(i, 0).text(), '21') for i in range(0, self.ex.qtHostList.rowCount()-1)]
                except Exception as e:
                    print('?????????????')
                    print(e)
                    print(traceback.print_exc())
                    print('---------')
            self.cftpcon = {}
            if not self.stopping:
                print('???????????????? ?????????? ???????????? ??????????????????')
            else:
                print('???????????????? ?????????? ???????????? ?????????????????????? ??????????????????????????')
            time.sleep(5)
            self.FreezeControls(True)
        self.FreezeControls(True)
        if not self.stopping:
            self.stat('???????????????? ???????????? ??????????????????')
        else:
            self.stat('???????????????? ???????????? ???????????????? ??????????????????????????')
            self.stopping = False
    def pingHosts(self):
        self.removeClones()
        self._pinghostjob = threading.Thread(target=self.pingHostsJob)
        self._pinghostjob.daemon = True
        self._pinghostjob.start()
    def loadConfig(self):
        with open(os.getcwd() + '\\config.json', 'r') as f:
            return json.loads(f.read())
    def exploreDirectory(self, obj):
        #print(obj.text())
        #ip=self.ex.ipinputLine.text()
        print(obj.text())
        self.exploreFunction(True, obj.text())
    def exploreFunction(self, chdir=False, cdir='', checker=False):
        ip=self.ex.ipinputLine.text()
        if not chdir:
            self.stat(f'???????????????????????? ?? {ip}')
            self.ex.curhostLabel.setText(f'?????????????? ????????: {ip} # ????????????????????: \\')
            self.ftpcon = ftplib.FTP()
            #self.ftpcon.set_debuglevel(2)
            files = []
            self.ftpcon.connect(ip, 21, timeout=10)
            self.ftpcon.encoding='utf-8'
            try:
                print('???????????????? ???????????????? UTF-8')
                print(self.ftpcon.sendcmd('OPTS UTF8 ON'))

                pass
            except:
                print(f'{ip} ???? ???????????????????????? UTF-8')
            
            try:
                self.ftpcon.login('anonymous', 'anonymous')
            except Exception as e:
                print(f'???? ?????????????? ????????????????????????: {e}')
                return False

            self.stat('??????????????????.')
            self.ex.qtFileList.clear()
            try:
                self.cudir = self.ftpcon.pwd()
                self.ex.curhostLabel.setText(f'?????????????? ????????: {ip} # ????????????????????: {self.ftpcon.pwd()}')
            except Exception as e:
                print(f'???? ???????????????????? ???????????? ?????? ?????????????? ???????????????????? ?? ??????????: {ip}')
            try:
                files = self.ftpcon.nlst()
                if files == []:
                    print('???????? ????????????')
                else:
                    for f in files:
                        #print(f)
                        self.ex.qtFileList.addItem(f)
            except Exception as e:
                self.stat(f'???????? {ip} ???? ???????? ???????????????? ???????????? ????????????: {e}')
                print(f'???????? {ip} ???? ???????? ???????????????? ???????????? ????????????: {e}')
                traceback.print_exc()
                print('--------')
        else:
            self.ex.qtFileList.clear()
            if not cdir == '[back]':
                try:
                    self.ftpcon.cwd(cdir)
                except Exception as e:
                    print(e)
                    if 'not a directory' in e.args[0].lower():
                        self.stat(f'??????????????????, ?????? {cdir} ???? ???????????????? ??????????????????????.')
            else:
                #print()
                #self.ftpcon.cwd('/' + self.remove_last_word(self.ftpcon.pwd()))
                self.ftpcon.cwd('..')
                #self.ftpcon.cwd(self.ftpcon.pwd().replace('/'+cdir, ''))
            try:
                self.cudir = self.ftpcon.pwd()
                self.ex.curhostLabel.setText(f'?????????????? ????????: {ip} # ????????????????????: {self.ftpcon.pwd()}')
            except Exception as e:
                print(f'???? ???????????????????? ???????????? ?????? ?????????????? ???????????????????? ?? ??????????: {ip}')
            try:
                files = self.ftpcon.nlst()
                self.ex.qtFileList.addItem('[back]')
                if files == []:
                    print('???????????? ??????????')
                else:
                    for f in files:
                        #print(f)
                        self.ex.qtFileList.addItem(f)
            except Exception as e:
                self.stat(f'???????? {ip} ???? ???????? ???????????????? ???????????? ????????????: {e}')
                print(f'???????? {ip} ???? ???????? ???????????????? ???????????? ????????????: {e}')            
    def remove_last_word(self, text):
        return text and '/'.join(word for word in text.split('/')[:-1])
    def refreshJob(self):
        self.stat('')
        self.exploreFunction(chdir=True, cdir=self.ftpcon.pwd())
    def openWinScp(self):
        ip=self.ex.ipinputLine.text()
        cmd = f'start "" "{self.config["winscp_path"]}/WinSCP.exe" ftp://anonymous:anonymous@{ip} /timeout=10 -rawsettings Utf={self.config["utf"]}'
        print(cmd)
        y = threading.Thread(target=os.system, args=(cmd,))
        y.start()
    def exploreSelectInList(self):
        #print(len(self.ex.qtHostList.selectedItems()))
        ip=self.ex.ipinputLine.text()
        for i in range(0, self.ex.qtHostList.rowCount()-1):
            try:
                if ip in self.ex.qtHostList.item(i, 0).text():
                    self.ex.qtHostList.clearSelection()
                    self.ex.qtHostList.item(i,0).setSelected(True)
                    self.ex.qtHostList.scrollToItem(self.ex.qtHostList.item(i,0), PySide2.QtWidgets.QAbstractItemView.PositionAtCenter)
            except Exception as e:
                print(e)
                pass #???????? ??????????????????
        self.ex.tabWidget.setCurrentIndex(0)
        pass
    def exploreRemoveItem(self):
        #print(len(self.ex.qtHostList.selectedItems()))
        ip=self.ex.ipinputLine.text()
        for i in range(0, self.ex.qtHostList.rowCount()-1):
            try:
                if ip in self.ex.qtHostList.item(i, 0).text():
                    self.ex.qtHostList.removeRow(i)
            except:
                pass #???????? ??????????????????, ???? ???????????????? ???????????? ???? ?????????????? ?????????????? ?????? ???????????????? ???????????? 
        self.ex.tabWidget.setCurrentIndex(0)
        self.ex.ipinputLine.setText('0.0.0.0')
        self.ex.curhostLabel.setText('?????????????? ????????: 0.0.0.0')
        self.ex.qtFileList.clear()
        self.cudir = ''
        pass
        #removesButton
    def exploreFavItem(self):
        ip=self.ex.ipinputLine.text()
        for row in self.ex.qtHostList.selectedItems():
            try:
                if row.column() == 0:
                    if ip in row.text():
                        color = self.ex.qtHostList.item(row.row(), 0).backgroundColor()
                        colors = f'{color.red()},{color.green()},{color.blue()}'
                        print(colors)
                        if not '255,250,205' in colors:
                            self.ex.qtHostList.item(row.row(), 0).setBackgroundColor(PySide2.QtGui.QColor(255,250,205))
                            self.stat(f'{ip} ?????????????????? ?? ?????????????????? ??????????')
                        else:
                            self.ex.qtHostList.item(row.row(), 0).setBackgroundColor(PySide2.QtGui.QColor(255,255,255))
                            self.stat(f'{ip} ???????????? ???? ?????????????????? ????????????')
            except:
                pass #???????? ??????????????????, ???? ???????????????? ???????????? ???? ?????????????? ?????????????? ?????? ???????????????? ????????????         
    def visualConfig(self):
        #Preparing config window
        self.ex.cfgList.setRowCount(len(self.config))
        self.ex.cfgList.setHorizontalHeaderLabels(['????????????????', '????????????????'])
        i=0
        for cfgitem in self.config:
            self.ex.cfgList.setRowHeight(i, 2)
            self.ex.cfgList.setItem(i,0,PySide2.QtWidgets.QTableWidgetItem(str(cfgitem)))
            self.ex.cfgList.setItem(i,1,PySide2.QtWidgets.QTableWidgetItem(str(self.config[cfgitem])))
            i+=1
    def loadSettings(self):
        #self.config['last_city']
        #self.config['pages']
        self.ex.cityLine.setText(self.config['last_city'])
        self.ex.pagesLine.setText(str(self.config['pages']))
        self.ex.pagesLineStart.setText(str(self.config['pages_start']))
    def saveSettings(self):
        print('Saving settings...')
        #self.config['token'] = self.ex.cfgList.
        self.config['last_city'] = self.ex.cityLine.text()
        self.config['pages'] = int(self.ex.pagesLine.text())
        self.config['pages_start'] = int(self.ex.pagesLineStart.text())

        with open(os.getcwd() + '\\config.json', 'w') as f:
            json.dump(self.config, f)
    def uiSaveSettings(self):
        for row in range(self.ex.cfgList.rowCount()):
            #print(self.config[self.ex.cfgList.item(row, 0).text()], ' + ', self.ex.cfgList.item(row, 1).text())
            self.config[self.ex.cfgList.item(row, 0).text()] = self.ex.cfgList.item(row, 1).text()
        #print(self.config)
        self.saveSettings()
        self.config = self.loadConfig()
        #print(self.config)
        self.visualConfig()
        self.loadSettings()
        self.api = shodan.Shodan(self.config['token'])
        self.countHosts()
    def uiSaveHostList(self):
        self.dlist = {}
        for row in range(self.ex.qtHostList.rowCount()):
            try:
                color = self.ex.qtHostList.item(row,0).backgroundColor()
                self.dlist[row] = f'{self.ex.qtHostList.item(row, 0).text()};{self.ex.qtHostList.item(row, 1).text()};{self.ex.qtHostList.item(row, 2).text()};{color.red()}#{color.green()}#{color.blue()}'
            except:
                continue
        with open(os.getcwd() + '\\list.json', 'w') as f:
            json.dump(self.dlist, f)
    def uiLoadHostList(self):
        with open(os.getcwd() + '\\list.json', 'r') as f:
            self.dlist = json.loads(f.read())
        #print(self.dlist)
        self.ex.qtHostList.clear()
        self.ex.qtHostList.setRowCount(1)
        for item in self.dlist:
            iii = self.dlist[item].split(';')
            self.ex.qtHostList.insertRow(int(item))
            self.ex.qtHostList.setItem(int(item), 0, PySide2.QtWidgets.QTableWidgetItem(iii[0]))
            self.ex.qtHostList.setItem(int(item), 1, PySide2.QtWidgets.QTableWidgetItem(iii[1]))
            self.ex.qtHostList.setItem(int(item), 2, PySide2.QtWidgets.QTableWidgetItem(iii[2]))
            if len(iii) > 3:
                color = iii[3].split('#')
                r=int(color[0])
                g=int(color[1])
                b=int(color[2])
                if not iii[3] == '0#0#0':
                    self.ex.qtHostList.item(int(item), 0).setBackgroundColor(PySide2.QtGui.QColor(r,g,b))
                else:
                    self.ex.qtHostList.item(int(item), 0).setBackgroundColor(PySide2.QtGui.QColor(255,255,255))
    def closeEvent(self):
        print('Someone closing me! Saving and exiting...')
        self.saveSettings()


if __name__=="__main__":
    try:
        MainWindow()
    except Exception as e:
        print('???????? ??????????: ')
        print(e)
        traceback.print_exc()
    print("???? ?? ???????? ?????? ????????????????????")