# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['smartsheet_inform.py'],
             pathex=['/opt/smartsheet_inform','/opt/smartsheet_inform/venv/python-venv-3.5.2/lib/python3.5/site-packages'],
             binaries=[],
             datas=[
                 ('.env','.'),
             ],
             hiddenimports=['smartsheet.reports'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='smartsheet_inform',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
