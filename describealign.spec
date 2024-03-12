# -*- mode: python ; coding: utf-8 -*-
import os

a = Analysis(
    ['describealign.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['gettext'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='describealign',
    debug=False,
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
