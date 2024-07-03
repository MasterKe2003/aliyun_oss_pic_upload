import sys
from flask import Flask, request
import oss2
import time
import os
from datetime import datetime

app = Flask(__name__)

# 使用环境变量获取敏感信息
ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.environ.get('ACCESS_KEY_SECRET')
ENDPOINT = os.environ.get('ENDPOINT')  # 'http://oss-cn-beijing.aliyuncs.com'
BUCKET_NAME = os.environ.get('BUCKET_NAME')  # 'masterke-picture'

auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, ENDPOINT, BUCKET_NAME, connect_timeout=30)

def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()

@app.route('/upload', methods=['POST'])
def upload_files():
    file = request.files.get('file')
    if file:
        file_name = file.filename
        file_format = file_name.split('.')[-1]
        # 生成新的文件名，确保月份和日期以两位数字显示
        now = datetime.now()
        new_file_name = now.strftime("%Y/%m/%d/") + f"{int(time.time())}.{file_format}"
        
        # 保存文件到 Vercel 提供的临时目录
        temp_dir = os.path.join('/tmp', 'uploads')
        file_path = os.path.join(temp_dir, new_file_name.replace('/', os.sep))

        # 创建目标目录（如果不存在）
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            print(f"Will upload {file_name} to the oss!")
            file.save(file_path)  # 保存文件到 Vercel 临时目录
            oss2.resumable_upload(bucket, new_file_name, file_path)
            # 确保 URL 格式正确
            url = f"https://{BUCKET_NAME}.{ENDPOINT.split('//')[1]}/{new_file_name}"
            return {"message": f"Upload successful!", "url": url}, 200
        except Exception as e:
            return {"message": f"Upload failed: {str(e)}"}, 500
        finally:
            # 删除临时保存的文件
            if os.path.exists(file_path):
                os.remove(file_path)
    else:
        return {"message": "No file provided"}, 400

if __name__ == '__main__':
    app.run(debug=True)