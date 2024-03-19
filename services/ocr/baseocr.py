from abc import ABC, abstractmethod

class BaseOCR(ABC):
    @abstractmethod
    def extract_text(self,image_path):
        raise NotImplementedError
    @abstractmethod
    def resize_image(self,image_path):
        raise NotImplementedError
    @abstractmethod
    def image_contrast(self,image_path):
        raise NotImplementedError
    @abstractmethod
    def image_binary(self,image_path):
        raise NotImplementedError