#encoding : utf-8
def main():
    f = None
    try:
        f = open('lunyu.txt', 'r',encoding='utf-8')
        print(f.read())
    # except FileNotFoundError:
    except LookupError:
        print('123!')
    except UnicodeDecodeError:
        print('123!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
