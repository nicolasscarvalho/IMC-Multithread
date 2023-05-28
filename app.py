class App():

    """
    user interface and functionalities for the IMC, TMB and QL
    """



    def __init__(self):

        # showing the app header 
        App.title("The shape of us! \n")
        print("=> Informe alguns dados para começar: \n")
        App.generate_header()
    

    # padding generator 
    @classmethod
    def padding(cls):
        print("\n\n")




    # header generator to guide user in entering data
    @classmethod
    def generate_header(cls):
        print("OBS: O Nivel de atividade varia de 1 (Sedentário) a 4 (Muito Ativo) !")
        print("Ex: {:^8s} {:^22s} {:^14s} {:^20s} {:^10s} \n".format("1.70", "70.0", "M", "3", "20"))




    # row of "*" 
    @classmethod
    def row(cls):
        print(f"\n{'*' * 81}\n")




    # row line generator 
    @classmethod
    def row_table(cls):
        print(f"+{'-' * 25}++{'-' * 25}++{'-' * 25}+")




    # title generator 
    @classmethod
    def title(cls, title):
        App.row()
        print('*{:^79s}*'.format(title))
        App.row()




    # collects user data
    @classmethod
    def collect_user_data(cls):

        print("{:^16s} {:^18s} {:^18s} {:^18s} {:^16s}".format("Altura (m):", "Peso (Kg):", "Sexo (M/F):", "Nvl de Ativ:", "Idade :"))
        
        user_data = input("").split(" ")

        App.row()

        return user_data




    # turns user data into a list type
    @classmethod
    def list_user_data(cls, values):
        list = []
        for i in values:
            if i != "":
                if (i in "Mm" or i in "Ff"):
                    list.append(i)
                else:
                    list.append(float(i))
        return list




    # validade the user data
    @classmethod
    def validate_data(cls, values):
        while True:

            # tries to turn user data into a dict
            try:
                list = App.list_user_data(values)
                user_data = App.generate_dict(list)

            # returns to collect user data if there are insufficient values
            except IndexError:
                print('\nPreencha todos os dados para prosseguir!\n'.upper())
                App.generate_header()
                values = App.collect_user_data()

            # returns to collect user data if there are incorrect value types
            except ValueError:
                print('\nValor inválido!\n'.upper())
                App.generate_header()
                values = App.collect_user_data()

            # keeps user data in a list type
            else:
                print('\nAlgum erro ocorreu!\n'.upper())
                list = App.list_user_data(values)
                break

        return list




    # turns a list into a dict
    @classmethod
    def generate_dict(cls, list):
        dic = {'altura': None, 'peso': None, 'sexo': None, 'nvlAtiv': None, 'idade': None}

        cont = 0
        for k, v in dic.items():
            dic[k] = list[cont]
            cont += 1

        return dic




    # show the calculation result
    @classmethod
    def print_result(cls, list):
        print()
        App.row()
        print('|{:^25s}||{:^25s}||{:^25s}|'.format(str(list[0][0]), str(list[0][1]), str(list[0][2])))
        App.row()




    # shows the result for IMC
    @classmethod
    def create_table_imc(cls, imc, status):
        content = [['Tabela de IMC', 'Intervalo', ' Status'],
                   ['Menos do que: ', '18,5', 'Abaixo do Peso !'],
                   ['Entre: ', '18,5 e 24,9', 'Peso Normal!'],
                   ['Entre: ', '25,0 e 29,9', 'Sobrepeso!'],
                   ['Entre: ', '30,0 e 34,9', 'Obesidade Grau 1!'],
                   ['Entre: ', '35,0 e 39,9', 'Obesidade Grau 2!'],
                   ['Mais do que: ', '40,0', 'Obesidade Grau 3!'],
                   ]

        # store the result for user IMC
        result = [['SEU IMC: ', str(imc), status]]
        print()

        # shows the IMC reference table 
        for row_index, row_content in enumerate(content):
            App.row_table()
            print('|{:^25s}||{:^25s}||{:^25s}|'.format( row_content[0], row_content[1], row_content[2]) )
            
        # prints the result for user values
        App.row_table()
        App.print_result(result)




    # shows de reference table for amount of calories
    @classmethod
    def create_table_qtd_cal(cls, dict):
        content = [
            ["Carboidratos: ", dict["carboidratos"], round(float((dict["carboidratos"])) / 4.0, 2)],
            ["Proteínas: ", dict["proteinas"], round(float((dict["proteinas"])) / 4.0, 2)],
            ["Gorduras", dict["gorduras"], round(float((dict["gorduras"])) / 9.0, 2)]
        ]

        for row in range(0, len(content)):
            App.row_table()
            print('|{:^25}||{:^25}||{:^25}|'.format(str(content[row][0]), str(content[row][1]) + " kcal", str(content[row][2]) + " g"))
            App.row_table()




    # manages the user choices: IMC, TBM, QTD KCAL and QUIT of the app
    @classmethod
    def menu(cls, response):
        while True:

            
            # get the user choice
            App.padding()
            print("=> Selecione uma opção: \n")
            print('{:^16s}{:^18s}{:^18s}{:^18s}{:2s}'.format("1 - IMC", "2 - TMB", "3 -  QTD KCAL", "4 - SAIR", ""), end="\t")
            
            opt = input()
            App.padding()




            # if opt == 1, the IMC is calculated and displayed
            if opt == "1":
                App.title("IMC")

                print("\n{:^81s}".format("O Indice de Massa Corporal (IMC) é um parâmetro"))
                print("{:^81s}".format("utilizado para saber se o peso está de acordo com a altura de um"))
                print("{:^81s}".format("indivíduo, o que pode interferir diretamente na sua saúde e qualidade de vida!"))

                App.create_table_imc(response["imc"], response["statusImc"])




            # if opt == 2, the TMB is calculated and displayed
            elif opt == "2":
                App.title("Taxa Metabólica Basal: ")

                print("\n{:^81s}".format("A Taxa de Metabolismo Basal (TMB) é a quantidade"))
                print("{:^81s}".format("mínima de energia (calorias) necessária para manter as"))
                print("{:^81s}".format("funções vitais do organismo em repouso. Essa taxa pode variar"))
                print("{:^81s}".format("de acordo com o sexo, peso, altura, idade e nível de atividade física."))

                result = [['RESULTADO :', 'SUA TMB:', str(response['tmb']) + " kcal"]]
                
                App.print_result(result)




            # if opt == 3, the QTD KCAL is calculated and displayed
            elif opt == "3":

                nut = response["nutrientes"]
                App.title("Quantidade de Calorias: ")

                print("\n{:^81s}".format("Calorias são a quantidade de energia que um determinado alimento"))
                print("{:^81s}".format("fornece após ser consumido, contribuindo para as funções essenciais do"))
                print("{:^81s}".format("organismo, como respiração, produção de hormônios, e funcionamento do cérebro."))
                print("\n{:^81s}".format("Você deve consumir aproximadamente: \n"))

                App.create_table_qtd_cal(nut)

                result = [['RESULTADO :', 'SUA QTD DE KCAL:', str(response['cal']) + " kcal"]]
                App.print_result(result)




            # if opt == 4, the client side app is closed
            elif opt == "4":
                print('{:^79s}'.format("Obrigado por usar nosso App !"))

                App.padding()
                App.row()

                break




            # if opt is different from all above, displays a alert for user
            else:
                print("Erro: Opção Inválida!")