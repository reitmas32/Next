from src.domain.types.dict_smart_t import DictSmart_t
from src.app.builders.cmake_t import Cmake_t

base_builders = DictSmart_t('NoneValue')


base_builders['cmake'] = Cmake_t()
#base_builders['basic'] = Basic_t()
#base_builders['conan'] = Conan_t()
#base_builders['premake'] = Premake_t()