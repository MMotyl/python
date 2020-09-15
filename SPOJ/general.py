import sys

def main():
    for line in sys.stdin.readlines()[1:]:
        if line.strip():
            num = int(line)
            result = num * num - 1
sys.stdout.write('%d\n' % result)

if name == 'main':
    main()



sys.stdout.write()
sys.stdin.readline()
