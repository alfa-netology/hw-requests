import requests
import modules.COLORS as COLORS

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    @property
    def _auth_header(self):
        """ заголовок для авторизации """
        return {'Authorization': self.token}

    def _get_upload_link(self, file_name):
        """ получает ссылку для загрузки """
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        params = {'path': file_name}
        response = requests.get(url, headers=self._auth_header, params=params)

        if response.ok:
            print(f"{COLORS.GREEN}Success:{COLORS.WHITE} Link to upload received.")
            return True, response.json()['href']
        else:
            status_code = f"Response code <{response.status_code}>."
            error_message = response.json()['message']
            return False, f"{COLORS.RED}Failure:{COLORS.WHITE} {status_code} {error_message}\n"

    def upload(self, file: str):
        """Метод загруджает файл file на яндекс диск"""
        file_name = file.split('/')[-1]
        status, result = self._get_upload_link(file_name)

        if status is True:
            url = result
            with open(file, encoding='utf-8') as f:
                data = f.read()
            response = requests.put(url, data)

            if response.status_code == 201:
                return f"{COLORS.GREEN}Success:{COLORS.WHITE} " \
                       f"'{file_name}' successfully upload to YaDisk.\n"
            else:
                status_code = f"Response code <{response.status_code}>"
                error_message = response.json()['message']
                return f"{COLORS.RED}Failure:{COLORS.WHITE} {status_code} {error_message}.\n"
        else:
            return result
