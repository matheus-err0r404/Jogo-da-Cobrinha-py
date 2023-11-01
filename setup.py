import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="Jogo Da Cobrinha",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['sons']}},

    executables = executables
    
)