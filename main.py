import json

from creatorsmarkets import CreatorsMarkets

if __name__ == "__main__":
    client = CreatorsMarkets()
    #ここにクリエイターID
    client.creator_id = ""
    #Cookieの値を入れる
    client.xsrf_token = ''
    client.cookies = {
        '_ldbrbid': '',
        '__is_login_sso': '1',
        'hss_session': '',
        'XSRF-TOKEN': client.xsrf_token,
    }

    # sticker_idを発行する
    requ = client.create_sticker_data("english_stickers", "This is english sticker.", "日本語のスタンプ名", "このスタンプは日本語のスタンプです", "@copyright")
    res = json.loads(requ)

    # 発行されたsticker_id
    sticker_id = res["sticker_id"]

    # スタンプ画像のアップロード
    print(client.upload_sticker_img(sticker_id, "01", "./01.png"))
