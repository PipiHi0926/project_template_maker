# cookiecutter-simple-pypackage 使用指南

歡迎使用 `cookiecutter-simple-pypackage`！本指南將幫助您快速且輕鬆地初始化 Python 專案。


## ⭐ 基礎功能
- 建立專案模板，包含README.md, setup.py, setup.cfg等多個架構下檔案
    ```
    # 模板預設
    my_project/
    ├── src/
    │    ├──__init__.py  
    │    └── main_program.py
    ├── tests/
    │    ├──__init__.py  
    │    └── test_example.py
    ├── docs/
    ├── Makefile
    ├── setup.cfg 
    ├── setup.py
    ├── use_example.py  
    ├── .gitignore
    └── README.md
    ```



- 留意，這邊只是小型專案的扁平化模板，大型專案建議可自行定義、調整，以下列出幾種典型方案
    -  主程式放在 `根目錄/src/程式`，可以幫助將程式碼和其他專案資源（如測試、文件等）分開，如本模板

    -  小專案、或者不需要過多複雜組織的情況下，主程式碼可能直接放在專案的根目錄中
        ```
        # 小型扁平化專案
        my_project/
        ├── main_program.py
        ├── tests/
        ├── docs/
        └── README.md
        ```
    -  需要將程式碼打包成庫或模組時，將主程式碼放在 lib/ 資料夾中
        ```
        # 程式碼需要打包成模組
        my_project/
        ├── lib/
        │   └── main_program.py
        ├── tests/
        ├── docs/
        └── README.md
        ```
    - 如果專案包含可執行的腳本或程式，這些腳本通常會放在 bin/ 資料夾中
        ```
        # 包含可執行腳本時
        my_project/
        ├── src/
        │   └── main_program.py
        ├── bin/
        │   └── run_program.sh
        ├── tests/
        ├── docs/
        └── README.md
        ```

- 預先幫你設置好.gitignore，來定義好來一般git管控上的「忽略清單」，即不會上傳至git




## ⭐ 操作方法


### 1. 切至目標路徑

- 開啟終端機(termernal)，切至你要的路徑
```
cd 你的路徑
```

- 或是直接在指定資料夾按下右鍵，選擇「在終端機開啟」

### 2. 從Git複製這個模組

- 在終端機輸入以下，意思是透過git指令，複製(clone)這份git上資訊下來

```
git clone https://github.com/PipiHi0926/project_template_maker.git
```

- 當然，你也可以跳過前面這些步驟，直接從這裡載下來這個檔案


### 3. 在你的環境下載cookiecutter套件 
- 請先確保已安裝 Python ， Python 版本是 3.4 以上會自帶pip指令

```
pip install cookiecutter
```
### 4. 使用我的檔案模板 (當然你也能用別的)
- 請確認剛剛載的檔案在目標路徑

- 目標路徑執行以下命令，生成模板

- 接下來會跳資訊，輸入你要的設定

```
cookiecutter project_template_maker
```

### 5. 根據提示輸入設定
#### 🔹 [1/3] project_name (Project_Name):

- 輸入專案名稱

#### 🔹 [2/3] project_slug (剛剛輸入的名稱):

- 輸入描述項目的簡短、可讀的字符串

- 若直接按enter，預設project_slug會與project_name相同

#### 🔹 [3/3] version (0.1.0):

- 輸入專案版本

### 6. 完成!!!



## ⭐ Makefile 目標及功能

這個 `Makefile` 提供了多個目標來管理和維護 Python 專案。以下是每個目標的功能及使用方法：

### `help`
顯示 `Makefile` 中所有可用目標的說明。
- **使用方法**：`make help`
- **功能**：打印出所有目標及其簡短說明。

### `clean`
移除所有構建、測試、覆蓋和 Python 檔案。
- **使用方法**：`make clean`
- **功能**：調用 `clean-build`、`clean-pyc` 和 `clean-test` 目標。

### `clean-build`
移除構建產物。
- **使用方法**：`make clean-build`
- **功能**：刪除 `build/` 目錄和 `.eggs/` 目錄，還有所有 `*.egg-info` 和 `*.egg` 檔案。

### `clean-pyc`
移除 Python 檔案產物。
- **使用方法**：`make clean-pyc`
- **功能**：刪除所有 `.pyc`、`.pyo` 檔案和 `__pycache__` 目錄。

### `clean-test`
移除測試和覆蓋產物。
- **使用方法**：`make clean-test`
- **功能**：刪除 `.coverage` 檔案和 `htmlcov/` 目錄以及 `.pytest_cache` 目錄。

### `lint`
使用 `black` 進行代碼格式化檢查。
- **使用方法**：`make lint`
- **功能**：檢查專案代碼風格，這裡用的是 `black` 工具。

### `test`
使用 `pytest` 執行測試。
- **使用方法**：`make test`
- **功能**：運行測試並顯示結果。

### `coverage`
檢查代碼覆蓋率。
- **使用方法**：`make coverage`
- **功能**：執行測試，生成覆蓋報告，並在瀏覽器中顯示報告。

### `install`
安裝專案到當前 Python 環境的 `site-packages`。
- **使用方法**：`make install`
- **功能**：清理之前的安裝，然後重新安裝當前專案。

### `patch`
更新版本號的修補版。
- **使用方法**：`make patch`
- **功能**：使用 `bump2version` 工具更新版本號的修補版。

### `minor`
更新版本號的小版本。
- **使用方法**：`make minor`
- **功能**：使用 `bump2version` 工具更新版本號的小版本。

### `major`
更新版本號的大版本。
- **使用方法**：`make major`
- **功能**：使用 `bump2version` 工具更新版本號的大版本。

### `release-patch`
發布修補版。
- **使用方法**：`make release-patch`
- **功能**：更新版本號為修補版，並推送更改和標籤到 Git。

### `release-minor`
發布小版本。
- **使用方法**：`make release-minor`
- **功能**：更新版本號為小版本，並推送更改和標籤到 Git。

### `release-major`
發布大版本。
- **使用方法**：`make release-major`
- **功能**：更新版本號為大版本，並推送更改和標籤到 Git。

### `release-tags`
推送所有更改和標籤到 Git。
- **使用方法**：`make release-tags`
- **功能**：推送所有本地提交和標籤到遠程 Git 倉庫。



----------
#### 以上內容特別感謝 陳宏誠 

