pyinstaller doc_templating\ContractGenerator.py ^
  -p doc_templating ^
  --collect-submodules doc_templating ^
  --add-data doc_templating\templates:doc_templating\templates ^
  --add-data doc_templating\static:doc_templating\static ^
  -y