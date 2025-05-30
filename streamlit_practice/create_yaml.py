import csv
import yaml
from streamlit_authenticator.utilities.hasher import Hasher

users_csv_path = "streamlit_practice/user_info.csv"
config_yaml_path = "streamlit_practice/config.yaml"

hasher = Hasher()

## ユーザー設定の一覧が記述されたデータを読み込み
with open(users_csv_path, "r") as f:
    csvreader = csv.DictReader(f)
    users = list(csvreader)

## yaml 設定一覧が記述されたデータを読み込み
with open(config_yaml_path,"r") as f:
    yaml_data = yaml.safe_load(f)

## パスワードのハッシュ化
users_dict = {}
for user in users:
    user["password"] = hasher.hash(user["password"])
    users_dict[user["id"]] = {
        "name": user["name"],
        "password": user["password"],
        "email": user["email"],
    }

## yaml 書き込み
yaml_data["credentials"]["usernames"] = users_dict
with open(config_yaml_path, "w") as f:
    yaml.dump(yaml_data, f)
    print("完了")