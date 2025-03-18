import requests;
class Teste:
    def __init__(self:object, name:str) -> None:
        self.name = name;
        pass;
    def rename(self:object) -> str:
        newName = input("Digite o novo nome: ");
        print(self.name, newName, sep="\n");
        pass;
    pass;
if __name__ == "__main__":
    newObject = Teste("NameFantasy");
    newObject.rename();
