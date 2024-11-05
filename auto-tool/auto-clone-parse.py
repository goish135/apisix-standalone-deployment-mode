"""
pip install gitpython
pip install pyyaml 
python3 auto-clone-parse.py
"""
import git
import os
import yaml

def clone_and_parse(repo_url, file_path, branch_name='main'):
    
    repo_name = repo_url.split('/')[-1].split('.')[0]  
    print('repo_name:',repo_name)
    file_full_path = os.path.join(repo_name, file_path)
    repo_path = os.path.join(os.getcwd(), repo_name)
    print('repo_path:',repo_path)
    

    if os.path.exists(file_full_path):
        repo_path = os.path.join(os.getcwd(), repo_name)
        repo = git.Repo(repo_path)
        print(f"警告：目錄 {file_full_path} 已存在，將覆蓋！")          
        if repo.is_dirty():        
            repo.git.stash()
            origin = repo.remote('origin')
            origin.pull(branch_name)
                       
    else:
        git.Repo.clone_from(repo_url, repo_name,branch=branch_name)
        repo = git.Repo(repo_path) 
        repo.git.checkout(branch_name)


    # 檢查檔案是否存在
    if not os.path.exists(file_full_path):
        print(f"檔案 {file_full_path} 不存在")
        return

    # 讀取檔案內容
    with open(file_full_path, 'r') as f:
        file_content = f.read()

    return file_content

# 指定要克隆的 repo 和解析的檔案
repo_url = "https://github.com/goish135/apisix-standalone-deployment-mode"
file_path = "apisix/apisix.yml"  # 請替換為實際的檔案路徑

# 呼叫函數並解析檔案內容
file_content = clone_and_parse(repo_url, file_path)
# 處理解析後的內容 (解析 YAML)
if file_content:
    try:
        data = yaml.safe_load(file_content)
        print(data)  
        print("---\n")
        print('upstream name:',data['upstreams'][0]['name'])
        print('upstream nodes:',data['upstreams'][0]['nodes'])
        print('upstream nodes:',data['routes'][0]['uri'])
        print('downstream consumer:',data['consumers'][0]['username'])
    except yaml.YAMLError as exc:
        print(f'YAML 解析錯誤: {exc}')  