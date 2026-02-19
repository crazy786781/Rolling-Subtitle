# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller打包配置文件
用于将地震预警及情报实况栏程序打包成Windows可执行文件
支持PyQt5 GUI框架
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

# 获取图标文件绝对路径
# PyInstaller执行时，当前工作目录是项目根目录
icon_path = os.path.abspath('logo/icon.ico')
if not os.path.exists(icon_path):
    # 如果找不到，尝试相对于spec文件的位置
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
        # 气象预警信号图片文件夹（必需）
        ('气象预警信号图片', '气象预警信号图片'),
        # 地名修正文件（必需）
        ('fe_fix.txt', '.'),
        # 预警地名修正文件夹（用于USGS和KMA预警消息的地名修正）
        ('预警地名修正', '预警地名修正'),
        # Logo图标文件（必需）
        ('logo/icon.ico', 'logo'),
        # 如果需要包含数据源文档，可以取消注释
        # ('数据源文档', '数据源文档'),
        # 如果需要包含图片，可以取消注释
        # ('图片', '图片'),
        # zoneinfo 时区数据（Windows 需 tzdata 包）
    ] + tzdata_datas,
    hiddenimports=[
        # PyQt5相关模块（主要GUI框架）
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'PyQt5.QtWidgets.QApplication',
        'PyQt5.QtWidgets.QMainWindow',
        'PyQt5.QtWidgets.QWidget',
        'PyQt5.QtWidgets.QVBoxLayout',
        'PyQt5.QtWidgets.QHBoxLayout',
        'PyQt5.QtWidgets.QGridLayout',
        'PyQt5.QtWidgets.QMenu',
        'PyQt5.QtWidgets.QColorDialog',
        'PyQt5.QtWidgets.QLineEdit',
        'PyQt5.QtWidgets.QScrollArea',
        'PyQt5.QtWidgets.QTextEdit',
        'PyQt5.QtWidgets.QMessageBox',
        'PyQt5.QtWidgets.QFrame',
        'PyQt5.QtWidgets.QTabWidget',
        'PyQt5.QtWidgets.QCheckBox',
        'PyQt5.QtWidgets.QSlider',
        'PyQt5.QtWidgets.QSpinBox',
        'PyQt5.QtWidgets.QRadioButton',
        'PyQt5.QtWidgets.QButtonGroup',
        'PyQt5.QtWidgets.QPushButton',
        'PyQt5.QtWidgets.QLabel',
        'PyQt5.QtWidgets.QDialog',
        'PyQt5.QtCore.Qt',
        'PyQt5.QtCore.QTimer',
        'PyQt5.QtCore.QRectF',
        'PyQt5.QtCore.pyqtSignal',
        'PyQt5.QtCore.QTranslator',
        'PyQt5.QtCore.QLocale',
        'PyQt5.QtCore.QUrl',
        'PyQt5.QtGui.QPainter',
        'PyQt5.QtGui.QFont',
        'PyQt5.QtGui.QColor',
        'PyQt5.QtGui.QPixmap',
        'PyQt5.QtGui.QImage',
        'PyQt5.QtGui.QFontMetrics',
        'PyQt5.QtGui.QFontDatabase',
        'PyQt5.QtGui.QDesktopServices',
        'PyQt5.QtGui.QSurfaceFormat',
        'PyQt5.QtGui.QIcon',
        'PyQt5.QtOpenGL',
        'PyQt5.QtOpenGL.QOpenGLWidget',
        'PyQt5.QtGui.QOpenGLContext',
        # 第三方库
        'websockets',
        'websockets.asyncio',
        'websockets.asyncio.connection',
        'websockets.asyncio.client',
        'websockets.asyncio.server',
        'websockets.client',
        'websockets.server',
        'requests',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'PIL.ImageDraw',
        'PIL.ImageFont',
        # 标准库
        'asyncio',
        'asyncio.events',
        'asyncio.streams',
        'threading',
        'queue',
        'json',
        'pathlib',
        'logging',
        'logging.handlers',
        'datetime',
        'time',
        'sys',
        'os',
        're',
        'dataclasses',
        'typing',
        'traceback',
        'io',
        'abc',
        'collections',
        'collections.abc',
        'urllib',
        'urllib.parse',
        'urllib.request',
        'hashlib',
        'random',  # 用于翻译服务生成随机salt
        'subprocess',  # 用于程序重启功能
        'platform',  # 用于检测操作系统（Windows系统GPU信息获取）
        # 项目模块
        'config',
        'adapters',
        'adapters.__init__',
        'adapters.base_adapter',
        'adapters.fanstudio_adapter',
        'adapters.p2pquake_adapter',
        'adapters.p2pquake_tsunami_adapter',
        'adapters.wolfx_adapter',
        'adapters.nied_adapter',
        'data_sources',
        'data_sources.__init__',
        'data_sources.websocket_manager',
        'data_sources.http_polling_manager',
        'gui',
        'gui.__init__',
        'gui.main_window',
        'gui.scrolling_text',
        'gui.message_manager',
        'gui.settings_window',
        'gui.color_manager',
        'utils',
        'utils.__init__',
        'utils.logger',
        'utils.message_processor',
        'utils.translation_service',
        'utils.place_name_fixer',
        'utils.region_name_fixer',
        'utils.timezone_utils',  # 时区转换
        'utils.timezone_names_zh',  # 时区中文显示
        'zoneinfo',  # 标准库时区
        'PyQt5.QtWidgets.QComboBox',  # 时区下拉框
    ] + tzdata_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 排除不需要的模块，减小打包体积
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'pytest',
        'unittest',
        'IPython',
        'jupyter',
        'notebook',
        # 注意：PIL/Pillow已从excludes中移除，因为代码中需要使用它来显示气象预警图片
    ],
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
    name='地震预警及情报实况栏',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 不显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path if icon_path and os.path.exists(icon_path) else None,  # 指定图标文件路径，用于exe文件图标
    uac_admin=False,  # 不需要管理员权限
)
