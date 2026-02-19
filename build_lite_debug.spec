# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller 调试版打包配置（带控制台）
与 build_lite.spec 相同，仅 console=True、输出 exe 名称不同。
若正式版 exe 无法打开，可用本 spec 打包后在命令行运行，查看控制台报错。
"""

import os
from pathlib import Path

try:
    from PyInstaller.utils.hooks import collect_all
    tzdata_datas, tzdata_binaries, tzdata_hiddenimports = collect_all('tzdata')
except Exception:
    tzdata_datas = []
    tzdata_binaries = []
    tzdata_hiddenimports = []

block_cipher = None

icon_path = os.path.abspath('logo/icon.ico')
if not os.path.exists(icon_path):
    try:
        spec_dir = os.path.dirname(os.path.abspath(SPECPATH if 'SPECPATH' in globals() else __file__))
        icon_path = os.path.join(spec_dir, 'logo', 'icon.ico')
    except Exception:
        icon_path = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=tzdata_binaries,
    datas=[
        ('气象预警信号图片', '气象预警信号图片'),
        ('fe_fix.txt', '.'),
        ('预警地名修正', '预警地名修正'),
        ('logo/icon.ico', 'logo'),
    ] + tzdata_datas,
    hiddenimports=[
        'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets',
        'PyQt5.QtWidgets.QApplication', 'PyQt5.QtWidgets.QMainWindow', 'PyQt5.QtWidgets.QWidget',
        'PyQt5.QtWidgets.QVBoxLayout', 'PyQt5.QtWidgets.QHBoxLayout', 'PyQt5.QtWidgets.QGridLayout',
        'PyQt5.QtWidgets.QMenu', 'PyQt5.QtWidgets.QColorDialog', 'PyQt5.QtWidgets.QLineEdit',
        'PyQt5.QtWidgets.QScrollArea', 'PyQt5.QtWidgets.QTextEdit', 'PyQt5.QtWidgets.QMessageBox',
        'PyQt5.QtWidgets.QFrame', 'PyQt5.QtWidgets.QTabWidget', 'PyQt5.QtWidgets.QCheckBox',
        'PyQt5.QtWidgets.QSlider', 'PyQt5.QtWidgets.QSpinBox', 'PyQt5.QtWidgets.QRadioButton',
        'PyQt5.QtWidgets.QButtonGroup', 'PyQt5.QtWidgets.QPushButton', 'PyQt5.QtWidgets.QLabel',
        'PyQt5.QtWidgets.QDialog', 'PyQt5.QtCore.Qt', 'PyQt5.QtCore.QTimer', 'PyQt5.QtCore.QRectF',
        'PyQt5.QtCore.pyqtSignal', 'PyQt5.QtCore.QTranslator', 'PyQt5.QtCore.QLocale', 'PyQt5.QtCore.QUrl',
        'PyQt5.QtGui.QPainter', 'PyQt5.QtGui.QFont', 'PyQt5.QtGui.QColor', 'PyQt5.QtGui.QPixmap',
        'PyQt5.QtGui.QImage', 'PyQt5.QtGui.QFontMetrics', 'PyQt5.QtGui.QFontDatabase',
        'PyQt5.QtGui.QDesktopServices', 'PyQt5.QtGui.QSurfaceFormat', 'PyQt5.QtGui.QIcon',
        'PyQt5.QtOpenGL', 'PyQt5.QtOpenGL.QOpenGLWidget', 'PyQt5.QtGui.QOpenGLContext',
        'websockets', 'websockets.asyncio', 'websockets.asyncio.connection', 'websockets.asyncio.client',
        'websockets.asyncio.server', 'websockets.client', 'websockets.server',
        'requests', 'PIL', 'PIL.Image', 'PIL.ImageTk', 'PIL.ImageDraw', 'PIL.ImageFont',
        'asyncio', 'asyncio.events', 'asyncio.streams', 'threading', 'queue', 'json', 'pathlib',
        'logging', 'logging.handlers', 'datetime', 'time', 'sys', 'os', 're', 'dataclasses', 'typing',
        'traceback', 'io', 'abc', 'collections', 'collections.abc', 'urllib', 'urllib.parse',
        'urllib.request', 'hashlib', 'random', 'subprocess', 'platform',
        'config', 'adapters', 'adapters.__init__', 'adapters.base_adapter', 'adapters.fanstudio_adapter',
        'adapters.p2pquake_adapter', 'adapters.p2pquake_tsunami_adapter', 'adapters.wolfx_adapter',
        'adapters.nied_adapter', 'data_sources', 'data_sources.__init__', 'data_sources.websocket_manager',
        'data_sources.http_polling_manager', 'gui', 'gui.__init__', 'gui.main_window', 'gui.scrolling_text',
        'gui.message_manager', 'gui.settings_window', 'gui.color_manager', 'utils', 'utils.__init__',
        'utils.logger', 'utils.message_processor', 'utils.translation_service', 'utils.place_name_fixer',
        'utils.region_name_fixer', 'utils.timezone_utils', 'utils.timezone_names_zh', 'zoneinfo',
        'PyQt5.QtWidgets.QComboBox',
    ] + tzdata_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas', 'scipy', 'pytest', 'unittest', 'IPython', 'jupyter', 'notebook'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='地震预警及情报实况栏_调试版',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 调试版：显示控制台，便于查看报错
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path if icon_path and os.path.exists(icon_path) else None,
    uac_admin=False,
)
