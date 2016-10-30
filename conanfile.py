from conans import ConanFile, CMake

class EntityX(ConanFile):
    name = 'EntityX'
    version = '1.2.0'
    settings = 'os', 'compiler', 'build_type', 'arch'
    url = 'https://github.com/alecthomas/entityx'
    license = 'MIT'

    def source(self):
    	self.run('git clone https://github.com/alecthomas/entityx.git')
    	self.run('cd entityx && git checkout tags/{}'.format(self.version))

    def build(self):
    	cmake = CMake(self.settings)
    	args = []
    	args += ['-DCMAKE_INSTALL_PREFIX=install']

    	self.run('cmake {}/entityx {}'.format(
    		self.conanfile_directory, cmake.command_line
    	))
    	self.run('cmake --build . --target install {}'.format(cmake.build_config))

    def package(self):
        self.copy('*.h', dst='include/entityx', src='entityx/entityx')
        self.copy('*.dylib', dst='lib', src='.')  # OSX

    def package_info(self):
    	self.cpp_info.libs=['entityx']
