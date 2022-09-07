from dataclasses import dataclass

if __name__ == '__main__':


    r = [1]

    d = r if len(r) > 1 else r + ['']

    print(d)

