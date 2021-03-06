AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
CCDEFINES_CAIRO = ['_REENTRANT']
CCFLAGS = ['-g', '-O3', '-Wall', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE']
CCFLAGS_MACBUNDLE = ['-fPIC']
CCFLAGS_NODE = ['-D_LARGEFILE_SOURCE', '-D_FILE_OFFSET_BITS=64']
CC_VERSION = ('4', '2', '1')
COMPILER_CXX = 'g++'
CPP = '/usr/bin/cpp'
CPPFLAGS = ['-DNDEBUG']
CPPFLAGS_NODE = ['-D_GNU_SOURCE']
CPPPATH_CAIRO = ['/opt/local/include/cairo', '/opt/local/include/glib-2.0', '/opt/local/lib/glib-2.0/include', '/opt/local/include', '/opt/local/include/pixman-1', '/opt/local/include/freetype2', '/opt/local/include/libpng14']
CPPPATH_NODE = '/usr/local/include/node'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES_CAIRO = ['_REENTRANT']
CXXDEFINES_ST = '-D%s'
CXXFLAGS = ['-g', '-O3', '-Wall', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE']
CXXFLAGS_DEBUG = ['-g']
CXXFLAGS_NODE = ['-D_LARGEFILE_SOURCE', '-D_FILE_OFFSET_BITS=64']
CXXFLAGS_RELEASE = ['-O2']
CXXLNK_SRC_F = ''
CXXLNK_TGT_F = ['-o', '']
CXX_NAME = 'gcc'
CXX_SRC_F = ''
CXX_TGT_F = ['-c', '-o', '']
DEST_CPU = 'x86_64'
DEST_OS = 'darwin'
FULLSTATIC_MARKER = '-static'
HAVE_CAIRO = 1
LIBDIR = '/Users/yair/.node_libraries'
LIBPATH_CAIRO = ['/opt/local/lib']
LIBPATH_NODE = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_CAIRO = ['cairo']
LIB_ST = '-l%s'
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINK_CXX = ['/usr/bin/g++']
NODE_PATH = '/Users/yair/.node_libraries'
PREFIX = '/usr/local'
PREFIX_NODE = '/usr/local'
RANLIB = '/usr/bin/ranlib'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = ''
SONAME_ST = ''
STATICLIBPATH_ST = '-L%s'
STATICLIB_MARKER = ''
STATICLIB_ST = '-l%s'
USE_PROFILING = False
defines = {'HAVE_CAIRO': 1}
macbundle_PATTERN = '%s.bundle'
program_PATTERN = '%s'
shlib_CXXFLAGS = ['-fPIC', '-compatibility_version', '1', '-current_version', '1']
shlib_LINKFLAGS = ['-dynamiclib']
shlib_PATTERN = 'lib%s.dylib'
staticlib_LINKFLAGS = []
staticlib_PATTERN = 'lib%s.a'
