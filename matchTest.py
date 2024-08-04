args = ['acc','hello.c','world.c']
match args:
    case ['acc']:
        print('gcc:missing source files.')
    case ['acc',file1,*files]:
        print('gcc compiled: '+file1+','+','.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')