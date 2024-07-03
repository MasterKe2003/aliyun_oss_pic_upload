# aliyun_oss_pic_upload

这个项目是一个使用 Flask 框架构建的简单应用程序，可以上传文件到阿里云 OSS。
## 功能
- 上传文件到阿里云 OSS
- 生成新的文件名，确保月份和日期以两位数字显示
- 显示上传进度
- 返回上传成功后的文件 URL
## 本地安装
1. 克隆项目到本地
2. 创建虚拟环境并激活
3. 安装依赖项：`pip install -r requirements.txt`
## 配置
1. 在环境变量中设置以下值：
   - `ACCESS_KEY_ID`：阿里云 OSS 的 Access Key ID
   - `ACCESS_KEY_SECRET`：阿里云 OSS 的 Access Key Secret
   - `ENDPOINT`：阿里云 OSS 的 Endpoint
   - `BUCKET_NAME`：阿里云 OSS 的 Bucket 名称
## 运行
1. 在项目根目录下，运行 `python index.py` 或 `flask run` 启动应用程序。
2. 打开浏览器，访问 `http://localhost:5000/upload` 上传文件。
## 部署到 Vercel
1. 准备项目：确保 Flask 应用可运行，创建 `requirements.txt` 和 `vercel.json` 配置文件。
2. 在 Vercel 上创建项目并使用 GitHub、GitLab 或 Bitbucket 账户登录。
3. 导入项目仓库，并配置项目选项，如环境变量。
4. 部署项目：点击“Deploy”按钮，Vercel 将自动构建并部署您的 Flask 应用。
5. 验证部署：访问 Vercel 提供的公开 URL，验证 Flask 应用是否正常运行。
