import requests
import pandas as pd
from tqdm import tqdm


def get_product_comments(product_id, page_num=10):
    comments = []
    base_url = "https://club.jd.com/comment/productPageComments.action"
    params = {
        "productId": product_id,
        "score": 0,
        "sortType": 5,
        "pageSize": 10,
        "isShadowSku": 0,
        "page": 0
    }
    for page in tqdm(range(page_num)):
        params["page"] = page
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('comments'):
                for comment in data['comments']:
                    comment_info = {
                        "用户昵称": comment.get('nickname'),
                        "评价时间": comment.get('creationTime'),
                        "评价内容": comment.get('content'),
                        "评分": comment.get('score')
                    }
                    comments.append(comment_info)
            else:
                break
        else:
            print(f"请求失败，状态码: {response.status_code}")
    df = pd.DataFrame(comments)
    df.to_csv('txt/京东iPad 11英寸 A16芯片2025年款用户评价.txt', index=False, encoding='utf-8-sig')
    print("京东iPad 11英寸 A16芯片2025年款用户评价.txt")


if __name__ == "__main__":
    product_id = "100153760305"
    get_product_comments(product_id)
