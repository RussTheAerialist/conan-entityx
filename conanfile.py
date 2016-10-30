from conans import ConanFile, CMake

class EntityX(ConanFile):
    name = 'EntityX'
    version = '1.2.0'
    settings = 'os', 'compiler', 'build_type', 'arch'

    def source(self):
    	self.run('git clone https://github.com/alecthomas/entityx.git')

    def build(self):
    	cmake = CMake(self.settings)
    	args = []
    	args += ['-DCMAKE_INSTALL_PREFIX="{}"'.format(self.package_folder)]

    	self.run('cmake {}/entityx {}'.format(
    		self.conanfile_directory, cmake.command_line
    	))
    	self.run('cmake --build . --target install {}'.format(cmake.build_config))

    def package(self):
        self.copy('*.h', dst='include', src=self.packge_folder)
        self.copy('*.*lib', dst='lib', src=self.packge_folder)
        self.copy('*.*a', dst='lib', src=self.packge_folder)

    def package_info(self):
    	pass  # Not sure what to do here
