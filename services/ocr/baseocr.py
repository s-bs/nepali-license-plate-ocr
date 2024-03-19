from abc import ABC, abstractmethod

class BaseOCR(ABC):
    @abstractmethod
    def extract_text(self,image_path):
        raise NotImplementedError