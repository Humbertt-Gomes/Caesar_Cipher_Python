def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'   
    if shift < 1 or shift > 25 :
        return 'Shift must be an integer between 1 and 25.'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encrypt:
        shift = 26 - shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text
def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)
while True:
    print ('Bem-vindo ao projeto Cifra de Cesar!')
    text = input ('Qual mensagem deseja criptografar?: ')
    try:
        shift = int(input('Em quantas casas quer pular a mensagem?: '))
        if shift < 1 or shift > 25:
            print("Escolha apenas um número de 1 25.")
            continue          
    except ValueError:
        print('Digite apenas números inteiros (Ex: 1, 2, 3 e etc..)')
        continue
    encrypted_text = encrypt(text, shift)
    print(f"Resultado:{encrypted_text}")
    question = input ('Quer fazer de novo? (sim/não): ').lower()
    if question in ['não', 'n', 'nao']:
        print("Até mais!:)")
        break


