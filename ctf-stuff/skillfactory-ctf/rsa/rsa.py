from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def cryptor_init(n:int, e:int, d:float):
	rsa = RSA.construct((n, e, d))
	cryptor = PKCS1_OAEP.new(rsa)
	return cryptor

def rsa_encrypt(cryptor, t:str) -> bytes:
	text = bytes(t, 'utf-8')
	encrypted = cryptor.encrypt(text)
	return encrypted

def rsa_decrypt(cryptor, t:bytes) -> str:
	decrypted = cryptor.decrypt(t)
	return decrypted

def inv(e, n):
    u = (e, 1)
    v = (n, 0)
    while v[0] != 0:
        q = u[0] // v[0]
        t = (u[0] % v[0], u[1] - q * v[1])
        u = v
        v = t
    if u[0] != 1: return 0
    return u[1] % n

p, q = 3490529510847650949147849619903898133417764638493387843990820577, 32769132993266709549961988190834461413177642967992942539798288533
n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541
e = 9007
fn = (p-1) * (q-1) #Функция эйлера
d = inv(e, fn) #Вычисление d через расширенный алгоритм евклида

cr = cryptor_init(n, e, d) #Инициализация криптора с n e d

#Тестовые данные для проверки
#en = rsa_encrypt(cr, 'Test data')

#Значение из output.txt
en = b'\x02\r\n\xca\x80\x15\xe5\xa3(\xbdY`\x00\x11\xd4/\xed\xa3\xa9\x91\xd8\x8eHKB\x93\\z\xdd\x821&\x04\xe5v0>\xd1\xd3J2\xb8\x06\x1ft_\xf5\xcb\x8a\x9f\xab\x9b\x92\x00'

de = rsa_decrypt(cr, en)
print(f'de: {de}')
