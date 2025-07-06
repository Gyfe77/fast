from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return 'Hello world'

def main():
    print('Мы тут')


if __name__ == '__main__':
    main()