#базовое исключение для всех ошибок
class AppException(Exception):
    def __init__(self, message="Базовое исключение"):
        super().__init__(message)

#специфичные исключения
class BadRequestException(AppException):
    def __init__(self, response, message="Запрос вернул не 200 статус код"):
        super().__init__(message)
        self.response = response
    
    def __str__(self):
        base_message = super().__str__()
        if self.response:
            base_message += f"\n{self.response.request.method} URL: {self.response.request.url}"
            base_message += f"\nStatus code: {self.response.status_code}"
            base_message += f"\nResponse body: {self.response.text}"
        return base_message




