# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_all

datas = []
binaries = []
hiddenimports = ['gettext']
tmp_ret = collect_all('gettext')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['describealign.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [('v', None, 'OPTION')],
    exclude_binaries=True,
    name='describealign',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['describealign.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='describealign',
)

extra = {}
version = os.getenv('APP_VERSION')
if version:
    extra['version'] = version

app = BUNDLE(
    coll,
    name='describealign.app',
    icon='describealign.png',
    bundle_identifier=None,
    **extra,
)
