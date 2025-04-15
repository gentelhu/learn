import requests


def download_exe(url, save_path):
    try:
        # 发送请求获取响应
        response = requests.get(url, stream=True)
        # 检查响应状态码
        response.raise_for_status()

        # 以二进制写入模式打开文件
        with open(save_path, 'wb') as file:
            # 遍历响应内容，分块写入文件
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        print(f"文件已成功下载到 {save_path}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 错误发生: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"请求发生错误: {req_err}")
    except Exception as e:
        print(f"发生未知错误: {e}")


if __name__ == "__main__":
    # 替换为实际的 exe 文件下载链接
    exe_url = "https://8a4fd1-704917774.antpcdn.com:19001/b/pkg-ant.baidu.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.54.0.103.exe"
    # 替换为你想要保存的路径和文件名
    save_file_path = "F:/gentel/learn/other/tool/baidunetdisk.exe"
    download_exe(exe_url, save_file_path)
