import requests

class CreatorsMarkets:
    def create_sticker_data(self, stickers_title_en:str, stickers_description_en:str, stickers_title_ja:str, stickers_description_ja:str, copyright:str):
        headers = {
            'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Origin': 'https://creator.line.me',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            'accept': 'application/json',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': self.xsrf_token,
        }
        json_data = {
            "sticker_type": "static",# static,animation,
            "copyright": f"{copyright}",
            "is_showcased": 1,
            "all_area": 1,
            "use_photo": 0,
            "design_url": "",
            #"categories[]": 5,
            #"categories[]": 21,
            "areas[]": "JP",
            "subscription_participation": 1,
            "request_comment": "",
            "meta[en][title]": f"{stickers_title_en}",
            "meta[en][description]": f"{stickers_description_en}",
            "meta[ja][title]": f"{stickers_title_ja}",
            "meta[ja][description]": f"{stickers_description_ja}",
        }

        response = requests.post(f'https://creator.line.me/my/{self.creator_id}/sticker/create', headers=headers, cookies=self.cookies, data=json_data)
        response = response.text.lstrip(")]}',")
        return response

    def upload_sticker_img(self, sticker_id:str, img_num: str, img_path:str):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ja;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://creator.line.me',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': self.xsrf_token,
        }
        json_data = {
            "type": img_num,
        }
        #POSTするファイルの読込
        files = { "image": open(img_path, 'rb') }
        response = requests.post(f'https://creator.line.me/my/{self.creator_id}/api/sticker/{sticker_id}/upload_image', cookies=self.cookies, data=json_data, headers=headers, files=files)
        return response.text